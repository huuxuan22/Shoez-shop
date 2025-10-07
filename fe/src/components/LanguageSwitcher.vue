<template>
  <div class="language-switcher">
    <!-- Dropdown hoặc button group -->
    <button
      v-for="lang in availableLanguages"
      :key="lang.value"
      :class="{ active: currentLang === lang.value }"
      @click="changeLanguage(lang.value)"
    >
      {{ lang.label }}
    </button>
  </div>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import { useI18n } from "vue-i18n";
import { MultiLanguage } from "@/common/enum.js";

const { locale } = useI18n();

// Danh sách ngôn ngữ hỗ trợ
const availableLanguages = [
  { value: MultiLanguage.VI, label: "Tiếng Việt" },
  { value: MultiLanguage.EN, label: "English" },
  { value: MultiLanguage.JA, label: "日本語" },
];

// Ngôn ngữ hiện tại
const currentLang = ref(localStorage.getItem("language") || MultiLanguage.VI);

// Theo dõi thay đổi ngôn ngữ
watchEffect(() => {
  currentLang.value = locale.value;
});

// Hàm chuyển đổi ngôn ngữ
const changeLanguage = (lang) => {
  locale.value = lang;
  localStorage.setItem("language", lang);

  // Có thể thêm animation/feedback tại đây
  console.log(`Ngôn ngữ đã chuyển sang: ${lang}`);
};
</script>

<style scoped>
.language-switcher {
  display: flex;
  gap: 8px;
}

button {
  padding: 5px 10px;
  border: 1px solid #ccc;
  background: white;
  cursor: pointer;
}

button.active {
  background: #007bff;
  color: white;
  border-color: #007bff;
}
</style>
