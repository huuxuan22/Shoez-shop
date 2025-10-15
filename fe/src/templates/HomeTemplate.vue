<template>
    <HomeLayout>
        <HeroSection />
        <FeaturedProductsSection />
        <!-- <FullwithVideoHero></FullwithVideoHero> -->
        <FullwithHero />
        <ShoeCustomizer />
        <BrandSection />
        <TestimonialsSection />
        <NewsletterSection />
    </HomeLayout>
</template>

<script setup>
import HomeLayout from '@/layouts/HomeLayout.vue'
import HeroSection from '@/components/home/HeroSection.vue'
import FeaturedProductsSection from '@/components/home/FeaturedProductsSection.vue'
import BrandSection from '@/components/home/BrandSection.vue'
import TestimonialsSection from '@/components/home/TestimonialsSection.vue'
import NewsletterSection from '@/components/home/NewsletterSection.vue'
import ShoeCustomizer from '@/components/home/ShoeCustomizer.vue'
import FullwithVideoHero from '@/layouts/FullwithVideoHero.vue'
import FullwithHero from '@/layouts/FullwithHero.vue'
</script>