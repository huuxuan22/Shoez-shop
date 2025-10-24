<template>
    <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-lg shadow-xl max-w-4xl w-full mx-4 max-h-[90vh] overflow-hidden">
            <!-- Header -->
            <div class="px-6 py-4 border-b border-gray-200 flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-900">Chi tiết đơn hàng #{{ order?.id?.slice(-8) }}</h3>
                <button @click="$emit('close')" class="text-gray-400 hover:text-gray-600">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>

            <!-- Content -->
            <div class="px-6 py-4 overflow-y-auto max-h-[calc(90vh-120px)]">
                <div v-if="order" class="space-y-6">
                    <!-- Order Info -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- Customer Info -->
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h4 class="font-semibold text-gray-900 mb-3">Thông tin khách hàng</h4>
                            <div class="space-y-2">
                                <p><span class="font-medium">Tên:</span> {{ order.user_id?.full_name || 'N/A' }}</p>
                                <p><span class="font-medium">Email:</span> {{ order.user_id?.email || 'N/A' }}</p>
                                <p><span class="font-medium">SĐT:</span> {{ order.user_id?.numberphone || 'N/A' }}</p>
                            </div>
                        </div>

                        <!-- Order Status -->
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h4 class="font-semibold text-gray-900 mb-3">Trạng thái đơn hàng</h4>
                            <div class="space-y-2">
                                <p><span class="font-medium">Trạng thái:</span>
                                    <span
                                        class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full ml-2"
                                        :class="getStatusClass(order.status)">
                                        {{ getStatusText(order.status) }}
                                    </span>
                                </p>
                                <p><span class="font-medium">Ngày đặt:</span> {{ formatDate(order.created_at) }}</p>
                                <p><span class="font-medium">Cập nhật:</span> {{ formatDate(order.updated_at) }}</p>
                            </div>
                        </div>
                    </div>

                    <!-- Products -->
                    <div>
                        <h4 class="font-semibold text-gray-900 mb-3">Sản phẩm</h4>
                        <div class="bg-gray-50 rounded-lg p-4">
                            <div v-if="order.products && order.products.length > 0" class="space-y-3">
                                <div v-for="(product, index) in order.products" :key="index"
                                    class="flex items-center justify-between border-b border-gray-200 pb-3 last:border-b-0">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-12 h-12 bg-gray-200 rounded-lg flex items-center justify-center">
                                            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor"
                                                viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                            </svg>
                                        </div>
                                        <div>
                                            <p class="font-medium text-gray-900">{{ product.name || 'Sản phẩm không tên'
                                            }}</p>
                                            <p class="text-sm text-gray-500">Số lượng: {{ product.quantity || 1 }}</p>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <p class="font-medium text-gray-900">{{ formatPrice(product.price) }}</p>
                                        <p class="text-sm text-gray-500">Tổng: {{ formatPrice((product.price || 0) *
                                            (product.quantity || 1)) }}</p>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="text-center text-gray-500 py-4">
                                Không có sản phẩm nào
                            </div>
                        </div>
                    </div>

                    <!-- Order Summary -->
                    <div class="bg-gray-50 rounded-lg p-4">
                        <h4 class="font-semibold text-gray-900 mb-3">Tổng kết đơn hàng</h4>
                        <div class="space-y-2">
                            <div class="flex justify-between">
                                <span>Tổng sản phẩm:</span>
                                <span>{{ order.products?.length || 0 }}</span>
                            </div>
                            <div class="flex justify-between">
                                <span>Tổng tiền:</span>
                                <span class="font-semibold">{{ formatPrice(calculateTotal()) }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="px-6 py-4 border-t border-gray-200 flex items-center justify-end space-x-3">
                <button @click="$emit('close')"
                    class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors">
                    Đóng
                </button>
                <button @click="printOrder"
                    class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
                    In đơn hàng
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
    isOpen: {
        type: Boolean,
        default: false
    },
    order: {
        type: Object,
        default: null
    }
});

const emit = defineEmits(['close']);

const getStatusText = (status) => {
    const statusMap = {
        'pending': 'Chờ xử lý',
        'processing': 'Đang xử lý',
        'complete': 'Hoàn thành',
        'cancelled': 'Đã hủy'
    };
    return statusMap[status] || status;
};

const getStatusClass = (status) => {
    const classMap = {
        'pending': 'bg-yellow-100 text-yellow-800',
        'processing': 'bg-blue-100 text-blue-800',
        'complete': 'bg-green-100 text-green-800',
        'cancelled': 'bg-red-100 text-red-800'
    };
    return classMap[status] || 'bg-gray-100 text-gray-800';
};

const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('vi-VN', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
};

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price || 0);
};

const calculateTotal = () => {
    if (!props.order?.products) return 0;
    return props.order.products.reduce((total, product) => {
        return total + ((product.price || 0) * (product.quantity || 1));
    }, 0);
};
</script>
