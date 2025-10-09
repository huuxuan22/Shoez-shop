<template>
    <div class="product-category">
      <h3 
        v-if="title" 
        class="text-lg font-semibold text-gray-900 mb-3"
      >
        {{ title }}
      </h3>
      
      <div class="product-list">
        <div
          v-for="product in products"
          :key="product.id"
          class="product-item"
          :class="{
            'border-gray-300': !product.featured,
            'border-gray-700': product.featured,
            'opacity-50': product.disabled
          }"
        >
          <span class="product-name">{{ product.name }}</span>
          <span 
            v-if="product.promotional" 
            class="promotional-badge"
          >
            KM
          </span>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    title: {
      type: String,
      default: ''
    },
    products: {
      type: Array,
      default: () => []
    }
  })
  </script>
  
  <style scoped>
  .product-category {
    padding: 16px;
  }
  
  .product-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .product-item {
    border: 1px solid;
    border-radius: 6px;
    padding: 8px 12px;
    background: white;
    position: relative;
    transition: all 0.2s ease;
  }
  
  .product-item:hover {
    background: #f9fafb;
  }
  
  .product-name {
    color: #111827;
    font-size: 14px;
  }
  
  .promotional-badge {
    position: absolute;
    top: 4px;
    right: 8px;
    background: #dc2626;
    color: white;
    font-size: 10px;
    padding: 1px 4px;
    border-radius: 4px;
  }
  </style>