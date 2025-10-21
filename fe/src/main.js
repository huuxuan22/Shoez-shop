import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "./assets/main.css";
import router from "./router";
import i18n from "@/config/language/i18n";
import { createPinia } from "pinia";
import { useAuthStore } from "@/stores/auth";

const pinia = createPinia();
const app = createApp(App);
app.use(pinia).use(i18n).use(router);
// Tắt auto-login từ localStorage
// const authStore = useAuthStore();
// authStore.initializeAuth();
// 🟢 Khôi phục dữ liệu từ localStorage
const authStore = useAuthStore();
authStore.initializeAuth();
app.mount("#app");
