<template>
  <aside class="w-64 bg-gray-900 text-white min-h-screen fixed left-0 top-0 overflow-y-auto">
    <!-- Logo -->
    <div class="p-6 border-b border-gray-700">
      <h1 class="text-2xl font-bold">Shoez Admin</h1>
      <p class="text-sm text-gray-400 mt-1">Management Panel</p>
    </div>

    <!-- Navigation -->
    <nav class="p-4 space-y-1">
      <!-- Dashboard -->
      <router-link
        to="/admin"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
        <span class="font-medium">Dashboard</span>
      </router-link>

      <!-- Products -->
      <router-link
        to="/admin/products"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/products') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
        </svg>
        <span class="font-medium">Sản phẩm</span>
      </router-link>

      <!-- Orders -->
      <router-link
        to="/admin/orders"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/orders') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
        <span class="font-medium">Đơn hàng</span>
      </router-link>

      <!-- Customers -->
      <router-link
        to="/admin/customers"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/customers') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <span class="font-medium">Khách hàng</span>
      </router-link>

      <!-- Categories -->
      <router-link
        to="/admin/categories"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/categories') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
        </svg>
        <span class="font-medium">Danh mục</span>
      </router-link>

      <!-- Brands -->
      <router-link
        to="/admin/brands"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/brands') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
        </svg>
        <span class="font-medium">Thương hiệu</span>
      </router-link>

      <!-- Analytics -->
      <router-link
        to="/admin/analytics"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/analytics') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        <span class="font-medium">Thống kê</span>
      </router-link>

      <!-- Settings -->
      <router-link
        to="/admin/settings"
        class="flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors"
        :class="isActive('/admin/settings') ? 'bg-black text-white' : 'text-gray-300 hover:bg-gray-800'"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span class="font-medium">Cài đặt</span>
      </router-link>
    </nav>

    <!-- User Info -->
    <div class="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-700 bg-gray-900">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center">
          <span class="text-sm font-semibold">AD</span>
        </div>
        <div class="flex-1">
          <p class="text-sm font-medium">Admin User</p>
          <p class="text-xs text-gray-400">admin@shoez.com</p>
        </div>
        <button class="text-gray-400 hover:text-white">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
        </button>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();

const isActive = (path) => {
  if (path === '/admin') {
    return route.path === '/admin' || route.path === '/admin/';
  }
  return route.path.startsWith(path);
};
</script>

<style scoped>
/* Custom scrollbar for sidebar */
aside::-webkit-scrollbar {
  width: 6px;
}

aside::-webkit-scrollbar-track {
  background: #1f2937;
}

aside::-webkit-scrollbar-thumb {
  background: #4b5563;
  border-radius: 3px;
}

aside::-webkit-scrollbar-thumb:hover {
  background: #6b7280;
}
</style>
