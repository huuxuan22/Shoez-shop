<template>
  <header class="bg-white shadow-md sticky top-0 z-50">
    <nav class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <router-link to="/" class="text-2xl font-bold text-blue-600 hover:text-blue-700">
          {{ shopTitle }}
        </router-link>

        <!-- Navigation Menu -->
        <div class="hidden md:flex items-center space-x-6">
          <router-link to="/" class="text-gray-700 hover:text-blue-600 transition-colors"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Home' }">
            {{ $t('Header.navigation.home') }}
          </router-link>
          <router-link to="/products" class="text-gray-700 hover:text-blue-600 transition-colors"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Products' }">
            {{ $t('Header.navigation.products') }}
          </router-link>
          <router-link to="/about" class="text-gray-700 hover:text-blue-600 transition-colors"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'About' }">
            {{ $t('Header.navigation.about') }}
          </router-link>
          <router-link to="/contact" class="text-gray-700 hover:text-blue-600 transition-colors"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Contact' }">
            {{ $t('Header.navigation.contact') }}
          </router-link>
        </div>

        <!-- User Actions -->
        <div class="flex items-center space-x-4">
          <!-- Favourite Icon (only show when logged in) -->
          <router-link v-if="isAuthenticated" to="/favourite" class="relative text-gray-700 hover:text-red-500 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
            <!-- Favourite Badge -->
            <span v-if="favouriteCount > 0"
              class="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center font-bold">
              {{ favouriteCount }}
            </span>
          </router-link>

          <!-- Cart Icon -->
          <router-link to="/cart" class="relative text-gray-700 hover:text-blue-600 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.5 6M7 13l-1.5 6m0 0h9m-9 0h9m0 0l1.5-6M7 13h10" />
            </svg>
            <!-- Cart Badge (optional) -->
            <span v-if="cartItemCount > 0"
              class="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ cartItemCount }}
            </span>
          </router-link>

          <!-- Auth Links -->
          <div v-if="!isAuthenticated" class="flex items-center space-x-2">
            <router-link to="/login" class="text-gray-700 hover:text-blue-600 transition-colors">
              {{ $t('Header.navigation.login') }}
            </router-link>
            <span class="text-gray-400">|</span>
            <router-link to="/register"
              class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
              {{ $t('Header.navigation.register') }}
            </router-link>
          </div>

          <!-- User Menu (when logged in) -->
          <div v-else class="relative">
            <button @click="toggleUserMenu"
              class="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition-colors">
              <span>{{ $t('Header.navigation.greeting', { name: userName }) }}</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Dropdown Menu -->
            <div v-if="showUserMenu" class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg py-2 border">
              <router-link to="/profile" class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
                @click="closeMenus">
                {{ $t('Header.navigation.profile') }}
              </router-link>
              <button @click="handleLogout" class="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100">
                {{ $t('Header.navigation.logout') }}
              </button>
            </div>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="toggleMobileMenu" class="md:hidden text-gray-700 hover:text-blue-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="showMobileMenu" class="md:hidden mt-4 pb-4 border-t border-gray-200">
        <div class="flex flex-col space-y-4 pt-4">
          <router-link to="/" class="text-gray-700 hover:text-blue-600 transition-colors"
            @click="closeMenus"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Home' }">
            {{ $t('Header.navigation.home') }}
          </router-link>
          <router-link to="/products" class="text-gray-700 hover:text-blue-600 transition-colors"
            @click="closeMenus"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Products' }">
            {{ $t('Header.navigation.products') }}
          </router-link>
          <router-link to="/about" class="text-gray-700 hover:text-blue-600 transition-colors"
            @click="closeMenus"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'About' }">
            {{ $t('Header.navigation.about') }}
          </router-link>
          <router-link to="/contact" class="text-gray-700 hover:text-blue-600 transition-colors"
            @click="closeMenus"
            :class="{ 'text-blue-600 font-semibold': $route.name === 'Contact' }">
            {{ $t('Header.navigation.contact') }}
          </router-link>
          <router-link v-if="isAuthenticated" to="/favourite" class="text-gray-700 hover:text-red-500 transition-colors"
            @click="closeMenus"
            :class="{ 'text-red-500 font-semibold': $route.name === 'Favourite' }">
            {{ $t('Header.navigation.favourite') }}
          </router-link>
          
          <!-- Mobile Auth Links -->
          <div v-if="!isAuthenticated" class="flex flex-col space-y-2 pt-4 border-t border-gray-200">
            <router-link to="/login" class="text-gray-700 hover:text-blue-600 transition-colors" @click="closeMenus">
              {{ $t('Header.navigation.login') }}
            </router-link>
            <router-link to="/register" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors text-center" @click="closeMenus">
              {{ $t('Header.navigation.register') }}
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useFavouriteStore } from '@/stores/favourite';
import { useI18n } from 'vue-i18n';
import { BrandConstants } from '@/common/enum';

const { t } = useI18n();
const shopTitle = BrandConstants.TITLE_SHOP;

const router = useRouter();
const favouriteStore = useFavouriteStore();

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

const cartItemCount = computed(() => {
  // This would come from a cart store in a real app
  return 0;
});

const favouriteCount = computed(() => {
  return favouriteStore.favourites.length;
});

// Methods
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

const handleLogout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
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

// Load favourites when authenticated
onMounted(async () => {
  document.addEventListener('click', handleClickOutside);
  
  // Load favourites if user is authenticated
  if (isAuthenticated.value) {
    try {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      const userId = user._id || user.id;
      if (userId) {
        await favouriteStore.fetchFavourites(userId);
      }
    } catch (error) {
      console.error('Error loading favourites:', error);
    }
  }
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>