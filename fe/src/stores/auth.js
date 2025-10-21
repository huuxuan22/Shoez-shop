import { defineStore } from "pinia";
import { loginApi, logoutApi, registerApi } from "@/api-services/AuthService";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        user: null,
        accessToken: null,
        refreshToken: null,
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken,
        isAdmin: (state) => {
            if (!state.user) return false;
            const role = state.user.role?.toLowerCase();
            return role === 'admin' || role === 'administrator';
        },
        userRole: (state) => state.user?.role || null,
    },

    actions: {
        // Tự động khôi phục session từ localStorage khi app khởi động
        initializeAuth() {
            const token = localStorage.getItem("token");
            const refreshToken = localStorage.getItem("refresh_token");
            const userStr = localStorage.getItem("user");

            if (token) {
                this.accessToken = token;
            }
            if (refreshToken) {
                this.refreshToken = refreshToken;
            }
            if (userStr) {
                try {
                    this.user = JSON.parse(userStr);
                } catch (error) {
                    this.user = null;
                }
            }
        },

        async updateUser(updatedData) {
            this.user = { ...this.user, ...updatedData };
            // Không lưu localStorage - chỉ cập nhật memory
        },

        async login(credentials) {
            try {
                const res = await loginApi(credentials);

                // Chỉ lưu state vào memory (Pinia), không lưu localStorage
                this.user = res.user_principal;
                this.accessToken = res.access_token;
                this.refreshToken = res.refresh_token;

                return res;
            } catch (error) {
                console.error("❌ Login failed:", error.message || error);
                throw error;
            }
        },

        async register(credentials) {
            try {
                const res = await registerApi(credentials);

                // Chỉ lưu state trong memory
                this.user = res.user_principal;
                this.accessToken = res.access_token;
                this.refreshToken = res.refresh_token;

                return res;
            } catch (error) {
                console.error("❌ Registration failed:", error.message || error);
                throw error;
            }
        },

        async logout() {
            try {
                // Gọi API logout (có thể fail nếu token không hợp lệ)
                await logoutApi();
            } catch (error) {
                console.warn("Logout API failed, but clearing local state anyway:", error);
            } finally {
                // Luôn clear state dù API có fail
                this.user = null;
                this.accessToken = null;
                this.refreshToken = null;
                localStorage.clear();
            }
        },
    },
});
