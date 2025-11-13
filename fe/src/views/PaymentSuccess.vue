<template>
    <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-xl max-w-md w-full p-8 text-center">
            <!-- Success Icon -->
            <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-12 h-12 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
            </div>

            <!-- Title -->
            <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ t('Views.PaymentSuccess.title') }}</h1>
            <p class="text-gray-600 mb-8">{{ t('Views.PaymentSuccess.description') }}</p>

            <!-- Order Info -->
            <div v-if="orderId" class="bg-gray-50 rounded-lg p-4 mb-6">
                <p class="text-sm text-gray-600 mb-1">{{ t('Views.PaymentSuccess.orderIdLabel') }}</p>
                <p class="font-semibold text-gray-800">{{ orderId }}</p>
            </div>

            <!-- Action Buttons -->
            <div class="space-y-3">
                <button @click="viewOrder"
                    class="w-full bg-black text-white font-semibold py-3 rounded-lg hover:bg-gray-800 transition-colors">
                    {{ t('Views.PaymentSuccess.actions.viewOrder') }}
                </button>
                <button @click="goHome"
                    class="w-full bg-gray-200 text-gray-700 font-semibold py-3 rounded-lg hover:bg-gray-300 transition-colors">
                    {{ t('Views.PaymentSuccess.actions.goHome') }}
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
