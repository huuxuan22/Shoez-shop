<template>
    <div class="bg-white border border-gray-200 rounded-lg p-6 sticky top-4">
        <h2 class="text-xl font-bold text-black mb-6">{{ $t('Cart.Summary.title') }}</h2>

        <div class="space-y-3">
            <div class="flex justify-between text-gray-600">
                <span>{{ $t('Cart.Summary.subtotal') }} ({{ totalItems }} {{ $t('Cart.Summary.itemsSuffix') }})</span>
                <span>{{ formatPrice(subtotal) }}</span>
            </div>

            <div class="flex justify-between text-gray-600">
                <span>{{ $t('Cart.Summary.shippingFee') }}</span>
                <span>{{ shippingFee > 0 ? formatPrice(shippingFee) : $t('Cart.Summary.shippingFree') }}</span>
            </div>

            <div class="flex justify-between text-gray-600">
                <span>{{ $t('Cart.Summary.discount') }}</span>
                <span class="text-green-600">-{{ formatPrice(discount) }}</span>
            </div>

            <Divider />

            <div class="flex justify-between text-lg font-bold text-black">
                <span>{{ $t('Cart.Summary.total') }}</span>
                <span>{{ formatPrice(total) }}</span>
            </div>
        </div>

        <div class="mt-6 space-y-2">
            <button @click="$emit('checkout-selected')" :disabled="selectedCount === 0"
                class="w-full bg-black text-white px-4 py-3 rounded-lg disabled:opacity-50">
                {{ $t('Cart.Summary.checkout') }} ({{ selectedCount }})
            </button>

            <div class="text-center">
                <button class="text-gray-600 hover:text-black transition-colors text-sm">
                    {{ $t('Cart.Summary.continueShopping') }}
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';
import Button from '../Button.vue';
import Divider from '../Divider.vue';

const { t } = useI18n();

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