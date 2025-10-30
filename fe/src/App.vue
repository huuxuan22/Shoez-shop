<template>
  <router-view />
  <ToastManager />
  <ReviewPromptBanner />
</template>

<script setup>
import { onMounted } from 'vue'
import ToastManager from '@/components/shared/ToastManager.vue'
import ReviewPromptBanner from '@/components/reviews/ReviewPromptBanner.vue'
import { useAuthStore } from '@/stores/auth'
import { useFavouriteStore } from '@/stores/favourite'

// Load favourites when app starts (if user is logged in)
onMounted(async () => {
  const authStore = useAuthStore()
  const favouriteStore = useFavouriteStore()
  
  // Wait for auth to initialize
  if (authStore.isAuthenticated && authStore.user) {
    try {
      const userId = authStore.user._id || authStore.user.id
      if (userId) {
        await favouriteStore.fetchFavourites(userId)
        console.log('[App] Loaded favourites on mount:', favouriteStore.favourites.length)
      }
    } catch (error) {
      console.error('[App] Error loading favourites on mount:', error)
    }
  }
})
</script>
