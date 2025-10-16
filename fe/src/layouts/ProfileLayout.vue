<template>
    <div class="min-h-screen bg-gray-50">
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
import { ref, reactive } from 'vue';

// Import components
import ProfileHeader from '@/components/profile/ProfileHeader.vue';
import ProfileInfo from '@/components/profile/ProfileInfo.vue';
import ProfilePassword from '@/components/profile/ProfilePassword.vue';
import ProfileAvatar from '@/components/profile/ProfileAvatar.vue';


// State
const activeTab = ref('info');
const isLoading = ref(false);
const isUploading = ref(false);

// User data
const user = reactive({
    id: 1,
    fullName: 'Nguyễn Văn A',
    email: 'nguyenvana@example.com',
    phone: '0901234567',
    address: '123 Nguyễn Văn Linh, Quận 7, TP.HCM',
    birthday: '1990-01-01',
    gender: 'male',
    avatar: '/images/avatars/default-avatar.jpg',
    joinDate: '2023-01-15'
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
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000));

        // Update user data
        Object.assign(user, profileData);

        toast.success('Cập nhật thông tin thành công!');
    } catch (error) {
        toast.error('Có lỗi xảy ra khi cập nhật thông tin');
    } finally {
        isLoading.value = false;
    }
};

const handleChangePassword = async (passwordData) => {
    isLoading.value = true;
    try {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000));

        toast.success('Đổi mật khẩu thành công!');
        return true;
    } catch (error) {
        toast.error('Có lỗi xảy ra khi đổi mật khẩu');
        return false;
    } finally {
        isLoading.value = false;
    }
};

const handleAvatarChange = async (file) => {
    isUploading.value = true;
    try {
        // Simulate upload
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Create preview URL
        const previewUrl = URL.createObjectURL(file);
        user.avatar = previewUrl;

        toast.success('Cập nhật ảnh đại diện thành công!');
    } catch (error) {
        toast.error('Có lỗi xảy ra khi tải lên ảnh');
    } finally {
        isUploading.value = false;
    }
};
</script>