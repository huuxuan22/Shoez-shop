import axios from "axios"
import { API_URL } from "@/config/url/url";
import BaseAxios from "./BaseAxios";

const PREFIX_AUTH = '/auth'
export const loginWithGoogle = () => {
    window.location.href = `${API_URL}/auth/google/login`;
}

export const handleCallback = async (provider, code) => {
    const response = await axios.get(`${API_URL}/${provider}/callback?code=${code}`);
    if (response.data.access_token) {
        localStorage.setItem("token", response.data.access_token);
    }
    return response.data;
}
export const loginWithFacebook = () => {
    window.location.href = `${API_URL}/auth/facebook/login`;
}

export const loginApi = async (data) => {
    return await BaseAxios.post(`${PREFIX_AUTH}/login`, data);

}

export default {
    loginWithGoogle,
    handleCallback,
    loginWithFacebook,
    loginApi
}