import axios from "axios";
import { API_URL } from "@/config/url/url";

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
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    config.metadata = { startTime: new Date() };
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

BaseAxios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      const { status, data } = error.response;

      if (status === 401) {
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        if (!window.location.pathname.includes('/403')) {
          window.location.href = '/403';
        }
      } else if (status === 403) {
        window.location.href = '/403';
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
