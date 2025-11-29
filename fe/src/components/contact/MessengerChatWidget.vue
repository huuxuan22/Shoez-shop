<template>
    <div class="fixed bottom-5 right-5 z-50 flex flex-col items-end gap-3">
        <!-- Chat Window -->
        <transition name="fade">
            <div v-if="open"
                class="w-[420px] sm:w-[460px] bg-white shadow-2xl border border-gray-200 rounded-xl overflow-hidden">
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
                    <div v-else class="flex flex-col gap-2">
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
                <div class="relative">
                    <form class="flex items-center gap-2 p-3 border-t bg-white" @submit.prevent="send">
                        <div class="relative flex-1">
                            <input ref="messageInput" v-model="draft" type="text"
                                :placeholder="$t('Shared.MessengerChatWidget.messagePlaceholder')"
                                :disabled="sendingMessage || !isAuthenticated"
                                class="w-full px-3 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-300 disabled:bg-gray-100 disabled:cursor-not-allowed"
                                @keydown.enter.exact.prevent="send" @focus="emojiPickerOpen = false" />
                        </div>

                        <input ref="fileInput" type="file" accept="image/*" class="hidden" @change="onFileChange" />

                        <!-- Emoji Button -->
                        <button ref="emojiButton" type="button" :disabled="!isAuthenticated" @click="toggleEmojiPicker"
                            class="w-10 h-10 rounded-full bg-white border border-gray-300 text-black flex items-center justify-center hover:bg-black hover:text-white disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            :title="$t('Shared.MessengerChatWidget.addEmoji')">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-3.5-9c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm7 0c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z" />
                            </svg>
                        </button>

                        <!-- File Upload Button -->
                        <button type="button" :disabled="!isAuthenticated" @click="triggerFile"
                            class="w-10 h-10 rounded-full bg-white border border-gray-300 text-black flex items-center justify-center hover:bg-black hover:text-white disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            :title="$t('Shared.MessengerChatWidget.sendImage')">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                                <path
                                    d="M16.5 6.5v8.25a4.75 4.75 0 1 1-9.5 0V7.75a3.25 3.25 0 1 1 6.5 0v6.75a1.75 1.75 0 1 1-3.5 0V8.5h1.5v6a.25.25 0 1 0 .5 0V7.75a4.75 4.75 0 1 0-9.5 0v7a6.25 6.25 0 1 0 12.5 0V6.5h1.5Z" />
                            </svg>
                        </button>

                        <!-- Send Button -->
                        <button type="submit" :disabled="!draft.trim() || sendingMessage || !isAuthenticated"
                            class="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center hover:brightness-110 disabled:opacity-50 disabled:cursor-not-allowed transition-colors">
                            <svg v-if="!sendingMessage" class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M2.01 21 23 12 2.01 3 2 10l15 2-15 2z" />
                            </svg>
                            <span v-else class="text-xs">...</span>
                        </button>
                    </form>
                </div>

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
            class="relative w-12 h-12 rounded-full bg-white shadow-lg border border-gray-300 flex items-center justify-center hover:bg-black hover:text-white"
            :title="$t('Shared.MessengerChatWidget.openChat')" @click="open = !open">
            <!-- Messenger icon -->
            <svg class="w-7 h-7 text-black" viewBox="0 0 24 24" fill="currentColor">
                <path
                    d="M12 2C6.48 2 2 6.02 2 10.98c0 2.73 1.35 5.17 3.5 6.85V22l3.2-1.76c1.01.28 2.09.44 3.3.44 5.52 0 10-4.02 10-8.98S17.52 2 12 2Zm.21 11.93-2.58-2.76-4.13 2.76 4.64-4.96 2.6 2.76 4.1-2.76-4.63 4.96Z" />
            </svg>
            <!-- Unread Badge -->
            <div v-if="unreadCount > 0 && !open"
                class="absolute -top-1 -right-1 h-5 bg-red-500 rounded-full flex items-center justify-center shadow-md border-2 border-white z-10"
                :style="{
                    minWidth: unreadCount > 99 ? '28px' : unreadCount > 9 ? '24px' : '20px',
                    paddingLeft: unreadCount > 99 ? '6px' : unreadCount > 9 ? '5px' : '4px',
                    paddingRight: unreadCount > 99 ? '6px' : unreadCount > 9 ? '5px' : '4px'
                }">
                <span class="text-white text-[11px] font-bold leading-none">
                    {{ unreadCount > 99 ? '99+' : unreadCount }}
                </span>
            </div>
        </button>
    </div>

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
import { ref, watch, nextTick, computed, onMounted, onUnmounted, onBeforeUnmount } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { io } from 'socket.io-client'
import { useAuthStore } from '@/stores/auth'
import MessageService from '@/api-services/MessageService'
import { useToast } from '@/composables/useToast'
import EmojiPicker from 'vue3-emoji-picker'
import 'vue3-emoji-picker/css'

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
const emojiPickerOpen = ref(false)
const unreadCount = ref(0) // Test: Set to 5 to see badge. Change back to 0 after testing

const scrollArea = ref(null)
const fileInput = ref(null)
const messageInput = ref(null)
const emojiButton = ref(null)
const emojiPickerPosition = ref(null)

const isAuthenticated = computed(() => authStore.isAuthenticated)
const userId = computed(() => {
    const user = authStore.user
    if (!user) return null
    // Normalize userId - ensure it's a string
    const id = user.id || user._id
    return id ? String(id) : null
})

const welcomeMessage = computed(() => t('Shared.MessengerChatWidget.welcomeMessage'))

// Try to find existing conversation
const findConversation = async () => {
    if (!isAuthenticated.value || !userId.value) return null

    try {
        // Try to get conversation from localStorage
        const storedConvId = localStorage.getItem(`conversation_${userId.value}`)
        if (storedConvId) {
            return storedConvId
        }
    } catch (error) {
        // Silent error handling
    }
    return null
}

// Initialize conversationId and load messages based on userId
const initializeConversation = async () => {
    if (!isAuthenticated.value || !userId.value) {
        messages.value = [
            { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
        ]
        return
    }

    loadingMessages.value = true
    try {
        const result = await MessageService.getUserMessages(1000)

        if (result && result.conversationId) {
            conversationId.value = result.conversationId
            // Save to localStorage
            localStorage.setItem(`conversation_${userId.value}`, result.conversationId)

            // Update unread count
            unreadCount.value = result.unread || 0

            // Format and set messages
            if (result.messages && result.messages.length > 0) {
                const formattedMessages = result.messages.map(msg => ({
                    type: 'text',
                    from: msg.senderId === userId.value ? 'user' : 'admin',
                    text: msg.content,
                    time: msg.createdAt,
                    id: msg.id || msg._id
                }))

                messages.value = formattedMessages

                // Mark as read and reset unread when opening widget
                if (open.value) {
                    try {
                        await MessageService.markAsRead(result.conversationId)
                        unreadCount.value = 0
                    } catch (error) {
                        throw error
                    }
                }

                nextTick(() => scrollToBottom())
            } else {
                messages.value = [
                    { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
                ]
            }
        } else {
            const storedConvId = localStorage.getItem(`conversation_${userId.value}`)
            if (storedConvId) {
                conversationId.value = storedConvId
                // Load messages using conversationId
                await loadMessages()
            } else {
                // No conversation yet, show welcome message
                messages.value = [
                    { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
                ]
            }
        }
    } catch (error) {
        // Fallback: try localStorage
        const storedConvId = localStorage.getItem(`conversation_${userId.value}`)
        if (storedConvId) {
            conversationId.value = storedConvId
            await loadMessages()
        } else {
            messages.value = [
                { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
            ]
        }
    } finally {
        loadingMessages.value = false
    }
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
        // Load all messages (increase limit to get all messages)
        const msgs = await MessageService.getMessages(conversationId.value, 1000)

        // Format messages for display
        const formattedMessages = msgs.map(msg => ({
            type: 'text',
            from: msg.senderId === userId.value ? 'user' : 'admin',
            text: msg.content,
            time: msg.createdAt,
            id: msg.id || msg._id
        }))

        // Always show messages if they exist, even if empty show welcome message
        if (formattedMessages.length > 0) {
            messages.value = formattedMessages
        } else {
            messages.value = [{ type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }]
        }

        // Mark as read and reset unread
        try {
            await MessageService.markAsRead(conversationId.value)
            unreadCount.value = 0
        } catch (error) {
            throw error;
        }

        nextTick(() => scrollToBottom())
    } catch (error) {
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

        // Reset unread count when user sends a message (user has replied)
        unreadCount.value = 0

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
        // Normalize userId to string before joining room
        const normalizedUserId = userId.value ? String(userId.value).trim() : null
        if (normalizedUserId) {
            socket.value.emit('join_user_room', { user_id: normalizedUserId })
        } else {
            throw new Error('Cannot join room: userId is null or empty')
        }
    })

    // Listen for new messages from admin
    socket.value.on('new_message', (data) => {
        // Normalize IDs to strings for comparison
        const normalizedReceiverId = data.receiverId ? String(data.receiverId).trim() : null
        const normalizedSenderId = data.senderId ? String(data.senderId).trim() : null
        const normalizedUserId = userId.value ? String(userId.value).trim() : null

        // Check if message is for current user AND from admin (not from user themselves)
        if (normalizedReceiverId === normalizedUserId && normalizedSenderId !== normalizedUserId) {
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

                // Increase unread count if widget is closed
                if (!open.value) {
                    unreadCount.value = (unreadCount.value || 0) + 1
                } else {
                    // If widget is open, mark as read immediately
                    if (conversationId.value) {
                        MessageService.markAsRead(conversationId.value).catch(err => {
                            throw err;
                        })
                    }
                }

                nextTick(() => scrollToBottom())
            } else {
                throw new Error('Message already exists')
            }
        } else {
            throw new Error('Message is not for this user or is from user themselves')
        }
    })

    socket.value.on('disconnect', () => {
        toast.info('Kết nối đã bị ngắt', 'Thông báo')
    })

    socket.value.on('connect_error', (error) => {
        toast.error('Lỗi kết nối', 'Lỗi')
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
        // Always reload messages when opening widget to get latest messages from admin
        // This ensures messages are refreshed every time the widget is opened
        if (isAuthenticated.value && userId.value) {
            await initializeConversation()
        } else {
            // Show welcome message for non-authenticated users
            messages.value = [
                { type: 'text', from: 'admin', text: welcomeMessage.value, time: new Date().toISOString() }
            ]
        }
        // Connect socket if authenticated
        if (isAuthenticated.value && !socket.value) {
            connectSocket()
        }
    } else {
        disconnectSocket()
    }
})

// Watch for authentication changes
watch(isAuthenticated, (newVal) => {
    if (newVal) {
        // Initialize conversation when user logs in
        initializeConversation()
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

// Watch for userId changes (when user data loads)
watch(userId, (newUserId) => {
    if (newUserId && isAuthenticated.value && !conversationId.value) {
        initializeConversation()
    }
})

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
        const textBefore = draft.value.substring(0, start)
        const textAfter = draft.value.substring(end)
        const emojiText = emoji.i || emoji.emoji || emoji
        draft.value = textBefore + emojiText + textAfter

        // Set cursor position after inserted emoji
        nextTick(() => {
            input.focus()
            const newPosition = start + emojiText.length
            input.setSelectionRange(newPosition, newPosition)
        })
    } else {
        // Fallback: append emoji to the end
        const emojiText = emoji.i || emoji.emoji || emoji
        draft.value += emojiText
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
    // Initialize conversation and load messages if user is authenticated
    if (isAuthenticated.value && userId.value) {
        initializeConversation()
        connectSocket()
    }

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
</style>
