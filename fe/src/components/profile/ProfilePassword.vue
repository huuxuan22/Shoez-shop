<template>
    <div class="p-6">
        <div class="flex items-center justify-between mb-6">
            <h2 class="text-xl font-bold text-black">Đổi mật khẩu</h2>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6 max-w-2xl">
            <!-- Current Password -->
            <InputField label="Mật khẩu hiện tại" name="currentPassword" type="password"
                v-model="formData.currentPassword" placeholder="Nhập mật khẩu hiện tại" :required="true"
                :error-message="errors.currentPassword" />

            <!-- New Password -->
            <InputField label="Mật khẩu mới" name="newPassword" type="password" v-model="formData.newPassword"
                placeholder="Nhập mật khẩu mới" :required="true" :error-message="errors.newPassword"
                hint="Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và số" />

            <!-- Confirm Password -->
            <InputField label="Xác nhận mật khẩu mới" name="confirmPassword" type="password"
                v-model="formData.confirmPassword" placeholder="Nhập lại mật khẩu mới" :required="true"
                :error-message="errors.confirmPassword" />

            <!-- Password Strength Indicator -->
            <div v-if="formData.newPassword" class="p-4 bg-gray-50 rounded-lg">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-sm font-medium text-gray-700">Độ mạnh mật khẩu:</span>
                    <span :class="passwordStrengthClass">{{ passwordStrengthText }}</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                    <div :class="passwordStrengthBarClass" class="h-2 rounded-full transition-all duration-300"
                        :style="{ width: passwordStrength + '%' }"></div>
                </div>
            </div>

            <!-- Security Tips -->
            <div class="p-4 bg-blue-50 rounded-lg">
                <h4 class="font-semibold text-blue-800 mb-2">Mẹo bảo mật:</h4>
                <ul class="text-sm text-blue-700 space-y-1">
                    <li>• Sử dụng mật khẩu dài ít nhất 8 ký tự</li>
                    <li>• Kết hợp chữ hoa, chữ thường, số và ký tự đặc biệt</li>
                    <li>• Không sử dụng thông tin cá nhân làm mật khẩu</li>
                    <li>• Đổi mật khẩu định kỳ 3-6 tháng một lần</li>
                </ul>
            </div>

            <!-- Action Buttons -->
            <div class="flex justify-end gap-3 pt-6 border-t border-gray-200">
                <Button type="button" variant="outline" @click="resetForm" :disabled="isLoading">
                    Hủy
                </Button>
                <Button type="submit" variant="primary" :disabled="isLoading || !isFormValid">
                    <span v-if="isLoading" class="flex items-center gap-2">
                        <svg class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                        Đang đổi mật khẩu...
                    </span>
                    <span v-else>
                        Đổi mật khẩu
                    </span>
                </Button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import InputField from './../FormInput.vue';
import Button from './../Button.vue';

const props = defineProps({
    isLoading: Boolean
});

const emit = defineEmits(['change-password']);

// Form data
const formData = reactive({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

// Errors
const errors = reactive({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

// Computed
const isFormValid = computed(() => {
    return formData.currentPassword &&
        formData.newPassword &&
        formData.confirmPassword &&
        formData.newPassword === formData.confirmPassword &&
        formData.newPassword.length >= 8;
});

const passwordStrength = computed(() => {
    const password = formData.newPassword;
    if (!password) return 0;

    let strength = 0;

    // Length check
    if (password.length >= 8) strength += 25;
    if (password.length >= 12) strength += 15;

    // Character variety
    if (/[a-z]/.test(password)) strength += 15;
    if (/[A-Z]/.test(password)) strength += 15;
    if (/[0-9]/.test(password)) strength += 15;
    if (/[^a-zA-Z0-9]/.test(password)) strength += 15;

    return Math.min(strength, 100);
});

const passwordStrengthText = computed(() => {
    const strength = passwordStrength.value;
    if (strength < 40) return 'Yếu';
    if (strength < 70) return 'Trung bình';
    if (strength < 90) return 'Mạnh';
    return 'Rất mạnh';
});

const passwordStrengthClass = computed(() => {
    const strength = passwordStrength.value;
    if (strength < 40) return 'text-red-600 font-semibold';
    if (strength < 70) return 'text-yellow-600 font-semibold';
    if (strength < 90) return 'text-blue-600 font-semibold';
    return 'text-green-600 font-semibold';
});

const passwordStrengthBarClass = computed(() => {
    const strength = passwordStrength.value;
    if (strength < 40) return 'bg-red-500';
    if (strength < 70) return 'bg-yellow-500';
    if (strength < 90) return 'bg-blue-500';
    return 'bg-green-500';
});

// Methods
const validateForm = () => {
    let isValid = true;

    // Reset errors
    Object.keys(errors).forEach(key => errors[key] = '');

    // Current password validation
    if (!formData.currentPassword) {
        errors.currentPassword = 'Vui lòng nhập mật khẩu hiện tại';
        isValid = false;
    }

    // New password validation
    if (!formData.newPassword) {
        errors.newPassword = 'Vui lòng nhập mật khẩu mới';
        isValid = false;
    } else if (formData.newPassword.length < 8) {
        errors.newPassword = 'Mật khẩu phải có ít nhất 8 ký tự';
        isValid = false;
    }

    // Confirm password validation
    if (!formData.confirmPassword) {
        errors.confirmPassword = 'Vui lòng xác nhận mật khẩu mới';
        isValid = false;
    } else if (formData.newPassword !== formData.confirmPassword) {
        errors.confirmPassword = 'Mật khẩu xác nhận không khớp';
        isValid = false;
    }

    return isValid;
};

const handleSubmit = async () => {
    if (!validateForm()) return;

    const success = await emit('change-password', formData);
    if (success) {
        resetForm();
    }
};

const resetForm = () => {
    formData.currentPassword = '';
    formData.newPassword = '';
    formData.confirmPassword = '';
    Object.keys(errors).forEach(key => errors[key] = '');
};
</script>