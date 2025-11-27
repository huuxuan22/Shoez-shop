<template>
    <AdminLayout>
        <div class="h-[calc(100vh-120px)] flex border border-gray-200 rounded-lg overflow-hidden bg-white">
            <!-- Left Sidebar: User List (30%) -->
            <div class="w-[30%] border-r border-gray-200 flex flex-col">
                <!-- Header -->
                <div class="p-4 border-b border-gray-200 bg-gray-50">
                    <h2 class="text-lg font-semibold text-gray-900 mb-3">Danh sách khách hàng</h2>
                    <!-- Search Bar -->
                    <div class="relative">
                        <input v-model="searchQuery" type="text" placeholder="Tìm kiếm khách hàng..."
                            class="w-full px-4 py-2 pl-10 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm" />
                        <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400"
                            fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                </div>

                <!-- User List -->
                <div class="flex-1 overflow-y-auto">
                    <!-- Loading State -->
                    <div v-if="conversationStore.loading" class="p-4 text-center text-gray-500">
                        <p>Đang tải danh sách khách hàng...</p>
                    </div>

                    <!-- Loading Search -->
                    <div v-else-if="isSearching" class="p-4 text-center text-gray-500">
                        <p>Đang tìm kiếm...</p>
                    </div>

                    <!-- Empty State -->
                    <div v-else-if="displayUserList.length === 0 && !searchQuery" class="p-4 text-center text-gray-500">
                        <p>Chưa có khách hàng nào nhắn tin</p>
                    </div>

                    <!-- No Search Results -->
                    <div v-else-if="displayUserList.length === 0 && searchQuery" class="p-4 text-center text-gray-500">
                        <p>Không tìm thấy khách hàng nào</p>
                    </div>

                    <!-- User List -->
                    <div v-else>
                        <div v-for="user in displayUserList" :key="`${user.id}-${user.isNewConversation || false}`"
                            @click="selectUser(user)"
                            class="p-4 border-b border-gray-100 cursor-pointer hover:bg-gray-50 transition-colors"
                            :class="{ 'bg-blue-50 border-l-4 border-l-blue-500': selectedUser?.id === user.id }">
                            <div class="flex items-center space-x-3">
                                <!-- Avatar -->
                                <div class="relative">
                                    <div
                                        class="w-12 h-12 rounded-full bg-gray-300 flex items-center justify-center overflow-hidden">
                                        <img v-if="user.avatar" :src="user.avatar" :alt="user.name"
                                            class="w-full h-full object-cover" />
                                        <span v-else class="text-gray-600 font-semibold text-lg">
                                            {{ user.name.charAt(0).toUpperCase() }}
                                        </span>
                                    </div>
                                    <!-- Unread Badge -->
                                    <div v-if="user.unread > 0"
                                        class="absolute -top-1 -right-1 h-5 bg-red-500 rounded-full flex items-center justify-center shadow-md border-2 border-white"
                                        :style="{
                                            minWidth: user.unread > 99 ? '28px' : user.unread > 9 ? '24px' : '20px',
                                            paddingLeft: user.unread > 99 ? '6px' : user.unread > 9 ? '5px' : '4px',
                                            paddingRight: user.unread > 99 ? '6px' : user.unread > 9 ? '5px' : '4px'
                                        }">
                                        <span class="text-white text-[11px] font-bold leading-none">
                                            {{ user.unread > 99 ? '99+' : user.unread }}
                                        </span>
                                    </div>
                                </div>

                                <!-- User Info -->
                                <div class="flex-1 min-w-0">
                                    <div class="flex items-center gap-2">
                                        <p class="font-medium text-gray-900 truncate">{{ user.name }}</p>
                                        <span v-if="user.isNewConversation"
                                            class="px-2 py-0.5 text-xs bg-green-100 text-green-700 rounded-full">
                                            Mới
                                        </span>
                                    </div>
                                    <p v-if="getLastMessage(user.id)" class="text-sm text-gray-500 truncate">
                                        {{ getLastMessage(user.id) }}
                                    </p>
                                    <p v-else-if="user.email || user.phone" class="text-sm text-gray-400 truncate">
                                        {{ user.email || user.phone }}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Side: Chat Area (7/10) -->
            <div class="flex-1 flex flex-col">
                <!-- Chat Header -->
                <div v-if="selectedUser" class="p-4 border-b border-gray-200 bg-gray-50 flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center overflow-hidden">
                        <img v-if="selectedUser.avatar" :src="selectedUser.avatar" :alt="selectedUser.name"
                            class="w-full h-full object-cover" />
                        <span v-else class="text-gray-600 font-semibold">
                            {{ selectedUser.name.charAt(0).toUpperCase() }}
                        </span>
                    </div>
                    <div>
                        <p class="font-semibold text-gray-900">{{ selectedUser.name }}</p>
                        <p class="text-sm text-gray-500">Đang hoạt động</p>
                    </div>
                </div>

                <!-- Empty State -->
                <div v-else class="flex-1 flex items-center justify-center">
                    <div class="text-center">
                        <svg class="w-16 h-16 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                        <p class="text-gray-500">Chọn một khách hàng để bắt đầu trò chuyện</p>
                    </div>
                </div>

                <!-- Messages Area -->
                <div v-if="selectedUser" ref="messagesContainer"
                    class="flex-1 overflow-y-auto p-4 bg-gray-50 space-y-4">
                    <div v-for="(msg, index) in currentMessages" :key="index" class="flex"
                        :class="msg.from === 'admin' ? 'justify-end' : 'justify-start'">
                        <div class="max-w-[70%] rounded-lg px-4 py-2"
                            :class="msg.from === 'admin' ? 'bg-blue-500 text-white' : 'bg-white text-gray-900 border border-gray-200'">
                            <p class="text-sm">{{ msg.message }}</p>
                            <p class="text-xs mt-1" :class="msg.from === 'admin' ? 'text-blue-100' : 'text-gray-500'">
                                {{ formatTime(msg.time) }}
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Message Input -->
                <div v-if="selectedUser" class="p-4 border-t border-gray-200 bg-white">
                    <form @submit.prevent="sendMessage" class="flex items-center space-x-2">
                        <input v-model="newMessage" type="text" placeholder="Nhập tin nhắn..."
                            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
                        <button type="submit" :disabled="!newMessage.trim()"
                            class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                            </svg>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </AdminLayout>
</template>

<script setup>
import { ref, computed, watch, nextTick, onMounted } from 'vue'
import AdminLayout from '@/layouts/admin/AdminLayout.vue'
import { useConversationStore } from '@/stores/conversation'
import ConversationService from '@/api-services/ConversationService'

const conversationStore = useConversationStore()

// Search query
const searchQuery = ref('')
const searchResults = ref([])
const isSearching = ref(false)

// Get userChatList from store
const userChatList = computed(() => conversationStore.userChatList)

// Check if query looks like email or phone
const isEmailOrPhone = (query) => {
    const trimmed = query.trim()
    // Check for email pattern
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    // Check for phone pattern (numbers, may have +, spaces, dashes)
    const phonePattern = /^[\d\s\+\-\(\)]+$/
    return emailPattern.test(trimmed) || (phonePattern.test(trimmed) && trimmed.replace(/\D/g, '').length >= 7)
}

// Filtered user list based on search query (from existing chat list)
const filteredUserList = computed(() => {
    if (!searchQuery.value.trim()) {
        return userChatList.value
    }

    const query = searchQuery.value.toLowerCase().trim()
    return userChatList.value.filter(user => {
        const name = (user.name || '').toLowerCase()
        const lastMessage = (user.lastMessage || '').toLowerCase()
        return name.includes(query) || lastMessage.includes(query)
    })
})

// Combined display list: existing chats + search results
const displayUserList = computed(() => {
    if (!searchQuery.value.trim()) {
        return userChatList.value
    }

    // If searching by email/phone, show search results
    if (isEmailOrPhone(searchQuery.value)) {
        // Merge: existing chats that match + new search results
        const existingIds = new Set(userChatList.value.map(u => u.id))
        const newUsers = searchResults.value.filter(u => !existingIds.has(u.id))
        return [...filteredUserList.value, ...newUsers]
    }

    // Otherwise, just show filtered existing chats
    return filteredUserList.value
})

// Search users by email/phone
const searchUsers = async () => {
    const query = searchQuery.value.trim()

    if (!query || query.length < 2) {
        searchResults.value = []
        return
    }

    // Only search by API if it looks like email/phone
    if (isEmailOrPhone(query)) {
        isSearching.value = true
        try {
            const results = await ConversationService.searchUsers(query)
            searchResults.value = results
        } catch (error) {
            console.error('Error searching users:', error)
            searchResults.value = []
        } finally {
            isSearching.value = false
        }
    } else {
        searchResults.value = []
    }
}

// Watch search query with debounce
let searchTimeout = null
watch(searchQuery, (newValue) => {
    if (searchTimeout) {
        clearTimeout(searchTimeout)
    }

    searchTimeout = setTimeout(() => {
        searchUsers()
    }, 500) // Debounce 500ms
})

// Fake messages data for each user
const messagesData = ref({
    1: [
        { from: "user", message: "Xin chào", time: "2025-11-10 10:32" },
        { from: "admin", message: "Tôi hỗ trợ gì cho bạn?", time: "2025-11-10 10:33" },
        { from: "user", message: "Tôi muốn hỏi về sản phẩm", time: "2025-11-10 10:35" },
    ],
    2: [
        { from: "user", message: "Sản phẩm có còn hàng không?", time: "2025-11-10 09:15" },
        { from: "admin", message: "Vâng, sản phẩm vẫn còn hàng", time: "2025-11-10 09:16" },
    ],
    3: [
        { from: "user", message: "Khi nào tôi nhận được hàng?", time: "2025-11-10 11:20" },
    ],
    4: [
        { from: "user", message: "Cảm ơn bạn", time: "2025-11-10 08:45" },
    ],
    5: [
        { from: "admin", message: "Chào bạn, bạn cần hỗ trợ gì?", time: "2025-11-10 14:00" },
    ],
})

const selectedUser = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)

const currentMessages = computed(() => {
    if (!selectedUser.value) return []
    return messagesData.value[selectedUser.value.id] || []
})

const getLastMessage = (userId) => {
    const user = userChatList.value.find(user => user.id === userId)
    return user?.lastMessage || ''
}

const selectUser = (user) => {
    selectedUser.value = user
    // Reset unread count when selecting user
    conversationStore.resetUnread(user.id)
    // Scroll to bottom when selecting user
    nextTick(() => {
        scrollToBottom()
    })
}

// Load conversation users on mount
onMounted(async () => {
    await conversationStore.fetchUsersChattingWithAdmin()
})

const sendMessage = () => {
    if (!newMessage.value.trim() || !selectedUser.value) return

    const message = {
        from: "admin",
        message: newMessage.value.trim(),
        time: new Date().toISOString().slice(0, 16).replace('T', ' ')
    }

    if (!messagesData.value[selectedUser.value.id]) {
        messagesData.value[selectedUser.value.id] = []
    }

    messagesData.value[selectedUser.value.id].push(message)
    newMessage.value = ''

    // Scroll to bottom after sending
    nextTick(() => {
        scrollToBottom()
    })
}

const formatTime = (timeStr) => {
    if (!timeStr) return ''
    try {
        const date = new Date(timeStr.replace(' ', 'T'))
        return date.toLocaleString('vi-VN', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        })
    } catch {
        return timeStr
    }
}

const scrollToBottom = () => {
    if (messagesContainer.value) {
        messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
}

// Watch for new messages and auto-scroll
watch(currentMessages, () => {
    nextTick(() => {
        scrollToBottom()
    })
}, { deep: true })
</script>

<style scoped></style>
