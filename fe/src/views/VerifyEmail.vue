<template>
    <!-- Toast Notification -->
    <Teleport to="body">
        <Transition name="toast">
            <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
                <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
            </div>
        </Transition>
    </Teleport>

    <div
        class="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100 py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
            <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8">
                <!-- Header -->
                <div class="text-center mb-8">
                    <div
                        class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-gradient-to-br from-gray-800 to-black mb-4">
                        <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                    </div>
                    <h2 class="text-3xl font-bold text-gray-900">Xác thực Email</h2>
                    <p class="mt-2 text-sm text-gray-600">
                        Chúng tôi đã gửi mã xác thực đến email
                    </p>
                    <p class="mt-1 text-sm font-semibold text-gray-800">{{ email || 'email của bạn' }}</p>
                </div>

                <!-- Form xác thực -->
                <Form @submit="onSubmit" :validation-schema="schema" class="mt-6 space-y-6">
                    <!-- Mã xác thực -->
                    <div>
                        <label for="code" class="block text-sm font-medium text-gray-700 mb-2">
                            Nhập mã xác thực 6 chữ số
                        </label>
                        <Field name="code" type="text" id="code" maxlength="6" autocomplete="off"
                            class="mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800 text-center text-2xl font-bold tracking-widest sm:text-sm px-4 py-3 border"
                            placeholder="000000" @input="handleCodeInput" v-model="code" />
                        <ErrorMessage name="code" class="text-red-600 text-sm mt-1 block" />
                        <p v-if="code.length === 6 && code.length > 0" class="text-sm text-gray-500 mt-2">
                            Đang kiểm tra...
                        </p>
                    </div>

                    <!-- Email (ẩn) -->
                    <Field name="email" type="hidden" :value="email" />

                    <!-- Submit Button -->
                    <div>
                        <FormButton :label="isVerifying ? 'Đang xác thực...' : 'Xác thực Email'" type="submit"
                            variant="black" class="w-full" :disabled="isVerifying || code.length !== 6" />
                    </div>

                    <!-- Resend code -->
                    <div class="text-center">
                        <p class="text-sm text-gray-600">
                            Chưa nhận được mã?
                        </p>
                        <button type="button" @click="resendCode" :disabled="isResending || resendCooldown > 0"
                            class="mt-2 text-sm font-medium text-gray-800 hover:text-black disabled:text-gray-400 disabled:cursor-not-allowed">
                            {{ resendCooldown > 0 ? `Gửi lại sau ${resendCooldown}s` : 'Gửi lại mã' }}
                        </button>
                    </div>
                </Form>
            </div>

            <!-- Footer -->
            <div class="text-center">
                <p class="text-sm text-gray-600">
                    Quay lại
                    <router-link to="/register" class="font-medium text-gray-800 hover:text-black">
                        Đăng ký
                    </router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import FormButton from "../components/FormButton.vue";
import ToastNotification from '@/components/ToastNotification.vue';
import { useAuthStore } from "@/stores/auth";
import { useRouter, useRoute } from "vue-router";
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import { verifyEmailApi, resendVerificationCodeApi } from "@/api-services/AuthService";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

// State
const email = ref(route.query.email || '');
const code = ref('');
const isVerifying = ref(false);
const isResending = ref(false);
const resendCooldown = ref(0);
let cooldownTimer = null;

// Toast notification
let timer = null;
const toast = ref({
    show: false,
    message: '',
    type: 'info',
});

// Show toast function
function showToast(message, type = 'info') {
    if (timer) {
        clearTimeout(timer);
    }
    toast.value.show = true;
    toast.value.message = message;
    toast.value.type = type;

    timer = setTimeout(() => {
        toast.value.show = false;
    }, 3000);
}

// Validation schema
const schema = yup.object({
    email: yup
        .string()
        .required("Email là bắt buộc")
        .email("Email không hợp lệ"),
    code: yup
        .string()
        .required("Vui lòng nhập mã xác thực")
        .length(6, "Mã xác thực phải có 6 chữ số")
        .matches(/^\d+$/, "Mã xác thực chỉ chứa số"),
});

// Handle code input - chỉ cho phép số
const handleCodeInput = (event) => {
    const value = event.target.value.replace(/\D/g, '');
    code.value = value.slice(0, 6);
    event.target.value = code.value;
};

// Submit handler
const onSubmit = async (values) => {
    if (code.value.length !== 6) {
        showToast('Vui lòng nhập đủ 6 chữ số', 'error');
        return;
    }

    isVerifying.value = true;
    try {
        const response = await verifyEmailApi({
            email: email.value,
            code: code.value
        });

        // Lưu thông tin đăng nhập
        if (response.data) {
            authStore.user = response.data.user_principal;
            authStore.accessToken = response.data.access_token;
            authStore.refreshToken = response.data.refresh_token;

            localStorage.setItem("token", response.data.access_token);
            localStorage.setItem("refresh_token", response.data.refresh_token);
            localStorage.setItem("user", JSON.stringify(response.data.user_principal));
        }

        showToast(response.data?.message || 'Xác thực thành công!', 'success');

        setTimeout(() => {
            router.push('/');
        }, 1500);
    } catch (error) {
        const errorMessage = error.response?.data?.detail || error.message || 'Xác thực thất bại!';
        showToast(errorMessage, 'error');
    } finally {
        isVerifying.value = false;
    }
};

// Resend code
const resendCode = async () => {
    if (!email.value) {
        showToast('Không tìm thấy email. Vui lòng đăng ký lại.', 'error');
        router.push('/register');
        return;
    }

    isResending.value = true;
    try {
        await resendVerificationCodeApi({ email: email.value });
        showToast('Đã gửi lại mã xác thực!', 'success');

        // Bắt đầu đếm ngược 60 giây
        resendCooldown.value = 60;
        cooldownTimer = setInterval(() => {
            resendCooldown.value--;
            if (resendCooldown.value <= 0) {
                clearInterval(cooldownTimer);
                cooldownTimer = null;
            }
        }, 1000);
    } catch (error) {
        const errorMessage = error.response?.data?.detail || error.message || 'Gửi lại mã thất bại!';
        showToast(errorMessage, 'error');
    } finally {
        isResending.value = false;
    }
};

onMounted(() => {
    // Nếu không có email, redirect về trang đăng ký
    if (!email.value) {
        showToast('Vui lòng đăng ký để nhận mã xác thực', 'error');
        setTimeout(() => {
            router.push('/register');
        }, 2000);
    }
});

onBeforeUnmount(() => {
    if (cooldownTimer) {
        clearInterval(cooldownTimer);
    }
    if (timer) {
        clearTimeout(timer);
    }
});
</script>

<style scoped>
/* Toast animations */
.toast-enter-active,
.toast-leave-active {
    transition: all 0.3s ease;
}

.toast-enter-from {
    opacity: 0;
    transform: translateX(100%);
}

.toast-leave-to {
    opacity: 0;
    transform: translateX(100%);
}
</style>