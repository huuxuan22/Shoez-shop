from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from repositories.favourite_product_repository import FavouriteProductRepository
from schemas.favourite_product_schemas import FavouriteProductCreateSchema

router = APIRouter(prefix="/favourite", tags=["Favourite"])
repo = FavouriteProductRepository()

@router.get("/{user_id}")
def get_favourite(user_id: str):
    doc = repo.get_by_user(user_id)
    if not doc:
        return {"user_id": user_id, "product": []}
    # Ensure JSON serializable
    if doc.get("_id") and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])
    return doc

@router.post("/add")
def add_favourite(data: FavouriteProductCreateSchema):
    ok = repo.add_product(data.user_id, data.product[0])
    if not ok:
        raise HTTPException(status_code=400, detail="Sản phẩm đã có trong danh sách yêu thích!")
    return {"success": True}

@router.post("/remove")
def remove_favourite(data: FavouriteProductCreateSchema):
    repo.remove_product(data.user_id, data.product[0])
    return {"success": True}
