import axios from "axios";
import { API_URL } from "@/config/url/url";

// Create axios instance with enhanced configuration
const BaseAxios = axios.create({
  baseURL: API_URL,
  timeout: 30000, // 30 seconds timeout
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true
});

// Request interceptor - Add auth token and logging
BaseAxios.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add request timestamp for performance monitoring
    config.metadata = { startTime: new Date() };

    // Log request in development
    if (import.meta.env.DEV) {
      console.log(`🚀 API Request: ${config.method?.toUpperCase()} ${config.url}`);
    }

    return config;
  },
  (error) => {
    console.error("❌ Request Error:", error);
    return Promise.reject(error);
  }
);

// Response interceptor - Enhanced error handling
BaseAxios.interceptors.response.use(
  (response) => {
    // Trả luôn data nếu request thành công
    return response.data;
  },
  (error) => {
    if (error.response) {
      const { status, data } = error.response;

      if (status === 401) {
        // Xử lý Unauthorized
        localStorage.removeItem("token");
        localStorage.removeItem("user");

        if (!window.location.pathname.includes('/login')) {
          console.warn("🔐 Session expired, redirecting to login...");
          window.location.href = '/login';
        }
      } else if (status === 403) {
        // Xử lý Forbidden
        console.error("🚫 Access forbidden - insufficient permissions");
      }

      // Nếu không phải 401/403, reject bình thường để phía gọi xử lý
      return Promise.reject({
        status,
        message: data?.message || `HTTP ${status} Error`,
        data: data,
        isApiError: true
      });
    } else {
      // Lỗi mạng hoặc cấu hình request
      return Promise.reject(error);
    }
  }
);


export default BaseAxios;
