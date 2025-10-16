<template>
    <div>
        <!-- Main Image -->
        <div class="bg-white rounded-lg shadow-lg overflow-hidden mb-4 border border-gray-200">
            <div class="relative pt-[100%]">
                <img :src="selectedImage" :alt="product.name" class="absolute inset-0 w-full h-full object-cover"
                    @error="handleImageError" />

                <!-- Zoom indicator -->
                <div class="absolute top-4 right-4 bg-white/90 px-3 py-1 rounded-full text-sm border border-gray-300">
                    <svg class="w-5 h-5 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                    </svg>
                </div>

                <!-- Sale badge -->
                <div v-if="product.discount"
                    class="absolute top-4 left-4 bg-black text-white px-4 py-2 rounded-full text-lg font-bold">
                    -{{ product.discount }}%
                </div>
            </div>
        </div>

        <!-- Thumbnail Gallery -->
        <div class="grid grid-cols-4 gap-2">
            <div v-for="(img, index) in productImages" :key="index" @click="$emit('update:selectedImage', img)" :class="[
                'relative pt-[100%] bg-white rounded-lg overflow-hidden cursor-pointer border-2 transition-all',
                selectedImage === img ? 'border-black shadow-lg' : 'border-gray-200 hover:border-gray-400'
            ]">
                <img :src="img" :alt="`${product.name} ${index + 1}`"
                    class="absolute inset-0 w-full h-full object-cover" @error="handleImageError" />
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    product: {
        type: Object,
        required: true
    },
    selectedImage: {
        type: String,
        required: true
    },
    productImages: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['update:selectedImage'])

const handleImageError = (event) => {
    event.target.src = '/images/shoes/placeholder.jpg';
}
</script>