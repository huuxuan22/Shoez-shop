<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="text-center">
      <h1 class="text-9xl font-bold text-gray-300">404</h1>
      <h2 class="text-3xl font-semibold text-gray-800 mt-4">Trang không tồn tại</h2>
      <p class="text-gray-600 mt-2 mb-8">Xin lỗi, trang bạn tìm kiếm không tồn tại.</p>
      <router-link 
        to="/" 
        class="inline-block bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors"
      >
        Về trang chủ
      </router-link>
    </div>
  </div>
</template>

<script setup>
// 404 Not Found page
</script>