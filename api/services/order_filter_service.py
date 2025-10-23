from typing import Dict, Any, Optional, List
from datetime import datetime
from utils.query_builder import OrderQueryBuilder, PaginationBuilder
from repositories.order_repository import OrderRepository
from services.order_service import OrderService


class OrderFilterService:
    """
    Service chuyên xử lý filter và search cho Orders
    Tuân thủ Single Responsibility Principle
    """
    
    def __init__(self, order_service: OrderService):
        self.order_service = order_service
    
    async def get_filtered_orders(
        self,
        page: int = 1,
        limit: int = 20,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        search_value: Optional[str] = None,
        status: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Lấy danh sách orders với các filter
        """
        # Xây dựng query
        query_builder = OrderQueryBuilder()
        query = (query_builder
                .add_time_filter(start_time, end_time)
                .add_search_filter(search_value)
                .add_status_filter(status)
                .add_user_filter(user_id)
                .build())
        
        # Xây dựng pagination
        pagination = PaginationBuilder(page, limit)
        
        # Đếm tổng số records
        total_orders = await self.order_service.count_orders_with_filter(query)
        
        # Lấy danh sách orders
        orders = await self.order_service.get_orders_paginated_with_filter(
            skip=pagination.get_skip(),
            limit=pagination.get_limit(),
            filter_query=query
        )
        
        return {
            "total_pages": pagination.calculate_total_pages(total_orders),
            "current_page": pagination.get_page(),
            "total_orders": total_orders,
            "orders": orders
        }
    
    async def get_orders_by_date_range(
        self,
        start_date: str,
        end_date: str,
        page: int = 1,
        limit: int = 20
    ) -> Dict[str, Any]:
        """
        Lấy orders trong khoảng thời gian cụ thể
        """
        return await self.get_filtered_orders(
            page=page,
            limit=limit,
            start_time=start_date,
            end_time=end_date
        )
    
    async def search_orders(
        self,
        search_term: str,
        page: int = 1,
        limit: int = 20
    ) -> Dict[str, Any]:
        """
        Tìm kiếm orders theo từ khóa
        """
        return await self.get_filtered_orders(
            page=page,
            limit=limit,
            search_value=search_term
        )
    
    async def get_orders_by_status(
        self,
        status: str,
        page: int = 1,
        limit: int = 20
    ) -> Dict[str, Any]:
        """
        Lấy orders theo status
        """
        return await self.get_filtered_orders(
            page=page,
            limit=limit,
            status=status
        )
