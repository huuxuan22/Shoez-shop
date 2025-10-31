<template>
  <router-view />
  <ToastManager />
  <ReviewPromptBanner />
  <GlobalLoading />
  <!-- Global contact buttons: appear for logged-in users on every page -->
  <div v-if="showContacts" class="fixed right-5 bottom-24 z-50 flex flex-col items-end gap-4">
    <TikTokContactButton :url="tiktokUrl" />
    <ZaloContactButton :url="zaloUrl" />
  </div>
  <MessengerChatWidget v-if="showContacts" />
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import ToastManager from '@/components/shared/ToastManager.vue'
import ReviewPromptBanner from '@/components/reviews/ReviewPromptBanner.vue'
import { useAuthStore } from '@/stores/auth'
import { useFavouriteStore } from '@/stores/favourite'
import GlobalLoading from '@/components/shared/GlobalLoading.vue'
import ZaloContactButton from '@/components/contact/ZaloContactButton.vue'
import TikTokContactButton from '@/components/contact/TikTokContactButton.vue'
import MessengerChatWidget from '@/components/contact/MessengerChatWidget.vue'
import { useToast } from '@/composables/useToast'
import ReviewService from '@/api-services/ReviewService'

// Load favourites when app starts (if user is logged in)
const router = useRouter()
const { info } = useToast()

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

  // After auth is ready, check if there are pending reviews and guide user
  try {
    if (authStore.isAuthenticated) {
      const pending = await ReviewService.getPending()
      if (Array.isArray(pending) && pending.length > 0) {
        // Try to resolve order id from first pending item
        const first = pending[0] || {}
        const orderId = first.order_id || first.orderId || first.order?.id || first.order?._id
        if (orderId) {
          info('Đơn hàng của bạn đã hoàn thành, vui lòng đánh giá đơn hàng')
          router.push({ path: `/orders/${orderId}`, query: { openReview: '1' } })
        }
      }
    }
  } catch (e) {
    // Silent fail; not critical
    console.warn('[App] pending review check failed:', e)
  }
})

// Show only for authenticated users
const authStore = useAuthStore()
authStore.initializeAuth()
const showContacts = computed(() => authStore.isAuthenticated && !!authStore.user)

// Replace with your real links
const zaloUrl = 'https://zalo.me/your-id-or-qr'
const tiktokUrl = 'https://www.tiktok.com/@your_account'
</script>
