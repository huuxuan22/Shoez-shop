from fastapi import APIRouter, HTTPException
from bson import ObjectId
from repositories.favourite_product_repository import FavouriteProductRepository
from schemas.favourite_product_schemas import FavouriteProductCreateSchema

router = APIRouter(prefix="/favourite", tags=["Favourite"])

@router.get("/{user_id}")
async def get_favourite(user_id: str):
    repo = FavouriteProductRepository()
    doc = await repo.get_by_user(user_id)
    if not doc:
        return {"user_id": user_id, "product": []}
    if doc.get("_id") and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])
    return doc

@router.post("/add")
async def add_favourite(data: FavouriteProductCreateSchema):
    repo = FavouriteProductRepository()
    ok = await repo.add_product(data.user_id, data.product[0])
    if not ok:
        raise HTTPException(status_code=400, detail="Sản phẩm đã có trong danh sách yêu thích!")
    return {"success": True}

@router.post("/remove")
async def remove_favourite(data: FavouriteProductCreateSchema):
    repo = FavouriteProductRepository()
    await repo.remove_product(data.user_id, data.product[0])
    return {"success": True}
