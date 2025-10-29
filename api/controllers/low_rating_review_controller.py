from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from config.context import get_current_user
from services.low_rating_review_service import get_low_rating_review_service

low_rating_review_router = APIRouter(prefix="/admin/low-rating-reviews", tags=["Low Rating Reviews"])

@low_rating_review_router.get("/unresolved")
async def get_unresolved_low_rating_reviews(
    limit: int = Query(50, ge=1, le=100),
    current_user: dict = Depends(get_current_user),
    service = Depends(get_low_rating_review_service)
):
    """Lấy danh sách reviews chưa resolved - Chỉ admin"""
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can access")
    
    try:
        reviews = await service.get_unresolved_reviews(limit)
        return JSONResponse(content=jsonable_encoder(reviews), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@low_rating_review_router.post("/respond/{review_id}")
async def mark_as_responded(
    review_id: str,
    current_user: dict = Depends(get_current_user),
    service = Depends(get_low_rating_review_service)
):
    """Đánh dấu admin đã phản hồi review - Chỉ admin"""
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can access")
    
    try:
        result = await service.mark_as_responded(review_id)
        if result:
            return JSONResponse(content={"message": "Marked as responded"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Review not found or already responded"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

