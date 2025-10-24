// Environment-based API URL configuration
const getApiUrl = () => {
    // Check for environment variable first
    if (import.meta.env.VITE_API_URL) {
        return import.meta.env.VITE_API_URL;
    }

    // Auto-detect based on current host
    const host = window.location.host;

    // Development environment
    if (host.includes('localhost') || host.includes('127.0.0.1')) {
        return "http://localhost:8000/api/v1";
    }

    // Production environment - adjust as needed
    return "/api";
};

export const API_URL = getApiUrl();

// API endpoints
export const API_ENDPOINTS = {
    AUTH: {
        LOGIN: "/auth/login",
        REGISTER: "/auth/register",
        LOGOUT: "/auth/logout",
        REFRESH: "/auth/refresh",
        ME: "/auth/me",
        GOOGLE: "/auth/google/login",
        FACEBOOK: "/auth/facebook/login"
    },
    PRODUCTS: {
        LIST: "/products/get-all",
        DETAIL: (id) => `/products/${id}`,
        TOP_RATED: "/products/top-rated",
        SEARCH: "/products/search",
        UPLOAD_IMAGES: (id) => `/products/${id}/upload-images`
    },
    CART: {
        GET: "/cart",
        ADD: "/cart/add",
        UPDATE: (id) => `/cart/items/${id}`,
        REMOVE: (id) => `/cart/items/${id}`,
        CLEAR: "/cart/clear"
    },
    ORDERS: {
        LIST: "/orders",
        CREATE: "/orders",
        DETAIL: (id) => `/orders/${id}`
    },
    USER: {
        PROFILE: "/user/profile",
        UPDATE: "/user/profile"
    }
};