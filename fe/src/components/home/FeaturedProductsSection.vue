<template>
    <section id="featured-products" class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <!-- Section header -->
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-black mb-2">
                    {{ $t('Home.FeaturedProducts.title') }}
                </h2>
                <p class="text-gray-600">
                    {{ $t('Home.FeaturedProducts.subtitle') }}
                </p>
            </div>

            <!-- Loading state -->
            <div v-if="loading" class="text-center py-12">
                <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
                <p class="mt-4 text-gray-600">{{ $t('Home.FeaturedProducts.loading') }}</p>
            </div>

            <!-- Error state -->
            <div v-if="error" class="text-center py-12">
                <p class="text-red-500">{{ $t('Home.FeaturedProducts.error') }} {{ error }}</p>
                <button @click="fetchProducts" class="mt-4 px-6 py-2 bg-black text-white rounded hover:bg-gray-800">
                    {{ $t('Home.FeaturedProducts.retry') }}
                </button>
            </div>

            <!-- Men's Shoes - Nike -->
            <div v-if="!loading && !error && nikeProducts.length" class="mb-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">{{ $t('Home.FeaturedProducts.menShoes') }}</h3>
                    <router-link to="/products?category=men"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        {{ $t('Home.FeaturedProducts.viewAll') }}
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="nikeProducts" :show-title="false" />
            </div>

            <!-- Women's Shoes - Puma -->
            <div v-if="!loading && !error && pumaProducts.length" class="mb-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">{{ $t('Home.FeaturedProducts.womenShoes') }}</h3>
                    <router-link to="/products?category=women"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        {{ $t('Home.FeaturedProducts.viewAll') }}
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="pumaProducts" :show-title="false" />
            </div>

            <!-- Sale Products - Adidas -->
            <div v-if="!loading && !error && adidasProducts.length" class="border-t border-gray-200 pt-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">{{ $t('Home.FeaturedProducts.sale') }}</h3>
                    <router-link to="/products?sale=true"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        {{ $t('Home.FeaturedProducts.viewAll') }}
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="adidasProducts" :show-title="false" />
            </div>

            <!-- Top Rated Products -->
            <div v-if="!loading && !error && topRatedProducts.length" class="border-t border-gray-200 pt-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">{{ $t('Home.FeaturedProducts.topRated') }}</h3>
                    <router-link to="/products?top-rated=true"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        {{ $t('Home.FeaturedProducts.viewAll') }}
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="topRatedProducts" :show-title="false" />
            </div>

            <!-- Empty state -->
            <div v-if="!loading && !error && !nikeProducts.length && !pumaProducts.length && !adidasProducts.length && !topRatedProducts.length"
                class="text-center py-12">
                <p class="text-gray-500">{{ $t('Home.FeaturedProducts.empty') }}</p>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import ProductCategory from '@/components/shared/ProductCategory.vue'
import ProductService from '@/api-services/ProductService'

const { t } = useI18n()

const loading = ref(false)
const error = ref(null)
const nikeProducts = ref([])
const pumaProducts = ref([])
const adidasProducts = ref([])
const topRatedProducts = ref([])

// Hàm fetch dữ liệu sản phẩm
const fetchProducts = async () => {
    loading.value = true
    error.value = null

    try {
        // Gọi 4 API song song
        const [nikeResponse, pumaResponse, adidasResponse, topRatedResponse] = await Promise.all([
            ProductService.getTopBrand('Nike'),
            ProductService.getTopBrand('Puma'),
            ProductService.getTopBrand('Adidas'),
            ProductService.getTopRate()
        ])

        // Transform dữ liệu cho từng danh sách
        nikeProducts.value = transformProductData(nikeResponse)
        pumaProducts.value = transformProductData(pumaResponse)
        adidasProducts.value = transformProductData(adidasResponse)
        topRatedProducts.value = transformProductData(topRatedResponse)

    } catch (err) {
        error.value = t('Home.FeaturedProducts.errorLoad')
    } finally {
        loading.value = false
    }
}

// Hàm transform dữ liệu từ API về format cần thiết
const transformProductData = (apiData) => {
    if (!apiData || !Array.isArray(apiData)) return []

    return apiData.map(product => ({
        id: product.id,
        name: product.name,
        brand: product.brand,
        price: product.price,
        originalPrice: product.originalPrice || null,
        discount: product.discount || 0,
        image: product.images && product.images.length > 0 ? product.images[0] : getFallbackImage(),
        category: product.category,
        colors: Array.isArray(product.colors) ? product.colors.map(color => translateColor(color)) : ['Đen', 'Trắng'],
        sizes: Array.isArray(product.sizes) ? product.sizes.map(sizeItem => sizeItem.size) : [38, 39, 40, 41, 42, 43],
        rating: product.rating || 0,
        reviewCount: product.totalReviews || 0,
        stock: product.stock || 0,
        description: product.description || ''
    })).slice(0, 8) // Chỉ lấy 4 sản phẩm đầu tiên
}

// Hàm dịch màu sắc từ tiếng Anh sang tiếng Việt
const translateColor = (color) => {
    const colorMap = {
        'white': 'Trắng',
        'black': 'Đen',
        'red': 'Đỏ',
        'blue': 'Xanh dương',
        'green': 'Xanh lá',
        'yellow': 'Vàng',
        'pink': 'Hồng',
        'purple': 'Tím',
        'gray': 'Xám',
        'brown': 'Nâu',
        'orange': 'Cam'
    }
    return colorMap[color.toLowerCase()] || color
}

// Hàm fallback image
const getFallbackImage = () => {
    return 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
}

// Fetch data khi component mounted
onMounted(() => {
    fetchProducts()
})
</script>

<style scoped>
#featured-products {
    scroll-margin-top: 2rem;
}

/* Animation cho loading spinner */
.animate-spin {
    animation: spin 1s linear infinite;
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}
</style>