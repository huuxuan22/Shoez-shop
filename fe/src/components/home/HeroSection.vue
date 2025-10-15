<template>
    <section class="relative min-h-screen flex items-center justify-center hero-section">
        <img src="https://images.unsplash.com/photo-1460353581641-37baddab0fa2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80"
            alt="Nền giày thể thao trắng đen" class="image-blur">

        <div class="container mx-auto px-4 content-overlay">
            <div class="max-w-3xl mx-auto text-center">
                <div class="inline-block bg-white text-black text-sm px-4 py-1 rounded-full mb-8 font-medium">
                    Giảm giá đến 50%
                </div>

                <h1 class="text-5xl md:text-7xl font-bold mb-6 text-white">
                    SHOEZ SHOP
                </h1>

                <p class="text-xl md:text-2xl mb-12 text-gray-200">
                    Giày thể thao chính hãng
                </p>

                <div class="flex flex-col sm:flex-row gap-4 justify-center mb-16">
                    <button
                        class="bg-white text-black px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition duration-300 shadow-lg"
                        @click="scrollToProducts">
                        Khám phá ngay
                    </button>

                    <button
                        class="border-2 border-white text-white px-8 py-3 rounded-lg font-medium hover:bg-white hover:text-black transition duration-300"
                        @click="$router.push('/products')">
                        Xem sản phẩm →
                    </button>
                </div>

                <div class="flex flex-wrap justify-center gap-8 md:gap-12 text-white">
                    <div class="stats-item">
                        <div class="text-2xl font-bold">1000+</div>
                        <div class="text-sm">Sản phẩm</div>
                    </div>
                    <div class="stats-item">
                        <div class="text-2xl font-bold">50K+</div>
                        <div class="text-sm">Khách hàng</div>
                    </div>
                    <div class="stats-item">
                        <div class="text-2xl font-bold">99%</div>
                        <div class="text-sm">Hài lòng</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const scrollToProducts = () => {
    const productsSection = document.querySelector('#featured-products')
    if (productsSection) {
        productsSection.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
}
</script>

<style scoped>
.hero-section {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1549298916-b41d501d3772?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2012&q=80');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.content-overlay {
    position: relative;
    z-index: 10;
}

.image-blur {
    filter: blur(3px);
    opacity: 0.7;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
}

.stats-item {
    transition: transform 0.3s ease;
}

.stats-item:hover {
    transform: translateY(-5px);
}

@media (max-width: 768px) {
    .hero-section {
        background-attachment: scroll;
    }
}
</style>