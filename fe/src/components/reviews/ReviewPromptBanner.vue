<template>
    <!-- Banner hiển thị khi có sản phẩm cần đánh giá -->
    <Transition name="slide-down">
        <div v-if="showBanner && pendingReviews.length > 0"
            class="fixed top-20 left-0 right-0 z-40 bg-yellow-50 border-b-4 border-yellow-400 shadow-lg">
            <div class="container mx-auto px-4 py-4">
                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-4 flex-1">
                        <div class="flex-shrink-0">
                            <svg class="w-12 h-12 text-yellow-600" fill="currentColor" viewBox="0 0 20 20">
                                <path
                                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                            </svg>
                        </div>
                        <div>
                            <h3 class="font-bold text-gray-900 text-lg">
                                Bạn có {{ pendingReviews.length }} sản phẩm chưa đánh giá!
                            </h3>
                            <p class="text-sm text-gray-600">
                                Hãy chia sẻ trải nghiệm của bạn để giúp người khác lựa chọn đúng sản phẩm
                            </p>
                        </div>
                    </div>

                    <div class="flex items-center gap-3">
                        <button @click="handleRemindLater"
                            class="px-4 py-2 text-gray-700 hover:text-gray-900 font-medium">
                            Để sau
                        </button>
                        <button @click="handleReviewNow"
                            class="px-6 py-2 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700 transition-colors font-semibold">
                            Đánh giá ngay
                        </button>
                        <button @click="dismissBanner" class="p-2 text-gray-400 hover:text-gray-600">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
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
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import ReviewService from '@/api-services/ReviewService'

const router = useRouter()
const authStore = useAuthStore()

const pendingReviews = ref([])
const showBanner = ref(false)

// Check từ localStorage xem user đã dismiss banner chưa
const isDismissedToday = () => {
    if (!authStore.user) return false

    const lastDismissed = localStorage.getItem(`review_banner_${authStore.user.id || authStore.user._id}`)
    if (!lastDismissed) return false

    const lastDismissedDate = new Date(lastDismissed)
    const today = new Date()

    // Reset sau 24h
    return today - lastDismissedDate < 24 * 60 * 60 * 1000
}

const loadPendingReviews = async () => {
    if (!authStore.user) {
        showBanner.value = false
        return
    }

    // Check xem đã dismiss hôm nay chưa
    if (isDismissedToday()) {
        showBanner.value = false
        return
    }

    try {
        const reviews = await ReviewService.getPending()
        pendingReviews.value = reviews || []
        showBanner.value = reviews && reviews.length > 0
    } catch (error) {
        console.error('Error loading pending reviews:', error)
        showBanner.value = false
    }
}

const handleReviewNow = () => {
    // Navigate đến trang orders để user đánh giá
    router.push('/orders')
}

const handleRemindLater = () => {
    // Dismiss banner trong 24h
    if (authStore.user) {
        localStorage.setItem(`review_banner_${authStore.user.id || authStore.user._id}`, new Date().toISOString())
    }
    showBanner.value = false
}

const dismissBanner = () => {
    handleRemindLater()
}

onMounted(() => {
    loadPendingReviews()
})
</script>

<style scoped>
.slide-down-enter-active,
.slide-down-leave-active {
    transition: all 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
    transform: translateY(-100%);
    opacity: 0;
}
</style>
