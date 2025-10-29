<template>
    <div class="bg-white border border-gray-200 rounded-lg p-6 sticky top-4">
        <h2 class="text-xl font-bold text-black mb-6">Tóm tắt đơn hàng</h2>

        <div class="space-y-3">
            <div class="flex justify-between text-gray-600">
                <span>Tạm tính ({{ totalItems }} sản phẩm)</span>
                <span>{{ formatPrice(subtotal) }}</span>
            </div>

            <div class="flex justify-between text-gray-600">
                <span>Phí vận chuyển</span>
                <span>{{ shippingFee > 0 ? formatPrice(shippingFee) : 'Miễn phí' }}</span>
            </div>

            <div class="flex justify-between text-gray-600">
                <span>Giảm giá</span>
                <span class="text-green-600">-{{ formatPrice(discount) }}</span>
            </div>

            <Divider />

            <div class="flex justify-between text-lg font-bold text-black">
                <span>Tổng cộng</span>
                <span>{{ formatPrice(total) }}</span>
            </div>
        </div>

        <div class="mt-6 space-y-2">
            <button @click="$emit('checkout-selected')" :disabled="selectedCount === 0"
                class="w-full bg-black text-white px-4 py-3 rounded-lg disabled:opacity-50">
                Thanh toán ({{ selectedCount }})
            </button>

            <div class="text-center">
                <button class="text-gray-600 hover:text-black transition-colors text-sm">
                    ← Tiếp tục mua sắm
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import Button from '../Button.vue';
import Divider from '../Divider.vue';

const props = defineProps({
    cartItems: Array,
    selectedCount: { type: Number, default: 0 }
});

defineEmits(['checkout', 'checkout-selected']);

// Computed
const subtotal = computed(() => {
    return props.cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
});

const totalItems = computed(() => {
    return props.cartItems.reduce((total, item) => total + item.quantity, 0);
});

const shippingFee = computed(() => {
    return subtotal.value > 5000000 ? 0 : 30000;
});

const discount = computed(() => {
    return props.cartItems.reduce((total, item) => {
        const originalTotal = item.originalPrice ? item.originalPrice * item.quantity : 0;
        const currentTotal = item.price * item.quantity;
        return total + (originalTotal > 0 ? originalTotal - currentTotal : 0);
    }, 0);
});

const total = computed(() => {
    return subtotal.value + shippingFee.value - discount.value;
});

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};
</script>