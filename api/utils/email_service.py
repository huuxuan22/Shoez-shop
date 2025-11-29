import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import get_settings
from utils.logger import logger
import secrets
import string

settings = get_settings()

def generate_verification_code(length: int = 6) -> str:
    """Tạo mã xác thực ngẫu nhiên"""
    alphabet = string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def get_verification_email_html(code: str) -> str:
    """Tạo HTML template cho email xác thực (tone trắng đen sang trọng)"""
    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Xác thực tài khoản Shoez Shop</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: #f9f9f9; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #222;">
        <table role="presentation" style="width: 100%; border-collapse: collapse; margin: 0; padding: 0;">
            <tr>
                <td align="center" style="padding: 40px 20px;">
                    <table role="presentation" style="max-width: 600px; width: 100%; border-collapse: collapse; background-color: #ffffff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        
                        <!-- Header -->
                        <tr>
                            <td style="padding: 40px 40px 20px; text-align: center; border-bottom: 1px solid #eee;">
                                <h1 style="margin: 0; font-size: 28px; font-weight: 700; letter-spacing: 2px; color: #000;">SHOEZ SHOP</h1>
                                <p style="margin: 10px 0 0; font-size: 15px; color: #555;">Xác thực tài khoản của bạn</p>
                            </td>
                        </tr>
                        
                        <!-- Content -->
                        <tr>
                            <td style="padding: 40px;">
                                <h2 style="margin: 0 0 20px; font-size: 22px; font-weight: 600; color: #111;">Xin chào!</h2>
                                <p style="margin: 0 0 25px; font-size: 15px; line-height: 1.7; color: #444;">
                                    Cảm ơn bạn đã đăng ký tài khoản tại <strong>Shoez Shop</strong>.<br>
                                    Vui lòng sử dụng mã xác thực bên dưới để hoàn tất quá trình đăng ký:
                                </p>

                                <!-- Code box -->
                                <div style="text-align: center; margin: 40px 0;">
                                    <div style="display: inline-block; padding: 25px 40px; border: 2px solid #000; border-radius: 8px; background-color: #fff;">
                                        <p style="margin: 0 0 10px; font-size: 13px; color: #555; letter-spacing: 1px; text-transform: uppercase;">
                                            Mã xác thực của bạn
                                        </p>
                                        <span style="font-size: 36px; font-weight: 700; letter-spacing: 8px; color: #000; font-family: 'Courier New', monospace;">{code}</span>
                                    </div>
                                </div>

                                <p style="margin: 0; font-size: 14px; color: #777; line-height: 1.6;">
                                    <strong>Lưu ý:</strong> Mã xác thực này sẽ hết hạn sau <strong>15 phút</strong>.<br>
                                    Nếu bạn không yêu cầu mã này, vui lòng bỏ qua email này.
                                </p>
                            </td>
                        </tr>
                        
                        <!-- Footer -->
                        <tr>
                            <td style="padding: 30px 40px; background-color: #fafafa; border-top: 1px solid #eee; text-align: center;">
                                <p style="margin: 0; font-size: 13px; color: #555;">
                                    Trân trọng,<br>
                                    <strong style="font-weight: 600; color: #000;">Đội ngũ Shoez Shop</strong>
                                </p>
                                <p style="margin: 10px 0 0; font-size: 12px; color: #999;">
                                    Email này được gửi tự động. Vui lòng không trả lời.
                                </p>
                            </td>
                        </tr>

                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

async def send_verification_email(to_email: str, code: str) -> bool:
    """
    Gửi email xác thực đến người dùng
    
    Args:
        to_email: Email người nhận
        code: Mã xác thực
        
    Returns:
        bool: True nếu gửi thành công, False nếu có lỗi
    """
    try:
        # Tạo message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Xác thực tài khoản Shoez Shop"
        message["From"] = settings.smtp_from_email
        message["To"] = to_email
        
        # Tạo HTML content
        html_content = get_verification_email_html(code)
        html_part = MIMEText(html_content, "html", "utf-8")
        message.attach(html_part)
        
        # Gửi email
        await aiosmtplib.send(
            message,
            hostname=settings.smtp_host,
            port=settings.smtp_port,
            username=settings.smtp_username,
            password=settings.smtp_password,
            use_tls=settings.smtp_use_tls,
        )
        
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        return False

