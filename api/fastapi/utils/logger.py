import logging
import os
from datetime import datetime

# ASCII Art Banner
SHOEZ_BANNER = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ███████╗██╗  ██╗ ██████╗ ███████╗███████╗███████╗          ║
║  ██╔════╝██║  ██║██╔═══██╗██╔════╝██╔════╝╚════██║          ║
║  ███████╗███████║██║   ██║█████╗  █████╗     ██╔╝          ║
║  ╚════██║██╔══██║██║   ██║██╔══╝  ██╔══╝    ██╔╝           ║
║  ███████║██║  ██║╚██████╔╝███████╗██║     ███████╗          ║
║  ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝          ║
║                                                              ║
║  🚀 SHOEZ API SERVER - Ready to Rock! 🚀                    ║
║  Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                    ║
╚══════════════════════════════════════════════════════════════╝
"""

class ShoezLogger:
    def __init__(self, name="SHOEZ"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Create file handler
        if not os.path.exists('logs'):
            os.makedirs('logs')
        file_handler = logging.FileHandler('logs/shoez.log')
        file_handler.setFormatter(logging.Formatter(
            '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        ))
        self.logger.addHandler(file_handler)
    
    def show_banner(self):
        """Display the SHOEZ banner"""
        print(SHOEZ_BANNER)
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def success(self, message):
        """Log success message"""
        self.logger.info(f"✅ {message}")
    
    def database_connected(self, url):
        """Log database connection success"""
        self.logger.info(f"🗄️  Database connected: {url}")
    
    def database_error(self, error):
        """Log database connection error"""
        self.logger.error(f"❌ Database error: {error}")
    
    def minio_connected(self, url):
        """Log MinIO connection success"""
        self.logger.info(f"☁️  MinIO connected: {url}")
    
    def minio_error(self, error):
        """Log MinIO connection error"""
        self.logger.error(f"❌ MinIO error: {error}")
    
    def server_started(self, host, port):
        """Log server start"""
        self.logger.info(f"🚀 Server started at http://{host}:{port}")
    
    def api_endpoint(self, method, path):
        """Log API endpoint access"""
        self.logger.info(f"📡 {method} {path}")

# Create global logger instance
logger = ShoezLogger()
