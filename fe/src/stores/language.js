import { defineStore } from "pinia";
import { MultiLanguage } from "@/common/enum";

export const useLanguageStore = defineStore("language", {
  state: () => ({
    currentLanguage: localStorage.getItem("language") || MultiLanguage.VI,
  }),
  actions: {
    setLanguage(lang) {
      this.currentLanguage = lang;
      localStorage.setItem("language", lang);
    },
  },
});
