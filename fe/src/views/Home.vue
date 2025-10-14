<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section - Minimalist Design -->
    <section class="relative min-h-screen flex items-center bg-white">
      <div class="container mx-auto px-4">
        <div class="max-w-3xl mx-auto text-center">
          <!-- Badge -->
          <div class="inline-block bg-black text-white text-sm px-4 py-1 rounded-full mb-8">
            Giảm giá đến 50%
          </div>

          <!-- Main heading -->
          <h1 class="text-6xl md:text-7xl font-bold mb-6 text-black">
            SHOEZ SHOP
          </h1>
          
          <p class="text-xl md:text-2xl mb-12 text-gray-600">
            Giày thể thao chính hãng
          </p>

          <!-- CTA Buttons -->
          <div class="flex gap-4 justify-center mb-16">
            <button 
              @click="$router.push('/products')"
              class="bg-black text-white px-8 py-3 rounded hover:bg-gray-800 transition"
            >
              Khám phá ngay
            </button>
            
            <button 
              @click="scrollToProducts"
              class="border-2 border-black text-black px-8 py-3 rounded hover:bg-black hover:text-white transition"
            >
              Xem sản phẩm →
            </button>
          </div>

          <!-- Stats -->
          <div class="flex justify-center gap-12 text-sm text-gray-500">
            <div>1000+ Sản phẩm</div>
            <div>50K+ Khách hàng</div>
            <div>99% Hài lòng</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section - Minimalist -->
    <section class="py-12 border-t border-gray-200">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          <div class="p-4">
            <div class="text-2xl mb-2">✓</div>
            <p class="text-sm font-medium">Chính hãng 100%</p>
          </div>
          
          <div class="p-4">
            <div class="text-2xl mb-2">💰</div>
            <p class="text-sm font-medium">Giá tốt nhất</p>
          </div>
          
          <div class="p-4">
            <div class="text-2xl mb-2">🚚</div>
            <p class="text-sm font-medium">Freeship</p>
          </div>
          
          <div class="p-4">
            <div class="text-2xl mb-2">↻</div>
            <p class="text-sm font-medium">Đổi trả 7 ngày</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Products - Minimalist -->
    <section ref="productsSection" class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <!-- Section header -->
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-black mb-2">
            Sản phẩm nổi bật
          </h2>
          <p class="text-gray-600">
            Những đôi giày được yêu thích nhất
          </p>
        </div>
        
        <!-- Men's Shoes -->
        <div class="mb-16">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-semibold text-black">Giày nam</h3>
            <router-link to="/products?category=men" class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
              Xem tất cả
              <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
          <ProductCategory
            :products="featuredMenShoes"
            :show-title="false"
          />
        </div>
        
        <!-- Women's Shoes -->
        <div class="mb-16">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-semibold text-black">Giày nữ</h3>
            <router-link to="/products?category=women" class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
              Xem tất cả
              <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
          <ProductCategory
            :products="featuredWomenShoes"
            :show-title="false"
          />
        </div>
        
        <!-- Sale Products -->
        <div class="border-t border-gray-200 pt-16">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-semibold text-black">🔥 Sale</h3>
            <router-link to="/products?sale=true" class="text-sm text-gray-600 hover:text-black flex items-center gap-1 group">
              Xem tất cả
              <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
          <ProductCategory
            :products="saleProducts"
            :show-title="false"
          />
        </div>
      </div>
    </section>

    <!-- Brand Section - Minimalist -->
    <section class="py-12 border-t border-gray-200 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-8">
          <h2 class="text-2xl md:text-3xl font-bold text-black">Thương hiệu</h2>
        </div>
        
        <div class="grid grid-cols-3 md:grid-cols-6 gap-4">
          <div 
            v-for="brand in brands" 
            :key="brand.name" 
            @click="filterByBrand(brand.name)"
            class="group cursor-pointer"
          >
            <div class="bg-white border border-gray-200 rounded p-6 hover:border-black transition">
              <img :src="brand.logo" :alt="brand.name" class="h-12 w-full object-contain filter grayscale hover:grayscale-0 transition">
            </div>
          </div>
        </div>

        <!-- Brand trust badges -->
        <div class="mt-8 flex flex-wrap justify-center gap-6 text-sm text-gray-500">
          <div class="flex items-center gap-2">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
            <span>Đối tác chính thức</span>
          </div>
          <div class="flex items-center gap-2">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
            <span>Hàng chính hãng 100%</span>
          </div>
          <div class="flex items-center gap-2">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
            <span>Bảo hành toàn cầu</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section - Minimalist -->
    <section class="py-12 bg-white border-t border-gray-200">
      <div class="container mx-auto px-4">
        <div class="text-center mb-8">
          <h2 class="text-2xl md:text-3xl font-bold text-black">Đánh giá</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
          <div v-for="(review, index) in testimonials" :key="index">
            <div class="border border-gray-200 rounded p-6 hover:border-black transition">
              <!-- Stars -->
              <div class="flex gap-1 mb-3">
                <span v-for="i in 5" :key="i" class="text-yellow-400">★</span>
              </div>

              <!-- Review text -->
              <p class="text-sm text-gray-700 mb-4">"{{ review.text }}"</p>

              <!-- Author -->
              <div class="text-sm">
                <div class="font-medium text-black">{{ review.author }}</div>
                <div class="text-gray-500">{{ review.role }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Newsletter Section - Minimalist -->
    <section class="py-12 bg-gray-50 border-t border-gray-200">
      <div class="container mx-auto px-4">
        <div class="max-w-2xl mx-auto text-center">
          <h2 class="text-2xl md:text-3xl font-bold text-black mb-2">Nhận ưu đãi</h2>
          <p class="text-gray-600 mb-6">Đăng ký để nhận mã giảm giá 100K</p>
          
          <form class="flex gap-2">
            <input 
              v-model="email"
              type="email" 
              placeholder="Email của bạn"
              class="flex-1 px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-black"
            />
            <button 
              type="submit"
              @click.prevent="subscribeNewsletter"
              class="bg-black text-white px-6 py-3 rounded hover:bg-gray-800 transition"
            >
              Đăng ký
            </button>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import ProductCategory from '@/components/ProductCategory.vue';

const router = useRouter();

// Refs
const productsSection = ref(null);
const email = ref('');

// Banner images for hero section
const banners = [
  '/images/banners/hero-banner-1.jpg',
  '/images/banners/hero-banner-2.jpg'
];

const currentBanner = ref(banners[0]);

// Testimonials data
const testimonials = ref([
  {
    text: 'Giày rất đẹp và chất lượng, đi rất êm chân. Giao hàng nhanh, đóng gói cẩn thận. Sẽ ủng hộ shop lâu dài!',
    author: 'Nguyễn Văn An',
    role: 'Khách hàng thân thiết'
  },
  {
    text: 'Mình đã mua 3 đôi giày ở đây rồi, tất cả đều chính hãng 100%. Giá cả hợp lý, nhân viên tư vấn nhiệt tình!',
    author: 'Trần Thị Bình',
    role: 'Đã mua 3 lần'
  },
  {
    text: 'Shop uy tín, hàng chính hãng, giá tốt. Freeship nhanh chóng. Rất hài lòng với dịch vụ. Recommend!',
    author: 'Lê Hoàng Minh',
    role: 'Khách hàng mới'
  }
]);

// Rotate banners every 5 seconds
onMounted(() => {
  let index = 0;
  setInterval(() => {
    index = (index + 1) % banners.length;
    currentBanner.value = banners[index];
  }, 5000);
});

// Scroll to products section
const scrollToProducts = () => {
  if (productsSection.value) {
    productsSection.value.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

// Newsletter subscription
const subscribeNewsletter = () => {
  if (!email.value) {
    alert('Vui lòng nhập email!');
    return;
  }
  
  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    alert('Email không hợp lệ!');
    return;
  }
  
  alert(`🎉 Đăng ký thành công! Mã giảm giá 100K đã được gửi đến ${email.value}`);
  email.value = '';
};

// Sample shoe data - Sử dụng ảnh từ thư mục public/images/shoes
const featuredMenShoes = [
  { 
    id: 1, 
    name: 'Nike Air Force 1', 
    brand: 'Nike',
    price: 2200000,
    image: '/images/shoes/nike-air-max-3.jpg',
    category: 'Sneakers',
    colors: ['Trắng', 'Đen', 'Xanh'],
    sizes: [38, 39, 40, 41, 42, 43]
  },
  { 
    id: 2, 
    name: 'Adidas Ultraboost 22', 
    brand: 'Adidas',
    price: 4500000,
    image: '/images/shoes/adidas-ultraboost-1.jpg',
    category: 'Running',
    colors: ['Đen', 'Trắng', 'Xám'],
    sizes: [39, 40, 41, 42, 43, 44]
  },
  { 
    id: 3, 
    name: 'Converse Chuck Taylor', 
    brand: 'Converse',
    price: 1500000,
    image: '/images/shoes/converse-chuck-taylor-1.jpg',
    category: 'Casual',
    colors: ['Đen', 'Trắng', 'Đỏ'],
    sizes: [36, 37, 38, 39, 40, 41, 42]
  },
  { 
    id: 4, 
    name: 'Puma RS-X', 
    brand: 'Puma',
    price: 2800000,
    image: '/images/shoes/puma-rs-x-1.jpg',
    category: 'Lifestyle',
    colors: ['Trắng Xanh', 'Đen', 'Xám'],
    sizes: [39, 40, 41, 42, 43]
  }
];

const featuredWomenShoes = [
  { 
    id: 5, 
    name: 'Nike Air Max 270', 
    brand: 'Nike',
    price: 3200000,
    image: '/images/shoes/nike-air-max-2.jpg',
    category: 'Lifestyle',
    colors: ['Xanh Dương', 'Hồng', 'Trắng'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
  { 
    id: 6, 
    name: 'Adidas NMD R1', 
    brand: 'Adidas',
    price: 3800000,
    image: '/images/shoes/adidas-nmd-1.jpg',
    category: 'Sneakers',
    colors: ['Xám', 'Đen', 'Hồng'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
  { 
    id: 7, 
    name: 'Vans Old Skool', 
    brand: 'Vans',
    price: 1800000,
    image: '/images/shoes/vans-old-skool-1.jpg',
    category: 'Skate',
    colors: ['Đen Trắng', 'Navy', 'Đỏ'],
    sizes: [36, 37, 38, 39, 40, 41]
  },
  { 
    id: 8, 
    name: 'New Balance 574', 
    brand: 'New Balance',
    price: 2500000,
    image: '/images/shoes/newbalance-574-1.jpg',
    category: 'Retro',
    colors: ['Xám', 'Navy', 'Be'],
    sizes: [35, 36, 37, 38, 39, 40]
  }
];

const saleProducts = [
  { 
    id: 9, 
    name: 'Nike Air Jordan 1', 
    brand: 'Nike',
    price: 3600000,
    originalPrice: 5000000,
    discount: 28,
    image: '/images/shoes/nike-jordan-1.jpg',
    category: 'Basketball',
    colors: ['Đỏ Đen', 'Xanh Đen'],
    sizes: [39, 40, 41, 42, 43]
  },
  { 
    id: 10, 
    name: 'Adidas Yeezy Boost 350', 
    brand: 'Adidas',
    price: 5200000,
    originalPrice: 7000000,
    discount: 26,
    image: '/images/shoes/adidas-yeezy-1.jpg',
    category: 'Lifestyle',
    colors: ['Be', 'Đen', 'Xám'],
    sizes: [38, 39, 40, 41, 42, 43]
  }
];

const brands = [
  { name: 'Nike', logo: '/images/brands/nike-logo.png' },
  { name: 'Adidas', logo: '/images/brands/adidas-logo.png' },
  { name: 'Converse', logo: '/images/brands/converse-logo.png' },
  { name: 'Puma', logo: '/images/brands/puma-logo.png' },
  { name: 'Vans', logo: '/images/brands/vans-logo.png' },
  { name: 'New Balance', logo: '/images/brands/newbalance-logo.png' }
];

// Navigate to products page with brand filter
const filterByBrand = (brandName) => {
  router.push({ name: 'Products', query: { brand: brandName } });
};
</script>

<style scoped>
/* Animations */
@keyframes float {
  0%, 100% {
    transform: translateY(0) translateX(0);
  }
  25% {
    transform: translateY(-20px) translateX(10px);
  }
  50% {
    transform: translateY(-10px) translateX(-10px);
  }
  75% {
    transform: translateY(-30px) translateX(5px);
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in-down {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-float {
  animation: float linear infinite;
}

.animate-fade-in {
  animation: fade-in 1s ease-out;
}

.animate-fade-in-up {
  animation: fade-in-up 1s ease-out;
}

.animate-fade-in-down {
  animation: fade-in-down 1s ease-out;
}

.animation-delay-200 {
  animation-delay: 0.2s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-300 {
  animation-delay: 0.3s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-400 {
  animation-delay: 0.4s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-500 {
  animation-delay: 0.5s;
  opacity: 0;
  animation-fill-mode: forwards;
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Custom gradient text */
.bg-clip-text {
  -webkit-background-clip: text;
  background-clip: text;
}
</style>