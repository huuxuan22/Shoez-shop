<template>
    <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
        <!-- Header -->
        <div class="flex items-center justify-between mb-8">
            <div>
                <h2 class="text-3xl font-bold text-gray-900 font-serif">Đánh giá sản phẩm</h2>
                <div class="flex items-center space-x-4 mt-2">
                    <!-- Rating Summary -->
                    <div class="text-center">
                        <div class="text-5xl font-bold text-gray-900">{{ averageRating }}</div>
                        <div class="flex items-center justify-center mt-1">
                            <StarRating :rating="averageRating" :size="20" />
                        </div>
                        <div class="text-gray-600 text-sm mt-1">{{ totalReviews }} đánh giá</div>
                    </div>

                    <!-- Rating Distribution -->
                    <div class="flex-1 max-w-xs">
                        <div v-for="i in 5" :key="i" class="flex items-center space-x-2 text-sm">
                            <span class="w-8 text-gray-600">{{ 6 - i }} ⭐</span>
                            <div class="flex-1 bg-gray-200 rounded-full h-2">
                                <div class="bg-yellow-400 h-2 rounded-full"
                                    :style="{ width: `${ratingDistribution[6 - i] || 0}%` }"></div>
                            </div>
                            <span class="w-12 text-gray-600 text-right">{{ ratingDistribution[6 - i] || 0 }}%</span>
                        </div>
                    </div>
                </div>
            </div>

            <button v-if="canReview" @click="showReviewModal = true"
                class="bg-gradient-to-r from-gray-900 to-black text-white px-6 py-3 rounded-2xl font-semibold hover:from-gray-800 hover:to-gray-900 transform hover:-translate-y-1 transition-all duration-300 shadow-lg">
                Viết đánh giá
            </button>
        </div>

        <!-- Reviews List -->
        <div class="space-y-6">
            <ProductReviewCard v-for="review in displayedReviews" :key="review.id" :review="review" />
        </div>

        <!-- Load More -->
        <div v-if="reviews.length > reviewsToShow" class="text-center mt-8">
            <button @click="loadMoreReviews"
                class="border-2 border-gray-300 text-gray-700 px-8 py-3 rounded-2xl font-semibold hover:border-gray-900 hover:text-gray-900 transition-all duration-300">
                Xem thêm đánh giá
            </button>
        </div>

        <!-- Empty State -->
        <div v-if="reviews.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 text-gray-300 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
            <h3 class="mt-4 text-lg font-semibold text-gray-900">Chưa có đánh giá nào</h3>
            <p class="mt-2 text-gray-600">Hãy là người đầu tiên đánh giá sản phẩm này</p>
            <button v-if="canReview" @click="showReviewModal = true"
                class="mt-4 bg-gray-900 text-white px-6 py-2 rounded-lg font-semibold hover:bg-gray-800 transition-colors">
                Viết đánh giá đầu tiên
            </button>
        </div>

        <!-- Review Modal -->
        <ReviewModal v-if="showReviewModal" :product="product" @submit="handleReviewSubmit"
            @close="showReviewModal = false" />
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import ProductReviewCard from './ProductReviewCard.vue'
import ReviewModal from './ReviewModal.vue'
import StarRating from '../shared/StarRating.vue'

const props = defineProps({
    product: {
        type: Object,
        required: true
    },
    reviews: {
        type: Array,
        default: () => []
    },
    canReview: {
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['review-submitted'])

const showReviewModal = ref(false)
const reviewsToShow = ref(5)

// Mock data - trong thực tế sẽ lấy từ API
const mockReviews = [
    {
        id: 1,
        user: {
            name: 'Nguyễn Văn A',
            avatar: null
        },
        rating: 5,
        comment: 'Sản phẩm rất tốt, chất lượng đúng như mô tả. Giao hàng nhanh, đóng gói cẩn thận.',
        images: [
            'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
        ],
        createdAt: new Date('2024-01-15'),
        verified: true
    },
    {
        id: 2,
        user: {
            name: 'Trần Thị B',
            avatar: null
        },
        rating: 4,
        comment: 'Giày đẹp, đi thoải mái. Size hơi nhỏ so với bình thường, nên chọn size lớn hơn 0.5.',
        images: [],
        createdAt: new Date('2024-01-10'),
        verified: true
    },
    {
        id: 3,
        user: {
            name: 'Lê Văn C',
            avatar: null
        },
        rating: 5,
        comment: 'Tuyệt vời! Đôi giày đẹp hơn cả mong đợi. Chất liệu tốt, form chuẩn.',
        images: [
            'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
        ],
        createdAt: new Date('2024-01-05'),
        verified: false
    }
]

// Computed properties
const displayedReviews = computed(() => {
    return props.reviews.slice(0, reviewsToShow.value)
})

const totalReviews = computed(() => {
    return props.reviews.length
})

const averageRating = computed(() => {
    if (props.reviews.length === 0) return 0
    const sum = props.reviews.reduce((total, review) => total + review.rating, 0)
    return (sum / props.reviews.length).toFixed(1)
})

const ratingDistribution = computed(() => {
    const distribution = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }

    props.reviews.forEach(review => {
        distribution[review.rating] = (distribution[review.rating] || 0) + 1
    })

    // Convert to percentages
    Object.keys(distribution).forEach(rating => {
        distribution[rating] = Math.round((distribution[rating] / props.reviews.length) * 100)
    })

    return distribution
})

// Methods
const loadMoreReviews = () => {
    reviewsToShow.value += 5
}

const handleReviewSubmit = (reviewData) => {
    // Thêm review mới vào danh sách
    const newReview = {
        id: Date.now(),
        user: {
            name: 'Bạn', // Trong thực tế sẽ lấy từ user info
            avatar: null
        },
        ...reviewData,
        createdAt: new Date(),
        verified: true
    }

    emit('review-submitted', newReview)
    showReviewModal.value = false
}

onMounted(() => {
    // Trong thực tế sẽ fetch reviews từ API
    if (props.reviews.length === 0) {
        // Gán mock data nếu không có reviews
        props.reviews.push(...mockReviews)
    }
})
</script>