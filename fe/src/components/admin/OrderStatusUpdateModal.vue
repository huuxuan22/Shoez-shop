<template>
    <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
            <!-- Header -->
            <div class="px-6 py-4 border-b border-gray-200">
                <h3 class="text-lg font-semibold text-gray-900">Cập nhật trạng thái đơn hàng</h3>
                <p class="text-sm text-gray-500 mt-1">Đơn hàng #{{ order?.id?.slice(-8) }}</p>
            </div>

            <!-- Content -->
            <div class="px-6 py-4">
                <div v-if="order">
                    <!-- Current Status -->
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">Trạng thái hiện tại</label>
                        <span class="px-3 py-2 inline-flex text-sm leading-5 font-semibold rounded-full"
                            :class="getStatusClass(order.status)">
                            {{ getStatusText(order.status) }}
                        </span>
                    </div>

                    <!-- New Status -->
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">Trạng thái mới</label>
                        <select v-model="newStatus"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
                            <option value="">Chọn trạng thái mới</option>
                            <option value="pending" :disabled="order.status === 'pending'">Chờ xử lý</option>
                            <option value="processing" :disabled="order.status === 'processing'">Đang xử lý</option>
                            <option value="complete" :disabled="order.status === 'complete'">Hoàn thành</option>
                            <option value="cancelled" :disabled="order.status === 'cancelled'">Đã hủy</option>
                        </select>
                    </div>

                    <!-- Reason (optional) -->
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">Lý do (tùy chọn)</label>
                        <textarea v-model="reason" rows="3" placeholder="Nhập lý do cập nhật trạng thái..."
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"></textarea>
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="px-6 py-4 border-t border-gray-200 flex items-center justify-end space-x-3">
                <button @click="$emit('close')"
                    class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors">
                    Hủy
                </button>
                <button @click="updateStatus" :disabled="!newStatus || newStatus === order?.status"
                    class="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
                    Cập nhật
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';

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

const emit = defineEmits(['close', 'updated']);

const newStatus = ref('');
const reason = ref('');

// Reset form when modal opens/closes
watch(() => props.isOpen, (isOpen) => {
    if (isOpen) {
        newStatus.value = '';
        reason.value = '';
    }
});

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

const updateStatus = () => {
    if (!newStatus.value || newStatus.value === props.order?.status) return;

    emit('updated', {
        orderId: props.order.id,
        newStatus: newStatus.value,
        reason: reason.value
    });

    emit('close');
};
</script>
