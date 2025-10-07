import axios from "axios";
import { API_URL } from "@/config/url/url";
// Tạo instance axios
const BaseAxios = axios.create({
  baseURL: API_URL, // URL mặc định (backend)
  timeout: 10000, // Thời gian timeout (ms)
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true
});

// Thêm interceptor để xử lý request
BaseAxios.interceptors.request.use(
    (config) => {
      // Ví dụ: gắn token vào header (nếu có)
      const token = localStorage.getItem("token");
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config; // 👈 phải return config
    },
    (error) => Promise.reject(error)
  );

// Thêm interceptor để xử lý response
BaseAxios.interceptors.response.use(
  (response) => response.data, // Trả về data luôn
  (error) => {
    // Ví dụ: nếu token hết hạn
    if (error.response && error.response.status === 401) {
      console.error("Unauthorized! Redirect to login...");
    }
    return Promise.reject(error);
  }
);

export default BaseAxios;
