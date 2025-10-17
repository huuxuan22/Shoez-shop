import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "./assets/main.css";
import router from "./router";
import i18n from "@/config/language/i18n";
import { createPinia } from "pinia";
const pinia = createPinia();
createApp(App).use(pinia).use(i18n).use(router).mount("#app");
