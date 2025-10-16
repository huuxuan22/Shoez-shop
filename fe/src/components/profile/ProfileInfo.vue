<template>
    <div class="p-6">
        <div class="flex items-center justify-between mb-6">
            <h2 class="text-xl font-bold text-black">Thông tin cá nhân</h2>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Full Name -->
                <InputField label="Họ và tên" name="fullName" v-model="formData.fullName" placeholder="Nhập họ và tên"
                    :required="true" />

                <!-- Email -->
                <InputField label="Email" name="email" type="email" v-model="formData.email" placeholder="Nhập email"
                    :required="true" :disabled="true" />

                <!-- Phone -->
                <InputField label="Số điện thoại" name="phone" type="tel" v-model="formData.phone"
                    placeholder="Nhập số điện thoại" :required="true" />

                <!-- Birthday -->
                <InputField label="Ngày sinh" name="birthday" type="date" v-model="formData.birthday"
                    :required="true" />

                <!-- Gender -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">
                        Giới tính
                    </label>
                    <div class="flex gap-4">
                        <label class="flex items-center">
                            <input type="radio" value="male" v-model="formData.gender"
                                class="text-black focus:ring-black" />
                            <span class="ml-2 text-gray-700">Nam</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="female" v-model="formData.gender"
                                class="text-black focus:ring-black" />
                            <span class="ml-2 text-gray-700">Nữ</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="other" v-model="formData.gender"
                                class="text-black focus:ring-black" />
                            <span class="ml-2 text-gray-700">Khác</span>
                        </label>
                    </div>
                </div>
            </div>

            <!-- Address -->
            <div>
                <InputField label="Địa chỉ" name="address" v-model="formData.address" placeholder="Nhập địa chỉ"
                    :required="true" />
            </div>

            <!-- Action Buttons -->
            <div class="flex justify-end gap-3 pt-6 border-t border-gray-200">
                <Button type="button" variant="outline" @click="resetForm" :disabled="isLoading">
                    Hủy
                </Button>
                <Button type="submit" variant="primary" :disabled="isLoading || !hasChanges">
                    <span v-if="isLoading" class="flex items-center gap-2">
                        <svg class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                        Đang lưu...
                    </span>
                    <span v-else>
                        Lưu thay đổi
                    </span>
                </Button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref, reactive, watch, computed } from 'vue';
import InputField from './../FormInput.vue';
import Button from './../Button.vue';

const props = defineProps({
    user: Object,
    isLoading: Boolean
});

const emit = defineEmits(['update-profile']);

// Form data
const formData = reactive({
    fullName: props.user.fullName,
    email: props.user.email,
    phone: props.user.phone,
    address: props.user.address,
    birthday: props.user.birthday,
    gender: props.user.gender
});

// Original data for comparison
const originalData = ref({ ...formData });

// Computed
const hasChanges = computed(() => {
    return JSON.stringify(formData) !== JSON.stringify(originalData.value);
});

// Methods
const handleSubmit = () => {
    if (!hasChanges.value) return;
    emit('update-profile', formData);
};

const resetForm = () => {
    Object.assign(formData, originalData.value);
};

// Update original data when user prop changes
watch(() => props.user, (newUser) => {
    Object.assign(formData, {
        fullName: newUser.fullName,
        email: newUser.email,
        phone: newUser.phone,
        address: newUser.address,
        birthday: newUser.birthday,
        gender: newUser.gender
    });
    originalData.value = { ...formData };
}, { immediate: true });
</script>