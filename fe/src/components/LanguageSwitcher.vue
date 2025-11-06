<template>
  <div class="language-switcher">
    <select :aria-label="$t('Shared.LanguageSwitcher.label')" v-model="currentLang" @change="onSelectChange" class="lang-select">
      <option v-for="lang in availableLanguages" :key="lang.value" :value="lang.value">
        {{ lang.label }}
      </option>
    </select>
  </div>

</template>

<script setup>
import { ref, computed, watchEffect } from "vue";
import { useI18n } from "vue-i18n";
import { changeLanguage } from "@/utils/i18n-helper";

const { locale, t } = useI18n();

// Danh sách ngôn ngữ hỗ trợ (computed để reactive với i18n)
const availableLanguages = computed(() => [
  { value: "vi", label: t('Shared.LanguageSwitcher.vietnamese') },
  { value: "en", label: t('Shared.LanguageSwitcher.english') },
  { value: "ja", label: t('Shared.LanguageSwitcher.japanese') },
]);

// Ngôn ngữ hiện tại
const currentLang = ref(localStorage.getItem("language") || "vi");

// Theo dõi thay đổi ngôn ngữ
watchEffect(() => {
  currentLang.value = locale.value;
});

// Sự kiện khi chọn ngôn ngữ từ select
const onSelectChange = () => {
  changeLanguage(currentLang.value);
  locale.value = currentLang.value;
};
</script>

<style scoped>
.language-switcher {
  display: flex;
  align-items: center;
}

.lang-select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 6px 28px 6px 10px;
  border: 1px solid #d1d5db;
  /* gray-300 */
  border-radius: 6px;
  background-color: #ffffff;
  /* white */
  color: #111827;
  /* gray-900 */
  font-size: 14px;
  line-height: 20px;
  background-image: url('data:image/svg+xml;utf8,<svg fill="none" stroke="%23111827" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M19 9l-7 7-7-7"/></svg>');
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 14px 14px;
}

.lang-select:focus {
  outline: none;
  border-color: #111827;
  /* black */
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1);
}

.lang-select option {
  background-color: #ffffff;
  color: #111827;
}
</style>
