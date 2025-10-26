<template>
    <!-- Product Detail Modal -->
    <div v-if="isVisible" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-2 sm:p-4 z-50">
        <div class="bg-white rounded-lg w-full max-w-6xl max-h-[95vh] overflow-y-auto">
            <!-- Header -->
            <div class="p-6 border-b border-gray-200 flex items-center justify-between">
                <h2 class="text-2xl font-bold text-gray-900">Chi tiết sản phẩm</h2>
                <button @click="closeModal" class="text-gray-400 hover:text-gray-600 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>

            <!-- Product Content -->
            <div v-if="props.product" class="p-6">
                <!-- Product Images -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <!-- Image Gallery -->
                    <div class="space-y-4">
                        <!-- Main Image -->
                        <div class="aspect-square bg-gray-100 rounded-lg overflow-hidden">
                            <img v-if="selectedImage" :src="selectedImage" :alt="props.product.name"
                                class="w-full h-full object-cover" />
                            <div v-else class="w-full h-full flex items-center justify-center text-gray-400">
                                <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                            </div>
                        </div>

                        <!-- Thumbnail Images -->
                        <div v-if="props.product.images && props.product.images.length > 1"
                            class="grid grid-cols-4 gap-2">
                            <button v-for="(image, index) in props.product.images" :key="index"
                                @click="selectedImage = image" :class="[
                                    'aspect-square bg-gray-100 rounded-lg overflow-hidden border-2 transition-colors',
                                    selectedImage === image ? 'border-black' : 'border-gray-200 hover:border-gray-300'
                                ]">
                                <img :src="image" :alt="`${props.product.name} ${index + 1}`"
                                    class="w-full h-full object-cover" />
                            </button>
                        </div>
                    </div>

                    <!-- Product Info -->
                    <div class="space-y-6">
                        <!-- Basic Info -->
                        <div>
                            <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ props.product.name }}</h1>
                            <div class="flex items-center space-x-4 mb-4">
                                <span class="text-lg text-gray-600">{{ props.product.brand }}</span>
                                <span class="px-2 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">{{
                                    props.product.category }}</span>
                            </div>

                            <!-- Rating -->
                            <div class="flex items-center space-x-2 mb-4">
                                <div class="flex items-center">
                                    <span v-for="i in 5" :key="i" class="text-yellow-400">
                                        <svg v-if="i <= Math.floor(props.product.rating)" class="w-5 h-5 fill-current"
                                            viewBox="0 0 20 20">
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                        <svg v-else class="w-5 h-5 text-gray-300" fill="currentColor"
                                            viewBox="0 0 20 20">
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                    </span>
                                </div>
                                <span class="text-gray-600">{{ props.product.rating?.toFixed(1) || '0.0' }} ({{
                                    props.product.total_reviews || 0 }} đánh giá)</span>
                            </div>
                        </div>

                        <!-- Price -->
                        <div class="space-y-2">
                            <div class="flex items-center space-x-3">
                                <span v-if="props.product.discount > 0" class="text-3xl font-bold text-red-600">
                                    {{ formatPrice(calculateDiscountedPrice(props.product.price,
                                        props.product.discount)) }}
                                </span>
                                <span v-else class="text-3xl font-bold text-gray-900">
                                    {{ formatPrice(props.product.price) }}
                                </span>
                                <span v-if="props.product.discount > 0"
                                    class="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm font-semibold">
                                    -{{ product.discount }}%
                                </span>
                            </div>
                            <div v-if="props.product.discount > 0" class="text-lg text-gray-500 line-through">
                                {{ formatPrice(props.product.price) }}
                            </div>
                        </div>

                        <!-- Description -->
                        <div v-if="props.product.description">
                            <h3 class="text-lg font-semibold text-gray-900 mb-2">Mô tả sản phẩm</h3>
                            <p class="text-gray-600 leading-relaxed">{{ props.product.description }}</p>
                        </div>

                        <!-- Colors -->
                        <div v-if="props.product.colors && props.product.colors.length > 0">
                            <h3 class="text-lg font-semibold text-gray-900 mb-3">Màu sắc</h3>
                            <div class="flex flex-wrap gap-2">
                                <span v-for="color in props.product.colors" :key="color"
                                    class="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                                    {{ color }}
                                </span>
                            </div>
                        </div>

                        <!-- Sizes & Stock -->
                        <div v-if="props.product.sizes && props.product.sizes.length > 0">
                            <h3 class="text-lg font-semibold text-gray-900 mb-3">Kích thước & Tồn kho</h3>
                            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                                <div v-for="sizeItem in props.product.sizes" :key="sizeItem.size" :class="[
                                    'p-3 border rounded-lg text-center transition-colors',
                                    sizeItem.stock > 0
                                        ? 'border-gray-200 hover:border-gray-300 bg-white'
                                        : 'border-gray-100 bg-gray-50 text-gray-400'
                                ]">
                                    <div class="font-semibold text-lg">{{ sizeItem.size }}</div>
                                    <div class="text-sm"
                                        :class="sizeItem.stock > 0 ? 'text-gray-600' : 'text-gray-400'">
                                        {{ sizeItem.stock > 0 ? `${sizeItem.stock} sản phẩm` : 'Hết hàng' }}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Stock Summary -->
                        <div class="bg-gray-50 p-4 rounded-lg">
                            <div class="flex items-center justify-between">
                                <span class="text-gray-700 font-medium">Tổng tồn kho:</span>
                                <span class="text-lg font-semibold text-gray-900">{{ props.product.stock }} sản
                                    phẩm</span>
                            </div>
                            <div class="mt-2">
                                <div class="flex items-center justify-between text-sm text-gray-600">
                                    <span>Trạng thái:</span>
                                    <span :class="getStatusClass(props.product)"
                                        class="px-2 py-1 rounded-full text-xs font-semibold">
                                        {{ getStatusText(props.product) }}
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Product ID & Dates -->
                        <div class="border-t pt-4 space-y-2 text-sm text-gray-500">
                            <div class="flex justify-between">
                                <span>Mã sản phẩm:</span>
                                <span class="font-mono">{{ props.product.id }}</span>
                            </div>
                            <div class="flex justify-between">
                                <span>Ngày tạo:</span>
                                <span>{{ formatDate(props.product.created_at) }}</span>
                            </div>
                            <div class="flex justify-between">
                                <span>Cập nhật lần cuối:</span>
                                <span>{{ formatDate(props.product.updated_at) }}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="mt-8 pt-6 border-t border-gray-200 flex flex-col sm:flex-row gap-4">
                    <button @click="editProduct"
                        class="flex-1 px-6 py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors flex items-center justify-center space-x-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg>
                        <span>Chỉnh sửa sản phẩm</span>
                    </button>
                    <button @click="showDeleteConfirm"
                        class="flex-1 px-6 py-3 bg-red-100 text-red-700 rounded-lg hover:bg-red-200 transition-colors flex items-center justify-center space-x-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                        <span>Xóa sản phẩm</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Delete Confirmation Modal -->
        <ConfirmModal :show="showDeleteConfirmModal" :message="deleteConfirmMessage" @confirm="confirmDeleteProduct"
            @cancel="cancelDeleteProduct" />
    </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import ConfirmModal from '@/components/ConfirmModal.vue'

// Props
const props = defineProps({
    product: {
        type: Object,
        required: true
    },
    isVisible: {
        type: Boolean,
        default: false
    }
})

// Emits
const emit = defineEmits(['close', 'edit', 'delete'])

// Reactive data
const selectedImage = ref('')
const showDeleteConfirmModal = ref(false)

// Computed
const hasImages = computed(() => {
    return props.product?.images && props.product.images.length > 0
})

const deleteConfirmMessage = computed(() => {
    if (!props.product) return 'Bạn có chắc chắn muốn xóa sản phẩm này?';
    return `Bạn có chắc chắn muốn xóa sản phẩm "${props.product.name}"? Hành động này không thể hoàn tác.`;
})

// Methods
const initializeProduct = () => {
    if (props.product && hasImages.value) {
        selectedImage.value = props.product.images[0]
    }
}

const closeModal = () => {
    emit('close')
}

const editProduct = () => {
    emit('edit', props.product)
}

const showDeleteConfirm = () => {
    showDeleteConfirmModal.value = true
}

const cancelDeleteProduct = () => {
    showDeleteConfirmModal.value = false
}

const confirmDeleteProduct = () => {
    emit('delete', props.product)
    showDeleteConfirmModal.value = false
}

// Format price to VND
const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price)
}

// Calculate discounted price
const calculateDiscountedPrice = (price, discount) => {
    return price * (1 - discount / 100)
}

// Format date
const formatDate = (dateString) => {
    if (!dateString) return 'N/A'
    const date = new Date(dateString)
    return date.toLocaleDateString('vi-VN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    })
}

// Get status text
const getStatusText = (product) => {
    if (product.stock === 0) return 'Hết hàng'
    if (product.stock < 10) return 'Sắp hết'
    return 'Đang bán'
}

// Get status class
const getStatusClass = (product) => {
    if (product.stock === 0) return 'bg-red-100 text-red-800'
    if (product.stock < 10) return 'bg-yellow-100 text-yellow-800'
    return 'bg-green-100 text-green-800'
}

// Watch for product changes
watch(() => props.product, (newProduct) => {
    if (newProduct && props.isVisible) {
        initializeProduct()
    }
}, { immediate: true })

// Watch for visibility changes
watch(() => props.isVisible, (isVisible) => {
    if (isVisible && props.product) {
        initializeProduct()
    } else if (!isVisible) {
        // Reset state when modal closes
        selectedImage.value = ''
    }
})
</script>

<style scoped>
/* Custom scrollbar for modal */
.overflow-y-auto::-webkit-scrollbar {
    width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}
</style>
