<template>
    <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
        <!-- Header -->
        <div class="flex items-center justify-between mb-8">
            <div>
                <h2 class="text-3xl font-bold text-gray-900 font-script">{{ $t('Product.Reviews.title') }}</h2>
                <div class="flex items-center space-x-4 mt-2">
                    <!-- Rating Summary -->
                    <div class="text-center">
                        <div class="text-5xl font-bold text-gray-900">{{ averageRating }}</div>
                        <div class="flex items-center justify-center mt-1">
                            <StarRating :rating="averageRating" :size="20" />
                        </div>
                        <div class="text-gray-600 text-sm mt-1">{{ totalReviews }} {{ $t('Product.Reviews.reviews') }}</div>
                    </div>

                    <!-- Rating Distribution -->
                    <div class="flex-1 max-w-xs">
                        <div v-for="i in 5" :key="i" class="flex items-center space-x-2 text-sm">
                            <span class="w-8 text-gray-600">{{ 6 - i }} ⭐</span>
                            <div class="flex-1 bg-gray-200 rounded-full h-2">
                                <div class="bg-yellow-400 h-2 rounded-full cursor-pointer hover:bg-yellow-500 transition-colors"
                                    :class="{ 'opacity-50': filterRating !== 0 && filterRating !== (6 - i) }"
                                    @click="filterByRating(6 - i)"
                                    :style="{ width: `${ratingDistribution[6 - i] || 0}%` }"></div>
                            </div>
                            <span class="w-12 text-gray-600 text-right">{{ ratingDistribution[6 - i] || 0 }}%</span>
                        </div>
                    </div>
                </div>
            </div>

            <button v-if="canReview" @click="showReviewModal = true"
                class="bg-gradient-to-r from-gray-900 to-black text-white px-6 py-3 rounded-2xl font-semibold hover:from-gray-800 hover:to-gray-900 transform hover:-translate-y-1 transition-all duration-300 shadow-lg">
                {{ $t('Product.Reviews.writeReview') }}
            </button>
        </div>

        <!-- Filters and Sort -->
        <div class="flex items-center justify-between mb-6 pb-6 border-b border-gray-200">
            <div class="flex items-center space-x-4">
                <span class="text-gray-700 font-medium">{{ $t('Product.Reviews.filterBy') }}</span>
                <button @click="filterByRating(0)"
                    :class="filterRating === 0 ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                    class="px-4 py-2 rounded-lg font-semibold transition-all duration-200">
                    {{ $t('Product.Reviews.all') }}
                </button>
                <button v-for="i in 5" :key="i" @click="filterByRating(6 - i)"
                    :class="filterRating === (6 - i) ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                    class="px-4 py-2 rounded-lg font-semibold transition-all duration-200">
                    {{ 6 - i }} ⭐
                </button>
            </div>

            <div class="flex items-center space-x-2">
                <span class="text-gray-700 font-medium">{{ $t('Product.Reviews.sortBy') }}</span>
                <select v-model="sortBy" @change="handleSortChange"
                    class="border border-gray-300 rounded-lg px-4 py-2 font-medium focus:outline-none focus:ring-2 focus:ring-gray-900">
                    <option value="newest">{{ $t('Product.Reviews.newest') }}</option>
                    <option value="oldest">{{ $t('Product.Reviews.oldest') }}</option>
                    <option value="highest">{{ $t('Product.Reviews.highestRating') }}</option>
                    <option value="lowest">{{ $t('Product.Reviews.lowestRating') }}</option>
                </select>
            </div>
        </div>

        <!-- Active Filter Badge -->
        <div v-if="filterRating !== 0" class="mb-4">
            <div class="inline-flex items-center space-x-2 bg-gray-100 rounded-full px-4 py-2">
                <span class="text-gray-700 font-medium">{{ $t('Product.Reviews.showing') }} {{ filteredReviews.length }} {{ $t('Product.Reviews.reviews') }}</span>
                <button @click="filterByRating(0)" class="ml-2 text-gray-500 hover:text-gray-900 transition-colors">
                    ✕
                </button>
            </div>
        </div>

        <!-- Reviews List -->
        <div v-if="paginatedReviews.length > 0" class="space-y-6">
            <ProductReviewCard v-for="review in paginatedReviews" :key="review.id" :review="review" />
        </div>

        <!-- Pagination -->
        <div v-if="totalPages > 1" class="mt-8 flex justify-center items-center space-x-2">
            <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1"
                class="px-4 py-2 rounded-lg border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 transition-colors font-medium">
                {{ $t('Product.Reviews.previous') }}
            </button>

            <div class="flex space-x-1">
                <button v-for="page in visiblePages" :key="page" @click="currentPage = page"
                    :class="currentPage === page ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                    class="px-4 py-2 rounded-lg font-semibold transition-all duration-200">
                    {{ page }}
                </button>
            </div>

            <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages"
                class="px-4 py-2 rounded-lg border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 transition-colors font-medium">
                {{ $t('Product.Reviews.next') }}
            </button>
        </div>

        <!-- Empty State -->
        <div v-if="filteredReviews.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 text-gray-300 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
            <h3 class="mt-4 text-lg font-semibold text-gray-900">{{ $t('Product.Reviews.notFound') }}</h3>
            <p class="mt-2 text-gray-600" v-if="filterRating !== 0">
                {{ $t('Product.Reviews.noReviewsForRating') }} {{ filterRating }} {{ $t('Product.Reviews.rating') }}
            </p>
            <p class="mt-2 text-gray-600" v-else>
                {{ $t('Product.Reviews.noReviewsYet') }}
            </p>
            <button v-if="canReview && filterRating === 0" @click="showReviewModal = true"
                class="mt-4 bg-gray-900 text-white px-6 py-2 rounded-lg font-semibold hover:bg-gray-800 transition-colors">
                {{ $t('Product.Reviews.writeFirstReview') }}
            </button>
        </div>

        <!-- Review Modal -->
        <ReviewModal v-if="showReviewModal" :product="product" @submit="handleReviewSubmit"
            @close="showReviewModal = false" />
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import ProductReviewCard from './ProductReviewCard.vue'
import ReviewModal from './ReviewModal.vue'
import StarRating from '../shared/StarRating.vue'

const { t } = useI18n()

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
const filterRating = ref(0) // 0 = Tất cả, 1-5 = Rating cụ thể
const sortBy = ref('newest')
const currentPage = ref(1)
const itemsPerPage = 5

// Mock data - trong thực tế sẽ lấy từ API
const mockReviews = [
    {
        id: 1,
        user: {
            name: 'Nguyễn Văn A',
            avatar: null
        },
        rating: 5,
        comment: 'Sản phẩm rất tốt, chất lượng đúng như mô tả. Giao hàng nhanh, đóng gói cẩn thận. Đúng size và màu như hình.',
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
    },
    {
        id: 4,
        user: {
            name: 'Phạm Thị D',
            avatar: null
        },
        rating: 3,
        comment: 'Sản phẩm ổn, giá cả hợp lý. Tuy nhiên màu sắc thực tế hơi khác so với hình.',
        images: [],
        createdAt: new Date('2024-01-03'),
        verified: true
    },
    {
        id: 5,
        user: {
            name: 'Hoàng Văn E',
            avatar: null
        },
        rating: 5,
        comment: 'Rất hài lòng! Chất lượng tốt, giao hàng đúng hạn, đóng gói chắc chắn.',
        images: [],
        createdAt: new Date('2023-12-28'),
        verified: true
    },
    {
        id: 6,
        user: {
            name: 'Lý Thị F',
            avatar: null
        },
        rating: 2,
        comment: 'Chất lượng không như mong đợi, có vẻ như hàng kém chất lượng.',
        images: [],
        createdAt: new Date('2023-12-25'),
        verified: false
    },
    {
        id: 7,
        user: {
            name: 'Vũ Văn G',
            avatar: null
        },
        rating: 4,
        comment: 'Giày đẹp, giá hợp lý. Phù hợp để đi hàng ngày.',
        images: [],
        createdAt: new Date('2023-12-20'),
        verified: true
    }
]

// Computed properties
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

const filteredReviews = computed(() => {
    let filtered = [...props.reviews]

    // Filter by rating
    if (filterRating.value !== 0) {
        filtered = filtered.filter(review => review.rating === filterRating.value)
    }

    // Sort reviews
    switch (sortBy.value) {
        case 'newest':
            filtered.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
            break
        case 'oldest':
            filtered.sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt))
            break
        case 'highest':
            filtered.sort((a, b) => b.rating - a.rating)
            break
        case 'lowest':
            filtered.sort((a, b) => a.rating - b.rating)
            break
    }

    return filtered
})

const totalPages = computed(() => {
    return Math.ceil(filteredReviews.value.length / itemsPerPage)
})

const paginatedReviews = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return filteredReviews.value.slice(start, end)
})

const visiblePages = computed(() => {
    const pages = []
    const maxVisible = 5
    let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2))
    let end = Math.min(totalPages.value, start + maxVisible - 1)

    if (end - start < maxVisible - 1) {
        start = Math.max(1, end - maxVisible + 1)
    }

    for (let i = start; i <= end; i++) {
        pages.push(i)
    }

    return pages
})

// Methods
const filterByRating = (rating) => {
    filterRating.value = rating
    currentPage.value = 1 // Reset về trang 1 khi filter
}

const changePage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' })
    }
}

const handleSortChange = () => {
    currentPage.value = 1 // Reset về trang 1 khi sort
}

const handleReviewSubmit = (reviewData) => {
    // Thêm review mới vào danh sách
    const newReview = {
        id: Date.now(),
        user: {
            name: 'Bạn',
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

<style scoped>
/* Custom styles nếu cần */
</style>
