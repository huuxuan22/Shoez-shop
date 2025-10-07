import { createI18n } from "vue-i18n";
import vi from "@/config/language/vi";
import en from "@/config/language/en";
import ja from "@/config/language/ja";
import { MultiLanguage } from "@/common/enum";

const lang = localStorage.getItem("language") || MultiLanguage.VI;

const i18n = createI18n({
  locale: lang,
  fallbackLocale: MultiLanguage.VI,
  messages: {
    vi,
    en,
    ja,
  },
});

export default i18n;
