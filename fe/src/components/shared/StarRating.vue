<template>
    <div class="flex items-center space-x-1" role="img" :aria-label="$t('Shared.StarRating.rating', { rating })">
        <span v-for="star in 5" :key="star" class="text-yellow-400" :class="[sizeClass]" :aria-hidden="true">
            {{ star <= rating ? '★' : '☆' }} </span>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
    rating: {
        type: Number,
        required: true,
        validator: value => value >= 0 && value <= 5
    },
    size: {
        type: Number,
        default: 20
    }
})

const sizeClass = computed(() => {
    const sizes = {
        16: 'text-base',
        20: 'text-lg',
        24: 'text-xl',
        28: 'text-2xl'
    }
    return sizes[props.size] || 'text-lg'
})
</script>