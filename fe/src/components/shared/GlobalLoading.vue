<template>
    <transition name="fade">
        <div v-if="isLoading" class="fixed inset-0 z-50 flex items-center justify-center bg-black/30">
            <div class="w-12 h-12 border-4 border-white/30 border-t-white rounded-full animate-spin"></div>
        </div>
    </transition>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useUiStore } from '@/stores/ui'

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
