<template>
    <section class="relative w-screen h-screen overflow-hidden">
        <!-- Video Background -->
        <div class="absolute inset-0 z-0">
            <video autoplay muted loop playsinline class="w-full h-full object-cover">
                <source src="@/assets/video/7119881205968.mp4" type="video/mp4">
                <!-- Fallback image -->
                <img :src="fallbackImage" alt="Hero background" class="w-full h-full object-cover">
            </video>
            <!-- Overlay -->
            <div class="absolute inset-0 bg-black/50"></div>
        </div>

        <!-- Content -->
        <div class="relative z-10 w-full h-full flex items-center justify-center text-center text-white px-4">
            <div class="max-w-4xl w-full">
                <!-- Badge -->
                <div
                    class="inline-block bg-white/20 backdrop-blur-sm text-white px-6 py-3 rounded-full mb-8 font-medium border border-white/30 text-lg">
                    {{ $t('Home.VideoHero.badge') }}
                </div>

                <!-- Title -->
                <h1 class="text-5xl md:text-7xl lg:text-8xl font-black mb-6 leading-tight tracking-tight">
                    {{ title || $t('Home.VideoHero.defaultTitle') }}
                </h1>

                <!-- Description -->
                <p
                    class="text-xl md:text-2xl lg:text-3xl mb-10 opacity-95 font-light max-w-2xl mx-auto leading-relaxed">
                    {{ description || $t('Home.VideoHero.defaultDescription') }}
                </p>

                <!-- CTA Button -->
                <button @click="handleCta"
                    class="group bg-white text-black px-12 py-5 rounded-full text-lg md:text-xl font-bold hover:bg-gray-50 transition-all duration-300 transform hover:scale-105 shadow-2xl hover:shadow-3xl relative overflow-hidden">
                    <!-- Shine effect -->
                    <div
                        class="absolute inset-0 bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                    </div>
                    <span class="relative">{{ ctaText || $t('Home.VideoHero.defaultCta') }}</span>
                </button>

                <!-- Scroll indicator -->
                <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
                    <div class="w-6 h-10 border-2 border-white rounded-full flex justify-center">
                        <div class="w-1 h-3 bg-white rounded-full mt-2 animate-pulse"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Animated background elements -->
        <div class="absolute inset-0 z-5 pointer-events-none overflow-hidden">
            <div v-for="i in 15" :key="i" class="absolute w-2 h-2 bg-white rounded-full opacity-20 animate-float"
                :style="{
                    top: Math.random() * 100 + '%',
                    left: Math.random() * 100 + '%',
                    animationDelay: Math.random() * 3 + 's',
                    animationDuration: (Math.random() * 3 + 2) + 's'
                }">
            </div>
        </div>

        <!-- Gradient overlays for better text readability -->
        <div class="absolute bottom-0 left-0 w-full h-1/3 bg-gradient-to-t from-black/30 to-transparent z-1"></div>
        <div class="absolute top-0 left-0 w-full h-1/3 bg-gradient-to-b from-black/20 to-transparent z-1"></div>
    </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

defineProps({
    title: {
        type: String,
        default: ''
    },
    description: {
        type: String,
        default: ''
    },
    ctaText: {
        type: String,
        default: ''
    },
    fallbackImage: {
        type: String,
        default: '/images/brands/nike.png'
    }
})

const handleCta = () => {
    // Handle CTA action - scroll to next section or navigate
    const nextSection = document.querySelector('#featured-products')
    if (nextSection) {
        nextSection.scrollIntoView({ behavior: 'smooth' })
    }
}
</script>

<style scoped>
/* Reset margin và padding để chiếm full màn hình */
section {
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    position: relative;
    left: 0;
    right: 0;
}

/* Đảm bảo video background chiếm toàn bộ không gian */
video,
img {
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
}

/* Custom animations */
@keyframes float {

    0%,
    100% {
        transform: translateY(0px) translateX(0px);
    }

    33% {
        transform: translateY(-20px) translateX(10px);
    }

    66% {
        transform: translateY(-10px) translateX(-10px);
    }
}

.animate-float {
    animation: float 6s ease-in-out infinite;
}

/* Text shadow for better readability */
h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* Smooth transitions */
* {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    section {
        height: 100vh;
        min-height: -webkit-fill-available;
        /* For mobile browsers */
    }

    h1 {
        font-size: 3.5rem !important;
        line-height: 1.1;
    }

    .max-w-4xl {
        padding: 0 1rem;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 2.8rem !important;
    }

    button {
        padding: 1rem 2rem !important;
        font-size: 1.1rem !important;
    }
}

/* Fix for mobile viewport height */
@supports (-webkit-touch-callout: none) {
    section {
        height: -webkit-fill-available;
    }
}

/* Ensure content stays centered and readable */
.container {
    max-width: none;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Improve button hover effects */
button:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

/* Loading state for video */
video {
    background: #000;
}

/* Fallback image styling */
img {
    filter: brightness(0.8);
}
</style>