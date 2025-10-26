<template>
    <div class="min-h-screen bg-gray-50 py-8">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <!-- Header -->
                <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
                    <h1 class="text-2xl font-bold text-gray-900">Thông báo</h1>
                    <p class="text-gray-600 mt-2">Quản lý tất cả thông báo của bạn</p>

                    <div class="flex items-center space-x-4 mt-4">
                        <button @click="markAllAsRead"
                            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
                            Đánh dấu đã đọc tất cả
                        </button>
                        <button @click="deleteAllRead"
                            class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors">
                            Xóa tất cả đã đọc
                        </button>
                    </div>
                </div>

                <!-- Notifications List -->
                <div class="space-y-4">
                    <div v-for="notification in paginatedNotifications" :key="notification.id"
                        class="bg-white rounded-lg shadow-sm p-6 hover:shadow-md transition-shadow"
                        :class="{ 'border-l-4 border-blue-500': !notification.read }">

                        <div class="flex items-start justify-between">
                            <div class="flex items-start space-x-4 flex-1">
                                <!-- Notification Icon -->
                                <div :class="getNotificationIconClass(notification.type)"
                                    class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center">
                                    <component :is="getNotificationIcon(notification.type)"
                                        class="w-5 h-5 text-white" />
                                </div>

                                <!-- Notification Content -->
                                <div class="flex-1">
                                    <h3 class="font-semibold text-gray-900">{{ notification.title }}</h3>
                                    <p class="text-gray-600 mt-1">{{ notification.message }}</p>
                                    <p class="text-sm text-gray-400 mt-2">{{ formatDate(notification.createdAt) }}</p>

                                    <!-- Action Buttons -->
                                    <div v-if="notification.link" class="mt-3">
                                        <router-link :to="notification.link"
                                            class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium">
                                            Xem chi tiết
                                            <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor"
                                                viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M9 5l7 7-7 7" />
                                            </svg>
                                        </router-link>
                                    </div>
                                </div>
                            </div>

                            <!-- Action Menu -->
                            <div class="flex items-center space-x-2">
                                <button v-if="!notification.read" @click="markAsRead(notification.id)"
                                    class="text-sm text-blue-600 hover:text-blue-800">
                                    Đánh dấu đã đọc
                                </button>
                                <button @click="deleteNotification(notification.id)"
                                    class="text-gray-400 hover:text-red-500 p-1">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Empty State -->
                <div v-if="notifications.length === 0" class="text-center py-12">
                    <svg class="w-16 h-16 text-gray-300 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 17h5l-5 5v-5zM10.24 8.56a5.97 5.97 0 01-4.66-7.5 1 1 0 00-1.14-1.14 7.97 7.97 0 00-5.34 11.3 1 1 0 001.14 1.14 5.97 5.97 0 014.66 7.5 1 1 0 001.14 1.14 7.97 7.97 0 005.34-11.3 1 1 0 00-1.14-1.14z" />
                    </svg>
                    <h3 class="mt-4 text-lg font-medium text-gray-900">Không có thông báo</h3>
                    <p class="mt-1 text-gray-500">Tất cả thông báo của bạn sẽ xuất hiện ở đây.</p>
                </div>

                <!-- Pagination -->
                <div v-if="totalPages > 1" class="flex justify-center mt-8">
                    <div class="flex space-x-2">
                        <button v-for="page in totalPages" :key="page" @click="currentPage = page" :class="[
                            'px-4 py-2 rounded-lg border',
                            currentPage === page
                                ? 'bg-blue-600 text-white border-blue-600'
                                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
                        ]">
                            {{ page }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Sử dụng cùng mock data như component NotificationBell
const mockNotifications = [
    // ... cùng dữ liệu như trên
]

const notifications = ref([])
const currentPage = ref(1)
const itemsPerPage = 10

const paginatedNotifications = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return notifications.value.slice(start, end)
})

const totalPages = computed(() => {
    return Math.ceil(notifications.value.length / itemsPerPage)
})

// Các hàm helper (giống như trong NotificationBell)
const getNotificationIcon = (type) => { /* ... */ }
const getNotificationIconClass = (type) => { /* ... */ }
const formatDate = (date) => {
    return new Date(date).toLocaleDateString('vi-VN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}

const markAsRead = (id) => {
    const notification = notifications.value.find(n => n.id === id)
    if (notification) {
        notification.read = true
    }
}

const markAllAsRead = () => {
    notifications.value.forEach(notification => {
        notification.read = true
    })
}

const deleteNotification = (id) => {
    notifications.value = notifications.value.filter(n => n.id !== id)
}

const deleteAllRead = () => {
    notifications.value = notifications.value.filter(n => !n.read)
}

onMounted(() => {
    notifications.value = mockNotifications
})
</script>