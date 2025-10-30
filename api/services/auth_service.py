import json
from fastapi import HTTPException
import httpx
from config.config import get_settings
from config.enum import ErrorCode, MessageKey
from exceptions.exception import UserExistException, UserNotFoundException
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from schemas.auth_schemas import UserCreate, LoginRequest, UserPrincipal, TokenResponse, VerifyEmailRequest, RegisterResponse
from utils.utils import hash_password, verify_password, convert_uuid_to_str
from config.enum import RoleEnum
from authlib.integrations.starlette_client import OAuth
from utils import auth
from fastapi.responses import RedirectResponse
from model.user_model import User
from i18n.translator import translate
from config.redis_client import redis_client
from utils.email_service import generate_verification_code, send_verification_email
settings = get_settings()

oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url=settings.server_metadata_url,
    client_id=settings.google_client_id,
    client_secret=settings.google_client_secret,
    client_kwargs=settings.client_kwargs
)

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register(self, user_data: UserCreate) -> "RegisterResponse":
        """
        Đăng ký user mới - chỉ tạo mã xác thực và gửi email, không lưu vào DB
        Args:
            user_data: Thông tin user cần đăng ký (email, password, full_name, numberphone, etc.)
        Returns:
            RegisterResponse: Thông báo thành công và email
        Raises:
            HTTPException: Nếu email đã tồn tại hoặc có lỗi validation
        """
        # Kiểm tra email đã tồn tại chưa
        existing_user = await self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise UserExistException(
                message=translate(MessageKey.USER_EXIST)
            )
        
        # Tạo mã xác thực ngẫu nhiên
        verification_code = generate_verification_code()
        
        # Hash mã code trước khi lưu vào Redis
        hashed_code = auth.hash_password(verification_code)
        
        # Lưu mã code vào Redis với key là email (thời hạn 15 phút)
        success = redis_client.set_email_verification_code(
            email=user_data.email,
            code=hashed_code,
            expire_seconds=900  # 15 phút
        )
        
        if not success:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Không thể lưu mã xác thực. Vui lòng thử lại sau."
            )
        
        # Lưu thông tin user tạm thời vào Redis để dùng khi verify (15 phút)
        import json
        user_temp_data = {
            "email": user_data.email,
            "password": hash_password(user_data.password),  # Hash password ngay
            "full_name": user_data.full_name,
            "numberphone": user_data.numberphone,
            "avatar": user_data.avatar,
            "is_active": user_data.is_active,
            "role": "USER",
            "is_login": "NORMAL"
        }
        redis_client.client.set(
            f"pending_registration:{user_data.email}",
            json.dumps(user_temp_data),
            ex=900  # 15 phút
        )
        
        # Gửi email xác thực
        email_sent = await send_verification_email(user_data.email, verification_code)
        
        if not email_sent:
            # Xóa mã code trong Redis nếu gửi email thất bại
            redis_client.delete_email_verification_code(user_data.email)
            redis_client.client.delete(f"pending_registration:{user_data.email}")
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Không thể gửi email xác thực. Vui lòng kiểm tra lại email và thử lại."
            )
        
        return RegisterResponse(
            message="Đã gửi mã xác thực đến email của bạn. Vui lòng kiểm tra hộp thư.",
            email=user_data.email
        )
    
    async def verify_email(self, verify_data: VerifyEmailRequest) -> "TokenResponse":
        """
        Xác thực email và đăng ký user vào database, sau đó tự động login
        Args:
            verify_data: Email và mã xác thực
        Returns:
            TokenResponse: Access token, refresh token và thông tin user
        Raises:
            HTTPException: Nếu mã xác thực không đúng hoặc đã hết hạn
        """
        # Lấy mã code đã hash từ Redis
        hashed_code = redis_client.get_email_verification_code(verify_data.email)
        
        if not hashed_code:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Mã xác thực không hợp lệ hoặc đã hết hạn. Vui lòng đăng ký lại."
            )
        
        # Verify mã code
        if not auth.verify_password(verify_data.code, hashed_code):
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Mã xác thực không đúng. Vui lòng kiểm tra lại."
            )
        
        # Lấy thông tin user tạm thời từ Redis
        user_temp_data_str = redis_client.client.get(f"pending_registration:{verify_data.email}")
        
        if not user_temp_data_str:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Thông tin đăng ký đã hết hạn. Vui lòng đăng ký lại."
            )
        
        user_temp_data = json.loads(user_temp_data_str)
        
        # Kiểm tra lại email đã tồn tại chưa (phòng trường hợp đã được đăng ký trong lúc chờ)
        existing_user = await self.user_repository.get_by_email(verify_data.email)
        if existing_user:
            # Xóa dữ liệu tạm
            redis_client.delete_email_verification_code(verify_data.email)
            redis_client.client.delete(f"pending_registration:{verify_data.email}")
            raise HTTPException(
                status_code=ErrorCode.CONFLICT,
                detail=translate(MessageKey.USER_EXIST)
            )
        
        # Tạo user mới trong database
        created_user = await self.user_repository.create(user_temp_data)
        
        # Set id = _id after creation
        if created_user and '_id' in created_user:
            created_user['id'] = str(created_user['_id'])
            # Update the document to add id field
            await self.user_repository.db["users"].update_one(
                {"_id": created_user['_id']},
                {"$set": {"id": created_user['id']}}
            )
        
        redis_client.delete_email_verification_code(verify_data.email)
        redis_client.client.delete(f"pending_registration:{verify_data.email}")
        
        # Tạo user principal để trả về
        user_principal = UserPrincipal(
            id=created_user.get('id'),
            email=created_user.get('email'),
            full_name=created_user.get('full_name'),
            numberphone=created_user.get('numberphone'),
            avatar=created_user.get('avatar'),
            is_active=created_user.get('is_active', True),
            role=created_user.get('role')
        )
        
        # Tạo token để tự động login
        to_encode = convert_uuid_to_str(user_principal.dict())
        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)
        
        return TokenResponse(
            message="Xác thực email thành công! Tài khoản của bạn đã được tạo.",
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )
    
    async def resend_verification_code(self, email: str) -> RegisterResponse:
        """
        Gửi lại mã xác thực email
        
        Args:
            email: Email của người dùng
            
        Returns:
            RegisterResponse: Thông báo thành công
            
        Raises:
            HTTPException: Nếu email không hợp lệ hoặc không có thông tin đăng ký tạm
        """
        # Kiểm tra có thông tin đăng ký tạm không
        user_temp_data_str = redis_client.client.get(f"pending_registration:{email}")
        
        if not user_temp_data_str:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Không tìm thấy thông tin đăng ký. Vui lòng đăng ký lại."
            )
        
        # Tạo mã xác thực mới
        verification_code = generate_verification_code()
        
        # Hash mã code
        hashed_code = auth.hash_password(verification_code)
        success = redis_client.set_email_verification_code(
            email=email,
            code=hashed_code,
            expire_seconds=900  
        )
        
        if not success:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Không thể lưu mã xác thực. Vui lòng thử lại sau."
            )
        
        # Gửi email xác thực
        email_sent = await send_verification_email(email, verification_code)
        
        if not email_sent:
            raise HTTPException(
                status_code=ErrorCode.BAD_REQUEST,
                detail="Không thể gửi email xác thực. Vui lòng kiểm tra lại email và thử lại."
            )
        
        return RegisterResponse(
            message="Đã gửi lại mã xác thực đến email của bạn.",
            email=email
        )

    async def login(self, email: str, password: str) -> "TokenResponse":
        user_dict = await self.user_repository.get_user_principal(email)
        if not user_dict:
            raise HTTPException(status_code=ErrorCode.NOT_FOUND, detail="Không tìm thấy người dùng")

        # Verify password using bcrypt
        hashed_password = user_dict.get("password")
        if not auth.verify_password(password, hashed_password):
            raise HTTPException(status_code=ErrorCode.BAD_REQUEST, detail="Sai mật khẩu")

        user_principal = UserPrincipal(**user_dict)
        to_encode = convert_uuid_to_str(user_principal.dict())

        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)

        return TokenResponse(
            message=translate(MessageKey.LOGIN_SUCCESS),
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )

    @staticmethod
    async def get_google_redirect_uri(request):
        # Ensure redirect URI includes API prefix to match mounted router paths
        redirect_uri = f"{settings.backend_api_base}/auth/google/callback"
        return await oauth.google.authorize_redirect(request, redirect_uri)

    @staticmethod
    async def get_facebook_redirect_uri(request):
        # Redirect người dùng tới Facebook OAuth
        # Scope cần thiết: public_profile (mặc định) và email (cần permission)
        fb_auth_url = (
            f"https://www.facebook.com/v18.0/dialog/oauth?"
            f"client_id={settings.facebook_app_id}&"
            f"redirect_uri={settings.backend_api_base}/auth/facebook/callback&"
            f"response_type=code&"
            f"scope=public_profile,email"  # public_profile là bắt buộc, email cần permission
        )
        return RedirectResponse(fb_auth_url)

    async def handle_google_callback(self, request):
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo") or {}

        email = user_info.get("email")
        name = user_info.get("name")
        picture = user_info.get("picture")

        if not email:
            raise HTTPException(status_code=ErrorCode.BAD_REQUEST, detail="Không lấy được email từ Google")

        # Tìm user theo email, nếu chưa có thì tạo mới
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            db_user = existing_user
        else:
            create_data = {
                "email": email,
                # Đăng ký qua Google không có password
                "full_name": name,
                "avatar": picture,
                "is_active": True,
                "role": "USER",
                "is_login": "GOOGLE"  # Đăng nhập bằng Google
            }
            db_user = await self.user_repository.create(create_data)

        # Ensure id exists
        if db_user and "_id" in db_user:
            db_user["id"] = str(db_user["_id"])

        user_principal = UserPrincipal(
            id=db_user.get("id"),
            email=db_user.get("email"),
            full_name=db_user.get("full_name"),
            numberphone=db_user.get("numberphone"),
            avatar=db_user.get("avatar"),
            is_active=db_user.get("is_active", True),
            role=db_user.get("role")
        )

        to_encode = convert_uuid_to_str(user_principal.dict())
        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)

        return TokenResponse(
            message=translate(MessageKey.LOGIN_SUCCESS),
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )

    async def handle_facebook_callback(self, request):
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(status_code=400, detail="No code provided by Facebook")

        token_url = (
            f"https://graph.facebook.com/v16.0/oauth/access_token?"
            f"client_id={settings.facebook_app_id}&"
            f"redirect_uri={settings.backend_api_base}/auth/facebook/callback&"
            f"client_secret={settings.facebook_app_secret}&"
            f"code={code}"
        )

        async with httpx.AsyncClient() as client:
            token_res = await client.get(token_url)
            token_data = token_res.json()
            fb_access_token = token_data.get("access_token")
            if not fb_access_token:
                raise HTTPException(status_code=400, detail="Cannot get Facebook access token")

            # 2. Lấy user info từ Facebook (id, name, email)
            profile_url = "https://graph.facebook.com/me"
            params = {"fields": "id,name,email,picture", "access_token": fb_access_token}
            profile_res = await client.get(profile_url, params=params)
            user_info = profile_res.json()

        email = user_info.get("email")
        name = user_info.get("name")
        picture = None
        pic_data = user_info.get("picture")
        if isinstance(pic_data, dict):
            picture = pic_data.get("data", {}).get("url")

        # 3. Tìm user theo name và is_login="FACEBOOK" (không dùng email)
        existing_user = await self.user_repository.get_by_name_and_login_type(name, "FACEBOOK")
        if existing_user:
            db_user = existing_user
            # Nếu user đã có email từ lần trước và giờ Facebook trả về email, cập nhật
            if email and not db_user.get("email"):
                db_user["email"] = email
                await self.user_repository.update_by_id(db_user.get("id"), {"email": email})
        else:
            # Tạo user mới với is_login="FACEBOOK"
            create_data = {
                "email": email,  # Có thể None nếu Facebook không trả về email
                "full_name": name,
                "avatar": picture,
                "is_active": True,
                "role": "USER",
                "is_login": "FACEBOOK"  # Đăng nhập bằng Facebook
            }
            db_user = await self.user_repository.create(create_data)

        if db_user and "_id" in db_user:
            db_user["id"] = str(db_user["_id"])

        user_principal = UserPrincipal(
            id=db_user.get("id"),
            email=db_user.get("email"),
            full_name=db_user.get("full_name"),
            numberphone=db_user.get("numberphone"),
            avatar=db_user.get("avatar"),
            is_active=db_user.get("is_active", True),
            role=db_user.get("role")
        )

        to_encode = convert_uuid_to_str(user_principal.dict())
        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)

        return TokenResponse(
            message=translate(MessageKey.LOGIN_SUCCESS),
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )







