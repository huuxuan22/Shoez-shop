from fastapi import APIRouter, Query, Depends, HTTPException
from fastapi import APIRouter, UploadFile, File,Path,Body
from typing import List, Optional, Annotated, Any
from fastapi.params import Depends

from dependences.dependencies import get_product_repo, get_image_repo
from repositories.image_repository import ImageRepository
from repositories.product_repository import ProductRepository
from schemas.product_schemas import ProductResponse, ProductCreate, ProductUpdate
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

@product_router.get("/get-all", response_model=List[ProductResponse])
async def list_products(
    name: Annotated[Optional[str], Query(description="Tên sản phẩm để search")] = None,
    brand: Annotated[Optional[str], Query()] = None,
    category: Annotated[Optional[str], Query()] = None,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    product_repo: ProductRepository = Depends(get_product_repo),
):
    service = ProductService(None, product_repo)
    return await service.list_products(
        skip=skip,
        limit=limit,
        name=name,
        brand=brand,
        category=category
    )

@product_router.get("/top-rated", response_model=List[ProductResponse])
async def get_top_rated_products(
    product_repo: ProductRepository = Depends(get_product_repo)
):
    service = ProductService(None,product_repo)
    return await service.get_top_rated_products(limit=8)

@product_router.get("/top-rated-by-brand", response_model=List[ProductResponse])
async def get_top_rated_by_brand(
    brand: Annotated[str, Query(..., description="Brand name")],
    product_repo: ProductRepository = Depends(get_product_repo)
):
    service = ProductService(None, product_repo)
    return await service.get_top_rated_by_brand(brand=brand, limit=8)

@product_router.delete("/delete/{product_id}")
async def delete_product(
    product_id: str,
    product_repo: ProductRepository = Depends(get_product_repo)
):
    service = ProductService(None, product_repo)
    deleted = await service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@product_router.get("/detail/{product_id}")
async def get_product_detail(
    product_id: str,
    product_repo: ProductRepository = Depends(get_product_repo)
) -> Any:
    service = ProductService(None, product_repo)
    product = await service.get_product_detail(product_id)
    if not product:
        raise HTTPException(404, "Product not found")  # <-- sửa như này
    return product

@product_router.put("/update/{product_id}", response_model=ProductResponse)
async def update_product_endpoint(
    product_id: str = Path(..., description="ID of the product to update"),
    product_data: ProductUpdate = Body(...),
    product_repo: ProductRepository = Depends(get_product_repo)
):
    service = ProductService(None, product_repo)  # hoặc inject repo
    return await service.update_product(product_id, product_data)


