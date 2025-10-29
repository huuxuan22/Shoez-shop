<template>
    <div class="bg-white rounded-lg shadow-sm p-12 text-center">
        <div class="max-w-md mx-auto">
            <svg class="w-24 h-24 text-gray-300 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>

            <h3 class="mt-6 text-xl font-semibold text-gray-900">
                {{ emptyTitle }}
            </h3>
            <p class="mt-2 text-gray-600">
                {{ emptyDescription }}
            </p>

            <div class="mt-8">
                <router-link to="/products"
                    class="inline-flex items-center px-6 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors font-medium">
                    <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                    Mua sắm ngay
                </router-link>

                <button v-if="filter !== 'all'" @click="$emit('reset-filter')"
                    class="ml-4 inline-flex items-center px-6 py-3 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors font-medium">
                    Xem tất cả đơn hàng
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
    filter: {
        type: String,
        default: 'all'
    }
})

defineEmits(['reset-filter'])

const emptyTitle = computed(() => {
    const titles = {
        all: 'Chưa có đơn hàng nào',
        pending: 'Không có đơn hàng chờ xác nhận',
        confirmed: 'Không có đơn hàng đã xác nhận',
        shipping: 'Không có đơn hàng đang giao',
        complete: 'Không có đơn hàng hoàn thành',
        cancelled: 'Không có đơn hàng đã hủy'
    }
    return titles[props.filter] || titles.all
})

const emptyDescription = computed(() => {
    const descriptions = {
        all: 'Hãy bắt đầu mua sắm và đơn hàng đầu tiên của bạn sẽ xuất hiện ở đây.',
        pending: 'Tất cả đơn hàng của bạn đã được xử lý hoặc chưa có đơn hàng nào ở trạng thái này.',
        confirmed: 'Không có đơn hàng nào đã được xác nhận.',
        shipping: 'Không có đơn hàng nào đang được giao.',
        complete: 'Bạn chưa có đơn hàng nào đã hoàn thành.',
        cancelled: 'Bạn chưa hủy đơn hàng nào.'
    }
    return descriptions[props.filter] || descriptions.all
})
</script>