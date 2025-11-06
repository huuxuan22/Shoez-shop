<template>
  <Header />
  <div class="max-w-5xl mx-auto mt-12 pb-16">
    <div class="bg-white text-gray-900 rounded-xl p-8 shadow-md border">
      <h1 class="text-4xl font-extrabold">{{ $t('Views.ReturnPolicy.title') }}</h1>
      <p class="mt-2 text-gray-700 max-w-2xl">{{ $t('Views.ReturnPolicy.subtitle') }}</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-8">
      <div class="bg-white rounded-lg shadow-md border p-6">
        <h3 class="text-xl font-semibold mb-3">{{ $t('Views.ReturnPolicy.conditionsTitle') }}</h3>
        <ul class="space-y-2 text-gray-700">
          <li>• {{ $t('Views.ReturnPolicy.condition1') }}</li>
          <li>• {{ $t('Views.ReturnPolicy.condition2') }}</li>
          <li>• {{ $t('Views.ReturnPolicy.condition3') }}</li>
        </ul>
      </div>

  <div class="bg-white rounded-lg shadow-md border p-6">
        <h3 class="text-xl font-semibold mb-3">{{ $t('Views.ReturnPolicy.processTitle') }}</h3>
        <ol class="list-decimal ml-5 space-y-2 text-gray-700">
          <li>{{ $t('Views.ReturnPolicy.process1') }}</li>
          <li>{{ $t('Views.ReturnPolicy.process2') }}</li>
          <li>{{ $t('Views.ReturnPolicy.process3') }}</li>
        </ol>
      </div>

  <div class="bg-white rounded-lg shadow-md border p-6">
        <h3 class="text-xl font-semibold mb-3">{{ $t('Views.ReturnPolicy.refundTitle') }}</h3>
        <p class="text-gray-700 mb-2">{{ $t('Views.ReturnPolicy.refundDesc') }}</p>
        <p class="text-gray-600 text-sm">{{ $t('Views.ReturnPolicy.refundNote') }}</p>
      </div>
    </div>

  <div class="bg-white rounded-lg shadow-md border p-6 mt-6">
      <h3 class="text-2xl font-semibold mb-4">{{ $t('Views.ReturnPolicy.guideTitle') }}</h3>
      <div class="prose max-w-none text-gray-700">
        <p>1. {{ $t('Views.ReturnPolicy.guide1') }} <router-link to="/contact" class="text-blue-600 underline">{{ $t('Views.ReturnPolicy.contact') }}</router-link></p>
        <p>2. {{ $t('Views.ReturnPolicy.guide2') }}</p>
        <p>3. {{ $t('Views.ReturnPolicy.guide3') }}</p>
      </div>
    </div>

    <div class="mt-6 text-right">
      <router-link to="/contact" class="inline-block bg-black text-white px-6 py-2 rounded-lg shadow hover:bg-gray-800">{{ $t('Views.ReturnPolicy.contactSupport') }}</router-link>
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
