<template>
  <HeaderTemplate />
  <section class="py-10">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between mb-6">
        <h1 class="text-2xl md:text-3xl font-bold tracking-tight">Sản phẩm yêu thích</h1>
        <router-link to="/products" class="hidden sm:inline-flex items-center gap-2 bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
          Mua sắm ngay
        </router-link>
      </div>

      <!-- Empty state -->
      <div v-if="!loading && favourites.length === 0" class="flex flex-col items-center justify-center text-center bg-white rounded-2xl border border-gray-200 p-10">
        <div class="w-24 h-24 rounded-full bg-pink-50 flex items-center justify-center mb-4">
          <svg class="w-12 h-12 text-pink-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12.1 21.35l-.1.1-.1-.1C7.14 17.24 4 14.39 4 10.5 4 8 6 6 8.5 6c1.54 0 3.04.99 3.57 2.36h.87C13.46 6.99 14.96 6 16.5 6 19 6 21 8 21 10.5c0 3.89-3.14 6.74-8.9 10.85z"/></svg>
        </div>
        <h2 class="text-xl font-semibold mb-2">Bạn chưa có sản phẩm yêu thích</h2>
        <p class="text-gray-500 mb-6">Hãy thêm vài sản phẩm để tiện xem lại và mua nhanh hơn.</p>
        <router-link to="/products" class="inline-flex items-center gap-2 bg-black text-white px-5 py-2.5 rounded-lg hover:bg-gray-800 transition">
          Khám phá sản phẩm
        </router-link>
      </div>

      <!-- Loading skeleton -->
      <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="n in 6" :key="n" class="animate-pulse">
          <div class="aspect-square rounded-xl bg-gray-100"></div>
          <div class="mt-4 h-4 bg-gray-100 rounded w-2/3"></div>
          <div class="mt-2 h-4 bg-gray-100 rounded w-1/3"></div>
        </div>
      </div>

      <!-- Favourites grid -->
      <div v-else-if="favourites.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <article
          v-for="item in favourites"
          :key="item._id || item.id"
          class="group bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="relative aspect-square bg-gray-50">
            <img :src="item.images?.[0] || item.image" :alt="item.name" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform" />
            <button
              @click="removeFavourite(item._id || item.id)"
              class="absolute top-3 right-3 w-10 h-10 rounded-full bg-white/95 hover:bg-white shadow flex items-center justify-center"
              title="Xóa khỏi yêu thích">
              <svg class="w-6 h-6 text-red-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12.1 21.35l-.1.1-.1-.1C7.14 17.24 4 14.39 4 10.5 4 8 6 6 8.5 6c1.54 0 3.04.99 3.57 2.36h.87C13.46 6.99 14.96 6 16.5 6 19 6 21 8 21 10.5c0 3.89-3.14 6.74-8.9 10.85z"/></svg>
            </button>
          </div>
          <div class="p-4">
            <p class="text-xs text-gray-500 uppercase tracking-wide">{{ item.brand }}</p>
            <h3 class="mt-1 text-base font-semibold text-black line-clamp-2 min-h-[44px]">{{ item.name }}</h3>
            <div class="mt-3 flex items-center justify-between">
              <p class="text-lg font-bold text-black">{{ formatPrice(item.price) }}</p>
              <router-link :to="`/products/${item._id || item.id}`" class="text-sm font-medium text-black/80 hover:text-black">Chi tiết</router-link>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
  <Footer />
</template>

<script setup>
import HeaderTemplate from '@/templates/Header.vue'
import Footer from '@/templates/Footer.vue'
import { useFavouriteStore } from '@/stores/favourite'
import { useAuthStore } from '@/stores/auth'
import { onMounted, ref } from 'vue'

const favouriteStore = useFavouriteStore()
const { favourites, fetchFavourites, removeFavourite } = favouriteStore
const loading = ref(true)

onMounted(async () => {
  const auth = useAuthStore()
  const uid = auth.user?._id || auth.user?.id
  
  // Check if favourites are already loaded
  if (favourites.length > 0) {
    console.log('[Favourite.vue] Favourites already loaded:', favourites.length)
    loading.value = false
    return
  }
  
  // Otherwise fetch from server
  await fetchFavourites(uid)
  loading.value = false
})

const formatPrice = (price) => new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price || 0)
</script>

<style scoped>
</style>
