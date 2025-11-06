<template>
    <div class="flex items-center border border-gray-300 rounded-lg" role="group" :aria-label="$t('Shared.QuantitySelector.quantity', { quantity })">
        <button @click="decrease" :disabled="quantity <= 1" :aria-label="$t('Shared.QuantitySelector.decrease')"
            :class="[
            'px-3 py-1 transition-colors',
            quantity <= 1 ? 'text-gray-400 cursor-not-allowed' : 'text-black hover:bg-gray-100'
        ]">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
            </svg>
        </button>

        <span class="px-4 py-1 text-black font-medium min-w-12 text-center" aria-live="polite">
            {{ quantity }}
        </span>

        <button @click="increase" :disabled="quantity >= maxQuantity" :aria-label="$t('Shared.QuantitySelector.increase')"
            :class="[
            'px-3 py-1 transition-colors',
            quantity >= maxQuantity ? 'text-gray-400 cursor-not-allowed' : 'text-black hover:bg-gray-100'
        ]">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
        </button>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const props = defineProps({
    quantity: Number,
    maxQuantity: Number
});

const emit = defineEmits(['update:quantity']);

const increase = () => {
    if (props.quantity < props.maxQuantity) {
        emit('update:quantity', props.quantity + 1);
    }
};

const decrease = () => {
    if (props.quantity > 1) {
        emit('update:quantity', props.quantity - 1);
    }
};
</script>