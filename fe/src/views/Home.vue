<template>
  <div>
    <h1>Hahahahah</h1>
      <ProductCategory
      title="SẢN PHẨM"
      :products="allProducts"
    />
  </div>
    
</template>

<script setup>
import ProductCategory from './../components/ProductCategory.vue'

const allProducts = [
  { id: 1, name: 'Bàn gỗ' },
  { id: 2, name: 'Kệ sách' },
  { id: 3, name: 'Rèm cửa' },
  // ...
]

const featuredProducts = [
  { id: 4, name: 'Ghế sopha', featured: true },
  { id: 7, name: 'Giường ngủ', featured: true }
]

const promotionalProducts = [
  { id: 2, name: 'Kệ sách', promotional: true },
  { id: 6, name: 'Tủ quần áo', promotional: true }
]
</script>