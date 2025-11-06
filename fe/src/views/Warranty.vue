<template>
  <Header />
  <div class="max-w-5xl mx-auto mt-12 pb-16">
    <div class="max-w-5xl mx-auto mt-12 pb-16">
      <div class="bg-white text-gray-900 rounded-xl shadow-md border p-8">
      <h1 class="text-3xl font-extrabold">{{ $t('Views.Warranty.title') }}</h1>
      <p class="mt-2 text-gray-700 max-w-2xl">{{ $t('Views.Warranty.subtitle') }}</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
      <div class="bg-white rounded-lg shadow-md border p-6">
        <h3 class="text-xl font-semibold mb-3">{{ $t('Views.Warranty.termsTitle') }}</h3>
        <p class="text-gray-700 mb-2">{{ $t('Views.Warranty.termsDesc') }}</p>
        <ul class="list-disc ml-6 text-gray-700">
          <li>{{ $t('Views.Warranty.terms1') }}</li>
          <li>{{ $t('Views.Warranty.terms2') }}</li>
          <li>{{ $t('Views.Warranty.terms3') }}</li>
        </ul>
      </div>

  <div class="bg-white rounded-lg shadow-md border p-6">
        <h3 class="text-xl font-semibold mb-3">{{ $t('Views.Warranty.notCoveredTitle') }}</h3>
        <ul class="list-disc ml-6 text-gray-700">
          <li>{{ $t('Views.Warranty.notCovered1') }}</li>
          <li>{{ $t('Views.Warranty.notCovered2') }}</li>
          <li>{{ $t('Views.Warranty.notCovered3') }}</li>
        </ul>
      </div>
    </div>

  <div class="bg-white rounded-lg shadow-md border p-6 mt-6">
      <h3 class="text-2xl font-semibold mb-4">{{ $t('Views.Warranty.processTitle') }}</h3>
      <ol class="list-decimal ml-6 space-y-2 text-gray-700">
        <li>{{ $t('Views.Warranty.process1') }}</li>
        <li>{{ $t('Views.Warranty.process2') }}</li>
        <li>{{ $t('Views.Warranty.process3') }}</li>
      </ol>
    </div>

    <div class="mt-6 text-right">
      <router-link to="/contact" class="inline-block bg-black text-white px-6 py-2 rounded-lg shadow hover:bg-gray-800">{{ $t('Views.Warranty.contactWarranty') }}</router-link>
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
