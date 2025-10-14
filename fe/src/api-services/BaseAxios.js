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
    // Log response time in development
    if (import.meta.env.DEV && response.config.metadata) {
      const duration = new Date() - response.config.metadata.startTime;
      console.log(`✅ API Response: ${response.config.method?.toUpperCase()} ${response.config.url} - ${duration}ms`);
    }

    return response.data;
  },
  (error) => {
    // Handle different error scenarios
    if (error.response) {
      const { status, data } = error.response;

      switch (status) {
        case 401:
          // Unauthorized - clear auth data and redirect to login
          localStorage.removeItem("token");
          localStorage.removeItem("user");

          // Only redirect if not already on login page
          if (!window.location.pathname.includes('/login')) {
            console.warn("🔐 Session expired, redirecting to login...");
            window.location.href = '/login';
          }
          break;

        case 403:
          console.error("🚫 Access forbidden - insufficient permissions");
          break;

        case 404:
          console.error("🔍 Resource not found");
          break;

        case 422:
          console.error("📝 Validation Error:", data);
          break;

        case 500:
          console.error("🔥 Server Error - please try again later");
          break;

        default:
          console.error(`⚠️ API Error ${status}:`, data);
      }

      // Return structured error object
      return Promise.reject({
        status,
        message: data?.message || data?.detail || `HTTP ${status} Error`,
        data: data,
        isApiError: true
      });
    } else if (error.request) {
      // Network error
      console.error("🌐 Network Error:", error.message);
      return Promise.reject({
        status: 0,
        message: "Network error - please check your internet connection",
        data: null,
        isNetworkError: true
      });
    } else {
      // Request setup error
      console.error("⚙️ Request Setup Error:", error.message);
      return Promise.reject({
        status: -1,
        message: error.message,
        data: null,
        isConfigError: true
      });
    }
  }
);

export default BaseAxios;
