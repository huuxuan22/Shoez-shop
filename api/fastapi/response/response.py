from fastapi.responses import JSONResponse


def response_fail(message: str, status_code: int = 400):
    """
    Trả về JSON thông báo lỗi chuẩn.

    Args:
        message (str): Nội dung thông báo lỗi
        status_code (int): Mã HTTP trả về (mặc định 400)
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message
        }
    )


def response_success(message: str, status_code: int = 200):
    """
    Trả về JSON thông báo lỗi chuẩn.

    Args:
        message (str): Nội dung thông báo lỗi
        status_code (int): Mã HTTP trả về (mặc định 400)
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message
        }
    )