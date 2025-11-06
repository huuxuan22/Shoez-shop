import axios from "axios";
import { API_URL } from "@/config/url/url";
import { useUiStore } from "@/stores/ui";

const BaseAxios = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true
});

BaseAxios.interceptors.request.use(
  (config) => {
    try {
      const ui = useUiStore();
      ui.incrementLoading();
    } catch (_) { }
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    // Add Accept-Language header for all requests
    const language = localStorage.getItem("language") || "vi";
    config.headers["Accept-Language"] = language;
    config.metadata = { startTime: new Date() };
    return config;
  },
  (error) => {
    try {
      const ui = useUiStore();
      ui.decrementLoading();
    } catch (_) { }
    return Promise.reject(error);
  }
);

BaseAxios.interceptors.response.use(
  (response) => {
    try {
      const ui = useUiStore();
      ui.decrementLoading();
    } catch (_) { }
    return response;
  },
  (error) => {
    try {
      const ui = useUiStore();
      ui.decrementLoading();
    } catch (_) { }
    if (error.response) {
      const { status, data } = error.response;

      // 401 Unauthorized: Chưa login hoặc token hết hạn
      if (status === 401) {
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        localStorage.removeItem("refresh_token");

        // KHÔNG redirect nếu đang ở trang public
        const currentPath = window.location.pathname;
        const isPublicPage = currentPath === '/' ||
          currentPath === '/products' ||
          currentPath.startsWith('/products/') ||
          currentPath.includes('/about') ||
          currentPath.includes('/contact') ||
          currentPath.includes('/faq');

        // Chỉ redirect về Login nếu KHÔNG phải trang public
        if (!isPublicPage &&
          !currentPath.includes('/login') &&
          !currentPath.includes('/register') &&
          !currentPath.includes('/403')) {
          window.location.href = '/login';
        }
      }
      // 403 Forbidden: Không có quyền truy cập -> Về 403
      else if (status === 403) {
        if (!window.location.pathname.includes('/403')) {
          window.location.href = '/403';
        }
      }

      return Promise.reject({
        status,
        message: data?.message || `HTTP ${status} Error`,
        data: data,
        isApiError: true
      });
    } else {
      return Promise.reject(error);
    }
  }
);

export default BaseAxios;
