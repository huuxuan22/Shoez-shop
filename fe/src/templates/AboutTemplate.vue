<template>
    <DefaultLayout>
      <div class="min-h-screen bg-white font-['Inter']">
        <!-- Hero Section với hình ảnh -->
        <section class="relative bg-gray-900 text-white py-24">
          <div class="absolute inset-0 bg-black opacity-50"></div>
          <img 
            src="https://images.unsplash.com/photo-1549298916-b41d501d3772?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2012&q=80" 
            alt="Delvor Shoes Collection"
            class="absolute inset-0 w-full h-full object-cover"
          >
          <div class="container mx-auto px-4 relative z-10">
            <div class="max-w-4xl mx-auto text-center">
              <h1 class="text-6xl font-bold mb-6 font-['Playfair_Display']">{{ $t('AboutTemplate.title') }}</h1>
              <p class="text-xl text-gray-200 leading-relaxed">
                {{ $t('AboutTemplate.subtitle') }}
              </p>
            </div>
          </div>
        </section>
  
        <!-- Mission & Vision với hình ảnh -->
        <section class="py-20 bg-white">
          <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
              
              <!-- Hình ảnh -->
              <div class="order-2 lg:order-1">
                <img 
                  src="https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1964&q=80" 
                  alt="Shoes Craftsmanship"
                  class="rounded-2xl shadow-2xl w-full h-96 object-cover"
                >
              </div>
  
              <!-- Nội dung -->
              <div class="order-1 lg:order-2">
                <h2 class="text-4xl font-bold text-gray-900 mb-8 font-['Playfair_Display']">{{ $t('AboutTemplate.mission') }}</h2>
                <p class="text-gray-600 leading-relaxed text-lg mb-6">
                  {{ $t('AboutTemplate.missionText') }}
                </p>
                <div class="bg-gray-50 p-6 rounded-xl border-l-4 border-gray-900">
                  <p class="text-gray-700 italic">
                    "{{ $t('AboutTemplate.missionQuote') }}"
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
  
        <!-- Giá trị cốt lõi với hình ảnh -->
        <section class="py-20 bg-gray-50">
          <div class="container mx-auto px-4">
            <div class="text-center mb-16">
              <h2 class="text-4xl font-bold text-gray-900 mb-4 font-['Playfair_Display']">{{ $t('AboutTemplate.coreValues') }}</h2>
              <p class="text-gray-600 text-lg max-w-2xl mx-auto">
                {{ $t('AboutTemplate.coreValuesSubtitle') }}
              </p>
            </div>
  
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
              <!-- Card 1 -->
              <div class="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 text-center group hover:transform hover:-translate-y-2 transition-all duration-300">
                <div class="w-20 h-20 bg-gradient-to-br from-gray-900 to-gray-700 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                  </svg>
                </div>
                <h3 class="text-2xl font-semibold text-gray-900 mb-4 font-['Playfair_Display']">{{ $t('AboutTemplate.quality') }}</h3>
                <p class="text-gray-600 leading-relaxed">
                  {{ $t('AboutTemplate.qualityText') }}
                </p>
              </div>
  
              <!-- Card 2 -->
              <div class="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 text-center group hover:transform hover:-translate-y-2 transition-all duration-300">
                <div class="w-20 h-20 bg-gradient-to-br from-gray-900 to-gray-700 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                  </svg>
                </div>
                <h3 class="text-2xl font-semibold text-gray-900 mb-4 font-['Playfair_Display']">{{ $t('AboutTemplate.design') }}</h3>
                <p class="text-gray-600 leading-relaxed">
                  {{ $t('AboutTemplate.designText') }}
                </p>
              </div>
  
              <!-- Card 3 -->
              <div class="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 text-center group hover:transform hover:-translate-y-2 transition-all duration-300">
                <div class="w-20 h-20 bg-gradient-to-br from-gray-900 to-gray-700 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                  </svg>
                </div>
                <h3 class="text-2xl font-semibold text-gray-900 mb-4 font-['Playfair_Display']">{{ $t('AboutTemplate.community') }}</h3>
                <p class="text-gray-600 leading-relaxed">
                  {{ $t('AboutTemplate.communityText') }}
                </p>
              </div>
            </div>
          </div>
        </section>
  
        <!-- Lịch sử phát triển với timeline visual -->
        <section class="py-20 bg-white">
          <div class="container mx-auto px-4">
            <div class="max-w-6xl mx-auto">
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                
                <!-- Timeline -->
                <div>
                  <h2 class="text-4xl font-bold text-gray-900 mb-12 font-['Playfair_Display']">{{ $t('AboutTemplate.journey') }}</h2>
                  
                  <div class="space-y-8 relative">
                    <!-- Timeline line -->
                    <div class="absolute left-6 top-0 bottom-0 w-0.5 bg-gray-300"></div>
                    
                    <!-- Item 1 -->
                    <div class="flex items-start space-x-6 relative">
                      <div class="flex-shrink-0 w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center relative z-10">
                        <span class="text-white font-bold text-sm">2015</span>
                      </div>
                      <div class="pb-8">
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ $t('AboutTemplate.timeline1Title') }}</h3>
                        <p class="text-gray-600">
                          {{ $t('AboutTemplate.timeline1Text') }}
                        </p>
                      </div>
                    </div>
  
                    <!-- Item 2 -->
                    <div class="flex items-start space-x-6 relative">
                      <div class="flex-shrink-0 w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center relative z-10">
                        <span class="text-white font-bold text-sm">2018</span>
                      </div>
                      <div class="pb-8">
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ $t('AboutTemplate.timeline2Title') }}</h3>
                        <p class="text-gray-600">
                          {{ $t('AboutTemplate.timeline2Text') }}
                        </p>
                      </div>
                    </div>
  
                    <!-- Item 3 -->
                    <div class="flex items-start space-x-6 relative">
                      <div class="flex-shrink-0 w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center relative z-10">
                        <span class="text-white font-bold text-sm">2020</span>
                      </div>
                      <div class="pb-8">
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ $t('AboutTemplate.timeline3Title') }}</h3>
                        <p class="text-gray-600">
                          {{ $t('AboutTemplate.timeline3Text') }}
                        </p>
                      </div>
                    </div>
  
                    <!-- Item 4 -->
                    <div class="flex items-start space-x-6 relative">
                      <div class="flex-shrink-0 w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center relative z-10">
                        <span class="text-white font-bold text-sm">2024</span>
                      </div>
                      <div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ $t('AboutTemplate.timeline4Title') }}</h3>
                        <p class="text-gray-600">
                          {{ $t('AboutTemplate.timeline4Text') }}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
  
                <!-- Hình ảnh timeline -->
                <div class="grid grid-cols-2 gap-4">
                  <img 
                    src="https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1025&q=80" 
                    alt="Sneaker Collection"
                    class="rounded-2xl shadow-lg h-48 w-full object-cover"
                  >
                  <img 
                    src="https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1964&q=80" 
                    alt="Shoes Detail"
                    class="rounded-2xl shadow-lg h-48 w-full object-cover"
                  >
                  <img 
                    src="https://images.unsplash.com/photo-1549298916-f52d724204b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80" 
                    alt="Running Shoes"
                    class="rounded-2xl shadow-lg h-48 w-full object-cover"
                  >
                  <img 
                    src="https://images.unsplash.com/photo-1560769624-7b2aaa2809c4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80" 
                    alt="Luxury Shoes"
                    class="rounded-2xl shadow-lg h-48 w-full object-cover"
                  >
                </div>
              </div>
            </div>
          </div>
        </section>
  
        <!-- CTA Section -->
        <section class="py-20 bg-gradient-to-r from-gray-900 to-black text-white">
          <div class="container mx-auto px-4 text-center">
            <h2 class="text-4xl font-bold mb-6 font-['Playfair_Display']">{{ $t('AboutTemplate.ctaTitle') }}</h2>
            <p class="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
              {{ $t('AboutTemplate.ctaSubtitle') }}
            </p>
            <div class="space-x-4">
              <router-link 
                to="/products" 
                class="bg-white text-gray-900 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-300 hover:scale-105 inline-block text-lg"
              >
                {{ $t('AboutTemplate.shopNow') }}
              </router-link>
              <router-link 
                to="/contact" 
                class="border border-white text-white px-8 py-4 rounded-lg font-semibold hover:bg-white hover:text-gray-900 transition-all duration-300 hover:scale-105 inline-block text-lg"
              >
                {{ $t('AboutTemplate.contact') }}
              </router-link>
            </div>
          </div>
        </section>
      </div>
    </DefaultLayout>
  </template>
  
  <script setup>
  // Vue i18n is available globally via $t() in template
  // No need to import useI18n for template-only usage
  </script>