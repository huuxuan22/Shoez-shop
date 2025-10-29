<template>
  <div class="product-category">
    <h3 
      v-if="showTitle && title" 
      class="text-2xl font-bold text-black mb-6"
    >
      {{ title }}
    </h3>
    
    <!-- Product Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div
        v-for="product in products"
        :key="product.id"
        @click="goToProduct(product.id)"
        class="group relative bg-white rounded-2xl overflow-hidden border border-gray-200 hover:border-black transition-all duration-300 transform hover:-translate-y-2 hover:shadow-2xl hover:shadow-black/20 cursor-pointer"
      >
        <!-- Wishlist Button -->
        <button
          @click.stop="toggleWishlist(product.id)"
          class="absolute top-4 right-4 z-10 w-10 h-10 bg-white/90 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white transition-all group/heart shadow-lg"
          :class="{ 'bg-red-500 hover:bg-red-600': isInWishlist(product.id) }"
        >
          <svg 
            class="w-5 h-5 transition-all"
            :class="isInWishlist(product.id) ? 'text-white scale-110' : 'text-black group-hover/heart:scale-110'"
            :fill="isInWishlist(product.id) ? 'currentColor' : 'none'"
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
          </svg>
        </button>

        <!-- Sale Badge -->
        <div
          v-if="product.discount"
          class="absolute top-4 left-4 z-10 bg-red-500 text-white px-3 py-1 rounded-full text-sm font-bold shadow-lg"
        >
          -{{ product.discount }}%
        </div>

        <!-- Product Image -->
        <div class="relative aspect-square bg-gray-100 overflow-hidden">
          <img 
            :src="product.image" 
            :alt="product.name"
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
            @error="handleImageError"
          />
          
          <!-- Quick View Overlay -->
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
            <div class="flex gap-3">
              <button
                @click.stop="quickView(product.id)"
                class="w-12 h-12 bg-white rounded-full flex items-center justify-center hover:scale-110 transition-transform"
              >
                <svg class="w-6 h-6 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </button>
              <!-- Heart overlay -->
              <button
                @click.stop="toggleFavourite(product)"
                class="w-12 h-12 bg-white rounded-full flex items-center justify-center hover:scale-110 transition-transform"
                :title="isInFavourites(product) ? 'Bỏ yêu thích' : 'Yêu thích'"
              >
                <svg v-if="!isInFavourites(product)" class="w-6 h-6 text-red-500" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                </svg>
                <svg v-else class="w-6 h-6 text-red-600" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12.1 21.35l-.1.1-.1-.1C7.14 17.24 4 14.39 4 10.5 4 8 6 6 8.5 6c1.54 0 3.04.99 3.57 2.36h.87C13.46 6.99 14.96 6 16.5 6 19 6 21 8 21 10.5c0 3.89-3.14 6.74-8.9 10.85z" />
                </svg>
              </button>
              
              <button
                @click.stop="addToCart(product)"
                class="w-12 h-12 bg-white rounded-full flex items-center justify-center hover:scale-110 transition-transform"
              >
                <svg class="w-6 h-6 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Product Info -->
        <div class="p-5">
          <!-- Brand -->
          <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">{{ product.brand }}</p>
          
          <!-- Product Name -->
          <h4 class="text-lg font-bold text-black mb-2 line-clamp-2 group-hover:text-gray-700 transition-colors">
            {{ product.name }}
          </h4>

          <!-- Colors -->
          <div class="flex gap-2 mb-3">
            <div 
              v-for="(color, index) in product.colors.slice(0, 4)" 
              :key="index"
              class="w-6 h-6 rounded-full border-2 border-gray-300 hover:border-black transition-colors cursor-pointer"
              :style="{ backgroundColor: getColorHex(color) }"
              :title="color"
            ></div>
            <span v-if="product.colors.length > 4" class="text-xs text-gray-400 self-center">
              +{{ product.colors.length - 4 }}
            </span>
          </div>

          <!-- Price & Action -->
          <div class="flex items-center justify-between">
            <div>
              <p class="text-xl font-bold text-black">
                {{ formatPrice(product.price) }}
              </p>
              <p v-if="product.originalPrice" class="text-sm text-gray-400 line-through">
                {{ formatPrice(product.originalPrice) }}
              </p>
            </div>

            <!-- Add to Cart Button (Mobile) -->
            <button
              @click.stop="addToCart(product)"
              class="lg:hidden w-10 h-10 bg-black rounded-full flex items-center justify-center hover:scale-110 transition-transform"
            >
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
            </button>
          </div>

          <!-- Sizes (Hidden on small screens) -->
          <div class="hidden lg:flex gap-2 mt-3 flex-wrap">
            <span 
              v-for="size in product.sizes.slice(0, 5)" 
              :key="size"
              class="text-xs px-2 py-1 bg-gray-100 text-gray-600 rounded border border-gray-300 hover:border-black hover:text-black transition-colors cursor-pointer"
            >
              {{ size }}
            </span>
            <span v-if="product.sizes.length > 5" class="text-xs text-gray-400 self-center">
              +{{ product.sizes.length - 5 }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useFavouriteStore } from '@/stores/favourite'
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  products: {
    type: Array,
    default: () => []
  },
  showTitle: {
    type: Boolean,
    default: true
  }
});

// Wishlist state
const wishlist = ref([]);

// Toggle wishlist
const toggleWishlist = (productId) => {
  const index = wishlist.value.indexOf(productId);
  if (index > -1) {
    wishlist.value.splice(index, 1);
  } else {
    wishlist.value.push(productId);
  }
};

const isInWishlist = (productId) => {
  return wishlist.value.includes(productId);
};

// Navigate to product detail
const goToProduct = (productId) => {
  router.push(`/products/${productId}`);
};

// Quick view
const quickView = (productId) => {
};

// Add to cart
const addToCart = (product) => {
  alert(`Đã thêm "${product.name}" vào giỏ hàng!`);
};

// Format price
const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { 
    style: 'currency', 
    currency: 'VND' 
  }).format(price);
};

// Handle image error
const handleImageError = (event) => {
  event.target.src = '/images/shoes/placeholder.jpg';
};

// Get color hex
const getColorHex = (colorName) => {
  const colorMap = {
    'Đen': '#000000',
    'Trắng': '#FFFFFF',
    'Xanh': '#3B82F6',
    'Đỏ': '#EF4444',
    'Xám': '#6B7280',
    'Hồng': '#EC4899',
    'Be': '#D4B896',
    'Navy': '#1E3A8A',
    'Xanh Dương': '#3B82F6',
    'Đỏ Đen': '#7F1D1D',
    'Xanh Đen': '#1E3A5F',
    'Đen Trắng': '#4B5563'
  };
  return colorMap[colorName] || '#9CA3AF';
};

// Favourite integration
const favouriteStore = useFavouriteStore()
const getId = (p) => p?._id || p?.id
const isInFavourites = (p) => !!favouriteStore.favourites.find(i => (i._id || i.id) === getId(p))
const toggleFavourite = async (p) => {
  if (isInFavourites(p)) {
    await favouriteStore.removeFavourite(getId(p))
  } else {
    await favouriteStore.addFavourite(p)
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
  
  .product-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .product-item {
    border: 1px solid;
    border-radius: 6px;
    padding: 8px 12px;
    background: white;
    position: relative;
    transition: all 0.2s ease;
  }
  
  .product-item:hover {
    background: #f9fafb;
  }
  
  .product-name {
    color: #111827;
    font-size: 14px;
  }
  
  .promotional-badge {
    position: absolute;
    top: 4px;
    right: 8px;
    background: #dc2626;
    color: white;
    font-size: 10px;
    padding: 1px 4px;
    border-radius: 4px;
  }
  </style>