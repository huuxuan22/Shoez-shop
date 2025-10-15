<template>
    <section class="py-12 border-t border-gray-200 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="text-center mb-8">
                <h2 class="text-2xl md:text-3xl font-bold text-black">Thương hiệu</h2>
            </div>

            <div class="grid grid-cols-3 md:grid-cols-6 gap-4">
                <div v-for="brand in brands" :key="brand.name" @click="filterByBrand(brand.name)"
                    class="group cursor-pointer">
                    <div class="bg-white border border-gray-200 rounded p-6 hover:border-black transition">
                        <img :src="brand.logo" :alt="brand.name"
                            class="h-12 w-full object-contain filter grayscale hover:grayscale-0 transition">
                    </div>
                </div>
            </div>

            <!-- Brand trust badges -->
            <div class="mt-8 flex flex-wrap justify-center gap-6 text-sm text-gray-500">
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Đối tác chính thức</span>
                </div>
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Hàng chính hãng 100%</span>
                </div>
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Bảo hành toàn cầu</span>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const brands = [
    { name: 'Nike', logo: '/images/brands/nike-logo.png' },
    { name: 'Adidas', logo: '/images/brands/adidas-logo.png' },
    { name: 'Converse', logo: '/images/brands/converse-logo.png' },
    { name: 'Puma', logo: '/images/brands/puma-logo.png' },
    { name: 'Vans', logo: '/images/brands/vans-logo.png' },
    { name: 'New Balance', logo: '/images/brands/newbalance-logo.png' }
]

const filterByBrand = (brandName) => {
    router.push({ name: 'Products', query: { brand: brandName } })
}
</script>