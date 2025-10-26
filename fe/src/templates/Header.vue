<template>
  <header class="bg-white shadow-md sticky top-0 z-50">
    <nav class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <router-link to="/" class="text-2xl font-bold text-black hover:text-gray-700 transition-colors font-alasassy">
          EzShopping
        </router-link>

        <!-- Navigation Menu -->
        <div class="hidden md:flex items-center space-x-6">
          <!-- Navigation Menu -->
          <div class="hidden md:flex items-center space-x-6">
            <router-link to="/"
              class="flex items-center space-x-1 text-gray-800 hover:text-black transition-colors font-medium"
              :class="{ 'text-black font-bold': $route.name === 'Home' }">
              <img src="@/assets/icons/home.png" alt="Trang chủ" class="w-5 h-5">
              <span>Trang chủ</span>
            </router-link>
            <router-link to="/products"
              class="flex items-center space-x-1 text-gray-800 hover:text-black transition-colors font-medium"
              :class="{ 'text-black font-bold': $route.name === 'Products' }">
              <img src="@/assets/icons/product.png" alt="Sản phẩm" class="w-5 h-5">
              <span>Sản phẩm</span>
            </router-link>
            <router-link to="/about"
              class="flex items-center space-x-1 text-gray-800 hover:text-black transition-colors font-medium"
              :class="{ 'text-black font-bold': $route.name === 'About' }">
              <img src="@/assets/icons/about.png" alt="Về chúng tôi" class="w-5 h-5">
              <span>Về chúng tôi</span>
            </router-link>
            <router-link to="/contact"
              class="flex items-center space-x-1 text-gray-800 hover:text-black transition-colors font-medium"
              :class="{ 'text-black font-bold': $route.name === 'Contact' }">
              <img src="@/assets/icons/contact.png" alt="Liên hệ" class="w-5 h-5">
              <span>Liên hệ</span>
            </router-link>
          </div>
        </div>

        <!-- User Actions -->
        <div class="flex items-center space-x-4">
          <!-- My Orders Button -->
          <router-link to="/orders" class="relative text-gray-800 hover:text-black transition-colors p-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span v-if="orderCount > 0"
              class="absolute -top-1 -right-1 bg-orange-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ orderCount > 9 ? '9+' : orderCount }}
            </span>
          </router-link>

          <!-- Cart Icon -->
          <router-link to="/cart" class="relative text-gray-800 hover:text-black transition-colors p-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.5 6M7 13l-1.5 6m0 0h9m-9 0h9m0 0l1.5-6M7 13h10" />
            </svg>
            <span v-if="cartItemCount > 0"
              class="absolute -top-1 -right-1 bg-black text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ cartItemCount > 9 ? '9+' : cartItemCount }}
            </span>
          </router-link>

          <!-- Notification Bell -->
          <NotificationBell />

          <!-- Auth Links -->
          <div v-if="!isAuthenticated" class="flex items-center space-x-2">
            <!-- Auth Links -->
            <div v-if="!isAuthenticated" class="flex items-center space-x-2">
              <router-link to="/login" class="text-gray-800 hover:text-black transition-colors font-medium">
                Đăng nhập
              </router-link>
              <span class="text-gray-400">|</span>
              <router-link to="/register"
                class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors font-medium">
                Đăng ký
              </router-link>
            </div>
          </div>

          <!-- User Menu (when logged in) -->
          <div v-else class="relative">
            <button @click="toggleUserMenu"
              class="flex items-center space-x-3 text-gray-800 hover:text-black transition-colors font-medium p-2">
              <!-- User Avatar -->
              <div class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center overflow-hidden">
                <img v-if="userAvatar" :src="userAvatar" :alt="userName" class="w-full h-full object-cover">
                <span v-else class="text-sm font-semibold text-gray-600">
                  {{ getUserInitials(userName) }}
                </span>
              </div>

              <div class="text-left">
                <span class="block text-sm font-medium">Xin chào, {{ userName }}</span>
                <span class="block text-xs text-gray-500">Tài khoản của tôi</span>
              </div>

              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Dropdown Menu -->
            <div v-if="showUserMenu"
              class="absolute right-0 mt-2 w-56 bg-white rounded-lg shadow-lg py-2 border border-gray-200 z-50">
              <router-link to="/profile" class="flex items-center px-4 py-2 text-gray-800 hover:bg-gray-100 font-medium"
                @click="closeMenus">
                <svg class="w-4 h-4 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                Hồ sơ cá nhân
              </router-link>

              <router-link to="/orders" class="flex items-center px-4 py-2 text-gray-800 hover:bg-gray-100 font-medium"
                @click="closeMenus">
                <svg class="w-4 h-4 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
                Đơn hàng của tôi
                <span v-if="orderCount > 0" class="ml-auto bg-orange-500 text-white text-xs px-2 py-1 rounded-full">
                  {{ orderCount }}
                </span>
              </router-link>

              <div class="border-t border-gray-200 my-2"></div>

              <button @click="handleLogout"
                class="flex items-center w-full text-left px-4 py-2 text-gray-800 hover:bg-gray-100 font-medium">
                <svg class="w-4 h-4 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                Đăng xuất
              </button>
            </div>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="toggleMobileMenu" class="md:hidden text-gray-800 hover:text-black">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="showMobileMenu" class="md:hidden mt-4 pb-4 border-t border-gray-200">
        <!-- Mobile Menu -->
        <div v-if="showMobileMenu" class="md:hidden mt-4 pb-4 border-t border-gray-200">
          <div class="flex flex-col space-y-4 pt-4">
            <router-link to="/"
              class="flex items-center space-x-2 text-gray-800 hover:text-black transition-colors font-medium"
              @click="closeMenus" :class="{ 'text-black font-bold': $route.name === 'Home' }">
              <img :src="home" alt="Trang chủ" class="w-5 h-5">
              <span>Trang chủ</span>
            </router-link>
            <router-link to="/products"
              class="flex items-center space-x-2 text-gray-800 hover:text-black transition-colors font-medium"
              @click="closeMenus" :class="{ 'text-black font-bold': $route.name === 'Products' }">
              <img :src="home" alt="Sản phẩm" class="w-5 h-5">
              <span>Sản phẩm</span>
            </router-link>
            <router-link to="/about"
              class="flex items-center space-x-2 text-gray-800 hover:text-black transition-colors font-medium"
              @click="closeMenus" :class="{ 'text-black font-bold': $route.name === 'About' }">
              <img :src="home" alt="Về chúng tôi" class="w-5 h-5">
              <span>Về chúng tôi</span>
            </router-link>
            <router-link to="/contact"
              class="flex items-center space-x-2 text-gray-800 hover:text-black transition-colors font-medium"
              @click="closeMenus" :class="{ 'text-black font-bold': $route.name === 'Contact' }">
              <img :src="home" alt="Liên hệ" class="w-5 h-5">
              <span>Liên hệ</span>
            </router-link>

            <!-- Mobile Auth Links -->
            <div v-if="!isAuthenticated" class="flex flex-col space-y-2 pt-4 border-t border-gray-200">
              <router-link to="/login" class="text-gray-800 hover:text-black transition-colors font-medium"
                @click="closeMenus">
                Đăng nhập
              </router-link>
              <router-link to="/register"
                class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors font-medium text-center"
                @click="closeMenus">
                Đăng ký
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import home from "@/assets/icons/home.png"
import { useAuthStore } from '@/stores/auth';
import NotificationBell from '@/components/shared/NotificationBell.vue';

const router = useRouter();
const authStore = useAuthStore();

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

const userAvatar = computed(() => {
  const user = localStorage.getItem('user');
  if (user) {
    try {
      return JSON.parse(user).avatar || null;
    } catch (e) {
      return null;
    }
  }
  return null;
});

const cartItemCount = computed(() => {
  // This would come from a cart store in a real app
  const cart = JSON.parse(localStorage.getItem('cart') || '[]');
  return cart.reduce((total, item) => total + item.quantity, 0);
});

const orderCount = computed(() => {
  // This would come from an order store in a real app
  const orders = JSON.parse(localStorage.getItem('orders') || '[]');
  return orders.filter(order => order.status === 'pending').length;
});

// Methods
const getUserInitials = (name) => {
  return name.split(' ').map(n => n[0]).join('').toUpperCase();
};

const toggleUserMenu = () => {
  showUserMenu.value = !showUserMenu.value;
  showMobileMenu.value = false;
};

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value;
  showUserMenu.value = false;
};

const closeMenus = () => {
  showUserMenu.value = false;
  showMobileMenu.value = false;
};

const handleLogout = async () => {
  await authStore.logout()
  closeMenus();
  router.push('/login');
};

const handleClickOutside = (e) => {
  if (!e.target.closest('.relative')) {
    showUserMenu.value = false;
  }
  if (!e.target.closest('nav')) {
    showMobileMenu.value = false;
  }
};

// Lifecycle
onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Alatsi&display=swap');

.font-alasassy {
  font-family: 'Alatsi', sans-serif;
  letter-spacing: 0.5px;
}
</style>