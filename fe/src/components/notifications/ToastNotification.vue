<template>
    <!-- Toast Container -->
    <Teleport to="body">
        <TransitionGroup name="toast" tag="div" class="fixed top-20 right-4 z-50 space-y-2">
            <!-- Toast Item -->
            <div v-for="toast in toasts" :key="toast.id"
                class="min-w-80 max-w-md bg-white rounded-lg shadow-xl border border-gray-200 p-4 flex items-start gap-3 animate-in slide-in-from-right"
                :class="getToastClass(toast.type)">
                <!-- Icon -->
                <div class="flex-shrink-0">
                    <svg v-if="toast.type === 'success'" class="w-6 h-6 text-green-600" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <svg v-else-if="toast.type === 'info'" class="w-6 h-6 text-blue-600" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <svg v-else class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                </div>

                <!-- Content -->
                <div class="flex-1 min-w-0">
                    <h3 class="font-semibold text-gray-900 text-sm">{{ toast.title }}</h3>
                    <p class="text-sm text-gray-600 mt-1">{{ toast.message }}</p>
                    <p v-if="toast.order_id" class="text-xs text-gray-500 mt-2">
                        {{ $t('Notifications.Toast.orderCode') }}#{{ toast.order_id }}
                    </p>
                </div>

                <!-- Close Button -->
                <button @click="removeToast(toast.id)"
                    class="flex-shrink-0 text-gray-400 hover:text-gray-600 transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        </TransitionGroup>
    </Teleport>
</template>

<script setup>
/**
 * ToastNotification Component
 * Giải thích: Component hiển thị toast notifications
 * 
 * Features:
 * - Auto dismiss sau 5 giây
 * - Multiple toasts có thể hiển thị cùng lúc
 * - Animation slide in from right
 * - Click để close
 */
import { ref, onMounted, onUnmounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useNotificationStore } from '@/stores/notification';

const { t } = useI18n();

const notificationStore = useNotificationStore();
const toasts = ref([]);
let unsubscribe;

onMounted(() => {
    // Subscribe to store để nhận notifications mới
    unsubscribe = notificationStore.$subscribe((mutation, state) => {
        const latestUnread = state.latestUnread;

        if (latestUnread) {
            // Kiểm tra xem notification này đã hiển thị chưa
            const alreadyShown = toasts.value.some(t => t.id === latestUnread.id);

            if (!alreadyShown) {
                showToast(latestUnread);
            }
        }
    });
});

onUnmounted(() => {
    if (unsubscribe) {
        unsubscribe();
    }
});

/**
 * Hiển thị toast
 */
const showToast = (notification) => {
    const toast = {
        id: Date.now(),
        type: getToastType(notification.type),
        title: notification.title || t('Notifications.Toast.defaultTitle'),
        message: notification.message,
        order_id: notification.order_id,
        duration: 5000 // 5 giây
    };

    toasts.value.push(toast);

    // Auto dismiss
    setTimeout(() => {
        removeToast(toast.id);
    }, toast.duration);
};

/**
 * Xóa toast
 */
const removeToast = (id) => {
    const index = toasts.value.findIndex(t => t.id === id);
    if (index > -1) {
        toasts.value.splice(index, 1);
        // Mark notification as read
        notificationStore.markAsRead(id);
    }
};

/**
 * Get toast type từ notification type
 */
const getToastType = (notificationType) => {
    const typeMap = {
        'order_confirmed': 'success',      // Đơn hàng đã được xác nhận
        'order_shipping': 'info',          // Đơn hàng đang giao
        'order_delivered': 'success',      // Đơn hàng đã được giao
        'order_placed': 'success',
        'new_order': 'info'
    };
    return typeMap[notificationType] || 'info';
};

/**
 * Get CSS class cho toast
 */
const getToastClass = (type) => {
    const classes = {
        success: 'border-green-200 bg-green-50',
        info: 'border-blue-200 bg-blue-50',
        warning: 'border-yellow-200 bg-yellow-50'
    };
    return classes[type] || classes.info;
};
</script>

<style scoped>
/* Transition animations */
.toast-enter-active {
    transition: all 0.3s ease-out;
}

.toast-enter-from {
    transform: translateX(100%);
    opacity: 0;
}

.toast-leave-active {
    transition: all 0.3s ease-in;
}

.toast-leave-to {
    transform: translateX(100%);
    opacity: 0;
}
</style>
