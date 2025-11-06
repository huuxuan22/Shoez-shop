<template>
    <div class="relative">
        <!-- Bell Icon -->
        <button @click="toggleDropdown" class="relative p-2 text-gray-700 hover:text-black transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>

            <!-- Badge -->
            <span v-if="unreadCount > 0"
                class="absolute -top-1 -right-1 bg-red-500 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center">
                {{ unreadCount > 9 ? '9+' : unreadCount }}
            </span>
        </button>

        <!-- Dropdown -->
        <Transition name="fade">
            <div v-if="showDropdown"
                class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-gray-200 z-50 max-h-96 overflow-hidden flex flex-col">
                <!-- Header -->
                <div class="p-4 border-b border-gray-200 flex items-center justify-between">
                    <h3 class="font-semibold text-gray-900">{{ $t('Notifications.Bell.title') }}</h3>
                    <button v-if="unreadCount > 0" @click="markAllAsRead"
                        class="text-sm text-blue-600 hover:text-blue-800">
                        {{ $t('Notifications.Bell.markAllAsRead') }}
                    </button>
                </div>

                <!-- Notifications List -->
                <div class="overflow-y-auto">
                    <div v-if="notifications.length === 0" class="p-8 text-center text-gray-500">
                        {{ $t('Notifications.Bell.noNotifications') }}
                    </div>

                    <div v-for="notification in notifications" :key="notification.id" @click="handleClick(notification)"
                        class="p-4 hover:bg-gray-50 cursor-pointer transition-colors border-b border-gray-100 last:border-b-0"
                        :class="{ 'bg-blue-50': !notification.is_read }">
                        <div class="flex items-start gap-3">
                            <!-- Icon -->
                            <div class="flex-shrink-0 mt-1">
                                <svg v-if="notification.type === 'order_confirmed' || notification.type === 'order_delivered'"
                                    class="w-5 h-5 text-green-600" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <svg v-else-if="notification.type === 'order_shipping'" class="w-5 h-5 text-purple-600"
                                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0" />
                                </svg>
                                <svg v-else class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </div>

                            <!-- Content -->
                            <div class="flex-1 min-w-0">
                                <p class="font-semibold text-sm text-gray-900">
                                    {{ notification.title }}
                                </p>
                                <p class="text-sm text-gray-600 mt-1">
                                    {{ notification.message }}
                                </p>
                                <p class="text-xs text-gray-400 mt-2">
                                    {{ formatTime(notification.timestamp) }}
                                </p>
                            </div>

                            <!-- Unread indicator -->
                            <div v-if="!notification.is_read" class="flex-shrink-0">
                                <div class="w-2 h-2 bg-blue-600 rounded-full"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Footer -->
                <div v-if="notifications.length > 0" class="p-4 border-t border-gray-200 text-center">
                    <button @click="viewAll" class="text-sm text-blue-600 hover:text-blue-800 font-medium">
                        {{ $t('Notifications.Bell.viewAll') }}
                    </button>
                </div>
            </div>
        </Transition>

        <!-- Backdrop -->
        <Transition name="fade">
            <div v-if="showDropdown" @click="toggleDropdown" class="fixed inset-0 z-40"></div>
        </Transition>
    </div>
</template>

<script setup>
/**
 * NotificationBell Component
 * Giải thích: Bell icon hiển thị số notifications chưa đọc
 * 
 * Features:
 * - Hiển thị badge với số unread notifications
 * - Dropdown danh sách notifications
 * - Click notification để đánh dấu đã đọc
 * - Click bên ngoài để đóng dropdown
 */
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useNotificationStore } from '@/stores/notification';

const { t } = useI18n();

const router = useRouter();
const notificationStore = useNotificationStore();

const showDropdown = ref(false);

// Computed từ store
const notifications = computed(() => notificationStore.notifications);
const unreadCount = computed(() => notificationStore.unreadCount);

/**
 * Toggle dropdown
 */
const toggleDropdown = () => {
    showDropdown.value = !showDropdown.value;
};

/**
 * Click notification
 * Giải thích: Khi click vào notification, chuyển đến trang chi tiết đơn hàng 
 * để hiển thị trạng thái hiện tại của đơn hàng đó
 */
const handleClick = (notification) => {
    // Đánh dấu đã đọc
    notificationStore.markAsRead(notification.id);

    // Nếu có order_id, navigate đến order detail để hiển thị trạng thái hiện tại
    if (notification.order_id) {
        router.push(`/orders/${notification.order_id}`);
        toggleDropdown();
    }
};

/**
 * Đánh dấu tất cả đã đọc
 */
const markAllAsRead = () => {
    notificationStore.markAllAsRead();
};

/**
 * Xem tất cả notifications
 */
const viewAll = () => {
    router.push('/notifications');
    toggleDropdown();
};

/**
 * Format time
 */
const formatTime = (timestamp) => {
    if (!timestamp) return '';

    const date = new Date(timestamp);
    const now = new Date();
    const diff = now - date;

    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (seconds < 60) return t('Notifications.Bell.timeAgo.justNow');
    if (minutes < 60) return t('Notifications.Bell.timeAgo.minutesAgo', { count: minutes });
    if (hours < 24) return t('Notifications.Bell.timeAgo.hoursAgo', { count: hours });
    if (days < 7) return t('Notifications.Bell.timeAgo.daysAgo', { count: days });

    return date.toLocaleDateString();
};

/**
 * Click outside to close
 */
const handleClickOutside = (event) => {
    if (!event.target.closest('.relative')) {
        showDropdown.value = false;
    }
};

onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
