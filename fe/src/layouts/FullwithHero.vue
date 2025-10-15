<template>
    <section class="hero-section">
        <div class="hero-background">
            <img src="/images/brands/nike.jpg" alt="Nike" class="hero-image" />
        </div>
    </section>
</template>

<script setup>
// Component chỉ hiển thị hình ảnh
</script>

<style scoped>
.hero-section {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    box-sizing: border-box;
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
}

.hero-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
</style>
