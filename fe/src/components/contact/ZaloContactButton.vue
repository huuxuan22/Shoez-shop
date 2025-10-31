<template>
    <button type="button"
        class="w-12 h-12 rounded-full bg-white border border-gray-300 shadow-lg flex items-center justify-center hover:bg-black hover:text-white transition"
        :title="title" @click="openZalo">
        <!-- Zalo Icon (monochrome) -->
        <svg class="w-6 h-6 text-black" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path
                d="M5.5 3h13A2.5 2.5 0 0 1 21 5.5v8A2.5 2.5 0 0 1 18.5 16H13l-3.5 4-.01-4H5.5A2.5 2.5 0 0 1 3 13.5v-8A2.5 2.5 0 0 1 5.5 3Z" />
        </svg>
    </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
    url: { type: String, default: 'https://zalo.me' },
    title: { type: String, default: 'Liên hệ qua Zalo' }
})

const targetUrl = computed(() => props.url || 'https://zalo.me')

function openZalo() {
    window.open(targetUrl.value, '_blank', 'noopener,noreferrer')
}
</script>

<style scoped></style>
