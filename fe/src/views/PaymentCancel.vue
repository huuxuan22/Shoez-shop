<template>
    <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-xl max-w-md w-full p-8 text-center">
            <!-- Cancel Icon -->
            <div class="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-12 h-12 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </div>

            <!-- Title -->
            <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ t('Views.PaymentCancel.title') }}</h1>
            <p class="text-gray-600 mb-8">{{ t('Views.PaymentCancel.description') }}</p>

            <!-- Order Info -->
            <div v-if="orderId" class="bg-gray-50 rounded-lg p-4 mb-6">
                <p class="text-sm text-gray-600 mb-1">{{ t('Views.PaymentCancel.orderIdLabel') }}</p>
                <p class="font-semibold text-gray-800">{{ orderId }}</p>
            </div>

            <!-- Action Buttons -->
            <div class="space-y-3">
                <button @click="retryPayment"
                    class="w-full bg-gradient-to-r from-[#A50064] to-[#D82D8B] text-white font-semibold py-3 rounded-lg hover:opacity-90 transition-opacity">
                    {{ t('Views.PaymentCancel.actions.retry') }}
                </button>
                <button @click="viewOrder"
                    class="w-full bg-gray-200 text-gray-700 font-semibold py-3 rounded-lg hover:bg-gray-300 transition-colors">
                    {{ t('Views.PaymentCancel.actions.viewOrder') }}
                </button>
                <button @click="goHome"
                    class="w-full bg-gray-100 text-gray-600 font-semibold py-3 rounded-lg hover:bg-gray-200 transition-colors">
                    {{ t('Views.PaymentCancel.actions.goHome') }}
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const route = useRoute();
const router = useRouter();
const orderId = ref('');
const { t } = useI18n();

onMounted(() => {
    orderId.value = route.query.order_id || '';
});

const retryPayment = () => {
    if (orderId.value) {
        router.push(`/checkout?order_id=${orderId.value}`);
    } else {
        router.push('/checkout');
    }
};

const viewOrder = () => {
    if (orderId.value) {
        router.push(`/orders/${orderId.value}`);
    } else {
        router.push('/orders');
    }
};

const goHome = () => {
    router.push('/');
};
</script>
