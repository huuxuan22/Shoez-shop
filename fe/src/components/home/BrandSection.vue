<template>
    <section class="py-12 border-t border-gray-200 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="text-center mb-8">
                <h2 class="text-2xl md:text-3xl font-bold text-black">Thương hiệu</h2>
            </div>

            <!-- Loading state với scroll ngang -->
            <div v-if="loading" class="overflow-x-auto pb-4 -mx-4 px-4 scrollbar-hide">
                <div class="flex gap-4 min-w-max">
                    <div v-for="i in 6" :key="i" class="flex-shrink-0 w-32 md:w-40">
                        <div class="bg-white border border-gray-200 rounded p-6 animate-pulse">
                            <div class="h-12 w-full bg-gray-200 rounded"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Brands grid với scroll ngang và navigation arrows -->
            <div v-else-if="brands.length > 0" class="relative">
                <!-- Left Arrow -->
                <button 
                    @click="scrollLeft"
                    :disabled="!canScrollLeft"
                    :class="[
                        'absolute left-0 top-1/2 -translate-y-1/2 z-10 bg-white shadow-lg rounded-full p-3 hover:bg-gray-100 transition-all',
                        canScrollLeft ? 'opacity-100 cursor-pointer' : 'opacity-0 cursor-not-allowed pointer-events-none'
                    ]">
                    <svg class="w-6 h-6 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                    </svg>
                </button>

                <!-- Brands Container -->
                <div ref="brandsContainer" class="overflow-x-auto pb-4 -mx-4 px-12 scrollbar-hide scroll-smooth">
                    <div class="flex gap-4 min-w-max">
                        <div v-for="brand in brands" :key="brand.id || brand.name" @click="filterByBrand(brand.name)"
                            class="group cursor-pointer flex-shrink-0 w-32 md:w-40">
                            <div class="bg-white border border-gray-200 rounded p-6 hover:border-black transition">
                                <img 
                                    :src="brand.logo" 
                                    :alt="brand.name"
                                    @error="handleImageError($event, brand.name)"
                                    class="h-12 w-full object-contain filter grayscale hover:grayscale-0 transition">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Arrow -->
                <button 
                    @click="scrollRight"
                    :disabled="!canScrollRight"
                    :class="[
                        'absolute right-0 top-1/2 -translate-y-1/2 z-10 bg-white shadow-lg rounded-full p-3 hover:bg-gray-100 transition-all',
                        canScrollRight ? 'opacity-100 cursor-pointer' : 'opacity-0 cursor-not-allowed pointer-events-none'
                    ]">
                    <svg class="w-6 h-6 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                    </svg>
                </button>
            </div>
            
            <!-- Empty state -->
            <div v-else class="text-center py-8 text-gray-500">
                <p>Chưa có thương hiệu nào</p>
            </div>

            <!-- Brand trust badges -->
            <div class="mt-8 flex flex-wrap justify-center gap-6 text-sm text-gray-500">
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Đối tác chính thức</span>
                </div>
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Hàng chính hãng 100%</span>
                </div>
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd" />
                    </svg>
                    <span>Bảo hành toàn cầu</span>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import BrandService from '@/api-services/BrandService'

const router = useRouter()
const brands = ref([])
const loading = ref(false)
const brandsContainer = ref(null)
const canScrollLeft = ref(false)
const canScrollRight = ref(true)

const loadBrands = async () => {
  loading.value = true
  try {
    const data = await BrandService.getAll()
    // Backend trả về array trực tiếp
    const brandsList = Array.isArray(data) ? data : (data?.brands || [])
    
    // Lọc chỉ lấy các brand đang active và có logo (không giới hạn số lượng)
    brands.value = brandsList
      .filter(b => b && b.name && b.is_active !== false && b.logo && b.logo.trim())
      .sort((a, b) => a.name.localeCompare(b.name))
  } catch (error) {
    // Fallback về empty array nếu lỗi
    brands.value = []
  } finally {
    loading.value = false
  }
}

const filterByBrand = (brandName) => {
  router.push({ name: 'Products', query: { brand: brandName } })
}

const handleImageError = (event, brandName) => {
  // Thay thế bằng placeholder nếu logo không load được
  event.target.src = `https://via.placeholder.com/150x50?text=${encodeURIComponent(brandName)}`
  event.target.onerror = null // Tránh loop
}

const checkScrollButtons = () => {
  if (!brandsContainer.value) return
  
  const container = brandsContainer.value
  const scrollLeft = container.scrollLeft
  const scrollWidth = container.scrollWidth
  const clientWidth = container.clientWidth
  
  canScrollLeft.value = scrollLeft > 0
  canScrollRight.value = scrollLeft < scrollWidth - clientWidth - 10 // 10px threshold
}

const scrollLeft = () => {
  if (!brandsContainer.value) return
  
  const scrollAmount = brandsContainer.value.clientWidth * 0.8
  brandsContainer.value.scrollBy({
    left: -scrollAmount,
    behavior: 'smooth'
  })
}

const scrollRight = () => {
  if (!brandsContainer.value) return
  
  const scrollAmount = brandsContainer.value.clientWidth * 0.8
  brandsContainer.value.scrollBy({
    left: scrollAmount,
    behavior: 'smooth'
  })
}

// Load brands khi component mount
onMounted(async () => {
  await loadBrands()
  
  // Check scroll buttons sau khi brands load xong và DOM render
  await new Promise(resolve => setTimeout(resolve, 100))
  checkScrollButtons()
  
  // Listen scroll events
  if (brandsContainer.value) {
    brandsContainer.value.addEventListener('scroll', checkScrollButtons)
    
    // Check lại sau khi resize window
    window.addEventListener('resize', checkScrollButtons)
  }
})

onUnmounted(() => {
  if (brandsContainer.value) {
    brandsContainer.value.removeEventListener('scroll', checkScrollButtons)
  }
  window.removeEventListener('resize', checkScrollButtons)
})
</script>

<style scoped>
/* Ẩn scrollbar nhưng vẫn có thể scroll */
.scrollbar-hide {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;  /* Chrome, Safari, Opera */
}

/* Smooth scroll */
.scrollbar-hide {
  scroll-behavior: smooth;
}

/* Style cho loading skeleton */
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: .5;
  }
}
</style>