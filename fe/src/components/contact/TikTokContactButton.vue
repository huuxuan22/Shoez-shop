<template>
    <a :href="targetUrl" target="_blank" rel="noopener noreferrer" :title="title"
        class="w-12 h-12 rounded-full bg-white border border-gray-300 text-black shadow-lg flex items-center justify-center hover:bg-black hover:text-white transition">
        <!-- TikTok Icon -->
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path
                d="M21 8.5c-2.18 0-4.13-.72-5.68-2V16a6 6 0 1 1-6-6c.35 0 .69.03 1.02.1V13a2.98 2.98 0 0 0-1.02-.18 3 3 0 1 0 3 3V2h3.02c.4 2.32 2.2 4.14 4.66 4.57V8.5Z" />
        </svg>
    </a>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
    url: { type: String, default: 'https://www.tiktok.com/@your_account' },
    title: { type: String, default: null }
})

const title = computed(() => props.title || t('Contact.tiktok'))
const targetUrl = computed(() => props.url || 'https://www.tiktok.com')
</script>

<style scoped></style>
