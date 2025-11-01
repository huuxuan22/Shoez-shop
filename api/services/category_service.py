from typing import Dict, Any, Optional, List
from fastapi import HTTPException
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository
from schemas.category_schemas import CategoryCreate, CategoryUpdate
from fastapi.encoders import jsonable_encoder


class CategoryService:
    def __init__(self, category_repository: CategoryRepository, product_repository: Optional[ProductRepository] = None):
        self.category_repository = category_repository
        self.product_repository = product_repository

    async def create_category(self, category_data: CategoryCreate) -> Dict[str, Any]:
        """Create a new category"""
        # Check if category with same name exists
        existing = await self.category_repository.get_by_name(category_data.name)
        if existing:
            raise HTTPException(status_code=400, detail="Category with this name already exists")

        category_dict = category_data.model_dump()
        created = await self.category_repository.create(category_dict)
        return created

    async def get_category_by_id(self, category_id: str) -> Dict[str, Any]:
        """Get category by ID"""
        return await self.category_repository.get_by_id(category_id)

    async def get_all_categories(self, is_active: Optional[bool] = None) -> List[Dict[str, Any]]:
        """Get all categories, optionally filtered by is_active"""
        if is_active is not None:
            categories = await self.category_repository.get_all(filter_query={"is_active": is_active})
        else:
            categories = await self.category_repository.get_all()
        
        # If categories empty but products have category values, seed categories from products
        if not categories and self.product_repository:
            try:
                distinct_names = await self.product_repository.get_distinct_categories()
                if distinct_names:
                    # Create categories that don't exist
                    for name in distinct_names:
                        existing = await self.category_repository.get_by_name(name)
                        if not existing:
                            await self.category_repository.create({
                                "name": name,
                                "description": None,
                                "is_active": True,
                            })
                    # Reload after seeding
                    categories = await self.category_repository.get_all()
            except Exception:
                # Best-effort; ignore seeding errors
                pass

        # Add product count to each category
        if self.product_repository:
            for category in categories:
                category_name = category.get("name")
                if category_name:
                    product_count = await self.product_repository.count(filter_query={"category": category_name})
                    category["product_count"] = product_count
                else:
                    category["product_count"] = 0
        else:
            # If no product repository, set count to 0
            for category in categories:
                category["product_count"] = 0
        
        return jsonable_encoder(categories)

    async def update_category(self, category_id: str, category_data: CategoryUpdate) -> Dict[str, Any]:
        """Update a category"""
        # Check if category exists
        existing = await self.category_repository.get_by_id(category_id)
        
        # If updating name, check for duplicates
        if category_data.name:
            duplicate = await self.category_repository.get_by_name(category_data.name)
            if duplicate and duplicate.get("id") != category_id:
                raise HTTPException(status_code=400, detail="Category with this name already exists")

        update_dict = category_data.model_dump(exclude_unset=True)
        updated = await self.category_repository.update(category_id, update_dict)
        
        if not updated:
            raise HTTPException(status_code=404, detail="Category not found")
        
        return updated

    async def delete_category(self, category_id: str) -> bool:
        """Delete a category"""
        # Check if category exists
        existing = await self.category_repository.get_by_id(category_id)
        
        # TODO: Check if category is used in products before deleting
        # For now, we'll just delete it
        
        deleted = await self.category_repository.delete(category_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Category not found")
        
        return True

    async def get_category_product_count(self, category_id: str) -> int:
        """Get count of products in this category"""
        category = await self.category_repository.get_by_id(category_id)
        category_name = category.get("name")
        if self.product_repository and category_name:
            return await self.product_repository.count(filter_query={"category": category_name})
        return 0

