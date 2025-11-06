import { createI18n } from "vue-i18n";
import vi from "@/config/language/vi";
import en from "@/config/language/en";
import ja from "@/config/language/ja";

const lang = localStorage.getItem("language") || "vi";

const i18n = createI18n({
  legacy: false,
  locale: lang,
  fallbackLocale: "vi",
  messages: {
    vi,
    en,
    ja,
  },
});

export default i18n;
