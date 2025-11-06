<template>
    <div class="flex items-center justify-between">
        <div class="flex items-center gap-4">
            <button @click="$emit('continue-shopping')"
                class="flex items-center gap-2 text-gray-600 hover:text-black transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                </svg>
                <span class="font-medium">{{ $t('Cart.Header.continueShopping') }}</span>
            </button>
        </div>

        <div class="text-center">
            <h1 class="text-3xl font-bold text-black">{{ $t('Cart.Header.title') }}</h1>
            <p class="text-gray-600 mt-1">{{ itemCount }} {{ $t('Cart.Header.itemsCount') }}</p>
        </div>

        <div class="w-20"></div> <!-- Spacer for balance -->
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

defineProps({
    itemCount: Number
});

defineEmits(['continue-shopping']);
</script>