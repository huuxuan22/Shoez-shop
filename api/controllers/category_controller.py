from fastapi import APIRouter, Depends, HTTPException, Query
from starlette.responses import JSONResponse
from typing import Optional
from fastapi.encoders import jsonable_encoder

from dependences.dependencies import get_category_repo, get_product_repo
from dependences.permissions import require_roles
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository
from schemas.category_schemas import CategoryCreate, CategoryUpdate
from services.category_service import CategoryService

category_router = APIRouter(prefix="/categories", tags=["Categories"])


@category_router.get("", summary="Lấy danh sách tất cả danh mục")
async def get_all_categories(
    is_active: Optional[bool] = Query(None, description="Lọc theo trạng thái hoạt động"),
    category_repo: CategoryRepository = Depends(get_category_repo),
    product_repo: Optional[ProductRepository] = Depends(get_product_repo)
):
    """
    Lấy danh sách tất cả danh mục
    - Có thể filter theo is_active (true/false)
    """
    service = CategoryService(category_repo, product_repo)
    categories = await service.get_all_categories(is_active=is_active)
    return JSONResponse(status_code=200, content=categories)


@category_router.get("/{category_id}", summary="Lấy thông tin danh mục theo ID")
async def get_category_by_id(
    category_id: str,
    category_repo: CategoryRepository = Depends(get_category_repo)
):
    """Lấy thông tin chi tiết của một danh mục"""
    service = CategoryService(category_repo)
    category = await service.get_category_by_id(category_id)
    return JSONResponse(status_code=200, content=category)


@category_router.post("", status_code=201, summary="Tạo danh mục mới")
@require_roles("ADMIN")
async def create_category(
    category_data: CategoryCreate,
    category_repo: CategoryRepository = Depends(get_category_repo)
):
    """Tạo danh mục mới (chỉ ADMIN)"""
    service = CategoryService(category_repo)
    created = await service.create_category(category_data)
    return JSONResponse(status_code=201, content=created)


@category_router.put("/{category_id}", summary="Cập nhật danh mục")
@require_roles("ADMIN")
async def update_category(
    category_id: str,
    category_data: CategoryUpdate,
    category_repo: CategoryRepository = Depends(get_category_repo)
):
    """Cập nhật thông tin danh mục (chỉ ADMIN)"""
    service = CategoryService(category_repo)
    updated = await service.update_category(category_id, category_data)
    return JSONResponse(status_code=200, content=updated)


@category_router.delete("/{category_id}", summary="Xóa danh mục")
@require_roles("ADMIN")
async def delete_category(
    category_id: str,
    category_repo: CategoryRepository = Depends(get_category_repo)
):
    """Xóa danh mục (chỉ ADMIN)"""
    service = CategoryService(category_repo)
    await service.delete_category(category_id)
    return JSONResponse(status_code=200, content={"message": "Category deleted successfully"})

