<template>
    <nav class="border-t border-gray-200">
      <ul class="flex items-center justify-center space-x-8 py-4">
        <li v-for="item in navigationItems" :key="item.name" class="relative group">
          <router-link
            v-if="!item.children"
            :to="item.path"
            class="text-gray-700 hover:text-gray-900 font-medium transition-colors duration-200"
            :class="{ 'text-gray-900 font-semibold': $route.path === item.path }"
          >
            {{ item.name }}
          </router-link>
          
          <!-- Dropdown cho SẢN PHẨM -->
          <div v-else class="relative">
            <button
              @click="toggleProducts"
              class="text-gray-700 hover:text-gray-900 font-medium transition-colors duration-200 flex items-center"
              :class="{ 'text-gray-900 font-semibold': isProductsOpen || $route.path.includes('/products') }"
            >
              {{ item.name }}
              <svg 
                class="w-4 h-4 ml-1 transition-transform duration-200" 
                :class="{ 'rotate-180': isProductsOpen }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <!-- Dropdown Menu -->
            <div
              v-show="isProductsOpen"
              class="absolute top-full left-0 mt-2 w-64 bg-white border border-gray-200 rounded-lg shadow-lg z-50"
            >
              <div class="py-2">
                <div 
                  v-for="product in item.children" 
                  :key="product.name"
                  class="px-4 py-3 hover:bg-gray-50 cursor-pointer transition-colors duration-200 border-b border-gray-100 last:border-b-0"
                  @click="navigateToProduct(product)"
                >
                  <div class="flex items-center justify-between">
                    <span class="text-gray-800 font-medium">{{ product.name }}</span>
                    <span v-if="product.promotional" class="text-xs bg-red-500 text-white px-2 py-1 rounded">
                      KM
                    </span>
                  </div>
                  <p v-if="product.description" class="text-sm text-gray-500 mt-1">
                    {{ product.description }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </nav>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const isProductsOpen = ref(false)
  
  const navigationItems = ref([
    { name: 'TRANG CHỦ', path: '/' },
    { name: 'GIỚI THIỆU', path: '/about' },
    { 
      name: 'SẢN PHẨM', 
      path: '/products',
      children: [
        { name: 'Bàn gỗ', path: '/products/ban-go', description: 'Bàn gỗ tự nhiên cao cấp', promotional: false },
        { name: 'Kệ sách', path: '/products/ke-sach', description: 'Kệ sách đa năng', promotional: true },
        { name: 'Rèm cửa', path: '/products/rem-cua', description: 'Rèm cửa vải cao cấp', promotional: false },
        { name: 'Ghế sopha', path: '/products/ghe-sopha', description: 'Ghế sopha phòng khách', promotional: false },
        { name: 'Phòng tắm', path: '/products/phong-tam', description: 'Nội thất phòng tắm', promotional: true },
        { name: 'Tủ quần áo', path: '/products/tu-quan-ao', description: 'Tủ quần áo gỗ óc chó', promotional: false },
        { name: 'Giường ngủ', path: '/products/giuong-ngu', description: 'Giường ngủ thông minh', promotional: true },
        { name: 'Đèn trang trí', path: '/products/den-trang-tri', description: 'Đèn LED trang trí', promotional: false }
      ]
    },
    { name: 'TIN TỨC', path: '/news' },
    { name: 'LIÊN HỆ', path: '/contact' }
  ])
  
  const toggleProducts = () => {
    isProductsOpen.value = !isProductsOpen.value
  }
  
  const navigateToProduct = (product) => {
    router.push(product.path)
    isProductsOpen.value = false
  }
  
  // Đóng dropdown khi click ra ngoài
  const handleClickOutside = (event) => {
    const dropdown = event.target.closest('.relative')
    if (!dropdown) {
      isProductsOpen.value = false
    }
  }
  
  onMounted(() => {
    document.addEventListener('click', handleClickOutside)
  })
  
  onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
  })
  </script>
  
  <style scoped>
  .group:hover .group-hover\:block {
    display: block;
  }
  </style>