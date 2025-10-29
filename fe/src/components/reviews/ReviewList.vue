<template>
    <div class="mt-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Đánh giá từ khách hàng</h2>

        <!-- Loading State -->
        <div v-if="loading" class="flex justify-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
        </div>

        <!-- Empty State -->
        <div v-else-if="reviews.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
            <p class="text-gray-600">Chưa có đánh giá nào</p>
        </div>

        <!-- Reviews List -->
        <div v-else class="space-y-6">
            <div v-for="review in reviews" :key="review.id" :id="`review-${review.id}`"
                class="bg-white border border-gray-200 rounded-lg p-6">
                <!-- Header -->
                <div class="flex items-start justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 bg-gray-200 rounded-full flex items-center justify-center">
                            <span class="text-lg font-bold text-gray-700">
                                {{ review.user_name?.charAt(0).toUpperCase() || 'A' }}
                            </span>
                        </div>
                        <div>
                            <p class="font-semibold text-gray-900">{{ review.user_name || 'Khách hàng' }}</p>
                            <p class="text-sm text-gray-500">{{ formatDate(review.created_at) }}</p>
                        </div>
                    </div>

                    <!-- Stars -->
                    <div class="flex gap-1">
                        <svg v-for="star in 5" :key="star" class="w-5 h-5"
                            :class="star <= review.rating ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor"
                            viewBox="0 0 20 20">
                            <path
                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                        </svg>
                    </div>
                </div>

                <!-- Comment -->
                <p class="text-gray-700 mb-4">{{ review.comment }}</p>

                <!-- Images -->
                <div v-if="review.images && review.images.length > 0" class="flex gap-2 mb-4">
                    <img v-for="(img, idx) in review.images" :key="idx" :src="img"
                        class="w-20 h-20 object-cover rounded-lg cursor-pointer" />
                </div>

                <!-- Helpful -->
                <div class="flex items-center gap-4 text-sm text-gray-500">
                    <button class="flex items-center gap-1 hover:text-gray-700">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                        </svg>
                        <span>Hữu ích ({{ review.helpful_count }})</span>
                    </button>
                </div>

                <!-- Admin Comments Section (chỉ hiện nếu có admin comments) -->
                <div v-if="review.admin_comments && review.admin_comments.length > 0"
                    class="mt-4 pt-4 border-t border-gray-200">
                    <h4 class="font-semibold text-gray-900 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd"
                                d="M18 13V5a2 2 0 00-2-2H4a2 2 0 00-2 2v8a2 2 0 002 2h3l3 3 3-3h3a2 2 0 002-2zM5 7a1 1 0 011-1h8a1 1 0 110 2H6a1 1 0 01-1-1zm1 3a1 1 0 100 2h3a1 1 0 100-2H6z"
                                clip-rule="evenodd" />
                        </svg>
                        Phản hồi từ Admin
                    </h4>
                    <div class="space-y-3">
                        <div v-for="(adminComment, idx) in review.admin_comments" :key="idx"
                            class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <svg class="w-4 h-4 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                                        clip-rule="evenodd" />
                                </svg>
                                <span class="font-semibold text-blue-900">{{ adminComment.admin_name || 'Admin'
                                }}</span>
                                <span class="text-xs text-blue-600">{{ formatDate(adminComment.created_at) }}</span>
                            </div>
                            <p class="text-gray-700">{{ adminComment.comment }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Load More -->
        <div v-if="reviews.length < total" class="text-center mt-8">
            <button @click="loadMore"
                class="px-6 py-2 border-2 border-black text-black rounded-lg hover:bg-black hover:text-white transition-colors">
                Xem thêm đánh giá
            </button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ReviewService from '@/api-services/ReviewService'

const props = defineProps({
    productId: String
})

const reviews = ref([])
const loading = ref(true)
const page = ref(1)
const limit = ref(5)
const total = ref(0)

const loadReviews = async () => {
    try {
        loading.value = true
        const response = await ReviewService.getByProduct(props.productId, {
            page: page.value,
            limit: limit.value
        })

        if (page.value === 1) {
            reviews.value = response.reviews || []
        } else {
            reviews.value.push(...(response.reviews || []))
        }

        total.value = response.total || 0
    } catch (error) {
        console.error('Error loading reviews:', error)
    } finally {
        loading.value = false
    }
}

const loadMore = () => {
    page.value++
    loadReviews()
}

const formatDate = (dateString) => {
    if (!dateString) return ''
    const date = new Date(dateString)
    return date.toLocaleDateString('vi-VN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    })
}

onMounted(() => {
    loadReviews()
})
</script>
