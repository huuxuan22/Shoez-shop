<template>
  <div id="app">
    <!-- Header -->
    <header class="bg-white shadow-md sticky top-0 z-50">
      <nav class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <router-link to="/" class="text-2xl font-bold text-blue-600 hover:text-blue-700">
            Shoez Shop
          </router-link>

          <!-- Navigation Menu -->
          <div class="hidden md:flex items-center space-x-6">
            <router-link to="/" class="text-gray-700 hover:text-blue-600 transition-colors"
              :class="{ 'text-blue-600 font-semibold': $route.name === 'Home' }">
              Trang chủ
            </router-link>
            <router-link to="/products" class="text-gray-700 hover:text-blue-600 transition-colors"
              :class="{ 'text-blue-600 font-semibold': $route.name === 'Products' }">
              Sản phẩm
            </router-link>
            <router-link to="/about" class="text-gray-700 hover:text-blue-600 transition-colors"
              :class="{ 'text-blue-600 font-semibold': $route.name === 'About' }">
              Về chúng tôi
            </router-link>
            <router-link to="/contact" class="text-gray-700 hover:text-blue-600 transition-colors"
              :class="{ 'text-blue-600 font-semibold': $route.name === 'Contact' }">
              Liên hệ
            </router-link>
          </div>

          <!-- User Actions -->
          <div class="flex items-center space-x-4">
            <!-- Cart Icon -->
            <router-link 
              to="/cart" 
              class="relative text-gray-700 hover:text-black transition-colors"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </router-link>

            <!-- Auth Links -->
            <div v-if="!isAuthenticated" class="flex items-center space-x-2">
              <router-link to="/login" class="text-gray-700 hover:text-blue-600 transition-colors">
                Đăng nhập
              </router-link>
              <span class="text-gray-400">|</span>
              <router-link to="/register"
                class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                Đăng ký
              </router-link>
            </div>

            <!-- User Menu (when logged in) -->
            <div v-else class="relative">
              <button @click="showUserMenu = !showUserMenu"
                class="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition-colors">
                <span>Xin chào, {{ userName }}</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              <!-- Dropdown Menu -->
              <div v-if="showUserMenu" class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg py-2 border">
                <router-link to="/profile" class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
                  @click="showUserMenu = true">
                  Hồ sơ
                </router-link>
                <button @click="handleLogout" class="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100">
                  Đăng xuất
                </button>
              </div>
            </div>

            <!-- Mobile Menu Button -->
            <button @click="showMobileMenu = !showMobileMenu" class="md:hidden text-gray-700 hover:text-blue-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Mobile Menu -->
      </nav>
    </header>

    <!-- Main Content -->
    <main>
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <!-- Company Info -->
          <div>
            <h3 class="text-xl font-bold mb-4">Shoez Shop</h3>
            <p class="text-gray-300 mb-4">
              Cửa hàng giày thể thao chính hãng với đa dạng thương hiệu nổi tiếng thế giới.
            </p>
            <div class="flex space-x-4">
              <a href="#" class="text-gray-300 hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
                </svg>
              </a>
              <a href="#" class="text-gray-300 hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-semibold mb-4">Liên kết nhanh</h4>
            <ul class="space-y-2">
              <li><router-link to="/" class="text-gray-300 hover:text-white">Trang chủ</router-link></li>
              <li><router-link to="/products" class="text-gray-300 hover:text-white">Sản phẩm</router-link></li>
              <li><router-link to="/about" class="text-gray-300 hover:text-white">Về chúng tôi</router-link></li>
              <li><router-link to="/contact" class="text-gray-300 hover:text-white">Liên hệ</router-link></li>
            </ul>
          </div>

          <!-- Customer Service -->
          <div>
            <h4 class="text-lg font-semibold mb-4">Hỗ trợ khách hàng</h4>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-300 hover:text-white">Chính sách đổi trả</a></li>
              <li><a href="#" class="text-gray-300 hover:text-white">Hướng dẫn mua hàng</a></li>
              <li><a href="#" class="text-gray-300 hover:text-white">Bảo hành sản phẩm</a></li>
              <li><a href="#" class="text-gray-300 hover:text-white">FAQ</a></li>
            </ul>
          </div>

          <!-- Contact Info -->
          <div>
            <h4 class="text-lg font-semibold mb-4">Thông tin liên hệ</h4>
            <div class="space-y-2 text-gray-300">
              <p>📍 123 Đường ABC, Quận 1, TP.HCM</p>
              <p>📞 (028) 1234 5678</p>
              <p>✉️ info@shoezshop.com</p>
              <p>🕒 8:00 - 22:00 (Thứ 2 - Chủ nhật)</p>
            </div>
          </div>
        </div>

        <div class="border-t border-gray-700 mt-8 pt-8 text-center text-gray-300">
          <p>&copy; 2025 Shoez Shop. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Reactive data
const showUserMenu = ref(false);
const showMobileMenu = ref(false);

// Computed properties
const isAuthenticated = computed(() => {
  return !!localStorage.getItem('token');
});

const userName = computed(() => {
  const user = localStorage.getItem('user');
  if (user) {
    try {
      return JSON.parse(user).full_name || 'User';
    } catch (e) {
      return 'User';
    }
  }
  return 'User';
});

// Methods
const handleLogout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
  showUserMenu.value = false;
  router.push('/login');
};

// Close dropdowns when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.relative')) {
    showUserMenu.value = false;
    showMobileMenu.value = false;
  }
});
</script>