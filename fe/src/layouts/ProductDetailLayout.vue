<template>
    <div class="min-h-screen bg-gray-50">
        <Header />
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
import Footer from '@/templates/Footer.vue'
import Header from '@/templates/Header.vue'
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const productId = parseInt(route.params.id)

// Reactive data
const selectedImage = ref('')
const selectedColor = ref('')
const selectedSize = ref(null)
const quantity = ref(1)

// Sample products data với nhiều sản phẩm hơn
const allProducts = [
    {
        id: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        originalPrice: 2500000,
        discount: 12,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Sneakers',
        colors: ['Trắng', 'Đen', 'Xám'],
        sizes: [38, 39, 40, 41, 42, 43],
        stock: 25
    },
    {
        id: 2,
        name: 'Adidas Ultraboost 22',
        brand: 'Adidas',
        price: 4500000,
        originalPrice: 5000000,
        discount: 10,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Running',
        colors: ['Đen', 'Trắng', 'Xám'],
        sizes: [39, 40, 41, 42, 43, 44],
        stock: 18
    },
    {
        id: 3,
        name: 'Converse Chuck Taylor All Star',
        brand: 'Converse',
        price: 1500000,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Casual',
        colors: ['Đen', 'Trắng', 'Đỏ', 'Xanh Navy'],
        sizes: [36, 37, 38, 39, 40, 41, 42],
        stock: 35
    },
    {
        id: 4,
        name: 'Puma RS-X',
        brand: 'Puma',
        price: 2800000,
        originalPrice: 3200000,
        discount: 12,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Lifestyle',
        colors: ['Trắng', 'Đen', 'Xám'],
        sizes: [39, 40, 41, 42, 43],
        stock: 22
    },
    {
        id: 5,
        name: 'Nike Air Max 270',
        brand: 'Nike',
        price: 3200000,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Lifestyle',
        colors: ['Xanh', 'Hồng', 'Trắng'],
        sizes: [35, 36, 37, 38, 39, 40],
        stock: 15
    },
    {
        id: 6,
        name: 'Vans Old Skool',
        brand: 'Vans',
        price: 1200000,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Skate',
        colors: ['Đen Trắng', 'Xanh Navy', 'Đỏ'],
        sizes: [36, 37, 38, 39, 40, 41, 42],
        stock: 40
    },
    {
        id: 7,
        name: 'New Balance 574',
        brand: 'New Balance',
        price: 1800000,
        originalPrice: 2000000,
        discount: 10,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Lifestyle',
        colors: ['Xám', 'Xanh Navy', 'Be'],
        sizes: [38, 39, 40, 41, 42, 43],
        stock: 28
    },
    {
        id: 8,
        name: 'Adidas Stan Smith',
        brand: 'Adidas',
        price: 1600000,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Casual',
        colors: ['Trắng Xanh', 'Trắng Đỏ', 'Trắng'],
        sizes: [37, 38, 39, 40, 41, 42],
        stock: 32
    },
    {
        id: 9,
        name: 'Nike Air Jordan 1',
        brand: 'Nike',
        price: 3600000,
        originalPrice: 5000000,
        discount: 28,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Basketball',
        colors: ['Đỏ Đen', 'Xanh Đen'],
        sizes: [39, 40, 41, 42, 43],
        stock: 12
    },
    {
        id: 10,
        name: 'Reebok Classic Leather',
        brand: 'Reebok',
        price: 1400000,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Casual',
        colors: ['Trắng', 'Đen', 'Xám'],
        sizes: [38, 39, 40, 41, 42],
        stock: 20
    },
    {
        id: 11,
        name: 'Asics Gel-Kayano 28',
        brand: 'Asics',
        price: 3800000,
        originalPrice: 4200000,
        discount: 9,
        image: 'https://tamanh.net/wp-content/uploads/2016/12/giay-luoi-nam-da-bo-cao-cap-gnta5501-d..jpg',
        category: 'Running',
        colors: ['Xanh', 'Đen', 'Xám'],
        sizes: [39, 40, 41, 42, 43, 44],
        stock: 16
    },
    {
        id: 12,
        name: 'Skechers Go Walk',
        brand: 'Skechers',
        price: 1100000,
        image: '/images/shoes/skechers-go-walk.jpg',
        category: 'Comfort',
        colors: ['Đen', 'Xám', 'Xanh Navy'],
        sizes: [36, 37, 38, 39, 40, 41],
        stock: 45
    }
]

// Computed properties
const product = computed(() => {
    return allProducts.find(p => p.id === productId)
})

const productImages = computed(() => {
    if (!product.value) return []
    // Trong thực tế, mỗi sản phẩm sẽ có nhiều ảnh từ API
    // Ở đây tạm dùng cùng 1 ảnh cho demo
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