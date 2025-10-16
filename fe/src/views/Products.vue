<template>
  <div class="min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <!-- Page Header -->
      <div class="mb-8">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">Tất cả sản phẩm</h1>
        <p class="text-gray-600">Tìm thấy {{ filteredProducts.length }} sản phẩm</p>
      </div>

      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Sidebar Filters -->
        <aside class="lg:w-1/4">
          <div class="bg-white rounded-lg shadow-md p-6 sticky top-4">
            <h2 class="text-xl font-bold mb-6 text-gray-800">Bộ lọc</h2>

            <!-- Search -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">Tìm kiếm</label>
              <input 
                v-model="filters.search"
                type="text" 
                placeholder="Tên sản phẩm..."
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            <!-- Brand Filter -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-3">Thương hiệu</label>
              <div class="space-y-2">
                <label v-for="brand in availableBrands" :key="brand" class="flex items-center cursor-pointer">
                  <input 
                    type="checkbox" 
                    :value="brand"
                    v-model="filters.brands"
                    class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500"
                  />
                  <span class="ml-2 text-gray-700">{{ brand }}</span>
                </label>
              </div>
            </div>

            <!-- Category Filter -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-3">Loại giày</label>
              <div class="space-y-2">
                <label v-for="category in availableCategories" :key="category" class="flex items-center cursor-pointer">
                  <input 
                    type="checkbox" 
                    :value="category"
                    v-model="filters.categories"
                    class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500"
                  />
                  <span class="ml-2 text-gray-700">{{ category }}</span>
                </label>
              </div>
            </div>

            <!-- Color Filter -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-3">Màu sắc</label>
              <div class="flex flex-wrap gap-2">
                <button
                  v-for="color in availableColors"
                  :key="color.name"
                  @click="toggleColor(color.name)"
                  :class="[
                    'px-3 py-1 rounded-full text-sm border-2 transition-all flex items-center gap-2',
                    filters.colors.includes(color.name)
                      ? ['border-2', color.activeBorder, color.activeBg, color.activeText, 'font-semibold']
                      : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                  ]"
                >
                  <span 
                    :class="['w-4 h-4 rounded-full border-2 border-gray-400', color.class]"
                  ></span>
                  {{ color.name }}
                </button>
              </div>
            </div>

            <!-- Size Filter -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-3">Size</label>
              <div class="grid grid-cols-4 gap-2">
                <button
                  v-for="size in availableSizes"
                  :key="size"
                  @click="toggleSize(size)"
                  :class="[
                    'py-2 rounded-lg text-sm border-2 transition-all',
                    filters.sizes.includes(size)
                      ? 'border-black bg-black text-white font-semibold'
                      : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                  ]"
                >
                  {{ size }}
                </button>
              </div>
            </div>

            <!-- Price Range -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-3">Giá</label>
              <div class="space-y-3">
                <div>
                  <input 
                    v-model.number="filters.priceRange[0]"
                    type="range" 
                    min="0" 
                    max="10000000" 
                    step="100000"
                    class="w-full"
                  />
                  <div class="flex justify-between text-xs text-gray-600 mt-1">
                    <span>{{ formatPrice(filters.priceRange[0]) }}</span>
                    <span>{{ formatPrice(filters.priceRange[1]) }}</span>
                  </div>
                </div>
                <input 
                  v-model.number="filters.priceRange[1]"
                  type="range" 
                  min="0" 
                  max="10000000" 
                  step="100000"
                  class="w-full"
                />
              </div>
            </div>

            <!-- Clear Filters -->
            <button
              @click="clearFilters"
              class="w-full bg-gray-200 text-gray-700 py-2 rounded-lg hover:bg-gray-300 transition-colors font-semibold"
            >
              Xóa bộ lọc
            </button>
          </div>
        </aside>

        <!-- Products Grid -->
        <main class="lg:w-3/4">
          <!-- Sort Options -->
          <div class="bg-white rounded-lg shadow-md p-4 mb-6 flex flex-wrap items-center justify-between gap-4">
            <div class="flex items-center gap-2">
              <span class="text-gray-700 font-semibold">Sắp xếp:</span>
              <select 
                v-model="sortBy"
                class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="default">Mặc định</option>
                <option value="price-asc">Giá: Thấp đến cao</option>
                <option value="price-desc">Giá: Cao đến thấp</option>
                <option value="name-asc">Tên: A-Z</option>
                <option value="name-desc">Tên: Z-A</option>
              </select>
            </div>

            <div class="flex gap-2">
              <button 
                @click="viewMode = 'grid'"
                :class="[
                  'p-2 rounded-lg transition-colors',
                  viewMode === 'grid' ? 'bg-black text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                ]"
              >
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
              </button>
              <button 
                @click="viewMode = 'list'"
                :class="[
                  'p-2 rounded-lg transition-colors',
                  viewMode === 'list' ? 'bg-black text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                ]"
              >
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Products -->
          <div v-if="filteredProducts.length > 0" :class="[
            viewMode === 'grid' 
              ? 'grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6'
              : 'space-y-4'
          ]">
            <div 
              v-for="product in sortedProducts" 
              :key="product.id"
              @click="$router.push(`/products/${product.id}`)"
              :class="[
                'bg-white rounded-lg shadow-md overflow-hidden cursor-pointer transition-all hover:shadow-xl',
                viewMode === 'list' ? 'flex' : ''
              ]"
            >
              <div :class="viewMode === 'list' ? 'w-48' : 'w-full'">
                <div class="relative pt-[100%] bg-gray-100">
                  <img 
                    :src="product.image" 
                    :alt="product.name"
                    class="absolute inset-0 w-full h-full object-cover hover:scale-110 transition-transform duration-300"
                    @error="handleImageError"
                  />
                  <div v-if="product.discount" class="absolute top-4 right-4 bg-red-500 text-white px-3 py-1 rounded-full text-sm font-bold">
                    -{{ product.discount }}%
                  </div>
                </div>
              </div>
              
              <div class="p-4 flex-1">
                <p class="text-sm text-gray-500 mb-1">{{ product.brand }}</p>
                <h3 class="text-lg font-semibold text-gray-800 mb-2 hover:text-blue-600">{{ product.name }}</h3>
                <p class="text-sm text-gray-600 mb-2">{{ product.category }}</p>
                
                <div class="flex flex-wrap gap-1 mb-3">
                  <span 
                    v-for="color in product.colors.slice(0, 3)" 
                    :key="color"
                    class="text-xs bg-gray-100 px-2 py-1 rounded"
                  >
                    {{ color }}
                  </span>
                </div>

                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-xl font-bold text-black">{{ formatPrice(product.price) }}</p>
                    <p v-if="product.originalPrice" class="text-sm text-gray-400 line-through">
                      {{ formatPrice(product.originalPrice) }}
                    </p>
                  </div>
                  <button 
                    @click.stop="addToCart(product)"
                    class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
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
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

// View mode: grid or list
const viewMode = ref('grid');

// Sort option
const sortBy = ref('default');

// Filters
const filters = ref({
  search: '',
  brands: [],
  categories: [],
  colors: [],
  sizes: [],
  priceRange: [0, 10000000]
});

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

// Sample products data - Sử dụng ảnh từ public/images/shoes
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

// Check URL params for pre-filled filters
onMounted(() => {
  if (route.query.brand) {
    filters.value.brands = [route.query.brand];
  }
});

// Computed: Filtered products
const filteredProducts = computed(() => {
  return allProducts.value.filter(product => {
    // Search filter
    if (filters.value.search && !product.name.toLowerCase().includes(filters.value.search.toLowerCase())) {
      return false;
    }

    // Brand filter
    if (filters.value.brands.length > 0 && !filters.value.brands.includes(product.brand)) {
      return false;
    }

    // Category filter
    if (filters.value.categories.length > 0 && !filters.value.categories.includes(product.category)) {
      return false;
    }

    // Color filter
    if (filters.value.colors.length > 0) {
      const hasMatchingColor = product.colors.some(color => 
        filters.value.colors.some(filterColor => color.includes(filterColor))
      );
      if (!hasMatchingColor) return false;
    }

    // Size filter
    if (filters.value.sizes.length > 0) {
      const hasMatchingSize = product.sizes.some(size => filters.value.sizes.includes(size));
      if (!hasMatchingSize) return false;
    }

    // Price range filter
    if (product.price < filters.value.priceRange[0] || product.price > filters.value.priceRange[1]) {
      return false;
    }

    return true;
  });
});

// Computed: Sorted products
const sortedProducts = computed(() => {
  const products = [...filteredProducts.value];
  
  switch (sortBy.value) {
    case 'price-asc':
      return products.sort((a, b) => a.price - b.price);
    case 'price-desc':
      return products.sort((a, b) => b.price - a.price);
    case 'name-asc':
      return products.sort((a, b) => a.name.localeCompare(b.name));
    case 'name-desc':
      return products.sort((a, b) => b.name.localeCompare(a.name));
    default:
      return products;
  }
});

// Toggle filter selections
const toggleColor = (color) => {
  const index = filters.value.colors.indexOf(color);
  if (index > -1) {
    filters.value.colors.splice(index, 1);
  } else {
    filters.value.colors.push(color);
  }
};

const toggleSize = (size) => {
  const index = filters.value.sizes.indexOf(size);
  if (index > -1) {
    filters.value.sizes.splice(index, 1);
  } else {
    filters.value.sizes.push(size);
  }
};

// Clear all filters
const clearFilters = () => {
  filters.value = {
    search: '',
    brands: [],
    categories: [],
    colors: [],
    sizes: [],
    priceRange: [0, 10000000]
  };
  sortBy.value = 'default';
};

// Format price
const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

// Handle image load error
const handleImageError = (event) => {
  event.target.src = '/images/shoes/placeholder.jpg';
};
</script>