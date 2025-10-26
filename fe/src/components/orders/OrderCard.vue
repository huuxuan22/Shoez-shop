<template>
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow">
        <!-- Order Header -->
        <div class="p-6 border-b border-gray-200">
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
                <div class="mb-4 lg:mb-0">
                    <div class="flex items-center space-x-4">
                        <h3 class="text-lg font-semibold text-gray-900">{{ order.orderNumber }}</h3>
                        <OrderStatusBadge :status="order.status" />
                    </div>
                    <p class="text-gray-600 text-sm mt-1">
                        Đặt ngày: {{ formatDate(order.createdAt) }}
                    </p>
                </div>

                <div class="text-right">
                    <p class="text-lg font-bold text-gray-900">{{ formatPrice(order.totalAmount) }}</p>
                    <p class="text-sm text-gray-600 capitalize">
                        {{ getPaymentMethodText(order.paymentMethod) }}
                    </p>
                </div>
            </div>
        </div>

        <!-- Order Items -->
        <div class="p-6 border-b border-gray-200">
            <div class="space-y-4">
                <div v-for="item in order.items" :key="item.id" class="flex items-center space-x-4">
                    <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded-lg flex-shrink-0" />
                    <div class="flex-1 min-w-0">
                        <h4 class="font-medium text-gray-900 truncate">{{ item.name }}</h4>
                        <p class="text-gray-600 text-sm">
                            Số lượng: {{ item.quantity }}
                        </p>
                    </div>
                    <div class="text-right flex-shrink-0">
                        <p class="font-medium text-gray-900">{{ formatPrice(item.price) }}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Order Footer -->
        <div class="p-6">
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
                <div class="mb-4 lg:mb-0">
                    <p class="text-sm text-gray-600">
                        <span class="font-medium">Địa chỉ giao hàng:</span>
                        {{ order.shippingAddress.address }}
                    </p>
                    <p v-if="order.trackingNumber" class="text-sm text-gray-600 mt-1">
                        <span class="font-medium">Mã theo dõi:</span>
                        {{ order.trackingNumber }}
                    </p>
                </div>

                <div class="flex flex-wrap gap-2">
                    <button @click="$emit('view-detail', order.id)"
                        class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors text-sm font-medium">
                        Xem chi tiết
                    </button>

                    <button v-if="canCancelOrder" @click="$emit('cancel-order', order.id)"
                        class="px-4 py-2 border border-red-300 text-red-700 rounded-lg hover:bg-red-50 transition-colors text-sm font-medium">
                        Hủy đơn hàng
                    </button>

                    <button v-if="canReorder" @click="$emit('reorder', order.id)"
                        class="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors text-sm font-medium">
                        Mua lại
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import OrderStatusBadge from './OrderStatusBadge.vue'

const props = defineProps({
    order: {
        type: Object,
        required: true
    }
})

defineEmits(['view-detail', 'cancel-order', 'reorder'])

const canCancelOrder = computed(() => {
    return ['pending', 'confirmed'].includes(props.order.status)
})

const canReorder = computed(() => {
    return ['delivered', 'cancelled'].includes(props.order.status)
})

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price)
}

const formatDate = (date) => {
    return new Date(date).toLocaleDateString('vi-VN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    })
}

const getPaymentMethodText = (method) => {
    const methods = {
        credit_card: 'Thẻ tín dụng',
        cod: 'Thanh toán khi nhận hàng',
        bank_transfer: 'Chuyển khoản ngân hàng'
    }
    return methods[method] || method
}
</script>