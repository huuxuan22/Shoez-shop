<template>
  <div class="bg-white rounded-lg shadow-md p-4 mb-6 flex flex-wrap items-center justify-between gap-4">
    <!-- Sort Dropdown -->
    <div class="flex items-center gap-2">
      <span class="text-gray-700 font-semibold">Sắp xếp:</span>
      <select 
        :value="sortBy"
        @change="$emit('update:sortBy', $event.target.value)"
        class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      >
        <option value="default">Mặc định</option>
        <option value="price-asc">Giá: Thấp đến cao</option>
        <option value="price-desc">Giá: Cao đến thấp</option>
        <option value="name-asc">Tên: A-Z</option>
        <option value="name-desc">Tên: Z-A</option>
      </select>
    </div>

    <!-- View Mode Toggle -->
    <div class="flex gap-2">
      <button 
        @click="$emit('update:viewMode', 'grid')"
        :class="[
          'p-2 rounded-lg transition-colors',
          viewMode === 'grid' ? 'bg-black text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
        ]"
        title="Xem dạng lưới"
      >
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
          <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
        </svg>
      </button>
      <button 
        @click="$emit('update:viewMode', 'list')"
        :class="[
          'p-2 rounded-lg transition-colors',
          viewMode === 'list' ? 'bg-black text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
        ]"
        title="Xem dạng danh sách"
      >
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  sortBy: {
    type: String,
    default: 'default'
  },
  viewMode: {
    type: String,
    default: 'grid',
    validator: (value) => ['grid', 'list'].includes(value)
  }
});

const emit = defineEmits(['update:sortBy', 'update:viewMode']);
</script>
