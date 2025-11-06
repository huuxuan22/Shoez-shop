<template>
    <div class="mt-12">
        <h2 class="text-3xl font-bold mb-8 text-gray-800">{{ $t('Product.RelatedProducts.title') }}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="relatedProduct in relatedProducts" :key="relatedProduct.id"
                @click="$emit('product-click', relatedProduct.id)"
                class="bg-white rounded-lg shadow-md overflow-hidden cursor-pointer hover:shadow-xl transition-all border border-gray-200">
                <div class="relative pt-[100%] bg-gray-100">
                    <img :src="relatedProduct.image" :alt="relatedProduct.name"
                        class="absolute inset-0 w-full h-full object-cover" />
                </div>
                <div class="p-4">
                    <p class="text-sm text-gray-500">{{ relatedProduct.brand }}</p>
                    <h3 class="font-semibold text-gray-800 mb-2">{{ relatedProduct.name }}</h3>
                    <p class="text-lg font-bold text-black">{{ formatPrice(relatedProduct.price) }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    relatedProducts: {
        type: Array,
        required: true
    }
})

defineEmits(['product-click'])

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};
</script>