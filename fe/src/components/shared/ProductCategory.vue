<template>
    <div class="product-category">
        <!-- Title (nếu có) -->
        <h3 v-if="showTitle && title" class="text-2xl font-bold mb-6">{{ title }}</h3>

        <!-- Products Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="product in products" :key="product.id" @click="goToProduct(product)"
                class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 cursor-pointer">
                <!-- Product Image -->
                <div class="relative overflow-hidden rounded-t-lg">
                    <img :src="product.image" :alt="product.name"
                        class="w-full h-48 object-cover hover:scale-105 transition-transform duration-300" />
                    <!-- Sale Badge -->
                    <div v-if="product.discount"
                        class="absolute top-2 right-2 bg-red-500 text-white px-2 py-1 rounded text-sm font-bold">
                        -{{ product.discount }}%
                    </div>
                </div>

                <!-- Product Info -->
                <div class="p-4">
                    <div class="flex justify-between items-start mb-2">
                        <h4
                            class="font-semibold text-lg flex-1 min-w-0 whitespace-nowrap overflow-hidden text-ellipsis">
                            {{ product.name }}</h4>
                        <span class="text-xs bg-gray-100 px-2 py-1 rounded">{{ product.brand }}</span>
                    </div>

                    <p class="text-gray-600 text-sm mb-3">{{ product.category }}</p>

                    <!-- Price -->
                    <div class="flex items-center gap-2 mb-3">
                        <span class="text-black font-bold text-lg">{{ formatPrice(product.price) }}</span>
                        <span v-if="product.originalPrice" class="text-gray-500 line-through text-sm">
                            {{ formatPrice(product.originalPrice) }}
                        </span>
                    </div>

                    <!-- Colors -->
                    <div class="flex items-center gap-1 mb-3">
                        <span class="text-xs text-gray-500">Màu:</span>
                        <div class="flex gap-1">
                            <span v-for="color in product.colors.slice(0, 3)" :key="color"
                                class="text-xs bg-gray-100 px-2 py-1 rounded">
                                {{ color }}
                            </span>
                            <span v-if="product.colors.length > 3" class="text-xs bg-gray-100 px-2 py-1 rounded">
                                +{{ product.colors.length - 3 }}
                            </span>
                        </div>
                    </div>

                    <!-- Sizes -->
                    <div class="flex items-center gap-1 mb-4">
                        <span class="text-xs text-gray-500">Size:</span>
                        <div class="flex gap-1 flex-wrap">
                            <span v-for="size in product.sizes.slice(0, 4)" :key="size"
                                class="text-xs bg-gray-100 px-2 py-1 rounded">
                                {{ size }}
                            </span>
                            <span v-if="product.sizes.length > 4" class="text-xs bg-gray-100 px-2 py-1 rounded">
                                +{{ product.sizes.length - 4 }}
                            </span>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex gap-2" @click.stop>
                        <button @click.stop="toggleFavourite(product)"
                            :class="[
                                'flex-1 px-3 py-2 rounded-lg transition-all text-sm font-semibold flex items-center justify-center gap-1 border-2',
                                isFavourited(product) ? 'bg-red-500 border-red-500 text-white hover:bg-red-600' : 'bg-white border-red-500 text-red-500 hover:bg-red-500 hover:text-white'
                            ]">
                            <svg class="w-4 h-4" :fill="isFavourited(product) ? 'currentColor' : 'none'" :stroke="isFavourited(product) ? 'none' : 'currentColor'" viewBox="0 0 24 24">
                                <path
                                    d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                            </svg>
                            <span>{{ isFavourited(product) ? 'Đã thích' : 'Yêu thích' }}</span>
                        </button>
                        <button @click.stop="handleBuyNow(product)"
                            class="flex-1 bg-black text-white px-3 py-2 rounded-lg hover:bg-gray-800 transition-all text-sm font-semibold flex items-center justify-center gap-1">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                            <span>Mua ngay</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Login Required Modal -->
        <ConfirmModal :show="showLoginModal" :message="loginModalMessage" confirm-text="Đăng nhập" cancel-text="Đóng"
            @confirm="handleLoginModalConfirm" @cancel="handleLoginModalCancel" />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useFavouriteStore } from '@/stores/favourite'
import { useNotificationStore } from '@/stores/notification'
import ConfirmModal from '@/components/ConfirmModal.vue'

const props = defineProps({
    products: {
        type: Array,
        required: true,
        default: () => []
    },
    showTitle: {
        type: Boolean,
        default: true
    },
    title: {
        type: String,
        default: ''
    }
})

const router = useRouter()
const authStore = useAuthStore()
const favouriteStore = useFavouriteStore()
const notificationStore = useNotificationStore()

// Modal state
const showLoginModal = ref(false)
const loginModalMessage = ref('')

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price)
}

const isAuthenticated = () => {
    return !!localStorage.getItem('token') && authStore.isAuthenticated;
}

// Favourite helpers
const isFavourited = (product) => {
    const productId = product._id || product.id
    return favouriteStore.favourites.some(p => (p._id || p.id) === productId)
}

const toggleFavourite = async (product) => {
    if (!isAuthenticated()) {
        loginModalMessage.value = 'Bạn chưa đăng nhập. Vui lòng đăng nhập để thêm sản phẩm vào yêu thích!';
        showLoginModal.value = true;
        return;
    }
    const productId = product._id || product.id
    if (!productId) return
    if (isFavourited(product)) {
        await favouriteStore.removeFavourite(productId)
    } else {
        await favouriteStore.addFavourite(product)
    }
}

const handleBuyNow = (product) => {
    // Kiểm tra đăng nhập
    if (!isAuthenticated()) {
        loginModalMessage.value = 'Bạn chưa đăng nhập. Vui lòng đăng nhập để mua sản phẩm!';
        showLoginModal.value = true;
        return;
    }

    // TODO: Implement buy now logic
    console.log('Buy now:', product);
}

const handleLoginModalConfirm = () => {
    showLoginModal.value = false;
    router.push('/login');
}

const handleLoginModalCancel = () => {
    showLoginModal.value = false;
}

function goToProduct(product) {
    if (!product || !product.id) return;
    router.push({ name: 'ProductDetail', params: { id: product.id } })
}
</script>

<style scoped>
.product-category {
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>