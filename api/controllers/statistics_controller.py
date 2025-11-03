from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional
from dependences.dependencies import get_database
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from repositories.category_repository import CategoryRepository
from repositories.brand_repository import BrandRepository
from services.statistics_service import StatisticsService
from dependences.permissions import require_roles

statistics_router = APIRouter(prefix="/statistics", tags=["Statistics"])


def get_statistics_service() -> StatisticsService:
    """Dependency để tạo StatisticsService"""
    db = get_database()
    order_repo = OrderRepository(db)
    product_repo = ProductRepository(db)
    user_repo = UserRepository(db)
    category_repo = CategoryRepository(db)
    brand_repo = BrandRepository(db)
    return StatisticsService(order_repo, product_repo, user_repo, category_repo, brand_repo)


@statistics_router.get("/overview")
@require_roles("ADMIN")
async def get_overview_statistics(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Lấy thống kê tổng quan: revenue, orders, products, customers
    """
    try:
        stats = await statistics_service.get_overview_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting statistics: {str(e)}")


@statistics_router.get("/revenue-chart")
@require_roles("ADMIN")
async def get_revenue_chart(
    days: int = Query(7, ge=1, le=30, description="Number of days"),
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Lấy dữ liệu biểu đồ doanh thu theo ngày
    """
    try:
        chart_data = await statistics_service.get_revenue_chart_data(days=days)
        return JSONResponse(content=jsonable_encoder(chart_data), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting chart data: {str(e)}")


@statistics_router.get("/top-products")
@require_roles("ADMIN")
async def get_top_products(
    limit: int = Query(5, ge=1, le=20, description="Number of top products"),
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Lấy top sản phẩm bán chạy nhất
    """
    try:
        top_products = await statistics_service.get_top_products(limit=limit)
        return JSONResponse(content=jsonable_encoder(top_products), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting top products: {str(e)}")


@statistics_router.get("/recent-orders")
@require_roles("ADMIN")
async def get_recent_orders(
    limit: int = Query(5, ge=1, le=20, description="Number of recent orders"),
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Lấy các đơn hàng gần đây
    """
    try:
        recent_orders = await statistics_service.get_recent_orders(limit=limit)
        return JSONResponse(content=jsonable_encoder(recent_orders), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting recent orders: {str(e)}")


@statistics_router.get("/detailed-revenue")
@require_roles("ADMIN")
async def get_detailed_revenue_stats(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê doanh thu chi tiết: hôm nay, tuần này, tháng này, năm này
    """
    try:
        stats = await statistics_service.get_detailed_revenue_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting detailed revenue stats: {str(e)}")


@statistics_router.get("/detailed-orders")
@require_roles("ADMIN")
async def get_detailed_order_stats(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê đơn hàng chi tiết theo trạng thái và thời gian
    """
    try:
        stats = await statistics_service.get_detailed_order_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting detailed order stats: {str(e)}")


@statistics_router.get("/cancellation")
@require_roles("ADMIN")
async def get_cancellation_stats(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê hủy hàng chi tiết: số lượng, tỷ lệ, doanh thu mất
    """
    try:
        stats = await statistics_service.get_cancellation_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting cancellation stats: {str(e)}")


@statistics_router.get("/debug/orders")
@require_roles("ADMIN")
async def debug_orders(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Debug endpoint để kiểm tra dữ liệu đơn hàng
    """
    try:
        from dependences.dependencies import get_database
        db = get_database()
        orders_collection = db["orders"]
        
        # Lấy 5 đơn hàng đầu tiên để kiểm tra
        sample_orders = await orders_collection.find({}).limit(5).to_list(length=5)
        
        # Đếm tổng
        total_count = await orders_collection.count_documents({})
        
        # Kiểm tra status
        status_counts = {}
        for status in ["pending", "confirmed", "shipping", "complete", "completed", "delivered", "cancelled", "canceled"]:
            count = await orders_collection.count_documents({"status": status})
            if count > 0:
                status_counts[status] = count
        
        debug_info = {
            "total_orders": total_count,
            "status_distribution": status_counts,
            "sample_orders": []
        }
        
        # Lấy thông tin sample orders
        for order in sample_orders:
            order_info = {
                "id": str(order.get("_id", "")),
                "status": order.get("status", "unknown"),
                "total": order.get("total", 0),
                "created_at": str(order.get("created_at", "")),
                "created_at_type": type(order.get("created_at")).__name__,
                "items_count": len(order.get("items", []))
            }
            debug_info["sample_orders"].append(order_info)
        
        return JSONResponse(content=jsonable_encoder(debug_info), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Debug error: {str(e)}")


@statistics_router.get("/users")
@require_roles("ADMIN")
async def get_user_statistics(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê người dùng: tổng số, active, inactive, mới trong tháng
    """
    try:
        stats = await statistics_service.get_user_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user statistics: {str(e)}")


@statistics_router.get("/categories")
@require_roles("ADMIN")
async def get_category_statistics(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê danh mục: tổng số, active, inactive, số sản phẩm mỗi danh mục
    """
    try:
        stats = await statistics_service.get_category_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting category statistics: {str(e)}")


@statistics_router.get("/brands")
@require_roles("ADMIN")
async def get_brand_statistics(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê thương hiệu: tổng số, active, inactive, số sản phẩm mỗi thương hiệu
    """
    try:
        stats = await statistics_service.get_brand_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting brand statistics: {str(e)}")


@statistics_router.get("/products")
@require_roles("ADMIN")
async def get_product_statistics(
    statistics_service: StatisticsService = Depends(get_statistics_service)
):
    """
    Thống kê sản phẩm: tổng số, active, inactive, mới trong tháng, tồn kho
    """
    try:
        stats = await statistics_service.get_product_stats()
        return JSONResponse(content=jsonable_encoder(stats), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting product statistics: {str(e)}")

