<template>
  <section class="py-10">
    <!-- Header -->
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between mb-8">
        <div>
          <h1 class="text-2xl md:text-3xl font-extrabold tracking-tight text-black">Danh sách yêu thích</h1>
          <p class="text-gray-500 mt-1">Các sản phẩm bạn đã đánh dấu trái tim</p>
        </div>
        <router-link
          to="/products"
          class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-black text-white hover:bg-gray-800 transition"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h18M3 9h18M3 15h18M3 21h18" />
          </svg>
          Xem sản phẩm
        </router-link>
      </div>

      <!-- Empty state -->
      <div v-if="favourites.length === 0" class="bg-white rounded-2xl border border-gray-200 p-12 text-center shadow-sm">
        <div class="mx-auto w-20 h-20 rounded-full bg-red-50 flex items-center justify-center mb-4">
          <svg class="w-10 h-10 text-red-500" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
          </svg>
        </div>
        <h3 class="text-lg font-semibold text-black">Bạn chưa có sản phẩm yêu thích nào</h3>
        <p class="text-gray-500 mt-1">Hãy khám phá và nhấn trái tim để lưu sản phẩm bạn thích</p>
        <router-link
          to="/products"
          class="mt-6 inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-black text-white hover:bg-gray-800 transition"
        >
          Bắt đầu mua sắm
        </router-link>
      </div>

      <!-- Grid -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <article
          v-for="item in favourites"
          :key="item._id || item.id"
          class="group bg-white rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition"
        >
          <div class="relative aspect-square bg-gray-50">
            <img :src="item.images?.[0] || item.image" :alt="item.name" class="w-full h-full object-cover" />
            <button
              @click="removeFavourite(item._id || item.id)"
              class="absolute top-3 right-3 w-10 h-10 rounded-full bg-white/90 hover:bg-white shadow flex items-center justify-center"
              title="Xóa khỏi yêu thích"
            >
              <svg class="w-6 h-6 text-red-600" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.1 21.35l-.1.1-.1-.1C7.14 17.24 4 14.39 4 10.5 4 8 6 6 8.5 6c1.54 0 3.04.99 3.57 2.36h.87C13.46 6.99 14.96 6 16.5 6 19 6 21 8 21 10.5c0 3.89-3.14 6.74-8.9 10.85z" />
              </svg>
            </button>
          </div>
          <div class="p-4">
            <p class="text-xs text-gray-500 uppercase tracking-wide">{{ item.brand }}</p>
            <h3 class="mt-1 text-base font-semibold text-black line-clamp-1">{{ item.name }}</h3>
            <div class="mt-2 flex items-center justify-between">
              <p class="text-lg font-bold text-black">{{ formatPrice(item.price) }}</p>
              <router-link :to="`/products/${item._id || item.id}`" class="text-sm text-black hover:underline">Chi tiết</router-link>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useFavouriteStore } from '@/stores/favourite'
import { onMounted } from 'vue'
const favouriteStore = useFavouriteStore()
import { useAuthStore } from '@/stores/auth'
const { favourites, fetchFavourites, removeFavourite } = favouriteStore

onMounted(() => {
  const auth = useAuthStore()
  const uid = auth.user?._id || auth.user?.id
  fetchFavourites(uid)
})

const formatPrice = (price) => new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price || 0)
</script>

<style scoped>
</style>
