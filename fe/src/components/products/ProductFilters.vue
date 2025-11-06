<template>
  <aside class="lg:w-1/4">
    <div class="bg-white rounded-lg shadow-md p-6 sticky top-4">
      <h2 class="text-xl font-bold mb-6 text-gray-800">{{ $t('Products.Filters.title') }}</h2>

      <!-- Search -->
      <div class="mb-6">
        <label class="block text-sm font-semibold text-gray-700 mb-2">{{ $t('Products.Filters.search') }}</label>
        <input 
          :value="filters.search"
          @input="$emit('update:filters', { ...filters, search: $event.target.value })"
          type="text" 
          :placeholder="$t('Products.Filters.searchPlaceholder')"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        />
      </div>

      <!-- Brand Filter -->
      <div class="mb-6">
        <label class="block text-sm font-semibold text-gray-700 mb-3">{{ $t('Products.Filters.brand') }}</label>
        <div class="space-y-2">
          <label v-for="brand in availableBrands" :key="brand" class="flex items-center cursor-pointer">
            <input 
              type="checkbox" 
              :value="brand"
              :checked="filters.brands.includes(brand)"
              @change="toggleBrand(brand)"
              class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500"
            />
            <span class="ml-2 text-gray-700">{{ brand }}</span>
          </label>
        </div>
      </div>

      <!-- Category Filter -->
      <div class="mb-6">
        <label class="block text-sm font-semibold text-gray-700 mb-3">{{ $t('Products.Filters.category') }}</label>
        <div class="space-y-2">
          <label v-for="category in availableCategories" :key="category" class="flex items-center cursor-pointer">
            <input 
              type="checkbox" 
              :value="category"
              :checked="filters.categories.includes(category)"
              @change="toggleCategory(category)"
              class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500"
            />
            <span class="ml-2 text-gray-700">{{ category }}</span>
          </label>
        </div>
      </div>

      <!-- Color Filter -->
      <div class="mb-6">
        <label class="block text-sm font-semibold text-gray-700 mb-3">{{ $t('Products.Filters.color') }}</label>
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
        <label class="block text-sm font-semibold text-gray-700 mb-3">{{ $t('Products.Filters.size') }}</label>
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
        <label class="block text-sm font-semibold text-gray-700 mb-3">{{ $t('Products.Filters.price') }}</label>
        <div class="space-y-3">
          <div>
            <input 
              :value="filters.priceRange[0]"
              @input="updatePriceMin($event.target.value)"
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
            :value="filters.priceRange[1]"
            @input="updatePriceMax($event.target.value)"
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
        @click="$emit('clear-filters')"
        class="w-full bg-gray-200 text-gray-700 py-2 rounded-lg hover:bg-gray-300 transition-colors font-semibold"
      >
        {{ $t('Products.Filters.reset') }}
      </button>
    </div>
  </aside>
</template>

<script setup>
const props = defineProps({
  filters: {
    type: Object,
    required: true
  },
  availableBrands: {
    type: Array,
    default: () => []
  },
  availableCategories: {
    type: Array,
    default: () => []
  },
  availableColors: {
    type: Array,
    default: () => []
  },
  availableSizes: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['update:filters', 'clear-filters']);

const toggleBrand = (brand) => {
  const brands = [...props.filters.brands];
  const index = brands.indexOf(brand);
  if (index > -1) {
    brands.splice(index, 1);
  } else {
    brands.push(brand);
  }
  emit('update:filters', { ...props.filters, brands });
};

const toggleCategory = (category) => {
  const categories = [...props.filters.categories];
  const index = categories.indexOf(category);
  if (index > -1) {
    categories.splice(index, 1);
  } else {
    categories.push(category);
  }
  emit('update:filters', { ...props.filters, categories });
};

const toggleColor = (color) => {
  const colors = [...props.filters.colors];
  const index = colors.indexOf(color);
  if (index > -1) {
    colors.splice(index, 1);
  } else {
    colors.push(color);
  }
  emit('update:filters', { ...props.filters, colors });
};

const toggleSize = (size) => {
  const sizes = [...props.filters.sizes];
  const index = sizes.indexOf(size);
  if (index > -1) {
    sizes.splice(index, 1);
  } else {
    sizes.push(size);
  }
  emit('update:filters', { ...props.filters, sizes });
};

const updatePriceMin = (value) => {
  emit('update:filters', { 
    ...props.filters, 
    priceRange: [Number(value), props.filters.priceRange[1]] 
  });
};

const updatePriceMax = (value) => {
  emit('update:filters', { 
    ...props.filters, 
    priceRange: [props.filters.priceRange[0], Number(value)] 
  });
};

const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};
</script>
