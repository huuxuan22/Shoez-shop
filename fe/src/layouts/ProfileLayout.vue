<template>
    <div class="min-h-screen bg-gray-50">
        <Teleport to="body">
            <Transition name="toast">
                <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
                    <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
                </div>
            </Transition>
        </Teleport>
        <div class="container mx-auto px-4 py-8">
            <!-- Header -->
            <ProfileHeader :user="user" :active-tab="activeTab" @update:active-tab="activeTab = $event" />

            <div class="mt-8">
                <div class="flex flex-col lg:flex-row gap-8">
                    <!-- Left Sidebar -->
                    <div class="lg:w-1/4">
                        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 sticky top-4">
                            <!-- Avatar Section -->
                            <ProfileAvatar :user="user" :is-uploading="isUploading"
                                @avatar-change="handleAvatarChange" />

                            <!-- Navigation -->
                            <nav class="mt-6 space-y-2">
                                <button v-for="tab in tabs" :key="tab.id" @click="activeTab = tab.id" :class="[
                                    'w-full text-left px-4 py-3 rounded-lg transition-all font-medium',
                                    activeTab === tab.id
                                        ? 'bg-black text-white shadow-sm'
                                        : 'text-gray-600 hover:text-black hover:bg-gray-100'
                                ]">
                                    <div class="flex items-center gap-3">
                                        <img :src="tab.icon" :alt="tab.label" class="w-5 h-5" />
                                        <span>{{ tab.label }}</span>
                                    </div>
                                </button>
                            </nav>
                        </div>
                    </div>

                    <!-- Right Content -->
                    <div class="lg:w-3/4">
                        <div class="bg-white rounded-lg shadow-sm border border-gray-200">
                            <!-- Profile Information -->
                            <div v-if="activeTab === 'info'">
                                <ProfileInfo :user="user" :is-loading="isLoading"
                                    @update-profile="handleUpdateProfile" />
                            </div>

                            <!-- Change Password -->
                            <div v-else-if="activeTab === 'password'">
                                <ProfilePassword :is-loading="isLoading" @change-password="handleChangePassword" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth';
import UserService from '@/api-services/UserService';

// Import components
import ProfileHeader from '@/components/profile/ProfileHeader.vue';
import ProfileInfo from '@/components/profile/ProfileInfo.vue';
import ProfilePassword from '@/components/profile/ProfilePassword.vue';
import ProfileAvatar from '@/components/profile/ProfileAvatar.vue';
import ToastNotification from '@/components/ToastNotification.vue';

// Auth Store
const authStore = useAuthStore();
const { user: authUser } = storeToRefs(authStore);
let timer = null;

// State
const activeTab = ref('info');
const isLoading = ref(false);
const isUploading = ref(false);

const toast = reactive({
    show: false,
    message: '',
    type: 'info',
});

// 3. Thêm hàm kích hoạt toast
function showToast(message, type = 'info') {
    if (timer) {
        clearTimeout(timer);
    }
    toast.show = true;
    toast.message = message;
    toast.type = type;

    timer = setTimeout(() => {
        toast.show = false;
    }, 3000);
}

// Map user data from API to component format
const user = computed(() => {
    if (!authUser.value) {
        return {
            id: '',
            fullName: '',
            email: '',
            phone: '',
            address: '',
            birthday: '',
            gender: 'male',
            avatar: '',
            joinDate: new Date().toISOString()
        };
    }

    return {
        id: authUser.value.id,
        fullName: authUser.value.full_name || '',
        email: authUser.value.email || '',
        phone: authUser.value.numberphone || '',
        address: authUser.value.address || '',
        birthday: authUser.value.birthday || '',
        gender: authUser.value.gender || 'male',
        avatar: authUser.value.avatar || '',
        joinDate: authUser.value.created_at || new Date().toISOString()
    };
});

// Tabs configuration với đường dẫn trực tiếp
const tabs = [
    {
        id: 'info',
        label: 'Thông tin cá nhân',
        icon: '/src/assets/icons/user_icon.png'
    },
    {
        id: 'password',
        label: 'Đổi mật khẩu',
        icon: '/src/assets/icons/lock.png'
    }
];

// Methods
const handleUpdateProfile = async (profileData) => {
    isLoading.value = true;
    try {
        // Prepare data for API (map to API format)
        const apiData = {
            id: authUser.value.id,
            full_name: profileData.fullName,
            numberphone: profileData.phone,
            address: profileData.address,
            birthday: profileData.birthday,
            gender: profileData.gender
        };
        debugger;
        // Call API
        const response = await UserService.updateProfile(apiData);
        // Update user data in auth store
        debugger;
        if (response.user_update) {
            // Dùng action trong store để cập nhật
            await authStore.updateUser(response.user_update);
        }
        showToast('Cập nhật thành công!', 'success');
    } catch (error) {
        showToast('Cập nhật không thành công!', 'error');
        throw error;
    } finally {
        isLoading.value = false;
    }
};

const handleChangePassword = async (passwordData) => {
    isLoading.value = true;
    try {
        const payload = {
            id: authUser.value.id, // id người dùng hiện tại
            current_password: passwordData.currentPassword,
            new_password: passwordData.newPassword,
        };
        debugger;
        console.log(payload);

        // Simulate API call    
        const response = await UserService.changePassword(payload)
        await new Promise(resolve => setTimeout(resolve, 1000));

        showToast('Thay đổi mật khẩu thành công!', 'success');
        return true;
    } catch (error) {
        console.log(error);
        if (error?.status === 400) {
            showToast(error?.data?.detail, 'error');
        } else if (error?.status === 404) {
            showToast(error?.data?.detail, 'error');
        } else {
            showToast('Cập nhật người dùng không thành công', 'error');
        }
        return false;
    } finally {
        isLoading.value = false;
    }
};

const handleAvatarChange = async (file) => {
    isUploading.value = true;
    try {
        // Upload avatar to server
        const response = await UserService.uploadAvatar(file);

        // Update avatar in auth store
        if (authUser.value && response.avatar_url) {
            authUser.value.avatar = response.avatar_url;
            // Update localStorage
            localStorage.setItem("user", JSON.stringify(authUser.value));
        }

        console.log('✅ Cập nhật ảnh đại diện thành công!');
    } catch (error) {
        console.error('❌ Có lỗi xảy ra khi tải lên ảnh:', error);
        throw error;
    } finally {
        isUploading.value = false;
    }
};
</script>