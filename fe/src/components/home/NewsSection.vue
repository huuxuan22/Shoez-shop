<template>
  <section class="mt-12 relative">
    <div class="text-center mb-6 max-w-6xl mx-auto">
      <h2 class="text-2xl font-bold">{{ $t('Home.NewsSection.title') }}</h2>
      <p class="text-sm text-gray-500">{{ $t('Home.NewsSection.hashtag') }}</p>
      <div class="w-16 h-1 bg-red-500 mx-auto mt-2 rounded"></div>
    </div>

    <!-- Navigation Buttons -->
    <button @click="prevSlide"
      class="absolute left-8 top-1/2 -translate-y-1/2 z-10 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition-colors">
      <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
      </svg>
    </button>
    <button @click="nextSlide"
      class="absolute right-8 top-1/2 -translate-y-1/2 z-10 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition-colors">
      <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
      </svg>
    </button>

    <div ref="container" class="overflow-hidden mx-[100px]">
      <div class="flex gap-6 items-stretch transition-transform duration-500 ease-in-out"
        :style="{ transform: `translateX(-${currentIndex * (100 / itemsPerPage)}%)` }">
        <div v-for="(item, idx) in news" :key="idx" @click="handleClick(idx)"
          class="flex-none w-full sm:w-1/2 lg:w-1/3 bg-gray-900 text-white rounded-lg overflow-hidden shadow hover:shadow-xl transition-shadow block cursor-pointer">
          <div class="relative h-60 bg-gray-100">
            <img :src="item.image" alt="" class="w-full h-full object-cover bg-gray-100" />
            <div class="absolute top-3 left-3 bg-black bg-opacity-70 text-white text-xs px-2 py-1 rounded">{{ item.date
            }}</div>
          </div>
          <div class="p-4 flex flex-col justify-between h-48">
            <div>
              <h3 class="text-base font-semibold mb-2 line-clamp-2 text-white">{{ getArticleTitle(item.id) }}</h3>
              <p class="text-sm text-gray-200 mb-3 line-clamp-2">{{ getArticleExcerpt(item.id) }}</p>
            </div>
            <div class="text-xs text-gray-300 mt-auto flex items-center gap-1">
              <span class="inline-block w-4 h-4"><img :src="logoSrc" alt="logo"
                  class="w-full h-full object-contain" /></span>
              {{ $t('Home.NewsSection.brandName') }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

// Import images from assets
import blog1 from '@/assets/images/blog/blog1.png';
import blog2 from '@/assets/images/blog/blog2.png';
import blog3 from '@/assets/images/blog/blog3.png';
import blog4 from '@/assets/images/blog/blog4.png';
import blog5 from '@/assets/images/blog/blog5.png';
import blog6 from '@/assets/images/blog/blog6.png';

const router = useRouter();
const container = ref(null);
const currentIndex = ref(0);
const itemsPerPage = computed(() => {
  if (window.innerWidth >= 1024) return 3; // lg
  if (window.innerWidth >= 640) return 2;  // sm
  return 1; // mobile
});

let autoSlideInterval = null;

const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % Math.ceil(news.length / itemsPerPage.value);
};

const prevSlide = () => {
  if (currentIndex.value === 0) {
    currentIndex.value = Math.ceil(news.length / itemsPerPage.value) - 1;
  } else {
    currentIndex.value--;
  }
};

function handleClick(idx) {
  const item = news[idx];
  if (!item || !item.id) return;
  router.push({ name: 'NewsDetail', params: { id: item.id } });
}

// Auto slide
onMounted(() => {
  autoSlideInterval = setInterval(() => {
    nextSlide();
  }, 5000); // Chuyển slide sau mỗi 5 giây
});

onUnmounted(() => {
  if (autoSlideInterval) {
    clearInterval(autoSlideInterval);
  }
});

const logoSrc = '/images/logo-shoez.png';
const news = [
  {
    image: blog1,
    date: '25 Oct',
    id: '1',
  },
  {
    image: blog2,
    date: '25 Oct',
    id: '2',
  },
  {
    image: blog3,
    date: '21 Oct',
    id: '3',
  },
  {
    image: blog4,
    date: '21 Oct',
    id: '4',
  },
  {
    image: blog5,
    date: '20 Oct',
    id: '5',
  },
  {
    image: blog6,
    date: '18 Oct',
    id: '6',
  },
];

// Helper functions to get translated article content
const getArticleTitle = (articleId) => {
  return t(`Home.NewsSection.articles.${articleId}.title`) || '';
};

const getArticleExcerpt = (articleId) => {
  return t(`Home.NewsSection.articles.${articleId}.excerpt`) || '';
};


// Đảm bảo id luôn trả về đúng cho router-link
function getNewsId(idx) {
  return news[idx].id || (idx + 1).toString();
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-clamp: 2;
}

.text-white {
  color: #fff;
}

.bg-gray-900 {
  background-color: #111827;
}
</style>
