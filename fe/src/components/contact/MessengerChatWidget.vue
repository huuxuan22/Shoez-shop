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
                            <p class="text-sm leading-tight opacity-90">Hỗ trợ khách hàng</p>
                            <p class="text-xs leading-tight opacity-80">Online</p>
                        </div>
                    </div>
                    <button class="p-1 rounded hover:bg-white/20" @click="open = false" title="Đóng">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!-- Messages -->
                <div ref="scrollArea" class="p-4 h-80 overflow-y-auto bg-gray-50">
                    <div class="space-y-3">
                        <div v-for="(m, i) in messages" :key="i">
                            <div v-if="m.type === 'text'" :class="[
                                'max-w-[85%] px-3 py-2 rounded-lg text-sm',
                                m.from === 'admin' ? 'bg-white border border-gray-200 text-gray-800' : 'bg-black text-white ml-auto'
                            ]">
                                {{ m.text }}
                                <div class="mt-1 text-[10px] text-gray-400">{{ m.time }}</div>
                            </div>
                            <div v-else-if="m.type === 'image'" :class="[
                                'max-w-[85%] rounded-lg overflow-hidden',
                                m.from === 'admin' ? 'border border-gray-200 bg-white' : 'ml-auto'
                            ]">
                                <img :src="m.imageUrl" alt="attachment" class="max-w-full h-auto" />
                                <div class="px-2 py-1 text-[10px] text-gray-400">{{ m.time }}</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Input -->
                <form class="flex items-center gap-2 p-3 border-t bg-white" @submit.prevent="send">
                    <input v-model="draft" type="text" placeholder="Nhập tin nhắn..."
                        class="flex-1 px-3 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-300"
                        @keydown.enter.exact.prevent="send" />
                    <input ref="fileInput" type="file" accept="image/*" class="hidden" @change="onFileChange" />
                    <button type="button"
                        class="w-10 h-10 rounded-full bg-white border border-gray-300 text-black flex items-center justify-center hover:bg-black hover:text-white"
                        @click="triggerFile" title="Gửi ảnh">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                            <path
                                d="M16.5 6.5v8.25a4.75 4.75 0 1 1-9.5 0V7.75a3.25 3.25 0 1 1 6.5 0v6.75a1.75 1.75 0 1 1-3.5 0V8.5h1.5v6a.25.25 0 1 0 .5 0V7.75a4.75 4.75 0 1 0-9.5 0v7a6.25 6.25 0 1 0 12.5 0V6.5h1.5Z" />
                        </svg>
                    </button>
                    <button type="submit"
                        class="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center hover:brightness-110">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M2.01 21 23 12 2.01 3 2 10l15 2-15 2z" />
                        </svg>
                    </button>
                </form>
            </div>
        </transition>

        <!-- Floating trigger button -->
        <button type="button"
            class="w-12 h-12 rounded-full bg-white shadow-lg border border-gray-300 flex items-center justify-center hover:bg-black hover:text-white"
            title="Mở chat hỗ trợ" @click="open = !open">
            <!-- Messenger icon -->
            <svg class="w-7 h-7 text-black" viewBox="0 0 24 24" fill="currentColor">
                <path
                    d="M12 2C6.48 2 2 6.02 2 10.98c0 2.73 1.35 5.17 3.5 6.85V22l3.2-1.76c1.01.28 2.09.44 3.3.44 5.52 0 10-4.02 10-8.98S17.52 2 12 2Zm.21 11.93-2.58-2.76-4.13 2.76 4.64-4.96 2.6 2.76 4.1-2.76-4.63 4.96Z" />
            </svg>
        </button>
    </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'

const open = ref(false)
const draft = ref('')
const messages = ref([
    { type: 'text', from: 'admin', text: 'Xin chào! Mình có thể hỗ trợ gì cho bạn?', time: 'now' }
])

const scrollArea = ref(null)
const fileInput = ref(null)

function send() {
    const text = draft.value.trim()
    if (!text) return
    messages.value.push({ type: 'text', from: 'user', text, time: new Date().toLocaleTimeString() })
    draft.value = ''
    // Fake admin reply for UI demo
    setTimeout(() => {
        messages.value.push({ type: 'text', from: 'admin', text: 'Cảm ơn bạn! Admin sẽ phản hồi sớm nhất.', time: new Date().toLocaleTimeString() })
    }, 600)
}

function triggerFile() {
    fileInput.value?.click()
}

function onFileChange(e) {
    const file = e.target.files?.[0]
    if (!file) return
    const url = URL.createObjectURL(file)
    messages.value.push({ type: 'image', from: 'user', imageUrl: url, time: new Date().toLocaleTimeString() })
    setTimeout(() => {
        messages.value.push({ type: 'text', from: 'admin', text: 'Đã nhận được hình ảnh của bạn.', time: new Date().toLocaleTimeString() })
    }, 500)
    e.target.value = ''
}

watch(messages, async () => {
    await nextTick()
    if (scrollArea.value) {
        scrollArea.value.scrollTop = scrollArea.value.scrollHeight
    }
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
