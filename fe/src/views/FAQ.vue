<template>
  <Header />
  <div class="max-w-5xl mx-auto mt-12 pb-16">
    <div class="max-w-5xl mx-auto mt-12 pb-16">
      <div class="bg-white text-gray-900 rounded-xl shadow-md border p-8">
      <h1 class="text-3xl font-extrabold mb-4">{{ $t('Views.FAQ.title') }}</h1>
      <p class="text-gray-700 mb-6">{{ $t('Views.FAQ.subtitle') }}</p>

      <div class="space-y-6">
        <div class="bg-gray-50 border rounded-lg shadow-md bg-white p-6">
          <h3 class="font-semibold text-lg">1. {{ $t('Views.FAQ.q1') }}</h3>
          <p class="text-gray-700 mt-2">{{ $t('Views.FAQ.a1') }}</p>
        </div>

  <div class="bg-gray-50 border rounded-lg shadow-md bg-white p-6">
          <h3 class="font-semibold text-lg">2. {{ $t('Views.FAQ.q2') }}</h3>
          <p class="text-gray-700 mt-2">{{ $t('Views.FAQ.a2') }}</p>
        </div>

  <div class="bg-gray-50 border rounded-lg shadow-md bg-white p-6">
          <h3 class="font-semibold text-lg">3. {{ $t('Views.FAQ.q3') }}</h3>
          <p class="text-gray-700 mt-2">{{ $t('Views.FAQ.a3') }}</p>
        </div>

        <div class="bg-gray-50 border rounded-lg p-6">
          <h3 class="font-semibold text-lg">4. {{ $t('Views.FAQ.q4') }}</h3>
          <p class="text-gray-700 mt-2">{{ $t('Views.FAQ.a4') }}</p>
        </div>

        <div class="text-right">
          <router-link to="/contact" class="inline-block bg-black text-white px-6 py-2 rounded-lg shadow hover:bg-gray-800">{{ $t('Views.FAQ.contactSupport') }}</router-link>
        </div>
      </div>
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
