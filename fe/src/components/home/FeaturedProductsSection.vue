<template>
    <section id="featured-products" class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <!-- Section header -->
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-black mb-2">
                    Sản phẩm nổi bật
                </h2>
                <p class="text-gray-600">
                    Những đôi giày được yêu thích nhất
                </p>
            </div>

            <!-- Men's Shoes -->
            <div class="mb-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">Giày nam</h3>
                    <router-link to="/products?category=men"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        Xem tất cả
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="featuredMenShoes" :show-title="false" />
            </div>

            <!-- Women's Shoes -->
            <div class="mb-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">Giày nữ</h3>
                    <router-link to="/products?category=women"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        Xem tất cả
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="featuredWomenShoes" :show-title="false" />
            </div>

            <!-- Sale Products -->
            <div class="border-t border-gray-200 pt-16">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="text-xl font-semibold text-black">🔥 Sale</h3>
                    <router-link to="/products?sale=true"
                        class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
                        Xem tất cả
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                    </router-link>
                </div>
                <ProductCategory :products="saleProducts" :show-title="false" />
            </div>
        </div>
    </section>
</template>

<script setup>
import ProductCategory from '@/components/shared/ProductCategory.vue'

// Sample data với đầy đủ sản phẩm
const featuredMenShoes = [
    {
        id: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
        category: 'Sneakers',
        colors: ['Trắng', 'Đen', 'Xanh'],
        sizes: [38, 39, 40, 41, 42, 43]
    },
    {
        id: 2,
        name: 'Adidas Ultraboost 22',
        brand: 'Adidas',
        price: 4500000,
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
        category: 'Running',
        colors: ['Đen', 'Trắng', 'Xám'],
        sizes: [39, 40, 41, 42, 43, 44]
    },
    {
        id: 3,
        name: 'Converse Chuck Taylor',
        brand: 'Converse',
        price: 1500000,
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Casual',
        colors: ['Đen', 'Trắng', 'Đỏ'],
        sizes: [36, 37, 38, 39, 40, 41, 42]
    },
    {
        id: 4,
        name: 'Puma RS-X',
        brand: 'Puma',
        price: 2800000,
        image: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
        category: 'Lifestyle',
        colors: ['Trắng Xanh', 'Đen', 'Xám'],
        sizes: [39, 40, 41, 42, 43]
    }
]

const featuredWomenShoes = [
    {
        id: 5,
        name: 'Nike Air Max 270',
        brand: 'Nike',
        price: 3200000,
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Lifestyle',
        colors: ['Xanh Dương', 'Hồng', 'Trắng'],
        sizes: [35, 36, 37, 38, 39, 40]
    },
    {
        id: 6,
        name: 'Adidas NMD R1',
        brand: 'Adidas',
        price: 3800000,
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Sneakers',
        colors: ['Xám', 'Đen', 'Hồng'],
        sizes: [35, 36, 37, 38, 39, 40]
    },
    {
        id: 7,
        name: 'Vans Old Skool',
        brand: 'Vans',
        price: 1800000,
        image: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Skate',
        colors: ['Đen Trắng', 'Navy', 'Đỏ'],
        sizes: [36, 37, 38, 39, 40, 41]
    },
    {
        id: 8,
        name: 'New Balance 574',
        brand: 'New Balance',
        price: 2500000,
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Retro',
        colors: ['Xám', 'Navy', 'Be'],
        sizes: [35, 36, 37, 38, 39, 40]
    }
]

const saleProducts = [
    {
        id: 9,
        name: 'Nike Air Jordan 1',
        brand: 'Nike',
        price: 3600000,
        originalPrice: 5000000,
        discount: 28,
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Basketball',
        colors: ['Đỏ Đen', 'Xanh Đen'],
        sizes: [39, 40, 41, 42, 43]
    },
    {
        id: 10,
        name: 'Adidas Yeezy Boost 350',
        brand: 'Adidas',
        price: 5200000,
        originalPrice: 7000000,
        discount: 26,
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Lifestyle',
        colors: ['Be', 'Đen', 'Xám'],
        sizes: [38, 39, 40, 41, 42, 43]
    },
    {
        id: 11,
        name: 'Puma Cali Sport',
        brand: 'Puma',
        price: 1900000,
        originalPrice: 2500000,
        discount: 24,
        image: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Lifestyle',
        colors: ['Trắng', 'Đen'],
        sizes: [36, 37, 38, 39, 40]
    },
    {
        id: 12,
        name: 'Converse Run Star',
        brand: 'Converse',
        price: 2200000,
        originalPrice: 2800000,
        discount: 21,
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60',
        category: 'Platform',
        colors: ['Đen', 'Trắng', 'Be'],
        sizes: [36, 37, 38, 39, 40, 41]
    }
]
</script>

<style scoped>
/* Thêm một số style để section đẹp hơn */
#featured-products {
    scroll-margin-top: 2rem;
}
</style>