from fastapi import APIRouter, UploadFile, File
from typing import List

from fastapi.params import Depends

from dependences.dependencies import get_product_repo, get_image_repo
from repositories.image_repository import ImageRepository
from repositories.product_repository import ProductRepository
from services.product_service import ProductService

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post("/{product_id}/upload-images")
async def upload_product_images(
    product_id: str,
    files: List[UploadFile] = File(...),
    product_repo: ProductRepository = Depends(get_product_repo),
    image_repo: ImageRepository = Depends(get_image_repo),
):
    service = ProductService(image_repo,product_repo)
    result = await service.upload_product_images(product_id, files)
    return result
