<template>
    <div class="product-category">
        <!-- Title (nếu có) -->
        <h3 v-if="showTitle && title" class="text-2xl font-bold mb-6">{{ title }}</h3>

        <!-- Products Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="product in products" :key="product.id"
                class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
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
                        <h4 class="font-semibold text-lg">{{ product.name }}</h4>
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
                    <div class="flex gap-2">
                        <button 
                            @click.stop
                            class="flex-1 bg-white border-2 border-black text-black px-3 py-2 rounded-lg hover:bg-black hover:text-white transition-all text-sm font-semibold flex items-center justify-center gap-1"
                        >
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                            </svg>
                            <span>Thêm</span>
                        </button>
                        <button 
                            @click.stop
                            class="flex-1 bg-black text-white px-3 py-2 rounded-lg hover:bg-gray-800 transition-all text-sm font-semibold flex items-center justify-center gap-1"
                        >
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                            <span>Mua ngay</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
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

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(price)
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