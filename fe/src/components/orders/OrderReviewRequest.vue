<template>
    <div v-if="showRequest" class="fixed bottom-6 right-6 z-40">
        <div class="bg-white rounded-2xl shadow-2xl border border-gray-200 p-6 max-w-sm">
            <!-- Header -->
            <div class="flex items-center space-x-3 mb-4">
                <div
                    class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-500 rounded-2xl flex items-center justify-center">
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                    </svg>
                </div>
                <div>
                    <h3 class="font-semibold text-gray-900">Đánh giá đơn hàng</h3>
                    <p class="text-sm text-gray-600">Bạn đã nhận được hàng?</p>
                </div>
            </div>

            <!-- Message -->
            <p class="text-gray-700 text-sm mb-4">
                Chia sẻ trải nghiệm của bạn để giúp người khác lựa chọn tốt hơn
            </p>

            <!-- Actions -->
            <div class="flex space-x-3">
                <button @click="hideRequest"
                    class="flex-1 border border-gray-300 text-gray-700 py-2 rounded-xl text-sm font-medium hover:bg-gray-50 transition-colors">
                    Để sau
                </button>
                <button @click="goToReview"
                    class="flex-1 bg-gradient-to-r from-gray-900 to-black text-white py-2 rounded-xl text-sm font-medium hover:from-gray-800 hover:to-gray-900 transition-all duration-300">
                    Đánh giá ngay
                </button>
            </div>

            <!-- Close Button -->
            <button @click="hideRequest"
                class="absolute -top-2 -right-2 w-6 h-6 bg-gray-100 text-gray-400 rounded-full flex items-center justify-center text-sm hover:bg-gray-200 transition-colors">
                ×
            </button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const showRequest = ref(false)

// Kiểm tra xem có đơn hàng mới được giao không
const checkForDeliveredOrders = () => {
    // Trong thực tế sẽ kiểm tra từ API hoặc store
    const hasDeliveredOrders = localStorage.getItem('hasDeliveredOrders') === 'true'
    const hasSeenRequest = localStorage.getItem('reviewRequestSeen') === 'true'

    if (hasDeliveredOrders && !hasSeenRequest) {
        showRequest.value = true
    }
}

// Methods
const hideRequest = () => {
    showRequest.value = false
    localStorage.setItem('reviewRequestSeen', 'true')
}

const goToReview = () => {
    hideRequest()
    // Điều hướng đến trang đánh giá hoặc mở modal
    router.push('/orders?tab=review')
}

onMounted(() => {
    // Kiểm tra sau 3 giây để đảm bảo trang đã load xong
    setTimeout(() => {
        checkForDeliveredOrders()
    }, 3000)
})
</script>