<template>
  <router-view />
  <ToastManager />
  <ReviewPromptBanner />
</template>

<script setup>
import ToastManager from '@/components/shared/ToastManager.vue'
import ReviewPromptBanner from '@/components/reviews/ReviewPromptBanner.vue'
</script>
