<template>
    <AdminLayout>
        <div class="h-[calc(100vh-120px)] flex border border-gray-200 rounded-lg overflow-hidden bg-white">
            <!-- Left Sidebar: User List (30%) -->
            <div class="w-[30%] border-r border-gray-200 flex flex-col">
                <!-- Header -->
                <div class="p-4 border-b border-gray-200 bg-gray-50">
                    <h2 class="text-lg font-semibold text-gray-900 mb-3">{{ $t('Admin.Chat.customerList') }}</h2>
                    <!-- Search Bar -->
                    <div class="relative">
                        <input v-model="searchQuery" type="text" :placeholder="$t('Admin.Chat.searchPlaceholder')"
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
                        <p>{{ $t('Admin.Chat.loading') }}</p>
                    </div>

                    <!-- Loading Search -->
                    <div v-else-if="isSearching" class="p-4 text-center text-gray-500">
                        <p>{{ $t('Admin.Chat.searching') }}</p>
                    </div>

                    <!-- Empty State -->
                    <div v-else-if="displayUserList.length === 0 && !searchQuery" class="p-4 text-center text-gray-500">
                        <p>{{ $t('Admin.Chat.noCustomers') }}</p>
                    </div>

                    <!-- No Search Results -->
                    <div v-else-if="displayUserList.length === 0 && searchQuery" class="p-4 text-center text-gray-500">
                        <p>{{ $t('Admin.Chat.noResults') }}</p>
                    </div>

                    <!-- User List -->
                    <div v-else>
                        <div v-for="user in displayUserList" :key="`${user.id}-${user.isNewConversation || false}`"
                            @click="() => { console.log('🖱️ Clicked on user:', user); selectUser(user); }"
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
                                            {{ $t('Admin.Chat.new') }}
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
                        <p class="text-sm text-gray-500">{{ $t('Admin.Chat.active') }}</p>
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
                        <p class="text-gray-500">{{ $t('Admin.Chat.selectCustomer') }}</p>
                    </div>
                </div>

                <!-- Messages Area -->
                <div v-if="selectedUser" ref="messagesContainer"
                    class="flex-1 overflow-y-auto p-4 bg-gray-50 space-y-4">
                    <!-- Loading State -->
                    <div v-if="loadingMessages" class="flex justify-center items-center h-full">
                        <p class="text-gray-500">{{ $t('Admin.Chat.loading') }}</p>
                    </div>

                    <!-- Messages -->
                    <div v-else-if="currentMessages.length > 0" class="flex flex-col gap-2">
                        <div v-for="msg in currentMessages" :key="msg.id || `${msg.time}-${msg.message}`" class="flex"
                            :class="msg.from === 'admin' ? 'justify-end' : 'justify-start'">
                            <div class="max-w-[70%] rounded-lg px-4 py-2"
                                :class="msg.from === 'admin' ? 'bg-blue-500 text-white' : 'bg-white text-gray-900 border border-gray-200'">
                                <p class="text-sm">{{ msg.message }}</p>
                                <p class="text-xs mt-1"
                                    :class="msg.from === 'admin' ? 'text-blue-100' : 'text-gray-500'">
                                    {{ formatTime(msg.time) }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Empty State -->
                    <div v-else class="flex justify-center items-center h-full">
                        <p class="text-gray-500">{{ $t('Admin.Chat.noMessages') }}</p>
                    </div>
                </div>

                <!-- Message Input -->
                <div v-if="selectedUser" class="p-4 border-t border-gray-200 bg-white">
                    <form @submit.prevent="sendMessage" class="flex items-center space-x-2">
                        <input ref="messageInput" v-model="newMessage" type="text"
                            :placeholder="$t('Admin.Chat.messagePlaceholder')"
                            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                            @focus="emojiPickerOpen = false" />

                        <!-- Emoji Button -->
                        <button ref="emojiButton" type="button" @click="toggleEmojiPicker"
                            class="w-10 h-10 rounded-full bg-white border border-gray-300 text-black flex items-center justify-center hover:bg-gray-100 transition-colors"
                            :title="$t('Admin.Chat.addEmoji')">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-3.5-9c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm7 0c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z" />
                            </svg>
                        </button>

                        <button type="submit" :disabled="!newMessage.trim() || sendingMessage"
                            class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors">
                            <svg v-if="!sendingMessage" class="w-5 h-5" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                            </svg>
                            <span v-else class="text-sm">...</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </AdminLayout>

    <!-- Emoji Picker - Rendered outside component using Teleport -->
    <Teleport to="body">
        <transition name="fade">
            <div v-if="emojiPickerOpen && emojiPickerPosition" class="emoji-picker-wrapper fixed z-[9999]" :style="{
                bottom: `${emojiPickerPosition.bottom}px`,
                right: `${emojiPickerPosition.right}px`
            }">
                <div class="emoji-picker-container bg-white rounded-lg shadow-2xl border border-gray-200 p-2">
                    <EmojiPicker :native="true" :disable-skin-tones="false" @select="onEmojiSelect" />
                </div>
            </div>
        </transition>
    </Teleport>
</template>

<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted, onBeforeUnmount } from 'vue'
import { io } from 'socket.io-client'
import AdminLayout from '@/layouts/admin/AdminLayout.vue'
import { useConversationStore } from '@/stores/conversation'
import ConversationService from '@/api-services/ConversationService'
import MessageService from '@/api-services/MessageService'
import { useToast } from '@/composables/useToast'
import EmojiPicker from 'vue3-emoji-picker'
import 'vue3-emoji-picker/css'

const conversationStore = useConversationStore()
const toast = useToast()

// Search query
const searchQuery = ref('')
const searchResults = ref([])
const isSearching = ref(false)

// Get userChatList from store
const userChatList = computed(() => conversationStore.userChatList)

// Messages data - keyed by userId
const messagesData = ref({})
const loadingMessages = ref(false)

// Socket for realtime updates
const socket = ref(null)

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

const selectedUser = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)
const sendingMessage = ref(false)
const emojiPickerOpen = ref(false)
const emojiPickerPosition = ref(null)
const messageInput = ref(null)
const emojiButton = ref(null)

const currentMessages = computed(() => {
    if (!selectedUser.value) return []
    return messagesData.value[selectedUser.value.id] || []
})

const getLastMessage = (userId) => {
    const user = userChatList.value.find(user => user.id === userId)
    return user?.lastMessage || ''
}

// Load messages for a user
const loadMessages = async (user) => {
    // If new conversation, no messages yet
    if (user.isNewConversation) {
        messagesData.value[user.id] = []
        loadingMessages.value = false
        return
    }

    // Check if conversationId exists - must be truthy and not empty string
    const hasConversationId = user.conversationId &&
        user.conversationId !== null &&
        user.conversationId !== undefined &&
        String(user.conversationId).trim() !== ''

    if (!hasConversationId) {
        messagesData.value[user.id] = []
        loadingMessages.value = false
        return
    }

    loadingMessages.value = true
    try {
        const convId = String(user.conversationId).trim()
        const messages = await MessageService.getMessages(convId, 100)
        if (!messages || messages.length === 0) {
            messagesData.value[user.id] = []
            return
        }

        // Format messages for display
        const formattedMessages = messages.map(msg => {
            // Determine if message is from admin or user
            // Admin messages have senderId = admin_id, user messages have senderId = user.id
            const isFromUser = msg.senderId === user.id || msg.senderId === user.userId
            return {
                from: isFromUser ? 'user' : 'admin',
                message: msg.content,
                time: msg.createdAt,
                id: msg.id || msg._id
            }
        })

        messagesData.value[user.id] = formattedMessages

        // Mark messages as read
        if (user.conversationId) {
            try {
                await MessageService.markAsRead(user.conversationId)
            } catch (error) {
                console.error('Error marking messages as read:', error)
            }
        }

        // Scroll to bottom after loading
        nextTick(() => {
            scrollToBottom()
        })
    } catch (error) {
        toast.error('Không thể tải tin nhắn', 'Lỗi')
        messagesData.value[user.id] = []
    } finally {
        loadingMessages.value = false
    }
}

const selectUser = async (user) => {
    selectedUser.value = user
    // Reset unread count when selecting user
    conversationStore.resetUnread(user.id)

    await loadMessages(user)

    nextTick(() => {
        scrollToBottom()
    })
}

// Send message
const sendMessage = async () => {
    if (!newMessage.value.trim() || !selectedUser.value || sendingMessage.value) return

    const content = newMessage.value.trim()
    sendingMessage.value = true

    try {
        const payload = {
            receiverId: selectedUser.value.id,
            content: content,
            conversationId: selectedUser.value.conversationId || null
        }

        const result = await MessageService.adminSendMessage(payload)

        // Update conversationId if it's a new conversation
        if (!selectedUser.value.conversationId && result.conversationId) {
            selectedUser.value.conversationId = result.conversationId
            // Update in store
            const userInStore = userChatList.value.find(u => u.id === selectedUser.value.id)
            if (userInStore) {
                userInStore.conversationId = result.conversationId
                userInStore.isNewConversation = false
            }
        }

        // Add message to local state
        const message = result.message || result
        if (!messagesData.value[selectedUser.value.id]) {
            messagesData.value[selectedUser.value.id] = []
        }

        messagesData.value[selectedUser.value.id].push({
            from: 'admin',
            message: message.content || content,
            time: message.createdAt || new Date().toISOString(),
            id: message.id || message._id
        })

        // Update last message in store
        const userInStore = userChatList.value.find(u => u.id === selectedUser.value.id)
        if (userInStore) {
            userInStore.lastMessage = content
            userInStore.lastMessageTime = message.createdAt || new Date().toISOString()
            userInStore.unread = 0
        }

        newMessage.value = ''

        // Refresh user list to update unread counts (admin's unread should be reset)
        await conversationStore.fetchUsersChattingWithAdmin()

        // Scroll to bottom after sending
        nextTick(() => {
            scrollToBottom()
        })

        // Scroll to bottom after sending
        nextTick(() => {
            scrollToBottom()
        })
    } catch (error) {
        console.error('Error sending message:', error)
        toast.error('Không thể gửi tin nhắn', 'Lỗi')
    } finally {
        sendingMessage.value = false
    }
}

const formatTime = (timeStr) => {
    if (!timeStr) return ''
    try {
        // Handle ISO format or other formats
        const date = new Date(timeStr)
        if (isNaN(date.getTime())) {
            // Try parsing as 'YYYY-MM-DD HH:mm' format
            const parsed = new Date(timeStr.replace(' ', 'T'))
            if (isNaN(parsed.getTime())) {
                return timeStr
            }
            return parsed.toLocaleString('vi-VN', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            })
        }
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

// Connect socket for realtime updates
const connectSocket = () => {
    socket.value = io('http://localhost:8000/notifications', {
        transports: ['websocket', 'polling'],
        autoConnect: true
    })

    socket.value.on('connect', () => {
        console.log('✅ Admin chat connected to socket')
        socket.value.emit('join_room', { room: 'admin' })
    })

    // Listen for new messages from users
    socket.value.on('new_message', (data) => {
        console.log('📬 Received new message:', data)

        // Find the user who sent the message
        const userId = data.senderId
        const user = userChatList.value.find(u => u.id === userId || u.userId === userId)

        if (user) {
            // Add message to messagesData
            if (!messagesData.value[userId]) {
                messagesData.value[userId] = []
            }

            // Check if message already exists (avoid duplicates)
            const existingMessage = messagesData.value[userId].find(
                msg => msg.id === data.id || (msg.message === data.content && msg.time === data.createdAt)
            )

            if (!existingMessage) {
                messagesData.value[userId].push({
                    from: 'user',
                    message: data.content,
                    time: data.createdAt,
                    id: data.id
                })

                // Update last message in store
                user.lastMessage = data.content
                user.lastMessageTime = data.createdAt

                // If this user is currently selected, scroll to bottom
                if (selectedUser.value && selectedUser.value.id === userId) {
                    nextTick(() => {
                        scrollToBottom()
                    })
                }
            }
        }

        // Refresh user list to update unread counts
        conversationStore.fetchUsersChattingWithAdmin()
    })

    socket.value.on('disconnect', () => {
        console.log('❌ Admin chat disconnected from socket')
    })

    socket.value.on('connect_error', (error) => {
        console.error('Socket connection error:', error)
    })
}

const disconnectSocket = () => {
    if (socket.value) {
        socket.value.disconnect()
        socket.value = null
    }
}

// Emoji picker functions
const calculateEmojiPickerPosition = () => {
    if (!emojiButton.value) return null

    const buttonRect = emojiButton.value.getBoundingClientRect()
    const pickerHeight = 400 // Approximate height of emoji picker
    const pickerWidth = 320 // Width of emoji picker
    const spacing = 8 // Space between button and picker

    // Calculate position
    // Position above the button
    const bottom = window.innerHeight - buttonRect.top + spacing
    const right = window.innerWidth - buttonRect.right

    // Check if picker would go off screen on the right
    const adjustedRight = right < 0 ? buttonRect.left : right

    // Check if picker would go off screen on the top
    const adjustedBottom = buttonRect.top < pickerHeight
        ? window.innerHeight - buttonRect.bottom - pickerHeight - spacing
        : bottom

    return {
        bottom: adjustedBottom,
        right: adjustedRight
    }
}

const toggleEmojiPicker = () => {
    if (!emojiPickerOpen.value) {
        // Calculate position before opening
        nextTick(() => {
            emojiPickerPosition.value = calculateEmojiPickerPosition()
            emojiPickerOpen.value = true
        })
    } else {
        emojiPickerOpen.value = false
    }
}

const onEmojiSelect = (emoji) => {
    // Insert emoji at cursor position or at the end
    const input = messageInput.value
    if (input) {
        const start = input.selectionStart || 0
        const end = input.selectionEnd || 0
        const textBefore = newMessage.value.substring(0, start)
        const textAfter = newMessage.value.substring(end)
        const emojiText = emoji.i || emoji.emoji || emoji
        newMessage.value = textBefore + emojiText + textAfter

        // Set cursor position after inserted emoji
        nextTick(() => {
            input.focus()
            const newPosition = start + emojiText.length
            input.setSelectionRange(newPosition, newPosition)
        })
    } else {
        // Fallback: append emoji to the end
        const emojiText = emoji.i || emoji.emoji || emoji
        newMessage.value += emojiText
    }

    // Close emoji picker after selection
    emojiPickerOpen.value = false
}

// Close emoji picker when clicking outside
const handleClickOutside = (event) => {
    if (emojiPickerOpen.value) {
        const emojiPicker = event.target.closest('.emoji-picker-container') ||
            event.target.closest('.emoji-picker') ||
            event.target.closest('.emoji-picker-wrapper') ||
            event.target.closest('[class*="emoji"]')
        const emojiButtonEl = event.target.closest('button[type="button"]')

        // Check if click is on the emoji button
        const isEmojiButton = emojiButton.value && emojiButton.value.contains(event.target)

        if (!emojiPicker && !isEmojiButton && !emojiButtonEl) {
            emojiPickerOpen.value = false
        }
    }
}

// Update position on window resize
const handleResize = () => {
    if (emojiPickerOpen.value) {
        emojiPickerPosition.value = calculateEmojiPickerPosition()
    }
}

// Load conversation users on mount
onMounted(async () => {
    await conversationStore.fetchUsersChattingWithAdmin()
    connectSocket()

    // Add click outside listener for emoji picker
    document.addEventListener('click', handleClickOutside)
    // Add resize listener to update emoji picker position
    window.addEventListener('resize', handleResize)
    window.addEventListener('scroll', handleResize, true)
})

onBeforeUnmount(() => {
    // Remove click outside listener
    document.removeEventListener('click', handleClickOutside)
    window.removeEventListener('resize', handleResize)
    window.removeEventListener('scroll', handleResize, true)
})

onUnmounted(() => {
    disconnectSocket()
})

// Watch for new messages and auto-scroll
watch(currentMessages, () => {
    nextTick(() => {
        scrollToBottom()
    })
}, { deep: true })
</script>

<style scoped>
/* Emoji Picker Styles */
.emoji-picker-wrapper {
    pointer-events: auto;
}

.emoji-picker-container {
    width: 320px;
    max-height: 400px;
    overflow: hidden;
    pointer-events: auto;
}

:deep(.emoji-picker) {
    width: 100%;
    max-height: 400px;
}

:deep(.emoji-picker__container) {
    border: none;
    box-shadow: none;
}

:deep(.emoji-picker__search) {
    padding: 8px;
}

:deep(.emoji-picker__emojis) {
    max-height: 300px;
    overflow-y: auto;
}

/* Fade transition for emoji picker */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.15s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
