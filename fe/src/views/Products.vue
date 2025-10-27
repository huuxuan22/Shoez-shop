<template>
  <div class="min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <!-- Page Header -->
      <div class="mb-8">
        <h1 class="text-5xl font-script font-bold text-gray-800 mb-2 tracking-wide">Tất cả sản phẩm</h1>
        <p class="text-gray-600 font-elegant text-lg">Tìm thấy {{ pagination.total || 0 }} sản phẩm</p>
      </div>

      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Sidebar Filters -->
        <ProductFilters :filters="filters" @update:filters="filters = $event" :available-brands="availableBrands"
          :available-categories="availableCategories" :available-colors="availableColors"
          :available-sizes="availableSizes" @clear-filters="clearFilters" />

        <!-- Products Grid -->
        <main class="lg:w-3/4">
          <!-- Sort Options -->
          <ProductSort v-model:sort-by="sortBy" v-model:view-mode="viewMode" />

          <!-- Loading State -->
          <div v-if="loading" class="flex justify-center items-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-800"></div>
          </div>

          <!-- Products -->
          <div v-else-if="products.length > 0" :class="[
            viewMode === 'grid'
              ? 'grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6'
              : 'space-y-4'
          ]">
            <ProductCard v-for="product in products" :key="product.id" :product="product" :view-mode="viewMode"
              @click="handleProductClick" @add-to-cart="handleAddToCart" @buy-now="handleBuyNow" />
          </div>

          <!-- No Results -->
          <div v-else class="bg-white rounded-lg shadow-md p-12 text-center">
            <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 class="text-xl font-semibold text-gray-700 mb-2">Không tìm thấy sản phẩm</h3>
            <p class="text-gray-500 mb-4">Thử điều chỉnh bộ lọc để xem thêm sản phẩm</p>
            <button @click="clearFilters"
              class="bg-black text-white px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors">
              Xóa bộ lọc
            </button>
          </div>

          <!-- Pagination -->
          <div v-if="!loading && pagination.total_pages > 1" class="mt-8 flex justify-center">
            <nav class="flex space-x-2">
              <button @click="changePage(pagination.page - 1)" :disabled="pagination.page === 1"
                class="px-4 py-2 rounded-lg border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100">
                Trước
              </button>
              <span class="px-4 py-2">
                Trang {{ pagination.page }} / {{ pagination.total_pages }}
              </span>
              <button @click="changePage(pagination.page + 1)" :disabled="pagination.page === pagination.total_pages"
                class="px-4 py-2 rounded-lg border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100">
                Sau
              </button>
            </nav>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ProductService from '@/api-services/ProductService';
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

// State
const products = ref([]);
const loading = ref(false);
const pagination = ref({
  total: 0,
  page: 1,
  limit: 10,
  total_pages: 0
});

// Filters
const filters = ref({
  search: '',
  brands: [],
  categories: [],
  colors: [],
  sizes: [],
  priceRange: [0, 10000000]
});

const sortBy = ref('default');

// Load products from API
const loadProducts = async (page = 1) => {
  try {
    loading.value = true;

    // Build API params
    const params = {
      skip: (page - 1) * pagination.value.limit,
      limit: pagination.value.limit,
      sort_by: 'created_at',
      sort_order: 'desc'
    };

    // Add filters if provided
    if (filters.value.search) {
      params.name = filters.value.search;
    }

    if (filters.value.brands.length > 0) {
      params.brand = filters.value.brands[0]; // Backend supports one brand
    }

    if (filters.value.categories.length > 0) {
      params.category = filters.value.categories[0]; // Backend supports one category
    }

    // Price filter
    if (filters.value.priceRange[0] > 0) {
      params.min_price = filters.value.priceRange[0];
    }
    if (filters.value.priceRange[1] < 10000000) {
      params.max_price = filters.value.priceRange[1];
    }

    // Color filter - nếu có màu đã chọn
    if (filters.value.colors.length > 0) {
      params.color = filters.value.colors[0]; // Backend supports one color
    }

    // Size filter - nếu có size đã chọn
    if (filters.value.sizes.length > 0) {
      params.size = filters.value.sizes[0]; // Backend supports one size
    }

    // Sort by
    if (sortBy.value === 'price-asc') {
      params.sort_by = 'price';
      params.sort_order = 'asc';
    } else if (sortBy.value === 'price-desc') {
      params.sort_by = 'price';
      params.sort_order = 'desc';
    }

    const response = await ProductService.getAll(params);

    if (response && response.products) {
      products.value = response.products;
      pagination.value = {
        total: response.total || 0,
        page: response.page || page,
        limit: response.limit || 10,
        total_pages: response.total_pages || 1
      };
    }
  } catch (error) {
    console.error('Error loading products:', error);
    products.value = [];
  } finally {
    loading.value = false;
  }
};

// Watch for filter changes
watch(filters, () => {
  loadProducts(1);
  pagination.value.page = 1;
}, { deep: true });

watch(sortBy, () => {
  loadProducts(1);
  pagination.value.page = 1;
});

// Pagination
const changePage = (page) => {
  if (page >= 1 && page <= pagination.value.total_pages) {
    loadProducts(page);
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

// Event handlers
const handleProductClick = (product) => {
  router.push(`/products/${product.id}`);
};

const handleAddToCart = (product) => {
  // TODO: Implement add to cart
};

const handleBuyNow = (product) => {
  // TODO: Implement buy now
};

// Load products on mount
onMounted(() => {
  loadProducts(1);
});
</script>