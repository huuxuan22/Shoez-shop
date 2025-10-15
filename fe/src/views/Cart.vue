<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Giỏ hàng</h1>
    <div class="bg-white rounded-lg shadow p-6">
      <p class="text-gray-600">Giỏ hàng của bạn đang trống</p>
      <router-link 
        to="/products" 
        class="inline-block mt-4 bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
      >
        Tiếp tục mua sắm
      </router-link>
    </div>
  </div>
</template>

<script setup>
// Cart functionality will be implemented later
</script>