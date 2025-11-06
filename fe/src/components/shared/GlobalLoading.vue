<template>
    <transition name="fade">
        <div v-if="isLoading" class="fixed inset-0 z-50 flex items-center justify-center bg-black/30" role="status" aria-live="polite">
            <div class="w-12 h-12 border-4 border-white/30 border-t-white rounded-full animate-spin" :aria-label="$t('Shared.GlobalLoading.loading')"></div>
        </div>
    </transition>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useI18n } from 'vue-i18n'
import { useUiStore } from '@/stores/ui'

const { t } = useI18n()
const ui = useUiStore()
const { isLoading } = storeToRefs(ui)
</script>

<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity .15s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
