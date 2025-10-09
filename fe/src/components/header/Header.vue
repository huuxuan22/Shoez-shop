<template>
    <header class="bg-white border-b border-gray-200">
      <div class="container mx-auto px-4">
        <!-- Top bar với search và utilities -->
        <div class="flex items-center justify-between py-3">
          <!-- Logo -->
          <div class="flex-shrink-0">
            <h1 class="text-2xl font-bold text-gray-900">d e Ko r</h1>
          </div>
  
          <!-- Search Bar -->
          <SearchBar class="flex-1 max-w-2xl mx-8" />
  
          <!-- Utilities -->
          <div class="flex items-center space-x-4">
            <button class="p-2 text-gray-600 hover:text-gray-900">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </button>
            <button class="p-2 text-gray-600 hover:text-gray-900">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </button>
          </div>
        </div>
  
        <!-- Navigation -->
        <Navigation />
      </div>
    </header>
  </template>
  
  <script setup>
  import Navigation from './Navigation.vue'
  import SearchBar from './SearchBar.vue'
  </script>