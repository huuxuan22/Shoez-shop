from typing import Dict, Any, Optional, List
from datetime import datetime
from bson import ObjectId


class OrderQueryBuilder:
    """
    Query Builder pattern để xây dựng MongoDB queries cho Orders
    Tuân thủ Single Responsibility Principle
    """
    
    def __init__(self):
        self._query: Dict[str, Any] = {}
        self._sort: List[tuple] = [("created_at", -1)]  # Default sort by created_at DESC
    
    def build(self) -> Dict[str, Any]:
        """Trả về query đã được xây dựng"""
        return self._query
    
    def get_sort(self) -> List[tuple]:
        """Trả về sort criteria"""
        return self._sort
    
    def reset(self) -> 'OrderQueryBuilder':
        """Reset query builder"""
        self._query = {}
        self._sort = [("created_at", -1)]
        return self
    
    def add_time_filter(self, start_time: Optional[str] = None, end_time: Optional[str] = None) -> 'OrderQueryBuilder':
        """
        Thêm filter theo thời gian
        """
        if not start_time and not end_time:
            return self
            
        time_filter = {}
        if start_time:
            time_filter["$gte"] = self._parse_datetime(start_time)
        if end_time:
            time_filter["$lte"] = self._parse_datetime(end_time)
            
        self._query["created_at"] = time_filter
        return self
    
    def add_search_filter(self, search_value: Optional[str] = None) -> 'OrderQueryBuilder':
        """
        Thêm filter tìm kiếm theo order ID, user ID, hoặc status
        """
        if not search_value:
            return self
            
        # Tạo regex pattern không phân biệt hoa thường
        regex_pattern = {"$regex": search_value, "$options": "i"}
        
        # Tìm kiếm trong các field
        search_conditions = [
            {"user_id": regex_pattern},
            {"status": regex_pattern}
        ]
        
        # Thêm search cho _id field nhưng không convert thành ObjectId
        # Để tránh lỗi serialization, chỉ search bằng regex
        search_conditions.append({"_id": regex_pattern})
        
        # Nếu đã có $or trong query, merge với điều kiện mới
        if "$or" in self._query:
            self._query["$and"] = [
                {"$or": self._query["$or"]},
                {"$or": search_conditions}
            ]
            del self._query["$or"]
        else:
            self._query["$or"] = search_conditions
            
        return self
    
    def add_status_filter(self, status: Optional[str] = None) -> 'OrderQueryBuilder':
        """
        Thêm filter theo status
        """
        if status:
            self._query["status"] = status
        return self
    
    def add_user_filter(self, user_id: Optional[str] = None) -> 'OrderQueryBuilder':
        """
        Thêm filter theo user_id
        """
        if user_id:
            self._query["user_id"] = user_id
        return self
    
    def add_custom_filter(self, field: str, value: Any, operator: str = "$eq") -> 'OrderQueryBuilder':
        """
        Thêm custom filter
        """
        if value is not None:
            if operator == "$eq":
                self._query[field] = value
            else:
                self._query[field] = {operator: value}
        return self
    
    def set_sort(self, field: str, direction: int = -1) -> 'OrderQueryBuilder':
        """
        Set sort criteria
        """
        self._sort = [(field, direction)]
        return self
    
    def add_sort(self, field: str, direction: int = -1) -> 'OrderQueryBuilder':
        """
        Thêm sort criteria
        """
        self._sort.append((field, direction))
        return self
    
    @staticmethod
    def _parse_datetime(time_str: str) -> datetime:
        """
        Parse datetime string thành datetime object
        """
        try:
            # Xử lý timezone Z thành +00:00
            if time_str.endswith('Z'):
                time_str = time_str.replace('Z', '+00:00')
            return datetime.fromisoformat(time_str)
        except ValueError:
            raise ValueError(f"Invalid datetime format: {time_str}")


class PaginationBuilder:
    """
    Builder pattern cho pagination
    """
    
    def __init__(self, page: int = 1, limit: int = 20):
        self.page = max(1, page)
        self.limit = max(1, min(100, limit))  # Giới hạn tối đa 100 items per page
    
    def get_skip(self) -> int:
        """Tính số records cần skip"""
        return (self.page - 1) * self.limit
    
    def get_limit(self) -> int:
        """Trả về limit"""
        return self.limit
    
    def get_page(self) -> int:
        """Trả về page number"""
        return self.page
    
    def calculate_total_pages(self, total_items: int) -> int:
        """Tính tổng số pages"""
        return (total_items + self.limit - 1) // self.limit
