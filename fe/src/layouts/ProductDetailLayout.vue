<template>
    <div class="min-h-screen bg-gray-50">
        <Header />

        <!-- Toast Notification -->
        <Transition name="toast">
            <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
                <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
            </div>
        </Transition>

        <!-- Loading State -->
        <div v-if="loading" class="container mx-auto px-4 py-16 text-center">
            <div class="flex justify-center items-center min-h-[400px]">
                <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-gray-900"></div>
            </div>
            <p class="mt-4 text-gray-600">Đang tải thông tin sản phẩm...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="container mx-auto px-4 py-16 text-center">
            <svg class="w-24 h-24 mx-auto text-red-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h2 class="text-2xl font-bold text-gray-700 mb-2">Không thể tải dữ liệu</h2>
            <p class="text-gray-600 mb-4">{{ error }}</p>
            <button @click="loadProduct"
                class="bg-gray-900 text-white px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors">
                Thử lại
            </button>
        </div>

        <!-- Product Content -->
        <div v-else-if="product" class="container mx-auto px-4 py-8">
            <!-- Breadcrumb -->
            <ProductBreadcrumb :product-name="product.name" />

            <!-- Product Details -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <!-- Image Gallery -->
                <ProductGallery :product="product" :selected-image="selectedImage" :product-images="productImages"
                    @update:selected-image="selectedImage = $event" />

                <!-- Product Info -->
                <ProductInfo :product="product" :selected-color="selectedColor" :selected-size="selectedSize"
                    :quantity="quantity" @update:selected-color="selectedColor = $event"
                    @update:selected-size="selectedSize = $event" @update:quantity="quantity = $event"
                    @add-to-cart="handleAddToCart" @buy-now="handleBuyNow" />
            </div>

            <!-- Product Description Tabs -->
            <ProductTabs :product="product" />

            <!-- Related Products -->
            <RelatedProducts :related-products="relatedProducts" @product-click="handleProductClick" />

            <!-- Product Reviews -->
            <ReviewList :product-id="product.id || product._id" />
        </div>

        <!-- Product Not Found -->
        <div v-else-if="!loading && !error && !product" class="container mx-auto px-4 py-16 text-center">
            <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h2 class="text-2xl font-bold text-gray-700 mb-2">Không tìm thấy sản phẩm</h2>
            <router-link to="/products" class="text-black hover:underline">Quay lại trang sản phẩm</router-link>
        </div>
        <Footer />
    </div>
</template>

<script setup>
import ProductBreadcrumb from '@/components/product/ProductBreadcrumb.vue'
import ProductGallery from '@/components/product/ProductGallery.vue'
import ProductInfo from '@/components/product/ProductInfo.vue'
import ProductTabs from '@/components/product/ProductTabs.vue'
import RelatedProducts from '@/components/product/RelatedProducts.vue'
import ReviewList from '@/components/reviews/ReviewList.vue'
import Footer from '@/templates/Footer.vue'
import Header from '@/templates/Header.vue'
import { ref, computed, onMounted, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { nextTick } from 'vue'
import ProductService from '@/api-services/ProductService'
import ToastNotification from '@/components/ToastNotification.vue'
import { useCartStore, useOrderStore } from '@/stores'

const orderStore = useOrderStore()
const toast = reactive({ show: false, message: '', type: 'info' })
function showToast(message, type = 'error') {
    toast.message = message
    toast.type = type
    toast.show = true
    setTimeout(() => { toast.show = false }, 2000)
}

const route = useRoute()
const router = useRouter()
const cartStore = useCartStore();
const productId = route.params.id // Lấy string từ route params thay vì parseInt

// Reactive data
const product = ref(null)
const loading = ref(true)
const error = ref(null)
const selectedImage = ref('')
const selectedColor = ref('')
const selectedSize = ref(null)
const quantity = ref(1)

// Related products và reviews
const relatedProducts = ref([])
const productReviews = ref([])

// Check if need to highlight a review
const highlightReviewId = computed(() => route.query.highlightReview)

// Load product from API
const loadProduct = async () => {
    try {
        loading.value = true
        error.value = null

        // Call API with include comments
        const data = await ProductService.getById(productId, true)

        // Transform sizes from array of objects to array of numbers
        if (data.sizes && Array.isArray(data.sizes)) {
            data.sizes = data.sizes.map(item => {
                if (typeof item === 'object' && item.size !== undefined) {
                    return item.size
                }
                return item
            })
        }

        product.value = data

        // Set default values
        if (data.images && data.images.length > 0) {
            selectedImage.value = data.images[0]
        }
        if (data.colors && data.colors.length > 0) {
            selectedColor.value = data.colors[0]
        }

        // Load reviews if available
        if (data.comments) {
            // Transform comments to match ProductReviews component format
            productReviews.value = data.comments.map(comment => ({
                id: comment.id,
                user: {
                    name: comment.user_name || 'User',
                    avatar: comment.user_avatar || null
                },
                rating: comment.rating,
                comment: comment.comment,
                images: comment.images || [],
                createdAt: new Date(comment.created_at),
                verified: comment.verified
            }))

            // Scroll to review nếu có highlightReviewId
            nextTick(() => {
                if (highlightReviewId.value) {
                    setTimeout(() => {
                        const reviewElement = document.getElementById(`review-${highlightReviewId.value}`)
                        if (reviewElement) {
                            reviewElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
                            // Add highlight effect
                            reviewElement.classList.add('highlight-review')
                            setTimeout(() => {
                                reviewElement.classList.remove('highlight-review')
                            }, 3000)
                        }
                    }, 500)
                }
            })
        }

        // Load related products (same brand)
        if (data.brand) {
            // TODO: Call API to get related products
            relatedProducts.value = [] // Will be populated when API is ready
        }

    } catch (err) {
        error.value = err.message || 'Không thể tải dữ liệu sản phẩm'
    } finally {
        loading.value = false
    }
}

// TODO: Load related products from API when backend is ready

const productImages = computed(() => {
    if (!product.value || !product.value.images) return []
    return product.value.images
})

// Methods
const handleProductClick = (productId) => {
    router.push(`/products/${productId}`)
}

const handleAddToCart = async () => {
    debugger;
    if (!selectedSize.value) { showToast('Vui lòng chọn size', 'error'); return; }
    if (!selectedColor.value) { showToast('Vui lòng chọn màu sắc', 'error'); return; }
    if (!product.value) return;

    const res = await cartStore.addToCart({
        id: product.value.id,
        quantity: quantity.value || 1,
        size: selectedSize.value,
        color: selectedColor.value,
        name: product.value.name,
        image: product.value.images?.[0] || '',
        price: product.value.price
    });

    if (res) {
        showToast('Đã thêm vào giỏ hàng!', 'success');
    } else {
        showToast(cartStore.error || 'Không thể thêm vào giỏ hàng', 'error');
    }
};

const handleBuyNow = () => {
    // Validate required fields
    if (!selectedSize.value) {
        showToast('Vui lòng chọn size', 'error')
        return
    }

    if (!selectedColor.value) {
        showToast('Vui lòng chọn màu sắc', 'error')
        return
    }

    if (!product.value) {
        return
    }

    const productWithOptions = {
        ...product.value,
        size: selectedSize.value,
        color: selectedColor.value,
        quantity: quantity.value
    }

    orderStore.setCheckoutFromProduct(productWithOptions)
    router.push('/checkout')
}

// Initialize
onMounted(() => {
    loadProduct()
})
</script>

<style scoped>
/* Toast animations */
.toast-enter-active,
.toast-leave-active {
    transition: all 0.25s ease;
}

/* Highlight review animation */
@keyframes highlight {

    0%,
    100% {
        background-color: transparent;
    }

    50% {
        background-color: #fef3c7;
        border: 2px solid #f59e0b;
    }
}

.highlight-review {
    animation: highlight 2s ease-in-out;
    border-radius: 8px;
    padding: 16px;
}

.toast-enter-from {
    opacity: 0;
    transform: translateY(-10px);
}

.toast-leave-to {
    opacity: 0;
    transform: translateY(-10px);
}
</style>