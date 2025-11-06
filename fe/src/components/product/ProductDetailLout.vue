<template>
    <div class="min-h-screen bg-gray-50">
        <div v-if="product" class="container mx-auto px-4 py-8">
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
                    @update:selected-size="selectedSize = $event" @update:quantity="quantity = $event" />
            </div>

            <!-- Product Description Tabs -->
            <ProductTabs :product="product" />

            <!-- Related Products -->
            <RelatedProducts :related-products="relatedProducts" @product-click="handleProductClick" />
        </div>

        <!-- Product Not Found -->
        <div v-else class="container mx-auto px-4 py-16 text-center">
            <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h2 class="text-2xl font-bold text-gray-700 mb-2">{{ $t('Product.Detail.notFound') }}</h2>
            <router-link to="/products" class="text-black hover:underline">{{ $t('Product.Detail.backToProducts') }}</router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// Import components
import ProductBreadcrumb from './ProductBreadcrumb.vue'
import ProductGallery from './ProductGallery.vue'
import ProductInfo from './ProductInfo.vue'
import ProductTabs from './ProductTabs.vue'
import RelatedProducts from './RelatedProducts.vue'

const route = useRoute()
const router = useRouter()
const productId = parseInt(route.params.id)

// Reactive data
const selectedImage = ref('')
const selectedColor = ref('')
const selectedSize = ref(null)
const quantity = ref(1)

// Sample products data
const allProducts = [
    {
        id: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        image: '/images/shoes/nike-air-max-3.jpg',
        category: 'Sneakers',
        colors: ['Trắng', 'Đen', 'Xám'],
        sizes: [38, 39, 40, 41, 42, 43]
    },
    // ... other products
]

// Computed properties
const product = computed(() => {
    return allProducts.find(p => p.id === productId)
})

const productImages = computed(() => {
    if (!product.value) return []
    return [
        product.value.image,
        product.value.image,
        product.value.image,
        product.value.image
    ]
})

const relatedProducts = computed(() => {
    if (!product.value) return []
    return allProducts
        .filter(p => p.brand === product.value.brand && p.id !== product.value.id)
        .slice(0, 4)
})

// Methods
const handleProductClick = (productId) => {
    router.push(`/products/${productId}`)
}

// Initialize
onMounted(() => {
    if (product.value) {
        selectedImage.value = product.value.image
        selectedColor.value = product.value.colors[0]
    }
})
</script>