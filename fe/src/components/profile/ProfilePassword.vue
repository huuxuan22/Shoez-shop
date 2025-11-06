<template>
    <div class="p-6">
        <div class="flex items-center justify-between mb-6">
            <h2 class="text-xl font-bold text-black">{{ $t('Profile.Password.title') }}</h2>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6 max-w-2xl">
            <!-- Current Password -->
            <InputField :label="$t('Profile.Password.currentPassword')" name="currentPassword" type="password"
                v-model="formData.currentPassword" :placeholder="$t('Profile.Password.currentPasswordPlaceholder')" :required="true"
                :error-message="errors.currentPassword" />

            <!-- New Password -->
            <InputField :label="$t('Profile.Password.newPassword')" name="newPassword" type="password" v-model="formData.newPassword"
                :placeholder="$t('Profile.Password.newPasswordPlaceholder')" :required="true" :error-message="errors.newPassword"
                :hint="$t('Profile.Password.passwordHint')" />

            <!-- Confirm Password -->
            <InputField :label="$t('Profile.Password.confirmPassword')" name="confirmPassword" type="password"
                v-model="formData.confirmPassword" :placeholder="$t('Profile.Password.confirmPasswordPlaceholder')" :required="true"
                :error-message="errors.confirmPassword" />

            <!-- Password Strength Indicator -->
            <div v-if="formData.newPassword" class="p-4 bg-gray-50 rounded-lg">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-sm font-medium text-gray-700">{{ $t('Profile.Password.strength') }}</span>
                    <span :class="passwordStrengthClass">{{ passwordStrengthText }}</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                    <div :class="passwordStrengthBarClass" class="h-2 rounded-full transition-all duration-300"
                        :style="{ width: passwordStrength + '%' }"></div>
                </div>
            </div>

            <!-- Security Tips -->
            <div class="p-4 bg-blue-50 rounded-lg">
                <h4 class="font-semibold text-blue-800 mb-2">{{ $t('Profile.Password.securityTips') }}</h4>
                <ul class="text-sm text-blue-700 space-y-1">
                    <li>• {{ $t('Profile.Password.tip1') }}</li>
                    <li>• {{ $t('Profile.Password.tip2') }}</li>
                    <li>• {{ $t('Profile.Password.tip3') }}</li>
                    <li>• {{ $t('Profile.Password.tip4') }}</li>
                </ul>
            </div>

            <!-- Action Buttons -->
            <div class="flex justify-end gap-3 pt-6 border-t border-gray-200">
                <Button type="button" variant="outline" @click="resetForm" :disabled="isLoading">
                    {{ $t('Profile.Password.cancel') }}
                </Button>
                <Button type="submit" variant="primary" :disabled="isLoading || !isFormValid">
                    <span v-if="isLoading" class="flex items-center gap-2">
                        <svg class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                        {{ $t('Profile.Password.changing') }}
                    </span>
                    <span v-else>
                        {{ $t('Profile.Password.changePassword') }}
                    </span>
                </Button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import InputField from './../FormInput.vue';
import Button from './../Button.vue';

const { t } = useI18n();

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
    if (strength < 40) return t('Profile.Password.strengthWeak');
    if (strength < 70) return t('Profile.Password.strengthMedium');
    if (strength < 90) return t('Profile.Password.strengthStrong');
    return t('Profile.Password.strengthVeryStrong');
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
        errors.currentPassword = t('Profile.Password.errors.currentPasswordRequired');
        isValid = false;
    }

    // New password validation
    if (!formData.newPassword) {
        errors.newPassword = t('Profile.Password.errors.newPasswordRequired');
        isValid = false;
    } else if (formData.newPassword.length < 8) {
        errors.newPassword = t('Profile.Password.errors.newPasswordMinLength');
        isValid = false;
    }
    // 🔹 Kiểm tra trùng với mật khẩu hiện tại
    else if (formData.newPassword === formData.currentPassword) {
        errors.newPassword = t('Profile.Password.errors.newPasswordSameAsCurrent');
        isValid = false;
    }

    // Confirm password validation
    if (!formData.confirmPassword) {
        errors.confirmPassword = t('Profile.Password.errors.confirmPasswordRequired');
        isValid = false;
    } else if (formData.newPassword !== formData.confirmPassword) {
        errors.confirmPassword = t('Profile.Password.errors.confirmPasswordMismatch');
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