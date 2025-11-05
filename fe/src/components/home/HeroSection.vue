<template>
    <section class="relative min-h-screen flex items-center justify-center hero-section">
        <!-- Background Image với overlay -->
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2068&q=80"
                :alt="$t('HEROSECTION.bgAlt')" class="w-full h-full object-cover image-grayscale" />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-br from-black/80 via-black/60 to-black/90"></div>
            <!-- Pattern Overlay -->
            <div
                class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_rgba(255,255,255,0.1)_0%,_transparent_70%)]">
            </div>
        </div>

        <div class="container mx-auto px-4 content-overlay">
            <div class="max-w-4xl mx-auto text-center">
                <div
                    class="inline-block bg-white text-black text-sm px-6 py-2 rounded-full mb-8 font-alasassy tracking-wider border-2 border-gray-300 shadow-lg">
                    {{ $t('HEROSECTION.badge') }}
                </div>

                <h1
                    class="text-6xl md:text-8xl lg:text-9xl font-alasassy font-bold mb-6 text-white tracking-tighter leading-none">
                    {{ $t('HEROSECTION.title1') }}
                </h1>

                <h2 class="text-4xl md:text-5xl lg:text-6xl font-alasassy font-bold mb-4 text-gray-300 tracking-tight">
                    {{ $t('HEROSECTION.title2') }}
                </h2>

                <p
                    class="text-xl md:text-2xl lg:text-3xl mb-12 text-gray-300 font-alasassy tracking-wider max-w-2xl mx-auto">
                    {{ $t('HEROSECTION.subtitle') }}
                </p>

                <div class="flex flex-col sm:flex-row gap-6 justify-center mb-16">
                    <button
                        class="bg-white text-black px-10 py-4 rounded-xl font-alasassy font-bold hover:bg-gray-100 transition-all duration-300 shadow-2xl border-2 border-gray-300 tracking-widest text-lg transform hover:scale-105 hover:shadow-2xl"
                        @click="scrollToProducts">
                        {{ $t('HEROSECTION.ctaExplore') }}
                    </button>

                    <button
                        class="border-2 border-white text-white px-10 py-4 rounded-xl font-alasassy font-bold hover:bg-white hover:text-black transition-all duration-300 tracking-widest text-lg transform hover:scale-105 backdrop-blur-sm"
                        @click="$router.push('/products')">
                        {{ $t('HEROSECTION.ctaViewProducts') }}
                    </button>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 md:gap-8 text-white max-w-2xl mx-auto">
                    <div class="stats-item">
                        <div class="text-3xl md:text-4xl font-bold font-alasassy tracking-wider mb-2">1000+</div>
                        <div class="text-sm md:text-base font-alasassy tracking-wider opacity-90">{{
                            $t('HEROSECTION.statsProducts') }}</div>
                    </div>
                    <div class="stats-item">
                        <div class="text-3xl md:text-4xl font-bold font-alasassy tracking-wider mb-2">50K+</div>
                        <div class="text-sm md:text-base font-alasassy tracking-wider opacity-90">{{
                            $t('HEROSECTION.statsCustomers') }}</div>
                    </div>
                    <div class="stats-item">
                        <div class="text-3xl md:text-4xl font-bold font-alasassy tracking-wider mb-2">99%</div>
                        <div class="text-sm md:text-base font-alasassy tracking-wider opacity-90">{{
                            $t('HEROSECTION.statsSatisfaction') }}</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Scroll Indicator -->
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-20">
            <div class="animate-bounce">
                <div class="w-6 h-10 border-2 border-white rounded-full flex justify-center">
                    <div class="w-1 h-3 bg-white rounded-full mt-2"></div>
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
@import url('https://fonts.googleapis.com/css2?family=Alatsi&display=swap');

.hero-section {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
}

.font-alasassy {
    font-family: 'Alatsi', sans-serif;
    font-weight: 400;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.content-overlay {
    position: relative;
    z-index: 20;
}

.image-grayscale {
    filter: grayscale(100%) brightness(60%) contrast(130%);
    animation: imageFloat 20s ease-in-out infinite;
}

@keyframes imageFloat {

    0%,
    100% {
        transform: scale(1) translateY(0px);
    }

    50% {
        transform: scale(1.05) translateY(-10px);
    }
}

.stats-item {
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 1.5rem 1rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
}

.stats-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s;
}

.stats-item:hover::before {
    left: 100%;
}

.stats-item:hover {
    transform: translateY(-8px) scale(1.02);
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.3);
    box-shadow:
        0 20px 40px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(255, 255, 255, 0.1);
}

/* Hiệu ứng glow cho tiêu đề */
h1 {
    text-shadow:
        0 0 20px rgba(255, 255, 255, 0.5),
        0 0 40px rgba(255, 255, 255, 0.3),
        0 0 80px rgba(255, 255, 255, 0.2);
    background: linear-gradient(135deg, #ffffff 0%, #e5e5e5 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: titleGlow 3s ease-in-out infinite alternate;
}

@keyframes titleGlow {
    from {
        text-shadow:
            0 0 20px rgba(255, 255, 255, 0.5),
            0 0 40px rgba(255, 255, 255, 0.3),
            0 0 80px rgba(255, 255, 255, 0.2);
    }

    to {
        text-shadow:
            0 0 25px rgba(255, 255, 255, 0.6),
            0 0 50px rgba(255, 255, 255, 0.4),
            0 0 100px rgba(255, 255, 255, 0.3);
    }
}

h2 {
    text-shadow:
        0 0 15px rgba(255, 255, 255, 0.4),
        0 0 30px rgba(255, 255, 255, 0.2);
}

/* Animation cho nút */
button {
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.6s;
}

button:hover::before {
    left: 100%;
}

/* Scroll indicator animation */
@keyframes bounce {

    0%,
    20%,
    50%,
    80%,
    100% {
        transform: translateY(0);
    }

    40% {
        transform: translateY(-10px);
    }

    60% {
        transform: translateY(-5px);
    }
}

.animate-bounce {
    animation: bounce 2s infinite;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    h1 {
        font-size: 4rem !important;
        line-height: 1;
    }

    h2 {
        font-size: 2.5rem !important;
    }

    .stats-item {
        padding: 1rem 0.5rem;
    }

    .stats-item div:first-child {
        font-size: 1.75rem;
    }

    button {
        padding: 0.75rem 1.5rem !important;
        font-size: 0.9rem !important;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 3rem !important;
    }

    h2 {
        font-size: 2rem !important;
    }

    .stats-item {
        padding: 0.75rem 0.25rem;
    }

    .stats-item div:first-child {
        font-size: 1.5rem;
    }
}

/* Floating particles background */
.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image:
        radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.05) 1px, transparent 1px),
        radial-gradient(circle at 80% 70%, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        radial-gradient(circle at 40% 80%, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
    background-size: 50px 50px, 80px 80px, 100px 100px;
    animation: particlesFloat 20s linear infinite;
    z-index: 1;
}

@keyframes particlesFloat {
    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(-50px);
    }
}
</style>

<!-- Global styles -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Alatsi&display=swap');

.font-alasassy {
    font-family: 'Alatsi', 'Arial Black', 'Helvetica Neue', sans-serif;
    font-weight: 400;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}
</style>