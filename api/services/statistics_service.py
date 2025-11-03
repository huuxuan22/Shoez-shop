from typing import Dict, Any, List
from datetime import datetime, timedelta
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from repositories.category_repository import CategoryRepository
from repositories.brand_repository import BrandRepository


class StatisticsService:
    def __init__(
        self,
        order_repo: OrderRepository,
        product_repo: ProductRepository,
        user_repo: UserRepository,
        category_repo: CategoryRepository = None,
        brand_repo: BrandRepository = None
    ):
        self.order_repo = order_repo
        self.product_repo = product_repo
        self.user_repo = user_repo
        self.category_repo = category_repo
        self.brand_repo = brand_repo

    async def get_overview_stats(self) -> Dict[str, Any]:
        """Lấy thống kê tổng quan"""
        try:
            # Tổng số đơn hàng
            total_orders = await self.order_repo.collection.count_documents({})
            
            # Tổng doanh thu (từ các đơn hàng đã hoàn thành)
            completed_orders = await self.order_repo.collection.find(
                {"status": {"$in": ["complete", "completed", "delivered"]}}
            ).to_list(length=None)
            total_revenue = sum(order.get("total", 0) for order in completed_orders)
            
            # Tổng số sản phẩm
            total_products = await self.product_repo.count({})
            
            # Tổng số khách hàng (users không phải admin, và không bị xóa)
            total_customers = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True}
            })
            
            # Đơn hàng tháng này - xử lý cả datetime object và string
            now = datetime.now()
            start_of_month = datetime(now.year, now.month, 1)
            orders_this_month = await self.order_repo.collection.find({
                "created_at": {"$gte": start_of_month}
            }).to_list(length=None)
            monthly_revenue = sum(order.get("total", 0) for order in orders_this_month if order.get("status") in ["complete", "completed", "delivered"])
            monthly_orders = len(orders_this_month)
            
            # Đơn hàng tháng trước (để so sánh)
            if now.month == 1:
                start_of_last_month = datetime(now.year - 1, 12, 1)
                end_of_last_month = datetime(now.year, 1, 1) - timedelta(seconds=1)
            else:
                start_of_last_month = datetime(now.year, now.month - 1, 1)
                end_of_last_month = datetime(now.year, now.month, 1) - timedelta(seconds=1)
            
            orders_last_month = await self.order_repo.collection.find({
                "created_at": {
                    "$gte": start_of_last_month,
                    "$lte": end_of_last_month
                }
            }).to_list(length=None)
            last_month_revenue = sum(order.get("total", 0) for order in orders_last_month if order.get("status") in ["complete", "completed", "delivered"])
            last_month_orders = len(orders_last_month)
        
            # Tính phần trăm thay đổi
            revenue_change = 0
            if last_month_revenue > 0:
                revenue_change = ((monthly_revenue - last_month_revenue) / last_month_revenue) * 100
            
            orders_change = 0
            if last_month_orders > 0:
                orders_change = ((monthly_orders - last_month_orders) / last_month_orders) * 100
            
            # Đếm đơn hàng theo trạng thái
            status_counts = {
                "pending": await self.order_repo.collection.count_documents({"status": "pending"}),
                "confirmed": await self.order_repo.collection.count_documents({"status": "confirmed"}),
                "shipping": await self.order_repo.collection.count_documents({"status": "shipping"}),
                "complete": await self.order_repo.collection.count_documents({"status": {"$in": ["complete", "completed", "delivered"]}}),
                "cancelled": await self.order_repo.collection.count_documents({"status": {"$in": ["cancelled", "canceled"]}})
            }
            
            return {
                "total_revenue": total_revenue,
                "total_orders": total_orders,
                "total_products": total_products,
                "total_customers": total_customers,
                "monthly_revenue": monthly_revenue,
                "monthly_orders": monthly_orders,
                "revenue_change": round(revenue_change, 2),
                "orders_change": round(orders_change, 2),
                "status_counts": status_counts
            }
        except Exception as e:
            # Trả về giá trị mặc định để tránh crash
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_revenue": 0,
                "total_orders": 0,
                "total_products": 0,
                "total_customers": 0,
                "monthly_revenue": 0,
                "monthly_orders": 0,
                "revenue_change": 0,
                "orders_change": 0,
                "status_counts": {
                    "pending": 0,
                    "confirmed": 0,
                    "shipping": 0,
                    "complete": 0,
                    "cancelled": 0
                }
            }

    async def get_revenue_chart_data(self, days: int = 7) -> List[Dict[str, Any]]:
        """Lấy dữ liệu biểu đồ doanh thu theo ngày"""
        try:
            now = datetime.now()
            chart_data = []
            
            for i in range(days - 1, -1, -1):
                date = now - timedelta(days=i)
                start_of_day = datetime(date.year, date.month, date.day, 0, 0, 0)
                end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)
                
                # Tìm đơn hàng trong ngày (không filter status để có thể thấy tất cả)
                # Nhưng chỉ tính doanh thu từ đơn hàng đã hoàn thành
                # Hỗ trợ cả datetime object và string ISO format
                start_str = start_of_day.isoformat()
                end_str = end_of_day.isoformat()
                
                # Query với cả datetime, ISO string và string chỉ có ngày (YYYY-MM-DD)
                all_orders = await self.order_repo.collection.find({
                    "$or": [
                        # Trường hợp created_at là datetime thực sự
                        {
                            "created_at": {
                                "$gte": start_of_day,
                                "$lte": end_of_day
                            }
                        },
                        # Trường hợp created_at là ISO string (có thời gian)
                        {
                            "created_at": {
                                "$gte": start_str,
                                "$lte": end_str
                            }
                        },
                        # Trường hợp created_at là string dạng chỉ có ngày: "YYYY-MM-DD" hoặc "YYYY-MM-DD ..."
                        {
                            "created_at": {"$regex": f"^{date.strftime('%Y-%m-%d')}"}
                        }
                    ]
                }).to_list(length=None)
                
                # Chỉ tính doanh thu từ đơn hàng đã hoàn thành
                completed_orders = [o for o in all_orders if o.get("status") in ["complete", "completed", "delivered"]]
                revenue = sum(order.get("total", 0) for order in completed_orders)
                order_count = len(all_orders)  # Tổng số đơn hàng trong ngày
                
                # Map day names to Vietnamese
                day_names_vn = {
                    'Monday': 'Thứ Hai',
                    'Tuesday': 'Thứ Ba',
                    'Wednesday': 'Thứ Tư',
                    'Thursday': 'Thứ Năm',
                    'Friday': 'Thứ Sáu',
                    'Saturday': 'Thứ Bảy',
                    'Sunday': 'Chủ Nhật'
                }
                day_name_en = date.strftime("%A")
                day_name_vn = day_names_vn.get(day_name_en, day_name_en)
                
                chart_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "day_name": day_name_vn if days <= 7 else date.strftime("%d/%m"),
                    "revenue": revenue,
                    "orders": order_count
                })
            
            return chart_data
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return []

    async def get_top_products(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Lấy top sản phẩm bán chạy nhất"""
        try:
            # Lấy tất cả đơn hàng (bao gồm cả pending để có dữ liệu hiển thị)
            # Nhưng ưu tiên đơn hàng đã hoàn thành
            all_orders = await self.order_repo.collection.find({}).to_list(length=None)
            
            # Đếm số lượng bán của từng sản phẩm
            product_sales = {}
            for order in all_orders:
                # Ưu tiên đơn hàng đã hoàn thành, nhưng vẫn tính cả pending
                status = order.get("status", "pending")
                items = order.get("items", [])
                
                for item in items:
                    product_id = item.get("product_id") or item.get("id") or item.get("productId")
                    product_name = item.get("name", item.get("productName", "Unknown"))
                    quantity = item.get("quantity", item.get("qty", 1))
                    price = item.get("price", item.get("productPrice", 0))
                    
                    if product_id:
                        if product_id not in product_sales:
                            product_sales[product_id] = {
                                "product_id": product_id,
                                "name": product_name,
                                "sold": 0,
                                "revenue": 0
                            }
                        product_sales[product_id]["sold"] += quantity
                        # Chỉ tính revenue từ đơn hàng đã hoàn thành
                        if status in ["complete", "completed", "delivered"]:
                            product_sales[product_id]["revenue"] += price * quantity
            
            # Sắp xếp theo số lượng bán
            top_products = sorted(
                product_sales.values(),
                key=lambda x: x["sold"],
                reverse=True
            )[:limit]
            
            return top_products
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return []

    async def get_recent_orders(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Lấy các đơn hàng gần đây"""
        try:
            orders = await self.order_repo.collection.find({}).sort(
                "created_at", -1
            ).limit(limit).to_list(length=limit)
            
            recent_orders = []
            for order in orders:
                order_id = str(order.get("_id", ""))
                created_at = order.get("created_at")
                # Xử lý cả datetime object và string
                if isinstance(created_at, datetime):
                    date_str = created_at.strftime("%Y-%m-%d")
                elif isinstance(created_at, str):
                    date_str = created_at[:10] if len(created_at) >= 10 else ""
                else:
                    date_str = ""
                
                recent_orders.append({
                    "id": order_id,
                    "customer": order.get("fullName", "Unknown"),
                    "date": date_str,
                    "total": order.get("total", 0),
                    "status": order.get("status", "pending")
                })
            
            return recent_orders
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return []

    async def get_detailed_revenue_stats(self) -> Dict[str, Any]:
        """Thống kê doanh thu chi tiết: hôm nay, tuần này, tháng này, năm này"""
        try:
            now = datetime.now()
            
            # Hôm nay - lấy tất cả đơn hàng, nhưng chỉ tính revenue từ đơn đã hoàn thành
            today_start = datetime(now.year, now.month, now.day, 0, 0, 0)
            today_end = datetime(now.year, now.month, now.day, 23, 59, 59)
            today_start_str = today_start.isoformat()
            today_end_str = today_end.isoformat()
            
            today_all_orders = await self.order_repo.collection.find({
                "$or": [
                    {"created_at": {"$gte": today_start, "$lte": today_end}},
                    {"created_at": {"$gte": today_start_str, "$lte": today_end_str}}
                ]
            }).to_list(length=None)
            today_completed = [o for o in today_all_orders if o.get("status") in ["complete", "completed", "delivered"]]
            today_revenue = sum(order.get("total", 0) for order in today_completed)
            today_count = len(today_all_orders)
            
            # Tuần này (từ thứ 2 đến hôm nay)
            days_since_monday = (now.weekday()) % 7
            week_start = datetime(now.year, now.month, now.day, 0, 0, 0) - timedelta(days=days_since_monday)
            week_start_str = week_start.isoformat()
            
            week_all_orders = await self.order_repo.collection.find({
                "$or": [
                    {"created_at": {"$gte": week_start}},
                    {"created_at": {"$gte": week_start_str}}
                ]
            }).to_list(length=None)
            week_completed = [o for o in week_all_orders if o.get("status") in ["complete", "completed", "delivered"]]
            week_revenue = sum(order.get("total", 0) for order in week_completed)
            week_count = len(week_all_orders)
            
            # Tháng này
            month_start = datetime(now.year, now.month, 1)
            month_start_str = month_start.isoformat()
            
            month_all_orders = await self.order_repo.collection.find({
                "$or": [
                    {"created_at": {"$gte": month_start}},
                    {"created_at": {"$gte": month_start_str}}
                ]
            }).to_list(length=None)
            month_completed = [o for o in month_all_orders if o.get("status") in ["complete", "completed", "delivered"]]
            month_revenue = sum(order.get("total", 0) for order in month_completed)
            month_count = len(month_all_orders)
            
            # Năm này
            year_start = datetime(now.year, 1, 1)
            year_start_str = year_start.isoformat()
            
            year_all_orders = await self.order_repo.collection.find({
                "$or": [
                    {"created_at": {"$gte": year_start}},
                    {"created_at": {"$gte": year_start_str}}
                ]
            }).to_list(length=None)
            year_completed = [o for o in year_all_orders if o.get("status") in ["complete", "completed", "delivered"]]
            year_revenue = sum(order.get("total", 0) for order in year_completed)
            year_count = len(year_all_orders)
            
            return {
                "today": {"revenue": today_revenue, "orders": today_count},
                "this_week": {"revenue": week_revenue, "orders": week_count},
                "this_month": {"revenue": month_revenue, "orders": month_count},
                "this_year": {"revenue": year_revenue, "orders": year_count}
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "today": {"revenue": 0, "orders": 0},
                "this_week": {"revenue": 0, "orders": 0},
                "this_month": {"revenue": 0, "orders": 0},
                "this_year": {"revenue": 0, "orders": 0}
            }

    async def get_detailed_order_stats(self) -> Dict[str, Any]:
        """Thống kê đơn hàng chi tiết theo trạng thái và thời gian"""
        try:
            now = datetime.now()
            
            # Đếm theo trạng thái
            status_stats = {
                "pending": await self.order_repo.collection.count_documents({"status": "pending"}),
                "confirmed": await self.order_repo.collection.count_documents({"status": "confirmed"}),
                "shipping": await self.order_repo.collection.count_documents({"status": "shipping"}),
                "complete": await self.order_repo.collection.count_documents({"status": {"$in": ["complete", "completed", "delivered"]}}),
                "cancelled": await self.order_repo.collection.count_documents({"status": {"$in": ["cancelled", "canceled"]}})
            }
            
            total_orders = sum(status_stats.values())
            
            # Đơn hàng hôm nay
            today_start = datetime(now.year, now.month, now.day, 0, 0, 0)
            today_end = datetime(now.year, now.month, now.day, 23, 59, 59)
            today_orders = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": today_start, "$lte": today_end}
            })
            
            # Đơn hàng tuần này
            days_since_monday = (now.weekday()) % 7
            week_start = datetime(now.year, now.month, now.day, 0, 0, 0) - timedelta(days=days_since_monday)
            week_orders = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": week_start}
            })
            
            # Đơn hàng tháng này
            month_start = datetime(now.year, now.month, 1)
            month_orders = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": month_start}
            })
            
            return {
                "by_status": status_stats,
                "total": total_orders,
                "today": today_orders,
                "this_week": week_orders,
                "this_month": month_orders,
                "status_percentages": {
                    status: round((count / total_orders * 100), 2) if total_orders > 0 else 0
                    for status, count in status_stats.items()
                }
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "by_status": {"pending": 0, "confirmed": 0, "shipping": 0, "complete": 0, "cancelled": 0},
                "total": 0,
                "today": 0,
                "this_week": 0,
                "this_month": 0,
                "status_percentages": {}
            }

    async def get_cancellation_stats(self) -> Dict[str, Any]:
        """Thống kê hủy hàng chi tiết"""
        try:
            now = datetime.now()
            
            # Tổng số đơn hàng đã hủy
            total_cancelled = await self.order_repo.collection.count_documents({
                "status": {"$in": ["cancelled", "canceled"]}
            })
            
            # Tổng doanh thu mất do hủy
            cancelled_orders = await self.order_repo.collection.find({
                "status": {"$in": ["cancelled", "canceled"]}
            }).to_list(length=None)
            lost_revenue = sum(order.get("total", 0) for order in cancelled_orders)
            
            # Tổng số đơn hàng
            total_orders = await self.order_repo.collection.count_documents({})
            
            # Tỷ lệ hủy
            cancellation_rate = (total_cancelled / total_orders * 100) if total_orders > 0 else 0
            
            # Hủy hôm nay
            today_start = datetime(now.year, now.month, now.day, 0, 0, 0)
            today_end = datetime(now.year, now.month, now.day, 23, 59, 59)
            today_cancelled = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": today_start, "$lte": today_end},
                "status": {"$in": ["cancelled", "canceled"]}
            })
            
            # Hủy tuần này
            days_since_monday = (now.weekday()) % 7
            week_start = datetime(now.year, now.month, now.day, 0, 0, 0) - timedelta(days=days_since_monday)
            week_cancelled = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": week_start},
                "status": {"$in": ["cancelled", "canceled"]}
            })
            
            # Hủy tháng này
            month_start = datetime(now.year, now.month, 1)
            month_cancelled = await self.order_repo.collection.count_documents({
                "created_at": {"$gte": month_start},
                "status": {"$in": ["cancelled", "canceled"]}
            })
            
            # Doanh thu mất theo thời gian
            today_cancelled_orders = await self.order_repo.collection.find({
                "created_at": {"$gte": today_start, "$lte": today_end},
                "status": {"$in": ["cancelled", "canceled"]}
            }).to_list(length=None)
            today_lost_revenue = sum(order.get("total", 0) for order in today_cancelled_orders)
            
            week_cancelled_orders = await self.order_repo.collection.find({
                "created_at": {"$gte": week_start},
                "status": {"$in": ["cancelled", "canceled"]}
            }).to_list(length=None)
            week_lost_revenue = sum(order.get("total", 0) for order in week_cancelled_orders)
            
            month_cancelled_orders = await self.order_repo.collection.find({
                "created_at": {"$gte": month_start},
                "status": {"$in": ["cancelled", "canceled"]}
            }).to_list(length=None)
            month_lost_revenue = sum(order.get("total", 0) for order in month_cancelled_orders)
            
            # Đơn hàng hủy gần đây (5 đơn mới nhất)
            recent_cancelled = await self.order_repo.collection.find({
                "status": {"$in": ["cancelled", "canceled"]}
            }).sort("created_at", -1).limit(5).to_list(length=5)
            
            recent_cancelled_list = []
            for order in recent_cancelled:
                order_id = str(order.get("_id", ""))
                created_at = order.get("created_at")
                if isinstance(created_at, datetime):
                    date_str = created_at.strftime("%Y-%m-%d")
                elif isinstance(created_at, str):
                    date_str = created_at[:10] if len(created_at) >= 10 else ""
                else:
                    date_str = ""
                
                recent_cancelled_list.append({
                    "id": order_id,
                    "customer": order.get("fullName", "Unknown"),
                    "date": date_str,
                    "total": order.get("total", 0)
                })
            
            return {
                "total_cancelled": total_cancelled,
                "total_orders": total_orders,
                "cancellation_rate": round(cancellation_rate, 2),
                "lost_revenue": lost_revenue,
                "today": {"count": today_cancelled, "lost_revenue": today_lost_revenue},
                "this_week": {"count": week_cancelled, "lost_revenue": week_lost_revenue},
                "this_month": {"count": month_cancelled, "lost_revenue": month_lost_revenue},
                "recent_cancelled": recent_cancelled_list
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_cancelled": 0,
                "total_orders": 0,
                "cancellation_rate": 0,
                "lost_revenue": 0,
                "today": {"count": 0, "lost_revenue": 0},
                "this_week": {"count": 0, "lost_revenue": 0},
                "this_month": {"count": 0, "lost_revenue": 0},
                "recent_cancelled": []
            }

    async def get_user_stats(self) -> Dict[str, Any]:
        """Thống kê người dùng: tổng số, active, inactive, mới trong tháng"""
        try:
            now = datetime.now()
            start_of_month = datetime(now.year, now.month, 1)
            
            # Tổng số người dùng (không phải admin, không bị xóa)
            total_users = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True}
            })
            
            # Số người dùng active (không bị xóa, có thể có trường is_active)
            active_users = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True},
                "$or": [
                    {"is_active": True},
                    {"is_active": {"$exists": False}}
                ]
            })
            
            # Số người dùng inactive
            inactive_users = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True},
                "is_active": False
            })
            
            # Người dùng mới trong tháng này
            new_users_this_month = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True},
                "$or": [
                    {"created_at": {"$gte": start_of_month}},
                    {"created_at": {"$gte": start_of_month.isoformat()}}
                ]
            })
            
            # Người dùng mới trong tuần này
            days_since_monday = (now.weekday()) % 7
            week_start = datetime(now.year, now.month, now.day, 0, 0, 0) - timedelta(days=days_since_monday)
            new_users_this_week = await self.user_repo.collection.count_documents({
                "role": {"$ne": "ADMIN"},
                "is_deleted": {"$ne": True},
                "$or": [
                    {"created_at": {"$gte": week_start}},
                    {"created_at": {"$gte": week_start.isoformat()}}
                ]
            })
            
            # Tổng số admin
            total_admins = await self.user_repo.collection.count_documents({
                "role": "ADMIN",
                "is_deleted": {"$ne": True}
            })
            
            return {
                "total_users": total_users,
                "active_users": active_users,
                "inactive_users": inactive_users,
                "new_users_this_month": new_users_this_month,
                "new_users_this_week": new_users_this_week,
                "total_admins": total_admins
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_users": 0,
                "active_users": 0,
                "inactive_users": 0,
                "new_users_this_month": 0,
                "new_users_this_week": 0,
                "total_admins": 0
            }

    async def get_category_stats(self) -> Dict[str, Any]:
        """Thống kê danh mục: tổng số, active, inactive, số sản phẩm mỗi danh mục"""
        try:
            if not self.category_repo:
                return {
                    "total_categories": 0,
                    "active_categories": 0,
                    "inactive_categories": 0,
                    "categories_with_products": []
                }
            
            # Tổng số danh mục
            total_categories = await self.category_repo.collection.count_documents({})
            
            # Số danh mục active
            active_categories = await self.category_repo.collection.count_documents({
                "$or": [
                    {"is_active": True},
                    {"is_active": {"$exists": False}}
                ]
            })
            
            # Số danh mục inactive
            inactive_categories = await self.category_repo.collection.count_documents({
                "is_active": False
            })
            
            # Lấy tất cả danh mục và đếm số sản phẩm trong mỗi danh mục
            categories = await self.category_repo.collection.find({}).to_list(length=None)
            categories_with_products = []
            
            for category in categories:
                category_id = str(category.get("_id", ""))
                category_name = category.get("name", "Unknown")
                
                # Đếm số sản phẩm trong danh mục này
                # Giả sử products có field category_id hoặc category
                products_count = await self.product_repo.collection.count_documents({
                    "$or": [
                        {"category_id": category_id},
                        {"category": category_id},
                        {"category": category_name}
                    ]
                })
                
                categories_with_products.append({
                    "id": category_id,
                    "name": category_name,
                    "is_active": category.get("is_active", True),
                    "products_count": products_count
                })
            
            # Sắp xếp theo số sản phẩm giảm dần
            categories_with_products.sort(key=lambda x: x["products_count"], reverse=True)
            
            return {
                "total_categories": total_categories,
                "active_categories": active_categories,
                "inactive_categories": inactive_categories,
                "categories_with_products": categories_with_products
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_categories": 0,
                "active_categories": 0,
                "inactive_categories": 0,
                "categories_with_products": []
            }

    async def get_brand_stats(self) -> Dict[str, Any]:
        """Thống kê thương hiệu: tổng số, active, inactive, số sản phẩm mỗi thương hiệu"""
        try:
            if not self.brand_repo:
                return {
                    "total_brands": 0,
                    "active_brands": 0,
                    "inactive_brands": 0,
                    "brands_with_products": []
                }
            
            # Tổng số thương hiệu (không bị xóa)
            total_brands = await self.brand_repo.collection.count_documents({
                "$or": [
                    {"is_deleted": False},
                    {"is_deleted": {"$exists": False}}
                ]
            })
            
            # Số thương hiệu active (không bị xóa và is_active = True)
            active_brands = await self.brand_repo.collection.count_documents({
                "$or": [
                    {"is_deleted": False},
                    {"is_deleted": {"$exists": False}}
                ],
                "$or": [
                    {"is_active": True},
                    {"is_active": {"$exists": False}}
                ]
            })
            
            # Số thương hiệu inactive
            inactive_brands = await self.brand_repo.collection.count_documents({
                "$or": [
                    {"is_deleted": False},
                    {"is_deleted": {"$exists": False}}
                ],
                "is_active": False
            })
            
            # Lấy tất cả thương hiệu và đếm số sản phẩm trong mỗi thương hiệu
            brands = await self.brand_repo.collection.find({
                "$or": [
                    {"is_deleted": False},
                    {"is_deleted": {"$exists": False}}
                ]
            }).to_list(length=None)
            
            brands_with_products = []
            for brand in brands:
                brand_id = str(brand.get("_id", ""))
                brand_name = brand.get("name", "Unknown")
                
                # Đếm số sản phẩm trong thương hiệu này
                products_count = await self.product_repo.collection.count_documents({
                    "$or": [
                        {"brand_id": brand_id},
                        {"brand": brand_id},
                        {"brand": brand_name}
                    ]
                })
                
                brands_with_products.append({
                    "id": brand_id,
                    "name": brand_name,
                    "is_active": brand.get("is_active", True),
                    "products_count": products_count
                })
            
            # Sắp xếp theo số sản phẩm giảm dần
            brands_with_products.sort(key=lambda x: x["products_count"], reverse=True)
            
            return {
                "total_brands": total_brands,
                "active_brands": active_brands,
                "inactive_brands": inactive_brands,
                "brands_with_products": brands_with_products
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_brands": 0,
                "active_brands": 0,
                "inactive_brands": 0,
                "brands_with_products": []
            }

    async def get_product_stats(self) -> Dict[str, Any]:
        """Thống kê sản phẩm: tổng số, active, inactive, mới trong tháng, tồn kho"""
        try:
            now = datetime.now()
            start_of_month = datetime(now.year, now.month, 1)
            
            # Tổng số sản phẩm
            total_products = await self.product_repo.collection.count_documents({})
            
            # Số sản phẩm active (có thể có trường is_active hoặc status)
            active_products = await self.product_repo.collection.count_documents({
                "$or": [
                    {"is_active": True},
                    {"status": "active"},
                    {"is_active": {"$exists": False}, "status": {"$exists": False}}
                ]
            })
            
            # Số sản phẩm inactive
            inactive_products = await self.product_repo.collection.count_documents({
                "$or": [
                    {"is_active": False},
                    {"status": {"$in": ["inactive", "disabled"]}}
                ]
            })
            
            # Sản phẩm mới trong tháng này
            new_products_this_month = await self.product_repo.collection.count_documents({
                "$or": [
                    {"created_at": {"$gte": start_of_month}},
                    {"created_at": {"$gte": start_of_month.isoformat()}}
                ]
            })
            
            # Sản phẩm mới trong tuần này
            days_since_monday = (now.weekday()) % 7
            week_start = datetime(now.year, now.month, now.day, 0, 0, 0) - timedelta(days=days_since_monday)
            new_products_this_week = await self.product_repo.collection.count_documents({
                "$or": [
                    {"created_at": {"$gte": week_start}},
                    {"created_at": {"$gte": week_start.isoformat()}}
                ]
            })
            
            # Tổng số tồn kho (tổng stock của tất cả sản phẩm)
            products = await self.product_repo.collection.find({}).to_list(length=None)
            total_stock = 0
            low_stock_count = 0  # Sản phẩm có stock < 10
            
            for product in products:
                # Tính tổng stock từ sizes array
                sizes = product.get("sizes", [])
                product_stock = sum(size.get("stock", 0) for size in sizes if isinstance(size, dict))
                total_stock += product_stock
                
                if product_stock < 10:
                    low_stock_count += 1
            
            # Sản phẩm hết hàng (stock = 0)
            out_of_stock_count = 0
            for product in products:
                sizes = product.get("sizes", [])
                product_stock = sum(size.get("stock", 0) for size in sizes if isinstance(size, dict))
                if product_stock == 0:
                    out_of_stock_count += 1
            
            return {
                "total_products": total_products,
                "active_products": active_products,
                "inactive_products": inactive_products,
                "new_products_this_month": new_products_this_month,
                "new_products_this_week": new_products_this_week,
                "total_stock": total_stock,
                "low_stock_count": low_stock_count,
                "out_of_stock_count": out_of_stock_count
            }
        except Exception as e:
            import traceback
            traceback.format_exc()  # Giữ lại để có thể debug nếu cần
            return {
                "total_products": 0,
                "active_products": 0,
                "inactive_products": 0,
                "new_products_this_month": 0,
                "new_products_this_week": 0,
                "total_stock": 0,
                "low_stock_count": 0,
                "out_of_stock_count": 0
            }

