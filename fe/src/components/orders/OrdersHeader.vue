<template>
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
            <div class="mb-4 lg:mb-0">
                <h1 class="text-2xl font-bold text-gray-900">Đơn hàng của tôi</h1>
                <p class="text-gray-600 mt-1">
                    Tổng số: <span class="font-semibold">{{ totalOrders }} đơn hàng</span>
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

const filters = [
    { value: 'all', label: 'Tất cả' },
    { value: 'pending', label: 'Chờ xác nhận' },
    { value: 'confirmed', label: 'Đã xác nhận' },
    { value: 'shipped', label: 'Đang giao' },
    { value: 'delivered', label: 'Đã giao' },
    { value: 'cancelled', label: 'Đã hủy' }
]
</script>