import  logging
from config.context import request_id
from config.config import get_settings

settings = get_settings()

# thằng này là để điều chỉnh format khi log ra dưới terminal
class OnlineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(OnlineExceptionFormatter,self).formatException(exc_info)
        return result

    def format(self, record):
        s = super(OnlineExceptionFormatter,self).format(record)

        if record:
            s = s.replace("\n", " ").replace("\r", " ")

        return s

# thằng này được gọi mỗi khi sự kiện log được gọi và nó sẽ
# tự động thêm request_id vào
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        return True


# Tạo một formatter tùy chỉnh để định dạng log theo chuỗi định sẵn
formatter = OnlineExceptionFormatter(
    "%(asctime)-15s - %(request_id)s - %(name)-5s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s"
)

# Lấy logger có tên "app.fastapi" để dùng trong app FastAPI của bạn
logger = logging.getLogger("app.fastapi")

# Đặt mức log tối thiểu của logger là DEBUG (ghi tất cả log từ DEBUG trở lên)
logger.setLevel(logging.DEBUG)

# Tạo một handler để log xuất ra console (terminal)
console_handle = logging.StreamHandler()

# Gán formatter đã tạo cho handler này, để log hiển thị theo định dạng trên
console_handle.setFormatter(formatter)

# Thêm filter để gán thêm biến `request_id` vào từng bản ghi log
logger.addFilter(ContextFilter())

# Lấy logger riêng để ghi log của SQLAlchemy (thường là các câu lệnh SQL)
sql_logger = logging.getLogger("sqlalchemy.engine.Engine")

# Đặt mức log tối thiểu cho logger SQL là DEBUG (ghi tất cả log DEBUG trở lên)
sql_logger.setLevel(logging.DEBUG)

# Thêm handler để ghi log ra console (terminal)
sql_logger.addHandler(console_handle)

# Thêm filter để gắn thêm biến request_id vào log SQL
sql_logger.addFilter(ContextFilter())


# Tạo handler để ghi log vào file,
# settings.system_log_file là đường dẫn file log,
# "w" nghĩa là mỗi lần chạy sẽ ghi đè file (xóa log cũ),
# encoding="utf-8" để đảm bảo mã hóa ký tự chuẩn UTF-8
file_handler = logging.FileHandler(settings.system_log_file, "w", encoding="utf-8")

# Gán formatter cho handler file để định dạng log giống console
file_handler.setFormatter(formatter)

# Thêm handler ghi log file vào logger chính
logger.addHandler(file_handler)

# Thêm handler ghi log file vào logger SQL
sql_logger.addHandler(file_handler)

# Thêm filter request_id cho logger SQL
sql_logger.addFilter(ContextFilter())


# Ngăn không cho các logger này truyền log lên root logger,
# để tránh ghi log bị trùng (duplicate log)
sql_logger.propagate = 0
logger.propagate = 0

