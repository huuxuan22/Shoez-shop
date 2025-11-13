<template>
    <div class="min-h-screen bg-gradient-to-br from-[#A50064] to-[#D82D8B] flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8">
            <!-- Demo Badge -->
            <div class="mb-6 text-center">
                <div
                    class="inline-block bg-yellow-100 text-yellow-800 text-xs font-semibold px-3 py-1 rounded-full mb-4">
                    {{ t('Views.PaymentDemo.badge') }}
                </div>
                <div
                    class="w-20 h-20 bg-gradient-to-br from-[#A50064] to-[#D82D8B] rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg class="w-12 h-12 text-white" fill="currentColor" viewBox="0 0 24 24">
                        <path
                            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z" />
                    </svg>
                </div>
                <h1 class="text-2xl font-bold text-gray-800 mb-2">{{ t('Views.PaymentDemo.title') }}</h1>
                <p class="text-gray-600 text-sm">{{ t('Views.PaymentDemo.subtitle') }}</p>
            </div>

            <!-- Order Info -->
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <div class="flex justify-between items-center mb-2">
                    <span class="text-gray-600">{{ t('Views.PaymentDemo.orderIdLabel') }}</span>
                    <span class="font-semibold text-gray-800">{{ orderId }}</span>
                </div>
                <div class="flex justify-between items-center mb-2">
                    <span class="text-gray-600">{{ t('Views.PaymentDemo.amountLabel') }}</span>
                    <span class="font-bold text-lg text-[#A50064]">{{ formatPrice(amount) }}</span>
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-gray-600">{{ t('Views.PaymentDemo.transactionIdLabel') }}</span>
                    <span class="text-xs text-gray-500 font-mono">{{ transactionId }}</span>
                </div>
            </div>

            <!-- Payment Form -->
            <div class="space-y-4 mb-6" v-if="currentStep === 'credentials'">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">
                        {{ t('Views.PaymentDemo.phoneLabel') }}
                    </label>
                    <input v-model="phoneNumber" type="text" :placeholder="t('Views.PaymentDemo.phonePlaceholder')"
                        maxlength="10"
                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#A50064] focus:border-transparent"
                        @input="formatPhoneInput" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">
                        {{ t('Views.PaymentDemo.passwordLabel') }}
                    </label>
                    <input v-model="password" type="password" :placeholder="t('Views.PaymentDemo.passwordPlaceholder')"
                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#A50064] focus:border-transparent" />
                </div>
            </div>

            <!-- OTP Form -->
            <div v-else class="space-y-4 mb-6">
                <div class="bg-purple-50 border border-purple-200 rounded-lg p-4">
                    <h2 class="text-sm font-semibold text-purple-800 mb-2">{{ t('Views.PaymentDemo.otpTitle') }}</h2>
                    <p class="text-xs text-purple-700">
                        {{ t('Views.PaymentDemo.otpInstruction') }}
                    </p>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">
                        {{ t('Views.PaymentDemo.otpInputLabel') }}
                    </label>
                    <input v-model="otpCode" type="text" maxlength="6"
                        :placeholder="t('Views.PaymentDemo.otpPlaceholder')"
                        class="w-full otp-input px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#A50064] focus:border-transparent tracking-[0.6em]"
                        @input="handleOtpInput" />
                    <p class="text-xs text-gray-500 mt-2">
                        {{ t('Views.PaymentDemo.otpDemoCodeMessage', { code: demoOtpCode }) }}
                    </p>
                    <p v-if="otpError" class="text-sm text-red-600 mt-2">{{ otpError }}</p>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="space-y-3" v-if="currentStep === 'credentials'">
                <button @click="handleSuccessClick" :disabled="processing"
                    class="w-full bg-gradient-to-r from-[#A50064] to-[#D82D8B] text-white font-semibold py-3 rounded-lg hover:opacity-90 transition-opacity disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2">
                    <span v-if="!processing">{{ t('Views.PaymentDemo.buttons.continue') }}</span>
                    <span v-else class="flex items-center gap-2">
                        <svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4">
                            </circle>
                            <path class="opacity-75" fill="currentColor"
                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                            </path>
                        </svg>
                        {{ t('Views.PaymentDemo.buttons.processing') }}
                    </span>
                </button>

                <button @click="cancelPayment"
                    class="w-full bg-gray-200 text-gray-700 font-semibold py-3 rounded-lg hover:bg-gray-300 transition-colors">
                    {{ t('Views.PaymentDemo.buttons.cancel') }}
                </button>
            </div>

            <div class="space-y-3" v-else>
                <button @click="confirmOtp" :disabled="processing"
                    class="w-full bg-gradient-to-r from-[#A50064] to-[#D82D8B] text-white font-semibold py-3 rounded-lg hover:opacity-90 transition-opacity disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2">
                    <span v-if="!processing">{{ t('Views.PaymentDemo.buttons.confirm') }}</span>
                    <span v-else class="flex items-center gap-2">
                        <svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4">
                            </circle>
                            <path class="opacity-75" fill="currentColor"
                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                            </path>
                        </svg>
                        {{ t('Views.PaymentDemo.buttons.processing') }}
                    </span>
                </button>

                <button @click="backToCredentials" :disabled="processing"
                    class="w-full bg-white border border-gray-300 text-gray-700 font-semibold py-3 rounded-lg hover:bg-gray-50 transition-colors">
                    {{ t('Views.PaymentDemo.buttons.back') }}
                </button>

                <button @click="cancelPayment"
                    class="w-full bg-gray-200 text-gray-700 font-semibold py-3 rounded-lg hover:bg-gray-300 transition-colors">
                    {{ t('Views.PaymentDemo.buttons.cancel') }}
                </button>
            </div>

            <!-- Info Box -->
            <div class="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <p class="text-xs text-blue-800">
                    <strong>{{ t('Views.PaymentDemo.infoNoteLabel') }}</strong>
                    {{ t('Views.PaymentDemo.infoNoteText') }}
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import BaseAxios from '@/api-services/BaseAxios';
import { useToast } from '@/composables/useToast';
import { useI18n } from 'vue-i18n';

const route = useRoute();
const router = useRouter();
const toast = useToast();
const { t } = useI18n();

const orderId = ref('');
const amount = ref(0);
const transactionId = ref('');
const returnUrl = ref('');
const phoneNumber = ref('');
const password = ref('');
const processing = ref(false);
const currentStep = ref('credentials');
const otpCode = ref('');
const otpError = ref('');
const demoOtpCode = '123456';

onMounted(() => {
    orderId.value = route.query.order_id || '';
    amount.value = parseInt(route.query.amount) || 0;
    transactionId.value = route.query.transaction_id || '';
    returnUrl.value = route.query.return_url || '';
});

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price);
};

const formatPhoneInput = (event) => {
    let value = event.target.value.replace(/\D/g, '');
    if (value.length > 10) {
        value = value.slice(0, 10);
    }
    phoneNumber.value = value;
    event.target.value = value;
};

const handleSuccessClick = () => {
    if (processing.value) {
        return;
    }

    if (phoneNumber.value.length !== 10) {
        toast.error(t('Views.PaymentDemo.toasts.invalidPhone'));
        return;
    }

    if (!password.value) {
        toast.error(t('Views.PaymentDemo.toasts.missingPassword'));
        return;
    }

    otpCode.value = '';
    otpError.value = '';
    currentStep.value = 'otp';
    toast.info(t('Views.PaymentDemo.toasts.otpSent'));
};

const handleOtpInput = (event) => {
    let value = event.target.value.replace(/\D/g, '');
    if (value.length > 6) {
        value = value.slice(0, 6);
    }
    otpCode.value = value;
    event.target.value = value;
};

const backToCredentials = () => {
    otpCode.value = '';
    otpError.value = '';
    currentStep.value = 'credentials';
};

const processPayment = async (result) => {
    if (!orderId.value) {
        toast.error(t('Views.PaymentDemo.toasts.noOrder'));
        return;
    }

    processing.value = true;

    try {
        // Gọi demo callback endpoint
        const response = await BaseAxios.post('/payments/momo/demo-callback', {
            order_id: orderId.value,
            result: result
        });

        const data = response.data;

        if (response.status === 200) {
            if (result === 'success') {
                toast.success(t('Views.PaymentDemo.toasts.success'));
                // Redirect về return URL hoặc success page
                if (returnUrl.value) {
                    window.location.href = returnUrl.value;
                } else {
                    router.push(`/payment/success?order_id=${orderId.value}`);
                }
            } else {
                toast.error(t('Views.PaymentDemo.toasts.failure'));
                router.push(`/payment/cancel?order_id=${orderId.value}`);
            }
        } else {
            toast.error(data.message || t('Views.PaymentDemo.toasts.genericError'));
        }
    } catch (error) {
        console.error('Error processing demo payment:', error);
        toast.error(t('Views.PaymentDemo.toasts.processError'));
    } finally {
        processing.value = false;
    }
};

const confirmOtp = async () => {
    if (processing.value) {
        return;
    }

    if (otpCode.value.length !== 6) {
        otpError.value = t('Views.PaymentDemo.otpErrors.incomplete');
        return;
    }

    if (otpCode.value !== demoOtpCode) {
        otpError.value = t('Views.PaymentDemo.otpErrors.incorrect');
        toast.error(t('Views.PaymentDemo.toasts.otpInvalid'));
        return;
    }

    otpError.value = '';

    await processPayment('success');
};

const cancelPayment = () => {
    router.push(`/payment/cancel?order_id=${orderId.value}`);
};
</script>

<style scoped>
/* Additional styles if needed */
</style>
