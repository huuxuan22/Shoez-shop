<template>
    <div class="bg-white rounded-lg shadow-lg p-8 border border-gray-200">
        <!-- Brand -->
        <p class="text-black font-semibold mb-2 uppercase tracking-wider">{{ product.brand }}</p>

        <!-- Product Name -->
        <h1 class="text-4xl font-bold text-gray-800 mb-4">{{ product.name }}</h1>

        <!-- Category -->
        <p class="text-gray-600 mb-6">{{ product.category }}</p>

        <!-- Rating -->
        <div class="flex items-center mb-6">
            <div class="flex text-yellow-400 mr-2">
                <svg v-for="star in 5" :key="star" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                    <path
                        d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
            </div>
            <span class="text-gray-600">(128 đánh giá)</span>
        </div>

        <!-- Price -->
        <div class="mb-8">
            <div class="flex items-baseline gap-4">
                <p class="text-4xl font-bold text-black">{{ formatPrice(product.price) }}</p>
                <p v-if="product.originalPrice" class="text-2xl text-gray-400 line-through">
                    {{ formatPrice(product.originalPrice) }}
                </p>
            </div>
            <p v-if="product.discount" class="text-gray-600 font-semibold mt-2">
                Tiết kiệm {{ formatPrice(product.originalPrice - product.price) }}
            </p>
        </div>

        <!-- Color Selection -->
        <div class="mb-8">
            <label class="block text-gray-700 font-semibold mb-3">
                Màu sắc: <span class="text-black">{{ selectedColor }}</span>
            </label>
            <div class="flex flex-wrap gap-3">
                <button v-for="color in product.colors" :key="color" @click="$emit('update:selectedColor', color)"
                    :class="[
                        'px-6 py-3 rounded-lg border-2 font-semibold transition-all flex items-center gap-2',
                        selectedColor === color
                            ? getColorClasses(color).active
                            : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                    ]">
                    <span :class="['w-4 h-4 rounded-full border-2 border-gray-400', getColorClasses(color).dot]"></span>
                    {{ color }}
                </button>
            </div>
        </div>

        <!-- Size Selection -->
        <div class="mb-8">
            <div class="flex justify-between items-center mb-3">
                <label class="block text-gray-700 font-semibold">
                    Size: <span class="text-black">{{ selectedSize || 'Chọn size' }}</span>
                </label>
                <!-- <button class="text-black text-sm hover:underline">Hướng dẫn chọn size</button> -->
            </div>
            <div class="grid grid-cols-6 gap-2">
                <button v-for="size in product.sizes" :key="size"
                    @click="$emit('update:selectedSize', getSizeValue(size))" :class="[
                        'py-3 rounded-lg border-2 font-semibold transition-all',
                        selectedSize === getSizeValue(size)
                            ? 'border-black bg-black text-white shadow-md'
                            : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                    ]">
                    {{ getSizeValue(size) }}
                </button>
            </div>
        </div>

        <!-- Quantity -->
        <div class="mb-8">
            <label class="block text-gray-700 font-semibold mb-3">Số lượng</label>
            <div class="flex items-center gap-4">
                <div class="flex items-center border-2 border-gray-300 rounded-lg">
                    <button @click="$emit('update:quantity', Math.max(1, quantity - 1))"
                        class="px-4 py-2 text-gray-600 hover:bg-gray-100 transition-colors">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                        </svg>
                    </button>
                    <input :value="quantity" @input="$emit('update:quantity', parseInt($event.target.value) || 1)"
                        type="number" min="1"
                        class="w-16 text-center border-x-2 border-gray-300 py-2 focus:outline-none" />
                    <button @click="$emit('update:quantity', quantity + 1)"
                        class="px-4 py-2 text-gray-600 hover:bg-gray-100 transition-colors">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                        </svg>
                    </button>
                </div>
                <p class="text-gray-600">{{ product.stock || 50 }} sản phẩm có sẵn</p>
            </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-4 mb-8">
            <button @click="$emit('add-to-cart')"
                class="flex-1 bg-white border-2 border-black text-black px-8 py-4 rounded-lg font-semibold hover:bg-black hover:text-white transition-all transform hover:scale-105 shadow-lg flex items-center justify-center gap-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                Thêm vào giỏ
            </button>
            <button @click="toggleFavourite"
                :class="[
                    'px-8 py-4 rounded-lg font-semibold transition-all transform hover:scale-105 shadow-lg flex items-center justify-center gap-2 border-2',
                    isFavourited ? 'bg-red-500 border-red-500 text-white hover:bg-red-600' : 'bg-white border-red-500 text-red-500 hover:bg-red-500 hover:text-white'
                ]">
                <svg class="w-6 h-6" :fill="isFavourited ? 'currentColor' : 'none'" :stroke="isFavourited ? 'none' : 'currentColor'" viewBox="0 0 24 24">
                    <path
                        d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                </svg>
                {{ isFavourited ? 'Đã thích' : 'Yêu thích' }}
            </button>
            <button @click="$emit('buy-now')"
                class="flex-1 bg-black text-white px-8 py-4 rounded-lg font-semibold hover:bg-gray-800 transition-all transform hover:scale-105 shadow-lg flex items-center justify-center gap-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                Mua ngay
            </button>
        </div>

        <!-- Product Features -->
        <div class="border-t border-gray-200 pt-6">
            <h3 class="font-semibold text-gray-800 mb-4">Đặc điểm nổi bật</h3>
            <ul class="space-y-2 text-gray-600">
                <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-800 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    Chính hãng 100%, tem check chống hàng giả
                </li>
                <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-800 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    Miễn phí vận chuyển toàn quốc cho đơn hàng từ 500k
                </li>
                <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-800 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    Đổi trả trong vòng 7 ngày nếu có lỗi từ nhà sản xuất
                </li>
                <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-800 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    Bảo hành 6 tháng chính hãng
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useFavouriteStore } from '@/stores/favourite'
import { useNotificationStore } from '@/stores/notification'

const props = defineProps({
    product: {
        type: Object,
        required: true
    },
    selectedColor: {
        type: String,
        required: true
    },
    selectedSize: {
        type: [String, Number],
        default: null
    },
    quantity: {
        type: Number,
        required: true
    }
})

defineEmits(['update:selectedColor', 'update:selectedSize', 'update:quantity', 'add-to-cart', 'buy-now'])

// Favourite logic
const favouriteStore = useFavouriteStore()
const notificationStore = useNotificationStore()

const productId = computed(() => props.product._id || props.product.id)
const isFavourited = computed(() => {
    return favouriteStore.favourites.some(p => (p._id || p.id) === productId.value)
})

const toggleFavourite = async () => {
    if (!productId.value) return
    if (isFavourited.value) {
        await favouriteStore.removeFavourite(productId.value)
    } else {
        await favouriteStore.addFavourite(props.product)
    }
}

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

const getColorClasses = (colorName) => {
    const lowerColor = colorName.toLowerCase();

    if (lowerColor.includes('đen')) {
        return {
            dot: 'bg-black',
            active: 'border-black bg-black text-white shadow-md transform scale-105'
        };
    }
    if (lowerColor.includes('trắng')) {
        return {
            dot: 'bg-white',
            active: 'border-gray-800 bg-white text-black shadow-md transform scale-105'
        };
    }
    if (lowerColor.includes('xanh')) {
        return {
            dot: 'bg-gray-500',
            active: 'border-gray-600 bg-gray-500 text-white shadow-md transform scale-105'
        };
    }
    if (lowerColor.includes('đỏ')) {
        return {
            dot: 'bg-gray-600',
            active: 'border-gray-700 bg-gray-600 text-white shadow-md transform scale-105'
        };
    }
    if (lowerColor.includes('xám')) {
        return {
            dot: 'bg-gray-400',
            active: 'border-gray-500 bg-gray-400 text-white shadow-md transform scale-105'
        };
    }

    return {
        dot: 'bg-gray-400',
        active: 'border-black bg-black text-white shadow-md transform scale-105'
    };
};

const getSizeValue = (size) => {
    // Handle both number and object format
    if (typeof size === 'object' && size.size !== undefined) {
        return size.size
    }
    return size
};
</script>