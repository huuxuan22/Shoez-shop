"""
Review Controller
Giải thích: API endpoints cho reviews
"""
import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi import UploadFile, File
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional, List
from datetime import datetime
from repositories.review_repository import ReviewRepository
from services.review_service import ReviewService
from schemas.review_schemas import ReviewCreateSchema, ReviewUpdateSchema
from config.database import get_database
from config.context import get_current_user
from repositories.image_repository import ImageRepository
from starlette.concurrency import run_in_threadpool

review_router = APIRouter(prefix="/reviews", tags=["Reviews"])


def get_review_repo():
    """Dependency để get review repository"""
    return ReviewRepository(get_database())


def get_review_service() -> ReviewService:
    """Dependency để get review service"""
    repo = ReviewRepository(get_database())
    return ReviewService(repo)


@review_router.post("/", response_model=dict)
async def create_review(
    review_data: ReviewCreateSchema,
    current_user: dict = Depends(get_current_user)
):
    """
    Tạo review mới cho sản phẩm
    - Chỉ user đã mua và nhận hàng mới được review
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    user_name = current_user.get("full_name") or current_user.get("name") or "User"
    
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    service = get_review_service()
    try:
        created_review = await service.create_review(review_data, user_id, user_name)
        return JSONResponse(
            content=jsonable_encoder(created_review),
            status_code=201
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@review_router.post("/upload-media")
async def upload_review_media(
    files: List[UploadFile] = File(...)
):
    """Upload ảnh/video đính kèm review, trả về danh sách URL"""
    if not files or len(files) == 0:
        raise HTTPException(status_code=400, detail="No files uploaded")

    image_repo = ImageRepository()
    uploaded_urls: List[str] = []
    try:
        for upload_file in files:
            fileobj = upload_file.file
            fileobj.seek(0)
            filename = upload_file.filename
            url = await run_in_threadpool(
                image_repo.upload,
                fileobj,
                filename,
                upload_file.content_type or "application/octet-stream",
            )
            uploaded_urls.append(url)

        return {"images": uploaded_urls}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")


@review_router.get("/product/{product_id}")
async def get_product_reviews(
    product_id: str,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    service: ReviewService = Depends(get_review_service)
):
    """Lấy reviews của 1 sản phẩm"""
    result = await service.get_reviews_by_product(product_id, page, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@review_router.get("/user")
async def get_user_reviews(
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Lấy tất cả reviews của user hiện tại"""
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    reviews = await service.get_reviews_by_user(user_id)
    return JSONResponse(content=jsonable_encoder(reviews), status_code=200)


@review_router.get("/order/{order_id}")
async def get_order_reviews(
    order_id: str,
    service: ReviewService = Depends(get_review_service)
):
    """Lấy reviews theo order_id"""
    reviews = await service.get_reviews_by_order(order_id)
    return JSONResponse(content=jsonable_encoder(reviews), status_code=200)


@review_router.put("/{review_id}")
async def update_review(
    review_id: str,
    update_data: ReviewUpdateSchema,
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Update review"""
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    try:
        updated_review = await service.update_review(review_id, update_data, user_id)
        return JSONResponse(content=jsonable_encoder(updated_review), status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))


@review_router.delete("/{review_id}")
async def delete_review(
    review_id: str,
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Xóa review"""
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    try:
        deleted = await service.delete_review(review_id, user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Review not found")
        return JSONResponse(content={"message": "Review deleted successfully"}, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))


@review_router.post("/{review_id}/helpful")
async def toggle_helpful(
    review_id: str,
    helpful: bool = Query(True),
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Toggle helpful cho review"""
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    try:
        updated_review = await service.toggle_helpful(review_id, user_id, helpful)
        return JSONResponse(content=jsonable_encoder(updated_review), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@review_router.get("/pending")
async def get_pending_reviews(
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Lấy danh sách sản phẩm cần đánh giá của user hiện tại"""
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    try:
        pending_reviews = await service.get_pending_reviews_for_user(user_id)
        return JSONResponse(content=jsonable_encoder(pending_reviews), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@review_router.post("/{review_id}/admin-comment")
async def add_admin_comment(
    review_id: str,
    admin_comment: dict = Depends(lambda: {"comment": None}),
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Admin comment vào review (chỉ admin mới được)"""
    # Check if user is admin
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can comment on reviews")
    
    comment_text = admin_comment.get("comment")
    if not comment_text:
        raise HTTPException(status_code=400, detail="Comment is required")
    
    user_id = str(current_user.get("_id") or current_user.get("id"))
    admin_name = current_user.get("full_name") or current_user.get("name") or "Admin"
    
    try:
        # Get review
        review = await service.review_repo.get_by_id(review_id)
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        
        # Add admin comment
        admin_comments = review.get("admin_comments", [])
        admin_comments.append({
            "admin_id": user_id,
            "admin_name": admin_name,
            "comment": comment_text,
            "created_at": datetime.utcnow().isoformat()
        })
        
        # Update review
        updated_review = await service.review_repo.update(review_id, {"admin_comments": admin_comments})
        return JSONResponse(content=jsonable_encoder(updated_review), status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@review_router.get("/admin/needs-attention")
async def get_reviews_needing_attention(
    current_user: dict = Depends(get_current_user),
    service: ReviewService = Depends(get_review_service)
):
    """Lấy danh sách reviews cần chú ý (rating <= 3) - Chỉ admin"""
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can access")
    
    try:
        from repositories.review_repository import ReviewRepository
        from config.database import get_database
        
        review_repo = ReviewRepository(get_database())
        reviews = await review_repo.get_all(
            skip=0,
            limit=100,
            filter_query={"needs_attention": True, "status": "approved"}
        )
        
        return JSONResponse(content=jsonable_encoder(reviews), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

