<template>
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
            <div class="mb-4 lg:mb-0">
                <h1 class="text-2xl font-bold text-gray-900">{{ $t('Orders.Header.title') }}</h1>
                <p class="text-gray-600 mt-1">
                    {{ $t('Orders.Header.totalOrders') }} <span class="font-semibold">{{ totalOrders }} {{ $t('Orders.Header.ordersSuffix') }}</span>
                </p>
            </div>

            <div class="flex flex-wrap gap-2">
                <button v-for="filter in filters" :key="filter.value" @click="$emit('filter-change', filter.value)"
                    :class="[
                        'px-4 py-2 rounded-lg border text-sm font-medium transition-colors',
                        activeFilter === filter.value
                            ? 'bg-black text-white border-black'
                            : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
                    ]">
                    {{ filter.label }}
                    <span v-if="filter.count !== undefined" class="ml-1">
                        ({{ filter.count }})
                    </span>
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

defineProps({
    totalOrders: {
        type: Number,
        default: 0
    },
    activeFilter: {
        type: String,
        default: 'all'
    }
})

defineEmits(['filter-change'])

const filters = computed(() => [
    { value: 'all', label: t('Orders.Header.filters.all') },
    { value: 'pending', label: t('Orders.Header.filters.pending') },
    { value: 'confirmed', label: t('Orders.Header.filters.confirmed') },
    { value: 'shipping', label: t('Orders.Header.filters.shipping') },
    { value: 'complete', label: t('Orders.Header.filters.complete') },
    { value: 'cancelled', label: t('Orders.Header.filters.cancelled') }
])
</script>