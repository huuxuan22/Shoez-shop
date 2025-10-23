# Order Management System - SOLID Design Patterns

## Architecture Overview

Hệ thống quản lý đơn hàng đã được refactor để tuân thủ các nguyên tắc SOLID và Design Patterns tốt nhất.

## SOLID Principles Implementation

### 1. Single Responsibility Principle (SRP)
- **OrderController**: Chỉ xử lý HTTP requests/responses
- **OrderService**: Chỉ xử lý business logic của orders
- **OrderFilterService**: Chỉ xử lý logic filter và search
- **OrderQueryBuilder**: Chỉ xây dựng MongoDB queries
- **PaginationBuilder**: Chỉ xử lý logic pagination

### 2. Open/Closed Principle (OCP)
- **OrderQueryBuilder**: Có thể mở rộng thêm filter mới mà không sửa code cũ
- **IOrderService**: Interface cho phép implement các service khác nhau

### 3. Liskov Substitution Principle (LSP)
- **OrderService** implement **IOrderService** có thể thay thế nhau
- **OrderFilterService** có thể hoạt động với bất kỳ implementation nào của IOrderService

### 4. Interface Segregation Principle (ISP)
- **IOrderService**: Interface nhỏ, tập trung vào các method cần thiết
- Không có interface lớn với nhiều method không liên quan

### 5. Dependency Inversion Principle (DIP)
- **OrderController** phụ thuộc vào **OrderFilterService** (abstraction)
- **OrderFilterService** phụ thuộc vào **IOrderService** (abstraction)
- Dependency injection được sử dụng thông qua FastAPI Depends

## Design Patterns Used

### 1. Builder Pattern
- **OrderQueryBuilder**: Xây dựng MongoDB queries một cách linh hoạt
- **PaginationBuilder**: Xây dựng pagination parameters

### 2. Dependency Injection Pattern
- Sử dụng FastAPI Depends để inject dependencies
- `get_order_filter_service()` function tạo và inject OrderFilterService

### 3. Service Layer Pattern
- **OrderService**: Core business logic
- **OrderFilterService**: Specialized service cho filtering

### 4. Repository Pattern
- **OrderRepository**: Data access layer
- **BaseRepository**: Generic repository với common operations

## File Structure

```
api/
├── controllers/
│   └── order_controller.py          # HTTP layer
├── services/
│   ├── order_service.py            # Core business logic
│   └── order_filter_service.py     # Filtering logic
├── interfaces/
│   └── order_service_interface.py   # Service contracts
├── utils/
│   └── query_builder.py            # Query building utilities
└── repositories/
    └── order_repository.py         # Data access layer
```

## API Endpoints

### Main Filtering Endpoint
```
GET /orders/admin/orders
Parameters:
- page: int (default: 1)
- limit: int (default: 20, max: 100)
- starttime: str (ISO format, optional)
- endtime: str (ISO format, optional)
- valueSearch: str (optional)
```

### Specialized Endpoints
```
GET /orders/admin/search?q={query}&page={page}&limit={limit}
GET /orders/admin/by-status?status={status}&page={page}&limit={limit}
GET /orders/admin/by-date-range?start_date={date}&end_date={date}&page={page}&limit={limit}
```

## Benefits of This Architecture

1. **Maintainability**: Mỗi class có một trách nhiệm rõ ràng
2. **Testability**: Dễ dàng mock dependencies và test từng component
3. **Extensibility**: Dễ dàng thêm filter mới hoặc service mới
4. **Reusability**: QueryBuilder và PaginationBuilder có thể tái sử dụng
5. **Flexibility**: Có thể thay đổi implementation mà không ảnh hưởng client code

## Usage Examples

### Basic Filtering
```python
# Controller sử dụng OrderFilterService
result = await filter_service.get_filtered_orders(
    page=1,
    limit=20,
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-12-31T23:59:59Z",
    search_value="pending"
)
```

### Query Building
```python
# Sử dụng QueryBuilder để tạo complex queries
query = (OrderQueryBuilder()
    .add_time_filter(start_time, end_time)
    .add_search_filter(search_value)
    .add_status_filter("pending")
    .build())
```

### Pagination
```python
# Sử dụng PaginationBuilder
pagination = PaginationBuilder(page=1, limit=20)
skip = pagination.get_skip()
limit = pagination.get_limit()
total_pages = pagination.calculate_total_pages(total_items)
```

## Future Enhancements

1. **Caching Layer**: Thêm Redis cache cho frequently accessed data
2. **Event Sourcing**: Track order state changes
3. **CQRS**: Separate read/write models
4. **Microservices**: Split thành các service nhỏ hơn
5. **GraphQL**: Thay thế REST API với GraphQL
