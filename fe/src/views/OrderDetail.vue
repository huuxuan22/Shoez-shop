<template>
    <div class="min-h-screen bg-gray-50">
        <Header />

        <div class="container mx-auto px-4 py-8">
            <!-- Loading State -->
            <div v-if="loading" class="flex justify-center items-center py-16">
                <div class="animate-spin rounded-full h-12 w-12 border-b-4 border-gray-800"></div>
            </div>

            <!-- Order Content -->
            <div v-else-if="order" class="max-w-5xl mx-auto">
                <!-- Header -->
                <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8 mb-6">
                    <div class="flex items-center justify-between mb-4">
                        <div>
                            <h1 class="text-3xl font-bold text-gray-900 font-script mb-2">Đơn hàng của bạn</h1>
                            <p class="text-gray-600">Cảm ơn bạn đã mua hàng tại Shoez</p>
                        </div>
                        <div class="text-right">
                            <div class="inline-block px-4 py-2 rounded-full font-semibold"
                                :class="getStatusClass(order.status)">
                                {{ getStatusText(order.status) }}
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-gray-200">
                        <div>
                            <p class="text-sm text-gray-600 mb-1">Mã đơn hàng</p>
                            <p class="text-lg font-bold text-black">{{ order.id || order._id }}</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600 mb-1">Ngày đặt</p>
                            <p class="text-lg font-bold text-black">{{ formatDate(order.created_at) }}</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600 mb-1">Dự kiến giao</p>
                            <p class="text-lg font-bold text-black">
                                {{ order.estimatedDelivery ? formatDate(order.estimatedDelivery) :
                                    calculateEstimatedDelivery(order.created_at) }}
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Order Items -->
                <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8 mb-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-6">Sản phẩm đã đặt</h2>
                    <div class="space-y-4">
                        <div v-for="(item, index) in order.items" :key="item.productId || item.id || index"
                            class="flex items-center gap-6 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
                            <img :src="item.image" :alt="item.name || item.productName"
                                class="w-24 h-24 object-cover rounded-lg cursor-pointer" @click="goToProduct(item)" />
                            <div class="flex-1 cursor-pointer" @click="goToProduct(item)">
                                <h3 class="font-bold text-gray-900 mb-1 hover:text-blue-600">{{ item.name ||
                                    item.productName }}</h3>
                                <div v-if="item.brand" class="text-sm text-gray-500 mb-2">{{ item.brand }}</div>
                                <div class="flex items-center gap-4 text-sm text-gray-600">
                                    <span>Size: {{ item.size }}</span>
                                    <span>Màu: {{ item.color }}</span>
                                    <span>Số lượng: {{ item.quantity }}</span>
                                </div>
                            </div>
                            <div class="text-right">
                                <p class="text-lg font-bold text-black">{{ formatPrice(item.price * item.quantity) }}
                                </p>
                                <p v-if="item.discount > 0" class="text-sm text-gray-500 line-through">
                                    {{ formatPrice(item.original_price * item.quantity) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Shipping & Payment Info -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                    <!-- Shipping Info -->
                    <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8">
                        <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            Địa chỉ giao hàng
                        </h2>
                        <div class="space-y-2 text-gray-700">
                            <p class="font-semibold text-black">{{ order.fullName }}</p>
                            <p>{{ order.phone }}</p>
                            <p>{{ order.email }}</p>
                            <p class="mt-2">{{ order.address }}, {{ order.ward }}, {{ order.district }}, {{ order.city
                            }}</p>
                            <p v-if="order.note" class="mt-3 text-sm italic text-gray-500">Ghi chú: {{ order.note }}</p>
                        </div>
                    </div>

                    <!-- Payment Info -->
                    <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8">
                        <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
                            </svg>
                            Phương thức thanh toán
                        </h2>
                        <div class="space-y-3">
                            <div class="flex items-center gap-3">
                                <div v-if="order.paymentMethod === 'cod'"
                                    class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                                    <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor"
                                        viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                                    </svg>
                                </div>
                                <div v-else class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                                    <svg class="w-6 h-6 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M12.5 2C6.512 2 1.5 7.012 1.5 13s5.012 11 11 11 11-5.012 11-11S18.488 2 12.5 2zm0 19c-4.408 0-8-3.592-8-8s3.592-8 8-8 8 3.592 8 8-3.592 8-8 8z" />
                                        <circle cx="8.5" cy="8.5" r="1.5" />
                                        <circle cx="16.5" cy="8.5" r="1.5" />
                                    </svg>
                                </div>
                                <div>
                                    <p class="font-semibold text-black">{{ getPaymentMethodText(order.paymentMethod) }}
                                    </p>
                                    <p class="text-sm text-gray-600">{{ getPaymentDescription(order.paymentMethod) }}
                                    </p>
                                </div>
                            </div>
                            <div v-if="order.shippingMethod" class="mt-4 pt-4 border-t border-gray-200">
                                <p class="text-sm text-gray-600 mb-1">Phương thức vận chuyển</p>
                                <p class="font-semibold text-black">{{ getShippingMethodText(order.shippingMethod) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Order Summary -->
                <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8">
                    <h2 class="text-2xl font-bold text-gray-900 mb-6">Tóm tắt đơn hàng</h2>
                    <div class="space-y-3">
                        <div class="flex justify-between text-gray-700">
                            <span>Tạm tính</span>
                            <span>{{ formatPrice(subtotal) }}</span>
                        </div>
                        <div class="flex justify-between text-gray-700">
                            <span>Phí vận chuyển</span>
                            <span :class="order.shippingFee > 0 ? '' : 'text-green-600'">
                                {{ order.shippingFee > 0 ? formatPrice(order.shippingFee) : 'Miễn phí' }}
                            </span>
                        </div>
                        <div class="flex justify-between text-lg font-bold border-t border-gray-300 pt-3">
                            <span class="text-black">Tổng cộng</span>
                            <span class="text-black">{{ formatPrice(order.total) }}</span>
                        </div>
                    </div>
                </div>

                <!-- Timeline -->
                <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8 mt-6">
                    <h2 class="text-xl font-bold text-gray-900 mb-6">Trạng thái đơn hàng</h2>
                    <div class="relative">
                        <div class="flex flex-col space-y-4">
                            <div v-for="(timeline, index) in orderTimeline" :key="index" class="flex items-start gap-4">
                                <div :class="[
                                    'w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0',
                                    timeline.active ? 'bg-black text-white' : 'bg-gray-200 text-gray-500'
                                ]">
                                    <svg v-if="!timeline.active" class="w-5 h-5" fill="currentColor"
                                        viewBox="0 0 20 20">
                                        <path fill-rule="evenodd"
                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z"
                                            clip-rule="evenodd" />
                                    </svg>
                                    <svg v-else class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd"
                                            d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                            clip-rule="evenodd" />
                                    </svg>
                                </div>
                                <div class="flex-1 pb-8">
                                    <p class="font-semibold text-black">{{ timeline.label }}</p>
                                    <p class="text-sm text-gray-600">{{ timeline.date }}</p>
                                    <p v-if="timeline.description" class="text-sm text-gray-500 mt-1">{{
                                        timeline.description }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Review Section (Chỉ hiển thị khi đơn hàng đã hoàn thành) -->
                <div v-if="order.status === 'complete'"
                    class="bg-white rounded-2xl shadow-lg border border-gray-200 p-8 mt-6">
                    <h2 class="text-xl font-bold text-gray-900 mb-6">Đánh giá sản phẩm</h2>
                    <p class="text-gray-600 mb-6">Chia sẻ trải nghiệm của bạn về sản phẩm đã mua</p>

                    <div class="space-y-4">
                        <div v-for="(item, index) in order.items" :key="index"
                            class="flex items-center gap-4 p-4 border border-gray-200 rounded-lg">
                            <img :src="item.image" :alt="item.name" class="w-20 h-20 object-cover rounded-lg" />
                            <div class="flex-1">
                                <h3 class="font-semibold text-gray-900">{{ item.name || item.productName }}</h3>
                                <p class="text-sm text-gray-600">Size: {{ item.size }} - Màu: {{ item.color }}</p>
                            </div>
                            <button @click="openReviewModal(item)"
                                class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors font-medium">
                                Đánh giá
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="flex gap-4 mt-8">
                    <button @click="router.push('/products')"
                        class="flex-1 bg-white border-2 border-black text-black px-8 py-4 rounded-lg font-semibold hover:bg-black hover:text-white transition-all">
                        Tiếp tục mua sắm
                    </button>
                    <button @click="router.push('/orders')"
                        class="flex-1 bg-black text-white px-8 py-4 rounded-lg font-semibold hover:bg-gray-800 transition-all">
                        Xem tất cả đơn hàng
                    </button>
                </div>
            </div>

            <!-- Not Found -->
            <div v-else class="max-w-2xl mx-auto text-center py-16">
                <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <h2 class="text-2xl font-bold text-gray-700 mb-2">Không tìm thấy đơn hàng</h2>
                <p class="text-gray-600 mb-4">Đơn hàng không tồn tại hoặc bạn không có quyền xem</p>
                <button @click="router.push('/orders')"
                    class="bg-black text-white px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors">
                    Quay lại danh sách đơn hàng
                </button>
            </div>
        </div>
    </div>
    <Footer />

    <!-- Review Modal -->
    <ReviewModal :isOpen="isReviewModalOpen" :product="selectedProduct" :orderId="order?.id || order?._id"
        @close="closeReviewModal" @submitted="handleReviewSubmitted" />
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useOrderStore } from '@/stores/order'
import Header from '@/templates/Header.vue'
import Footer from '@/templates/Footer.vue'
import ReviewModal from '@/components/reviews/ReviewModal.vue'

const route = useRoute()
const router = useRouter()
const orderStore = useOrderStore()

const loading = ref(true)
const order = ref(null)

// Review modal state
const isReviewModalOpen = ref(false)
const selectedProduct = ref(null)

// Computed
const subtotal = computed(() => {
    if (!order.value || !order.value.total || !order.value.shippingFee) return 0
    return order.value.total - order.value.shippingFee
})

const orderTimeline = computed(() => {
    if (!order.value) return []

    const status = order.value.status

    return [
        {
            label: 'Đơn hàng đã được đặt',
            date: formatDate(order.value.created_at),
            active: true, // Luôn active
            description: 'Đơn hàng đã được đặt'
        },
        {
            label: 'Đã xác nhận',
            date: formatDate(order.value.created_at),
            active: ['confirmed', 'shipping', 'complete'].includes(status),
            description: 'Đơn hàng đã được xác nhận'
        },
        {
            label: 'Đang giao hàng',
            date: 'Dự kiến: ' + (order.value.estimatedDelivery ? formatDate(order.value.estimatedDelivery) : calculateEstimatedDelivery(order.value.created_at)),
            active: ['shipping', 'complete'].includes(status),
            description: 'Hàng đang được vận chuyển'
        },
        {
            label: 'Hoàn thành',
            date: order.value.estimatedDelivery ? formatDate(order.value.estimatedDelivery) : calculateEstimatedDelivery(order.value.created_at),
            active: status === 'complete',
            description: 'Đơn hàng đã hoàn thành'
        }
    ]
})

// Methods
const loadOrder = async () => {
    try {
        const orderId = route.params.id

        // Luôn fetch từ API để có dữ liệu mới nhất (không dùng cache trong store)
        const orderData = await orderStore.loadOrderDetail(orderId)
        if (orderData) {
            order.value = orderData
        } else {
            // Nếu API không tìm thấy, thử check trong store như fallback
            if (orderStore.orders && orderStore.orders.length > 0) {
                order.value = orderStore.orders.find(o => o.id === orderId || o._id === orderId)
            }
        }

        // If still not found, show error
        if (!order.value) {
            console.error('Order not found')
        }

    } catch (error) {
        console.error('Error loading order:', error)
    } finally {
        loading.value = false
    }
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

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price)
}

const getStatusText = (status) => {
    const statusMap = {
        'pending': 'Chờ xác nhận',
        'confirmed': 'Đã xác nhận',
        'shipping': 'Đang giao',
        'complete': 'Hoàn thành',
        'cancelled': 'Đã hủy'
    }
    return statusMap[status] || status
}

const getStatusClass = (status) => {
    const classMap = {
        'pending': 'bg-yellow-100 text-yellow-800',
        'confirmed': 'bg-blue-100 text-blue-800',
        'shipping': 'bg-purple-100 text-purple-800',
        'complete': 'bg-green-100 text-green-800',
        'cancelled': 'bg-red-100 text-red-800'
    }
    return classMap[status] || 'bg-gray-100 text-gray-800'
}

const getPaymentMethodText = (method) => {
    const methodMap = {
        'cod': 'Thanh toán khi nhận hàng',
        'credit_card': 'Thẻ tín dụng',
        'momo': 'MoMo'
    }
    return methodMap[method] || method
}

const getPaymentDescription = (method) => {
    const descMap = {
        'cod': 'Bạn sẽ thanh toán khi nhận hàng',
        'credit_card': 'Đã thanh toán bằng thẻ',
        'bank_transfer': 'Đã chuyển khoản ngân hàng',
        'momo': 'Đã thanh toán qua MoMo'
    }
    return descMap[method] || ''
}

const getShippingMethodText = (method) => {
    const methodMap = {
        'standard': 'Giao hàng tiêu chuẩn',
        'express': 'Giao hàng nhanh',
        'pickup': 'Nhận tại cửa hàng'
    }
    return methodMap[method] || method
}

const calculateEstimatedDelivery = (createdAt) => {
    if (!createdAt) return ''
    const deliveryDays = 5 + Math.floor(Math.random() * 2)
    const createdDate = new Date(createdAt)
    const estimatedDate = new Date(createdDate.getTime() + deliveryDays * 24 * 60 * 60 * 1000)
    return formatDate(estimatedDate.toISOString())
}

watch(() => route.params.id, (newId) => {
    if (newId) {
        loading.value = true
        order.value = null
        loadOrder()
    }
})

// Review modal methods
const openReviewModal = (product) => {
    selectedProduct.value = product
    isReviewModalOpen.value = true
}

const closeReviewModal = () => {
    isReviewModalOpen.value = false
    selectedProduct.value = null
}

const handleReviewSubmitted = () => {
    // Reload orders để cập nhật
    loadOrder()
}

// Navigate to product detail page
const goToProduct = (item) => {
    const productId = item.productId || item._id || item.id
    if (productId) {
        router.push(`/products/${productId}`)
    }
}

onMounted(() => {
    loadOrder().then(() => {
        // Auto-open review modal if requested via query
        const shouldOpen = route.query.openReview === '1' || route.query.openReview === 'true'
        if (shouldOpen && order.value && order.value.status === 'complete') {
            let productToReview = null
            const productIdFromQuery = route.query.productId
            if (productIdFromQuery && Array.isArray(order.value.items)) {
                productToReview = order.value.items.find(it => (
                    (it.productId || it._id || it.id) === productIdFromQuery
                )) || null
            }
            if (!productToReview && Array.isArray(order.value.items) && order.value.items.length > 0) {
                productToReview = order.value.items[0]
            }
            if (productToReview) {
                openReviewModal(productToReview)
            }
            // Clean query so it doesn't reopen on navigation
            router.replace({ path: route.path, query: {} })
        }
    })
})
</script>
