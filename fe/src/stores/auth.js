import { defineStore } from "pinia";
import { loginApi, registerApi } from "@/api-services/AuthService";

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
        // Initialize auth from localStorage
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
                    console.error("❌ Failed to parse user from localStorage:", error);
                    this.user = null;
                }
            }
        },

        async updateUser(updatedData) {
            this.user = { ...this.user, ...updatedData };
            localStorage.setItem("user", JSON.stringify(this.user));
        },

        async login(credentials) {
            try {
                const res = await loginApi(credentials);

                // Lưu state
                this.user = res.user_principal;
                this.accessToken = res.access_token;
                this.refreshToken = res.refresh_token;

                // Lưu localStorage
                localStorage.setItem("token", res.access_token);
                localStorage.setItem("refresh_token", res.refresh_token);
                localStorage.setItem("user", JSON.stringify(res.user_principal));

                return res;
            } catch (error) {
                console.error("❌ Login failed:", error.message || error);
                throw error;
            }
        },

        async register(credentials) {
            try {
                const res = await registerApi(credentials);

                this.user = res.user_principal;
                this.accessToken = res.access_token;
                this.refreshToken = res.refresh_token;

                // Lưu localStorage
                localStorage.setItem("token", res.access_token);
                localStorage.setItem("refresh_token", res.refresh_token);
                localStorage.setItem("user", JSON.stringify(res.user_principal));

                return res;
            } catch (error) {
                console.error("❌ Registration failed:", error.message || error);
                throw error;
            }
        },

        logout() {
            this.user = null;
            this.accessToken = null;
            this.refreshToken = null;
            localStorage.clear();
        },
    },
});
