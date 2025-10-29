import axios from "axios"
import { API_URL } from "@/config/url/url";
import BaseAxios from "./BaseAxios";
import router from "@/router";

const PREFIX_AUTH = '/auth'
const FRONTEND_URL = window.location.origin;

export const loginWithGoogle = () => {
    const width = 500;
    const height = 600;
    const left = (window.screen.width / 2) - (width / 2);
    const top = (window.screen.height / 2) - (height / 2);

    window.open(
        `${API_URL}/auth/google/login`,
        'google-login',
        `width=${width},height=${height},left=${left},top=${top},toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes`
    );
}

export const handleCallback = async (provider, code) => {
    const response = await axios.get(`${API_URL}/${provider}/callback?code=${code}`);
    if (response.data.access_token) {
        localStorage.setItem("token", response.data.access_token);
    }
    return response.data;
}
export const loginWithFacebook = () => {
    const width = 500;
    const height = 600;
    const left = (window.screen.width / 2) - (width / 2);
    const top = (window.screen.height / 2) - (height / 2);

    window.open(
        `${API_URL}/auth/facebook/login`,
        'facebook-login',
        `width=${width},height=${height},left=${left},top=${top},toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes`
    );
}

export const fetchSession = async () => {
    debugger;
    return await BaseAxios.get(`/auth/session`);
}

export const hydrateFromOAuthRedirect = async (authStore) => {
    try {
        if (!authStore) return;
        debugger;
        // Initialize và hydrate từ cookies
        authStore.initializeAuth();
        authStore.hydrateFromCookies();

        // Gọi API session để lấy user và token từ cookie
        const res = await fetchSession();
        const data = res?.data;

        if (!data) {
            throw new Error('Không nhận được dữ liệu từ session');
        }

        // Lưu vào store
        if (typeof authStore.updateUser === 'function') {
            authStore.updateUser(data.user_principal || {});
        } else {
            authStore.user = data.user_principal;
        }
        authStore.accessToken = data.access_token;
        authStore.refreshToken = data.refresh_token;

        // Lưu vào localStorage
        if (data.access_token) localStorage.setItem("token", data.access_token);
        if (data.refresh_token) localStorage.setItem("refresh_token", data.refresh_token);
        if (data.user_principal) localStorage.setItem("user", JSON.stringify(data.user_principal));

        return data;
    } catch (e) {
        console.error('Error hydrating OAuth:', e);
        throw e;
    }
}

export const loginApi = async (data) => {
    return await BaseAxios.post(`${PREFIX_AUTH}/login`, data);

}

export const registerApi = async (data) => {
    return await BaseAxios.post(`${PREFIX_AUTH}/register`, data);
}

export const logoutApi = async (data) => {
    return await BaseAxios.post(`${PREFIX_AUTH}/logout`);
}

export default {
    loginWithGoogle,
    handleCallback,
    loginWithFacebook,
    fetchSession,
    hydrateFromOAuthRedirect,
    loginApi,
    registerApi,
    logoutApi
}