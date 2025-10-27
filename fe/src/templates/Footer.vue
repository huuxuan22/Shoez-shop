<template>
  <footer class="bg-gray-800 text-white py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Company Info -->
        <div>
          <h3 class="text-xl font-bold mb-4">Shoez Shop</h3>
          <p class="text-gray-300 mb-4">
            Cửa hàng giày thể thao chính hãng với đa dạng thương hiệu nổi tiếng thế giới.
          </p>
          <div class="flex space-x-4">
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
              </svg>
            </a>
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z" />
              </svg>
            </a>
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.174-.105-.949-.199-2.403.042-3.441.219-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.567-.994 3.993-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.741.099.12.112.225.085.345-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.402.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.357-.629-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24.001 12.017 24.001c6.624 0 11.99-5.367 11.99-11.988C24.007 5.367 18.641.001 12.017.001z" />
              </svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Liên kết nhanh</h4>
          <ul class="space-y-2">
            <li>
              <router-link to="/" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Trang chủ
              </router-link>
            </li>
            <li>
              <router-link to="/products" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Sản phẩm
              </router-link>
            </li>
            <li>
              <router-link to="/about" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Về chúng tôi
              </router-link>
            </li>
            <li>
              <router-link to="/contact" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Liên hệ
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Customer Service -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Hỗ trợ khách hàng</h4>
          <ul class="space-y-2">
            <li>
              <router-link to="/policy/returns" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Chính sách đổi trả
              </router-link>
            </li>
            <li>
              <router-link to="/guide/purchase" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Hướng dẫn mua hàng
              </router-link>
            </li>
            <li>
              <router-link to="/policy/warranty" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                Bảo hành sản phẩm
              </router-link>
            </li>
            <li>
              <router-link to="/faq" class="text-gray-300 hover:text-white transition-colors" @click="scrollToTop">
                FAQ
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Thông tin liên hệ</h4>
          <div class="space-y-2 text-gray-300">
            <p class="flex items-center">
              <span class="mr-2">📍</span>
              123 Đường ABC, Quận 1, TP.HCM
            </p>
            <p class="flex items-center">
              <span class="mr-2">📞</span>
              (028) 1234 5678
            </p>
            <p class="flex items-center">
              <span class="mr-2">✉️</span>
              info@shoezshop.com
            </p>
            <p class="flex items-center">
              <span class="mr-2">🕒</span>
              8:00 - 22:00 (Thứ 2 - Chủ nhật)
            </p>
          </div>
        </div>
      </div>

      <div class="border-t border-gray-700 mt-8 pt-8 text-center text-gray-300">
        <p>&copy; {{ currentYear }} Shoez Shop. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Computed properties
const currentYear = computed(() => {
  return new Date().getFullYear();
});

// Methods
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

// Watch for route changes to scroll to top
router.afterEach(() => {
  scrollToTop();
});
</script>