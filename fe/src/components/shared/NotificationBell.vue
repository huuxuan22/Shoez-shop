<template>
    <div class="relative">
        <!-- Notification Bell -->
        <button @click="toggleNotifications" class="relative text-gray-800 hover:text-black transition-colors p-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 17h5l-5 5v-5zM10.24 8.56a5.97 5.97 0 01-4.66-7.5 1 1 0 00-1.14-1.14 7.97 7.97 0 00-5.34 11.3 1 1 0 001.14 1.14 5.97 5.97 0 014.66 7.5 1 1 0 001.14 1.14 7.97 7.97 0 005.34-11.3 1 1 0 00-1.14-1.14z" />
            </svg>

            <!-- Notification Badge -->
            <span v-if="unreadCount > 0"
                class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center animate-pulse">
                {{ unreadCount > 9 ? '9+' : unreadCount }}
            </span>
        </button>

        <!-- Notification Dropdown -->
        <div v-if="showNotifications"
            class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-lg border border-gray-200 z-50 max-h-96 overflow-y-auto">
            <div class="p-4 border-b border-gray-200">
                <h3 class="font-semibold text-lg">Thông báo</h3>
                <button @click="markAllAsRead" class="text-sm text-blue-600 hover:text-blue-800">
                    Đánh dấu đã đọc tất cả
                </button>
            </div>

            <!-- Notifications List -->
            <div v-if="notifications.length > 0">
                <div v-for="notification in notifications" :key="notification.id"
                    class="p-4 border-b border-gray-100 hover:bg-gray-50 cursor-pointer"
                    :class="{ 'bg-blue-50': !notification.read }" @click="handleNotificationClick(notification)">

                    <!-- Notification Icon based on type -->
                    <div class="flex items-start space-x-3">
                        <div :class="getNotificationIconClass(notification.type)"
                            class="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center">
                            <component :is="getNotificationIcon(notification.type)" class="w-4 h-4 text-white" />
                        </div>

                        <div class="flex-1">
                            <p class="text-sm font-medium text-gray-900">{{ notification.title }}</p>
                            <p class="text-xs text-gray-600 mt-1">{{ notification.message }}</p>
                            <p class="text-xs text-gray-400 mt-1">{{ formatTime(notification.createdAt) }}</p>
                        </div>

                        <span v-if="!notification.read" class="w-2 h-2 bg-blue-500 rounded-full flex-shrink-0"></span>
                    </div>
                </div>
            </div>

            <!-- Empty State -->
            <div v-else class="p-8 text-center">
                <svg class="w-12 h-12 text-gray-300 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 17h5l-5 5v-5zM10.24 8.56a5.97 5.97 0 01-4.66-7.5 1 1 0 00-1.14-1.14 7.97 7.97 0 00-5.34 11.3 1 1 0 001.14 1.14 5.97 5.97 0 014.66 7.5 1 1 0 001.14 1.14 7.97 7.97 0 005.34-11.3 1 1 0 00-1.14-1.14z" />
                </svg>
                <p class="text-gray-500 mt-2">Không có thông báo</p>
            </div>

            <div class="p-4 border-t border-gray-200">
                <router-link to="/notifications" class="block text-center text-blue-600 hover:text-blue-800 font-medium"
                    @click="showNotifications = false">
                    Xem tất cả thông báo
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const showNotifications = ref(false)
const notifications = ref([])

// Mock data - trong thực tế sẽ lấy từ API
const mockNotifications = [
    {
        id: 1,
        type: 'order',
        title: 'Đơn hàng đã được xác nhận',
        message: 'Đơn hàng #12345 của bạn đã được xác nhận và đang được chuẩn bị.',
        read: false,
        createdAt: new Date(Date.now() - 1000 * 60 * 5), // 5 phút trước
        link: '/orders/12345'
    },
    {
        id: 2,
        type: 'promotion',
        title: 'Khuyến mãi đặc biệt',
        message: 'Giảm 20% cho tất cả giày Nike. Áp dụng đến hết ngày 31/12.',
        read: false,
        createdAt: new Date(Date.now() - 1000 * 60 * 30), // 30 phút trước
        link: '/products?brand=Nike'
    },
    {
        id: 3,
        type: 'system',
        title: 'Cập nhật hệ thống',
        message: 'Hệ thống sẽ bảo trì từ 2:00 đến 4:00 ngày mai.',
        read: true,
        createdAt: new Date(Date.now() - 1000 * 60 * 60 * 2), // 2 giờ trước
        link: null
    }
]

const unreadCount = computed(() => {
    return notifications.value.filter(n => !n.read).length
})

// Notification icons based on type
const getNotificationIcon = (type) => {
    const icons = {
        order: 'OrderIcon',
        promotion: 'PromotionIcon',
        system: 'SystemIcon'
    }
    return icons[type] || 'SystemIcon'
}

const getNotificationIconClass = (type) => {
    const classes = {
        order: 'bg-green-500',
        promotion: 'bg-orange-500',
        system: 'bg-blue-500'
    }
    return classes[type] || 'bg-gray-500'
}

// Icon components
const OrderIcon = {
    template: `
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
              d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
      </svg>
    `
}

const PromotionIcon = {
    template: `
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
              d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
    `
}

const SystemIcon = {
    template: `
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
              d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
      </svg>
    `
}

const toggleNotifications = () => {
    showNotifications.value = !showNotifications.value
}

const handleNotificationClick = (notification) => {
    // Mark as read
    notification.read = true

    // Navigate if has link
    if (notification.link) {
        router.push(notification.link)
    }

    showNotifications.value = false
}

const markAllAsRead = () => {
    notifications.value.forEach(notification => {
        notification.read = true
    })
}

const formatTime = (date) => {
    const now = new Date()
    const diff = now - date

    const minutes = Math.floor(diff / 60000)
    const hours = Math.floor(diff / 3600000)
    const days = Math.floor(diff / 86400000)

    if (minutes < 1) return 'Vừa xong'
    if (minutes < 60) return `${minutes} phút trước`
    if (hours < 24) return `${hours} giờ trước`
    return `${days} ngày trước`
}

const handleClickOutside = (event) => {
    if (!event.target.closest('.relative')) {
        showNotifications.value = false
    }
}

onMounted(() => {
    // Load notifications from API
    notifications.value = mockNotifications
    document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
})
</script>