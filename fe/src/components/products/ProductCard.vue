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
        <button @click.stop="toggleFavourite"
          :class="[
            'flex-1 px-3 py-2 rounded-lg transition-all text-sm font-semibold flex items-center justify-center gap-1 border-2',
            isFavourited ? 'bg-red-500 border-red-500 text-white hover:bg-red-600' : 'bg-white border-red-500 text-red-500 hover:bg-red-500 hover:text-white'
          ]">
          <svg class="w-4 h-4" :fill="isFavourited ? 'currentColor' : 'none'" :stroke="isFavourited ? 'none' : 'currentColor'" viewBox="0 0 24 24">
            <path
              d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
          </svg>
          <span>{{ isFavourited ? 'Đã thích' : 'Yêu thích' }}</span>
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
import { computed } from 'vue'
import { useFavouriteStore } from '@/stores/favourite'
import { useNotificationStore } from '@/stores/notification'
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

const emit = defineEmits(['click', 'add-to-cart', 'buy-now', 'add-to-favorites']);

const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

const handleImageError = (event) => {
  event.target.src = '/images/shoes/placeholder.jpg';
};

// Favourite logic
const favouriteStore = useFavouriteStore()
const notificationStore = useNotificationStore()

const productId = computed(() => props.product._id || props.product.id)
const isFavourited = computed(() => {
  return favouriteStore.favourites.some(p => (p._id || p.id) === productId.value)
})

const toggleFavourite = async () => {
  if (!productId.value) return
  if (isFavourited.value) {
    await favouriteStore.removeFavourite(productId.value)
  } else {
    await favouriteStore.addFavourite(props.product)
  }
}
</script>
