import { defineStore } from "pinia";
import { loginApi } from "@/api-services/AuthService";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        user: null,
        accessToken: null,
        refreshToken: null,
    }),

    actions: {
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

        logout() {
            this.user = null;
            this.accessToken = null;
            this.refreshToken = null;
            localStorage.clear();
        },
    },
});
