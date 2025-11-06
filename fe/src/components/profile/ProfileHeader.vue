<template>
    <div class="flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-bold text-black">{{ $t('Profile.Header.title') }}</h1>
            <p class="text-gray-600 mt-2">{{ $t('Profile.Header.subtitle') }}</p>
        </div>

        <div class="flex items-center gap-4">
            <div class="text-right">
                <p class="font-semibold text-black">{{ user.fullName }}</p>
                <p class="text-sm text-gray-600">{{ $t('Profile.Header.memberSince') }} {{ formatJoinDate(user.joinDate) }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    user: Object,
    activeTab: String
});

const formatJoinDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('vi-VN');
};
</script>