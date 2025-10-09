<template>
    <footer class="bg-gray-900 text-white">
      <div class="container mx-auto px-4 py-12">
        <!-- Main Footer Content -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          <!-- Column 1: Giới thiệu -->
          <div class="lg:col-span-2">
            <h3 class="text-xl font-bold mb-4">GIỚI THIỆU</h3>
            <p class="text-gray-300 leading-relaxed mb-4">
              Đến với Delvor, bạn hoàn toàn yên tâm để chọn được cho mình một bộ giày phù hợp nhất, 
              kết hợp đầy đủ, hài hòa các yếu tố về màu sắc, kiểu dáng, kích thước để làm cho phong cách 
              của bạn trở nên ấn tượng hơn!
            </p>
            
            <!-- Địa chỉ liên hệ -->
            <div class="mt-6">
              <h4 class="font-semibold mb-3">ĐỊA CHỈ LIÊN HỆ</h4>
              <div class="space-y-2 text-gray-300">
                <p class="flex items-center">
                  <MapPinIcon class="w-5 h-5 mr-2" />
                  Tầng 6, 266 Đội Cẩn, Hà Nội
                </p>
                <p class="flex items-center">
                  <PhoneIcon class="w-5 h-5 mr-2" />
                  1900 6750
                </p>
                <p class="flex items-center">
                  <EnvelopeIcon class="w-5 h-5 mr-2" />
                  hellocalcin@gmail.com
                </p>
              </div>
            </div>
          </div>
  
          <!-- Column 2: Tin mới -->
          <div>
            <h3 class="text-xl font-bold mb-4">TIN MỚI</h3>
            <div class="space-y-4">
              <div 
                v-for="news in newsList" 
                :key="news.id"
                class="border-b border-gray-700 pb-4 last:border-b-0 last:pb-0"
              >
                <a href="#" class="hover:text-gray-300 transition-colors">
                  <h4 class="font-medium mb-1">{{ news.title }}</h4>
                  <p class="text-gray-400 text-sm">{{ news.date }}</p>
                </a>
              </div>
            </div>
          </div>
  
          <!-- Column 3: Facebook -->
          <div>
            <h3 class="text-xl font-bold mb-4">FACEBOOK</h3>
            <div class="bg-gray-800 rounded-lg p-4 mb-4">
              <!-- Facebook Page Placeholder -->
              <div class="aspect-w-16 aspect-h-9 bg-gray-700 rounded flex items-center justify-center">
                <div class="text-center text-gray-400">
                  <svg class="w-8 h-8 mx-auto mb-2" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                  <p class="text-sm">Theo dõi chúng tôi trên Facebook</p>
                </div>
              </div>
            </div>
            
            <!-- Copyright -->
            <div class="text-gray-400 text-sm">
              <p>Sapo ©</p>
              <p class="mt-1">9 giờ trước</p>
            </div>
          </div>
        </div>
  
        <!-- Bottom Bar -->
        <div class="border-t border-gray-700 mt-8 pt-6 text-center text-gray-400">
          <p>&copy; 2024 Delvor. Tất cả quyền được bảo lưu.</p>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  // Icons components
  const MapPinIcon = { template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>' }
  const PhoneIcon = { template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>' }
  const EnvelopeIcon = { template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>' }
  
  const newsList = ref([
    { id: 1, title: 'Bí quyết bảo quản giày da', date: '07/11/2015' },
    { id: 2, title: 'Kinh nghiệm mua, bảo quản giày thể thao', date: '07/11/2015' },
    { id: 3, title: 'Chọn giày phù hợp, cần tránh những gì?', date: '07/11/2015' }
  ])
  </script>
  
  <style scoped>
  .aspect-w-16 {
    position: relative;
  }
  
  .aspect-w-16::before {
    content: "";
    display: block;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
  }
  
  .aspect-w-16 > * {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
  }
  </style>