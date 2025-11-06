<template>
  <Header />
  <div class="max-w-5xl mx-auto mt-12 pb-16">
  <div class="bg-white text-gray-900 rounded-xl shadow-md border p-8">
      <h1 class="text-3xl font-extrabold mb-4">{{ $t('Views.PurchaseGuide.title') }}</h1>
      <p class="text-gray-700 mb-6">{{ $t('Views.PurchaseGuide.subtitle') }}</p>

      <div class="grid gap-6 md:grid-cols-3">
        <div class="p-4 border rounded-lg shadow-md bg-white transition">
          <div class="text-indigo-600 text-2xl mb-3">🛒</div>
          <h3 class="font-semibold mb-2">{{ $t('Views.PurchaseGuide.step1Title') }}</h3>
          <p class="text-gray-700 text-sm">{{ $t('Views.PurchaseGuide.step1Desc') }}</p>
        </div>
        <div class="p-4 border rounded-lg shadow-md bg-white transition">
          <div class="text-green-600 text-2xl mb-3">💳</div>
          <h3 class="font-semibold mb-2">{{ $t('Views.PurchaseGuide.step2Title') }}</h3>
          <p class="text-gray-700 text-sm">{{ $t('Views.PurchaseGuide.step2Desc') }}</p>
        </div>
        <div class="p-4 border rounded-lg shadow-md bg-white transition">
          <div class="text-blue-600 text-2xl mb-3">📦</div>
          <h3 class="font-semibold mb-2">{{ $t('Views.PurchaseGuide.step3Title') }}</h3>
          <p class="text-gray-700 text-sm">{{ $t('Views.PurchaseGuide.step3Desc') }}</p>
        </div>
      </div>

  <div class="mt-6 bg-gray-50 border rounded-lg shadow-md p-4">
        <h3 class="font-semibold mb-2">{{ $t('Views.PurchaseGuide.tipsTitle') }}</h3>
        <ul class="list-disc ml-6 text-gray-700">
          <li>{{ $t('Views.PurchaseGuide.tip1') }}</li>
          <li>{{ $t('Views.PurchaseGuide.tip2') }}</li>
        </ul>
      </div>

      <div class="mt-6 text-right">
        <router-link to="/contact" class="inline-block bg-black text-white px-6 py-2 rounded-lg shadow hover:bg-gray-800">{{ $t('Views.PurchaseGuide.contactSupport') }}</router-link>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script setup>
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
