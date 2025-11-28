<template>
    <div class="fixed bottom-5 right-5 z-50 flex flex-col items-end gap-3">
        <!-- Chat Window -->
        <transition name="fade">
            <div v-if="open"
                class="w-[320px] sm:w-[360px] bg-white shadow-2xl border border-gray-200 rounded-xl overflow-hidden">
                <!-- Header -->
                <div class="flex items-center justify-between px-4 py-3 bg-black text-white">
                    <div class="flex items-center gap-2">
                        <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center">
                            <!-- Messenger glyph -->
                            <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M12 2C6.48 2 2 6.02 2 10.98c0 2.73 1.35 5.17 3.5 6.85V22l3.2-1.76c1.01.28 2.09.44 3.3.44 5.52 0 10-4.02 10-8.98S17.52 2 12 2Zm.21 11.93-2.58-2.76-4.13 2.76 4.64-4.96 2.6 2.76 4.1-2.76-4.63 4.96Z" />
                            </svg>
                        </div>
                        <div>
                            <p class="text-sm leading-tight opacity-90">{{
                                $t('Shared.MessengerChatWidget.customerSupport') }}</p>
                            <p class="text-xs leading-tight opacity-80">{{ $t('Shared.MessengerChatWidget.online') }}
                            </p>
                        </div>
                    </div>
                    <button class="p-1 rounded hover:bg-white/20" @click="open = false"
                        :title="$t('Shared.MessengerChatWidget.close')">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!-- Messages -->
                <div ref="scrollArea" class="p-4 h-80 overflow-y-auto bg-gray-50">
                    <!-- Loading State -->
                    <div v-if="loadingMessages" class="flex justify-center items-center h-full">
                        <p class="text-gray-500 text-sm">{{ $t('Shared.MessengerChatWidget.loading') }}</p>
                    </div>

                    <!-- Messages List -->
                    <div v-else class="space-y-3">
                        <div v-for="(m, i) in messages" :key="m.id || i" class="flex"
                            :class="m.from === 'user' ? 'justify-end' : 'justify-start'">
                            <div v-if="m.type === 'text'" :class="[
                                'max-w-[85%] px-3 py-2 rounded-lg text-sm',
                                m.from === 'admin' ? 'bg-white border border-gray-200 text-gray-800' : 'bg-black text-white'
                            ]">
                                {{ m.text }}
                                <div class="mt-1 text-[10px]"
                                    :class="m.from === 'admin' ? 'text-gray-400' : 'text-gray-300'">
                                    {{ formatTime(m.time) }}
                                </div>
                            </div>
                            <div v-else-if="m.type === 'image'" :class="[
                                'max-w-[85%] rounded-lg overflow-hidden',
                                m.from === 'admin' ? 'border border-gray-200 bg-white' : ''
                            ]">
                                <img :src="m.imageUrl" alt="attachment" class="max-w-full h-auto" />
                                <div class="px-2 py-1 text-[10px] text-gray-400">{{ formatTime(m.time) }}</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Input -->
                <form class="flex items-center gap-2 p-3 border-t bg-white" @submit.prevent="send">
                    <input v-model="draft" type="text"
                        :placeholder="$t('Shared.MessengerChatWidget.messagePlaceholder')"
                        :disabled="sendingMessage || !isAuthenticated"
                        class="flex-1 px-3 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-300 disabled:bg-gray-100 disabled:cursor-not-allowed"
                        @keydown.enter.exact.prevent="send" />
                    <input ref="fileInput" type="file" accept="image/*" class="hidden" @change="onFileChange" />
                    <button type="button" :disabled="!isAuthenticated"
                        class="w-10 h-10 rounded-full bg-white border border-gray-300 text-black flex items-center justify-center hover:bg-black hover:text-white disabled:opacity-50 disabled:cursor-not-allowed"
                        @click="triggerFile" :title="$t('Shared.MessengerChatWidget.sendImage')">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                            <path
                                d="M16.5 6.5v8.25a4.75 4.75 0 1 1-9.5 0V7.75a3.25 3.25 0 1 1 6.5 0v6.75a1.75 1.75 0 1 1-3.5 0V8.5h1.5v6a.25.25 0 1 0 .5 0V7.75a4.75 4.75 0 1 0-9.5 0v7a6.25 6.25 0 1 0 12.5 0V6.5h1.5Z" />
                        </svg>
                    </button>
                    <button type="submit" :disabled="!draft.trim() || sendingMessage || !isAuthenticated"
                        class="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center hover:brightness-110 disabled:opacity-50 disabled:cursor-not-allowed">
                        <svg v-if="!sendingMessage" class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M2.01 21 23 12 2.01 3 2 10l15 2-15 2z" />
                        </svg>
                        <span v-else class="text-xs">...</span>
                    </button>
                </form>

                <!-- Not authenticated message -->
                <div v-if="!isAuthenticated"
                    class="px-3 py-2 bg-yellow-50 border-t border-yellow-200 text-xs text-yellow-800">
                    <p>{{ $t('Shared.MessengerChatWidget.loginRequired') }}</p>
                    <button @click="router.push('/login')" class="mt-1 text-blue-600 hover:underline">
                        {{ $t('Shared.MessengerChatWidget.login') }}
                    </button>
                </div>
            </div>
        </transition>

        <!-- Floating trigger button -->
        <button type="button"
            class="w-12 h-12 rounded-full bg-white shadow-lg border border-gray-300 flex items-center justify-center hover:bg-black hover:text-white"
            :title="$t('Shared.MessengerChatWidget.openChat')" @click="open = !open">
            <!-- Messenger icon -->
            <svg class="w-7 h-7 text-black" viewBox="0 0 24 24" fill="currentColor">
                <path
                    d="M12 2C6.48 2 2 6.02 2 10.98c0 2.73 1.35 5.17 3.5 6.85V22l3.2-1.76c1.01.28 2.09.44 3.3.44 5.52 0 10-4.02 10-8.98S17.52 2 12 2Zm.21 11.93-2.58-2.76-4.13 2.76 4.64-4.96 2.6 2.76 4.1-2.76-4.63 4.96Z" />
            </svg>
        </button>
    </div>
</template>

<script setup>
import { ref, watch, nextTick, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { io } from 'socket.io-client'
import { useAuthStore } from '@/stores/auth'
import MessageService from '@/api-services/MessageService'
import { useToast } from '@/composables/useToast'

const { t } = useI18n()
const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const open = ref(false)
const draft = ref('')
const messages = ref([])
const conversationId = ref(null)
const loadingMessages = ref(false)
const sendingMessage = ref(false)
const socket = ref(null)

const scrollArea = ref(null)
const fileInput = ref(null)

const isAuthenticated = computed(() => authStore.isAuthenticated)
const userId = computed(() => {
    const user = authStore.user
    return user?.id || user?._id || null
})

const welcomeMessage = computed(() => t('Shared.MessengerChatWidget.welcomeMessage'))

// Try to find existing conversation
const findConversation = async () => {
    if (!isAuthenticated.value || !userId.value) return null

    try {
        // Try to get conversation by checking if user has sent any messages
        // For now, we'll rely on conversationId from previous messages
        // In the future, we can add an API endpoint to get user's conversation
        const storedConvId = localStorage.getItem(`conversation_${userId.value}`)
        if (storedConvId) {
            return storedConvId
        }
    } catch (error) {
        console.error('Error finding conversation:', error)
    }
    return null
}

// Load messages when opening chat
const loadMessages = async () => {
    if (!isAuthenticated.value || !userId.value) {
        // Show welcome message for non-authenticated users
        messages.value = [
            { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
        ]
        return
    }

    // Try to find existing conversation
    if (!conversationId.value) {
        const foundConvId = await findConversation()
        if (foundConvId) {
            conversationId.value = foundConvId
        } else {
            // No conversation yet, just show welcome message
            messages.value = [
                { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
            ]
            return
        }
    }

    loadingMessages.value = true
    try {
        const msgs = await MessageService.getMessages(conversationId.value)

        // Format messages for display
        const formattedMessages = msgs.map(msg => ({
            type: 'text',
            from: msg.senderId === userId.value ? 'user' : 'admin',
            text: msg.content,
            time: msg.createdAt,
            id: msg.id || msg._id
        }))

        messages.value = formattedMessages.length > 0
            ? formattedMessages
            : [{ type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }]

        // Mark as read
        try {
            await MessageService.markAsRead(conversationId.value)
        } catch (error) {
            console.error('Error marking messages as read:', error)
        }

        nextTick(() => scrollToBottom())
    } catch (error) {
        console.error('Error loading messages:', error)
        messages.value = [
            { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
        ]
    } finally {
        loadingMessages.value = false
    }
}

// Send message
const send = async () => {
    const text = draft.value.trim()
    if (!text || sendingMessage.value) return

    // Check authentication
    if (!isAuthenticated.value) {
        toast.info('Vui lòng đăng nhập để gửi tin nhắn', 'Thông báo')
        router.push('/login')
        return
    }

    sendingMessage.value = true

    try {
        const payload = {
            content: text,
            conversationId: conversationId.value || null
        }

        const result = await MessageService.userSendMessage(payload)

        // Update conversationId if it's a new conversation
        if (!conversationId.value && result.conversationId) {
            conversationId.value = result.conversationId
            // Save to localStorage for future use
            if (userId.value) {
                localStorage.setItem(`conversation_${userId.value}`, result.conversationId)
            }
        }

        // Add message to local state
        const message = result.message || result
        messages.value.push({
            type: 'text',
            from: 'user',
            text: message.content || text,
            time: message.createdAt || new Date().toISOString(),
            id: message.id || message._id
        })

        draft.value = ''
        nextTick(() => scrollToBottom())
    } catch (error) {
        console.error('Error sending message:', error)
        toast.error('Không thể gửi tin nhắn', 'Lỗi')
    } finally {
        sendingMessage.value = false
    }
}

// Connect socket for realtime updates
const connectSocket = () => {
    if (!isAuthenticated.value || !userId.value) return

    socket.value = io('http://localhost:8000/notifications', {
        transports: ['websocket', 'polling'],
        autoConnect: true
    })

    socket.value.on('connect', () => {
        console.log('✅ User chat connected to socket')
        socket.value.emit('join_user_room', { user_id: userId.value })
    })

    // Listen for new messages from admin
    socket.value.on('new_message', (data) => {
        console.log('📬 Received new message from admin:', data)

        // Check if message is for current user
        if (data.receiverId === userId.value || data.senderId !== userId.value) {
            // Check if message already exists (avoid duplicates)
            const existingMessage = messages.value.find(
                msg => msg.id === data.id || (msg.text === data.content && msg.time === data.createdAt)
            )

            if (!existingMessage) {
                messages.value.push({
                    type: 'text',
                    from: 'admin',
                    text: data.content,
                    time: data.createdAt,
                    id: data.id
                })

                // Update conversationId if needed
                if (data.conversationId && !conversationId.value) {
                    conversationId.value = data.conversationId
                    // Save to localStorage for future use
                    if (userId.value) {
                        localStorage.setItem(`conversation_${userId.value}`, data.conversationId)
                    }
                }

                nextTick(() => scrollToBottom())
            }
        }
    })

    socket.value.on('disconnect', () => {
        console.log('❌ User chat disconnected from socket')
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

// Watch for chat open/close
watch(open, async (newVal) => {
    if (newVal) {
        // Load messages when opening
        await loadMessages()
        // Connect socket if authenticated
        if (isAuthenticated.value && !socket.value) {
            connectSocket()
        }
    }
})

// Watch for authentication changes
watch(isAuthenticated, (newVal) => {
    if (newVal && open.value) {
        loadMessages()
        if (!socket.value) {
            connectSocket()
        }
    } else if (!newVal) {
        disconnectSocket()
        conversationId.value = null
        messages.value = [
            { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
        ]
    }
})

function triggerFile() {
    fileInput.value?.click()
}

function onFileChange(e) {
    const file = e.target.files?.[0]
    if (!file) return

    // For now, just show a message that image upload is not yet implemented
    toast.info('Tính năng gửi ảnh đang được phát triển', 'Thông báo')
    e.target.value = ''
}

function formatTime(timeStr) {
    if (!timeStr) return ''
    try {
        const date = new Date(timeStr)
        if (isNaN(date.getTime())) return timeStr

        const now = new Date()
        const diff = now - date
        const minutes = Math.floor(diff / 60000)

        if (minutes < 1) return 'Vừa xong'
        if (minutes < 60) return `${minutes} phút trước`
        if (minutes < 1440) return `${Math.floor(minutes / 60)} giờ trước`

        return date.toLocaleString('vi-VN', {
            day: '2-digit',
            month: '2-digit',
            hour: '2-digit',
            minute: '2-digit'
        })
    } catch {
        return timeStr
    }
}

function scrollToBottom() {
    if (scrollArea.value) {
        scrollArea.value.scrollTop = scrollArea.value.scrollHeight
    }
}

watch(messages, async () => {
    await nextTick()
    scrollToBottom()
})

onMounted(() => {
    // Connect socket if authenticated
    if (isAuthenticated.value) {
        connectSocket()
    }
})

onUnmounted(() => {
    disconnectSocket()
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity .15s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
