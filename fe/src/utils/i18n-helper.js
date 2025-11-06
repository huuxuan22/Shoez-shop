import i18n from "@/config/language/i18n";

export const changeLanguage = (lang) => {
    const supportedLanguages = ["vi", "en", "ja"];
    if (!supportedLanguages.includes(lang)) {
        lang = "vi"; // Default to Vietnamese if unsupported language is provided
    }
    i18n.global.locale = lang;
    localStorage.setItem("language", lang);

    window.location.reload(); // Reload the page to apply the new language setting
}
