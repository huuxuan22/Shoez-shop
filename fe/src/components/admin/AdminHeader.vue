<template>
  <header class="bg-white border-b border-gray-200 h-16 fixed top-0 left-64 right-0 z-10">
    <div class="h-full px-8 flex items-center justify-between">
      <!-- Search Bar -->
      <div class="flex-1 max-w-2xl">
        <div class="relative">
          <input type="text" placeholder="Tìm kiếm..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent" />
          <svg class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" fill="none"
            stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>

      <!-- Right Section -->
      <div class="flex items-center space-x-4 ml-8">
        <!-- Notifications Dropdown -->
        <div class="relative">
          <button @click="toggleNotifications"
            class="relative p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
            <span v-if="notificationCount > 0"
              class="absolute top-1 right-1 w-5 h-5 bg-red-500 text-white text-xs font-bold rounded-full flex items-center justify-center">
              {{ notificationCount > 9 ? '9+' : notificationCount }}
            </span>
          </button>

          <!-- Notifications Dropdown -->
          <Transition name="dropdown">
            <div v-if="showNotifications"
              class="absolute right-0 mt-2 w-96 bg-white rounded-lg shadow-xl border border-gray-200 z-50 max-h-96 overflow-hidden">
              <div class="p-4 border-b border-gray-200 flex items-center justify-between">
                <h3 class="font-semibold text-gray-900">Thông báo</h3>
                <button @click="clearAllNotifications" class="text-sm text-blue-600 hover:text-blue-800">
                  Xóa tất cả
                </button>
              </div>

              <div class="overflow-y-auto max-h-80">
                <div v-if="notifications.length === 0" class="p-8 text-center text-gray-500">
                  Không có thông báo
                </div>

                <div v-for="notif in notifications" :key="notif.id"
                  class="p-4 border-b border-gray-100 hover:bg-gray-50 cursor-pointer"
                  @click="handleNotificationClick(notif)">
                  <div class="flex items-start gap-3">
                    <div class="flex-shrink-0 mt-1">
                      <svg class="w-5 h-5 text-orange-600" fill="currentColor" viewBox="0 0 20 20">
                        <path
                          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" />
                      </svg>
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-semibold text-sm text-gray-900">{{ notif.message }}</p>
                      <p class="text-xs text-gray-500 mt-1">{{ formatTime(notif.timestamp) }}</p>
                    </div>
                    <button @click.stop="dismissNotification(notif.id)"
                      class="flex-shrink-0 text-gray-400 hover:text-gray-600">
                      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                          d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                          clip-rule="evenodd" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </Transition>
        </div>

        <!-- Messages -->
        <button class="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
          </svg>
        </button>

        <!-- User Profile -->
        <div class="flex items-center space-x-3 pl-4 border-l border-gray-200">
          <div class="text-right">
            <p class="text-sm font-medium text-gray-900">Admin User</p>
            <p class="text-xs text-gray-500">Administrator</p>
          </div>
          <div class="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center">
            <span class="text-sm font-semibold text-white">AD</span>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { io } from 'socket.io-client'
import AdminService from '@/api-services/AdminService'
import { useToast } from '@/composables/useToast'

const router = useRouter()
const { error: showErrorToast, success: showSuccessToast } = useToast()

const showNotifications = ref(false)
const notifications = ref([])
const socket = ref(null)

const notificationCount = computed(() => notifications.value.length)

const toggleNotifications = () => {
  showNotifications.value = !showNotifications.value
}

const handleNotificationClick = async (notif) => {
  if (notif.type === 'low_rating_review' && notif.product_id && notif.review_id) {
    // Navigate to product detail page với review highlight
    router.push({
      path: `/products/${notif.product_id}`,
      query: { highlightReview: notif.review_id }
    })

    // Đánh dấu admin đã click vào notification
    try {
      await AdminService.respondToLowRatingReview(notif.review_id)
      // Remove notification khỏi list
      notifications.value = notifications.value.filter(n => n.id !== notif.id)
    } catch (error) {
      showErrorToast('Không thể đánh dấu thông báo là đã phản hồi. Vui lòng thử lại.')
    }
  }
  showNotifications.value = false
}

const dismissNotification = (id) => {
  notifications.value = notifications.value.filter(n => n.id !== id)
}

const clearAllNotifications = () => {
  notifications.value = []
}

const formatTime = (timestamp) => {
  if (!timestamp) return ''
  const date = new Date(timestamp)
  const now = new Date()
  const diff = now - date

  const seconds = Math.floor(diff / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)

  if (seconds < 60) return 'Vừa xong'
  if (minutes < 60) return `${minutes} phút trước`
  if (hours < 24) return `${hours} giờ trước`
  if (days < 7) return `${days} ngày trước`

  return date.toLocaleDateString('vi-VN')
}

// Connect to WebSocket
const connectSocket = () => {
  socket.value = io('http://localhost:8000/notifications', {
    transports: ['websocket', 'polling'],
    autoConnect: true
  })

  socket.value.on('connect', () => {
    socket.value.emit('join_room', { room: 'admin' })
  })

  // Listen for admin notifications (low rating reviews)
  socket.value.on('admin_notification', (data) => {
    const notification = {
      id: Date.now(),
      type: data.type,
      message: data.message,
      review_id: data.review_id,
      product_id: data.product_id,
      rating: data.rating,
      timestamp: data.timestamp || new Date().toISOString()
    }

    notifications.value.unshift(notification)
  })

  socket.value.on('disconnect', () => {
  })

  socket.value.on('connect_error', (error) => {
  })
}

const disconnectSocket = () => {
  if (socket.value) {
    socket.value.disconnect()
    socket.value = null
  }
}

onMounted(() => {
  connectSocket()
})

onUnmounted(() => {
  disconnectSocket()
})
</script>

<style scoped>
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
