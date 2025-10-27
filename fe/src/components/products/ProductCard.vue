<template>
  <div @click="$emit('click', product)" :class="[
    'bg-white rounded-lg shadow-md overflow-hidden cursor-pointer transition-all hover:shadow-xl',
    viewMode === 'list' ? 'flex' : ''
  ]">
    <!-- Product Image -->
    <div :class="viewMode === 'list' ? 'w-48' : 'w-full'">
      <div class="relative pt-[100%] bg-gray-100">
        <img :src="product.images[0]" :alt="product.name"
          class="absolute inset-0 w-full h-full object-cover hover:scale-110 transition-transform duration-300"
          @error="handleImageError" />
        <div v-if="product.discount"
          class="absolute top-4 right-4 bg-red-500 text-white px-3 py-1 rounded-full text-sm font-bold">
          -{{ product.discount }}%
        </div>
      </div>
    </div>

    <!-- Product Info -->
    <div class="p-4 flex-1">
      <p class="text-sm text-gray-500 mb-1">{{ product.brand }}</p>
      <h3 class="text-lg font-semibold text-gray-800 mb-2">{{ product.name }}</h3>
      <p class="text-sm text-gray-600 mb-2">{{ product.category }}</p>

      <!-- Colors -->
      <div class="flex flex-wrap gap-1 mb-3">
        <span v-for="color in product.colors.slice(0, 3)" :key="color" class="text-xs bg-gray-100 px-2 py-1 rounded">
          {{ color }}
        </span>
      </div>

      <!-- Price -->
      <div class="mb-4">
        <p class="text-xl font-bold text-black">{{ formatPrice(product.price) }}</p>
        <p v-if="product.originalPrice" class="text-sm text-gray-400 line-through">
          {{ formatPrice(product.originalPrice) }}
        </p>
      </div>

      <!-- Action Buttons -->
      <div class="flex gap-2">
        <button @click.stop="$emit('add-to-cart', product)"
          class="flex-1 bg-white border-2 border-black text-black px-3 py-2 rounded-lg hover:bg-black hover:text-white transition-all text-sm font-semibold flex items-center justify-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
          </svg>
          <span>Thêm</span>
        </button>
        <button @click.stop="$emit('buy-now', product)"
          class="flex-1 bg-black text-white px-3 py-2 rounded-lg hover:bg-gray-800 transition-all text-sm font-semibold flex items-center justify-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          <span>Mua ngay</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: true
  },
  viewMode: {
    type: String,
    default: 'grid',
    validator: (value) => ['grid', 'list'].includes(value)
  }
});

const emit = defineEmits(['click', 'add-to-cart', 'buy-now']);

const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

const handleImageError = (event) => {
  event.target.src = '/images/shoes/placeholder.jpg';
};
</script>
