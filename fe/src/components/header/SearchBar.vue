<template>
    <div class="relative">
      <input
        type="text"
        placeholder="Tìm kiếm..."
        v-model="searchQuery"
        @input="handleSearch"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-transparent bg-white text-gray-900"
      />
      <div class="absolute right-3 top-1/2 transform -translate-y-1/2">
        <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const searchQuery = ref('')
  
  const handleSearch = () => {
    // Xử lý tìm kiếm
    console.log('Search:', searchQuery.value)
  }
  </script>