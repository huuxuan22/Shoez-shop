<template>
  <div class="min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <!-- Page Header -->
      <div class="mb-8">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">Tất cả sản phẩm</h1>
        <p class="text-gray-600">Tìm thấy {{ sortedProducts.length }} sản phẩm</p>
      </div>

      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Sidebar Filters -->
        <ProductFilters
          :filters="filters"
          @update:filters="filters = $event"
          :available-brands="availableBrands"
          :available-categories="availableCategories"
          :available-colors="availableColors"
          :available-sizes="availableSizes"
          @clear-filters="clearFilters"
        />

        <!-- Products Grid -->
        <main class="lg:w-3/4">
          <!-- Sort Options -->
          <ProductSort
            v-model:sort-by="sortBy"
            v-model:view-mode="viewMode"
          />

          <!-- Products -->
          <div v-if="sortedProducts.length > 0" :class="[
            viewMode === 'grid' 
              ? 'grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6'
              : 'space-y-4'
          ]">
            <ProductCard
              v-for="product in sortedProducts" 
              :key="product.id"
              :product="product"
              :view-mode="viewMode"
              @click="handleProductClick"
              @add-to-cart="handleAddToCart"
              @buy-now="handleBuyNow"
            />
          </div>

          <!-- No Results -->
          <div v-else class="bg-white rounded-lg shadow-md p-12 text-center">
            <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 class="text-xl font-semibold text-gray-700 mb-2">Không tìm thấy sản phẩm</h3>
            <p class="text-gray-500 mb-4">Thử điều chỉnh bộ lọc để xem thêm sản phẩm</p>
            <button 
              @click="clearFilters"
              class="bg-black text-white px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors"
            >
              Xóa bộ lọc
            </button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useProductFilters } from '@/composables/useProductFilters';
import ProductFilters from '@/components/products/ProductFilters.vue';
import ProductCard from '@/components/products/ProductCard.vue';
import ProductSort from '@/components/products/ProductSort.vue';

const route = useRoute();
const router = useRouter();

// View mode: grid or list
const viewMode = ref('grid');

// Available filter options
const availableBrands = ['Nike', 'Adidas', 'Puma', 'Vans', 'New Balance', 'Converse'];
const availableCategories = ['Sneakers', 'Running', 'Casual', 'Lifestyle', 'Basketball', 'Skate', 'Retro'];
const availableColors = [
  { 
    name: 'Đen', 
    class: 'bg-black',
    activeBorder: 'border-black',
    activeBg: 'bg-black',
    activeText: 'text-white'
  },
  { 
    name: 'Trắng', 
    class: 'bg-white',
    activeBorder: 'border-gray-800',
    activeBg: 'bg-white',
    activeText: 'text-black'
  },
  { 
    name: 'Xanh', 
    class: 'bg-blue-500',
    activeBorder: 'border-blue-600',
    activeBg: 'bg-blue-500',
    activeText: 'text-white'
  },
  { 
    name: 'Đỏ', 
    class: 'bg-red-500',
    activeBorder: 'border-red-600',
    activeBg: 'bg-red-500',
    activeText: 'text-white'
  },
  { 
    name: 'Xám', 
    class: 'bg-gray-500',
    activeBorder: 'border-gray-600',
    activeBg: 'bg-gray-500',
    activeText: 'text-white'
  },
  { 
    name: 'Hồng', 
    class: 'bg-pink-400',
    activeBorder: 'border-pink-500',
    activeBg: 'bg-pink-400',
    activeText: 'text-white'
  },
  { 
    name: 'Be', 
    class: 'bg-amber-200',
    activeBorder: 'border-amber-400',
    activeBg: 'bg-amber-200',
    activeText: 'text-gray-800'
  },
  { 
    name: 'Navy', 
    class: 'bg-blue-900',
    activeBorder: 'border-blue-900',
    activeBg: 'bg-blue-900',
    activeText: 'text-white'
  }
];
const availableSizes = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45];

// Sample products data
const allProducts = ref([
  { 
    id: 1, 
    name: 'Nike Air Force 1', 
    brand: 'Nike',
    price: 2200000,
    image: '/images/shoes/nike-air-max-3.jpg',
    category: 'Sneakers',
    colors: ['Trắng', 'Đen', 'Xanh'],
    sizes: [38, 39, 40, 41, 42, 43]
  },
  { 
    id: 2, 
    name: 'Adidas Ultraboost 22', 
    brand: 'Adidas',
    price: 4500000,
    image: '/images/shoes/adidas-ultraboost-1.jpg',
    category: 'Running',
    colors: ['Đen', 'Trắng', 'Xám'],
    sizes: [39, 40, 41, 42, 43, 44]
  },
  { 
    id: 3, 
    name: 'Converse Chuck Taylor', 
    brand: 'Converse',
    price: 1500000,
    image: '/images/shoes/converse-chuck-taylor-1.jpg',
    category: 'Casual',
    colors: ['Đen', 'Trắng', 'Đỏ'],
    sizes: [36, 37, 38, 39, 40, 41, 42]
  },
  { 
    id: 4, 
    name: 'Puma RS-X', 
    brand: 'Puma',
    price: 2800000,
    image: '/images/shoes/puma-rs-x-1.jpg',
    category: 'Lifestyle',
    colors: ['Trắng', 'Đen', 'Xám'],
    sizes: [39, 40, 41, 42, 43]
  },
  { 
    id: 5, 
    name: 'Nike Air Max 270', 
    brand: 'Nike',
    price: 3200000,
    image: '/images/shoes/nike-air-max-2.jpg',
    category: 'Lifestyle',
    colors: ['Xanh', 'Hồng', 'Trắng'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
  { 
    id: 6, 
    name: 'Adidas NMD R1', 
    brand: 'Adidas',
    price: 3800000,
    image: '/images/shoes/adidas-nmd-1.jpg',
    category: 'Sneakers',
    colors: ['Xám', 'Đen', 'Hồng'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
  { 
    id: 7, 
    name: 'Vans Old Skool', 
    brand: 'Vans',
    price: 1800000,
    image: '/images/shoes/vans-old-skool-1.jpg',
    category: 'Skate',
    colors: ['Đen', 'Navy', 'Đỏ'],
    sizes: [36, 37, 38, 39, 40, 41]
  },
  { 
    id: 8, 
    name: 'New Balance 574', 
    brand: 'New Balance',
    price: 2500000,
    image: '/images/shoes/newbalance-574-1.jpg',
    category: 'Retro',
    colors: ['Xám', 'Navy', 'Be'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
  { 
    id: 9, 
    name: 'Nike Air Jordan 1', 
    brand: 'Nike',
    price: 3600000,
    originalPrice: 5000000,
    discount: 28,
    image: '/images/shoes/nike-jordan-1.jpg',
    category: 'Basketball',
    colors: ['Đỏ', 'Đen'],
    sizes: [39, 40, 41, 42, 43]
  },
  { 
    id: 10, 
    name: 'Adidas Yeezy Boost 350', 
    brand: 'Adidas',
    price: 5200000,
    originalPrice: 7000000,
    discount: 26,
    image: '/images/shoes/adidas-yeezy-1.jpg',
    category: 'Lifestyle',
    colors: ['Be', 'Đen', 'Xám'],
    sizes: [38, 39, 40, 41, 42, 43]
  },
  { 
    id: 11, 
    name: 'Nike Air Max 90', 
    brand: 'Nike',
    price: 2900000,
    image: '/images/shoes/nike-air-max-1.jpg',
    category: 'Sneakers',
    colors: ['Trắng', 'Đen', 'Xanh'],
    sizes: [38, 39, 40, 41, 42, 43]
  },
  { 
    id: 12, 
    name: 'Adidas Superstar', 
    brand: 'Adidas',
    price: 2100000,
    image: '/images/shoes/adidas-superstar-1.jpg',
    category: 'Casual',
    colors: ['Trắng', 'Đen'],
    sizes: [36, 37, 38, 39, 40, 41, 42]
  },
  { 
    id: 13, 
    name: 'Puma Suede Classic', 
    brand: 'Puma',
    price: 1900000,
    image: '/images/shoes/puma-suede-1.jpg',
    category: 'Casual',
    colors: ['Đỏ', 'Xanh', 'Đen'],
    sizes: [38, 39, 40, 41, 42]
  },
  { 
    id: 14, 
    name: 'Vans Authentic', 
    brand: 'Vans',
    price: 1600000,
    image: '/images/shoes/vans-authentic-1.jpg',
    category: 'Casual',
    colors: ['Trắng', 'Đen', 'Navy'],
    sizes: [36, 37, 38, 39, 40, 41]
  },
  { 
    id: 15, 
    name: 'New Balance 990', 
    brand: 'New Balance',
    price: 3500000,
    image: '/images/shoes/newbalance-990-1.jpg',
    category: 'Running',
    colors: ['Navy', 'Xám', 'Đen'],
    sizes: [38, 39, 40, 41, 42, 43]
  },
  { 
    id: 16, 
    name: 'Converse Chuck Taylor Hi', 
    brand: 'Converse',
    price: 1700000,
    image: '/images/shoes/converse-chuck-taylor-2.jpg',
    category: 'Casual',
    colors: ['Trắng', 'Đen', 'Đỏ'],
    sizes: [36, 37, 38, 39, 40, 41, 42]
  },
  { 
    id: 17, 
    name: 'Nike Air Jordan 4', 
    brand: 'Nike',
    price: 4200000,
    image: '/images/shoes/nike-jordan-2.jpg',
    category: 'Basketball',
    colors: ['Trắng', 'Xanh'],
    sizes: [39, 40, 41, 42, 43, 44]
  },
  { 
    id: 18, 
    name: 'Adidas Ultraboost 21', 
    brand: 'Adidas',
    price: 4300000,
    image: '/images/shoes/adidas-ultraboost-2.jpg',
    category: 'Running',
    colors: ['Trắng', 'Đen', 'Xám'],
    sizes: [39, 40, 41, 42, 43]
  },
  { 
    id: 19, 
    name: 'Puma Future Rider', 
    brand: 'Puma',
    price: 2400000,
    image: '/images/shoes/puma-future-rider-1.jpg',
    category: 'Lifestyle',
    colors: ['Trắng', 'Xanh', 'Đỏ'],
    sizes: [38, 39, 40, 41, 42]
  },
  { 
    id: 20, 
    name: 'Vans SK8-Hi', 
    brand: 'Vans',
    price: 2000000,
    image: '/images/shoes/vans-sk8-hi-1.jpg',
    category: 'Skate',
    colors: ['Đen', 'Navy', 'Đỏ'],
    sizes: [37, 38, 39, 40, 41, 42]
  }
]);

// Use composable for filtering and sorting
const { filters, sortBy, sortedProducts, clearFilters, setInitialFilters } = useProductFilters(allProducts);

// Check URL params for pre-filled filters
onMounted(() => {
  setInitialFilters(route.query);
});

// Event handlers
const handleProductClick = (product) => {
  router.push(`/products/${product.id}`);
};

const handleAddToCart = (product) => {
  console.log('Add to cart:', product);
  // TODO: Implement add to cart logic
};

const handleBuyNow = (product) => {
  console.log('Buy now:', product);
  // TODO: Implement buy now logic
};
</script>