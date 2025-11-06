<template>
    <span :class="statusClasses" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium capitalize">
        {{ statusText }}
    </span>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
    status: {
        type: String,
        required: true
    }
})

const statusText = computed(() => {
    return t(`Orders.StatusBadge.${props.status}`) || props.status
})

const statusClasses = computed(() => {
    const classes = {
        pending: 'bg-yellow-100 text-yellow-800',
        confirmed: 'bg-blue-100 text-blue-800',
        shipping: 'bg-purple-100 text-purple-800',
        complete: 'bg-green-100 text-green-800',
        cancelled: 'bg-red-100 text-red-800'
    }
    return classes[props.status] || 'bg-gray-100 text-gray-800'
})
</script>