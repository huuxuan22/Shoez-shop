<template>
  <div class="min-h-screen bg-gray-50">
    <div v-if="product" class="container mx-auto px-4 py-8">
      <!-- Breadcrumb -->
      <nav class="flex mb-8" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-1 md:space-x-3">
          <li class="inline-flex items-center">
            <router-link to="/" class="text-gray-700 hover:text-black">
              Trang chủ
            </router-link>
          </li>
          <li>
            <div class="flex items-center">
              <span class="mx-2 text-gray-400">/</span>
              <router-link to="/products" class="text-gray-700 hover:text-black">
                Sản phẩm
              </router-link>
            </div>
          </li>
          <li aria-current="page">
            <div class="flex items-center">
              <span class="mx-2 text-gray-400">/</span>
              <span class="text-gray-500">{{ product.name }}</span>
            </div>
          </li>
        </ol>
      </nav>

      <!-- Product Details -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Image Gallery -->
        <div>
          <!-- Main Image -->
          <div class="bg-white rounded-lg shadow-lg overflow-hidden mb-4">
            <div class="relative pt-[100%]">
              <img 
                :src="selectedImage" 
                :alt="product.name"
                class="absolute inset-0 w-full h-full object-cover"
                @error="handleImageError"
              />
              
              <!-- Zoom indicator -->
              <div class="absolute top-4 right-4 bg-white/90 px-3 py-1 rounded-full text-sm">
                <svg class="w-5 h-5 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                </svg>
              </div>

              <!-- Sale badge -->
              <div v-if="product.discount" class="absolute top-4 left-4 bg-red-500 text-white px-4 py-2 rounded-full text-lg font-bold">
                -{{ product.discount }}%
              </div>
            </div>
          </div>

          <!-- Thumbnail Gallery -->
          <div class="grid grid-cols-4 gap-2">
            <div 
              v-for="(img, index) in productImages" 
              :key="index"
              @click="selectedImage = img"
              :class="[
                'relative pt-[100%] bg-white rounded-lg overflow-hidden cursor-pointer border-2 transition-all',
                selectedImage === img ? 'border-black shadow-lg' : 'border-gray-200 hover:border-gray-400'
              ]"
            >
              <img 
                :src="img" 
                :alt="`${product.name} ${index + 1}`"
                class="absolute inset-0 w-full h-full object-cover"
                @error="handleImageError"
              />
            </div>
          </div>
        </div>

        <!-- Product Info -->
        <div>
          <div class="bg-white rounded-lg shadow-lg p-8">
            <!-- Brand -->
            <p class="text-black font-semibold mb-2 uppercase tracking-wider">{{ product.brand }}</p>
            
            <!-- Product Name -->
            <h1 class="text-4xl font-bold text-gray-800 mb-4">{{ product.name }}</h1>
            
            <!-- Category -->
            <p class="text-gray-600 mb-6">{{ product.category }}</p>

            <!-- Rating -->
            <div class="flex items-center mb-6">
              <div class="flex text-yellow-400 mr-2">
                <svg v-for="star in 5" :key="star" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
              </div>
              <span class="text-gray-600">(128 đánh giá)</span>
            </div>

            <!-- Price -->
            <div class="mb-8">
              <div class="flex items-baseline gap-4">
                <p class="text-4xl font-bold text-black">{{ formatPrice(product.price) }}</p>
                <p v-if="product.originalPrice" class="text-2xl text-gray-400 line-through">
                  {{ formatPrice(product.originalPrice) }}
                </p>
              </div>
              <p v-if="product.discount" class="text-green-600 font-semibold mt-2">
                Tiết kiệm {{ formatPrice(product.originalPrice - product.price) }}
              </p>
            </div>

            <!-- Color Selection -->
            <div class="mb-8">
              <label class="block text-gray-700 font-semibold mb-3">
                Màu sắc: <span class="text-black">{{ selectedColor }}</span>
              </label>
              <div class="flex flex-wrap gap-3">
                <button
                  v-for="color in product.colors"
                  :key="color"
                  @click="selectedColor = color"
                  :class="[
                    'px-6 py-3 rounded-lg border-2 font-semibold transition-all flex items-center gap-2',
                    selectedColor === color
                      ? getColorClasses(color).active
                      : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                  ]"
                >
                  <span :class="['w-4 h-4 rounded-full border-2 border-gray-400', getColorClasses(color).dot]"></span>
                  {{ color }}
                </button>
              </div>
            </div>

            <!-- Size Selection -->
            <div class="mb-8">
              <div class="flex justify-between items-center mb-3">
                <label class="block text-gray-700 font-semibold">
                  Size: <span class="text-black">{{ selectedSize || 'Chọn size' }}</span>
                </label>
                <button class="text-black text-sm hover:underline">Hướng dẫn chọn size</button>
              </div>
              <div class="grid grid-cols-6 gap-2">
                <button
                  v-for="size in product.sizes"
                  :key="size"
                  @click="selectedSize = size"
                  :class="[
                    'py-3 rounded-lg border-2 font-semibold transition-all',
                    selectedSize === size
                      ? 'border-black bg-black text-white shadow-md'
                      : 'border-gray-300 bg-white text-gray-700 hover:border-gray-400'
                  ]"
                >
                  {{ size }}
                </button>
              </div>
            </div>

            <!-- Quantity -->
            <div class="mb-8">
              <label class="block text-gray-700 font-semibold mb-3">Số lượng</label>
              <div class="flex items-center gap-4">
                <div class="flex items-center border-2 border-gray-300 rounded-lg">
                  <button 
                    @click="quantity = Math.max(1, quantity - 1)"
                    class="px-4 py-2 text-gray-600 hover:bg-gray-100 transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                    </svg>
                  </button>
                  <input 
                    v-model.number="quantity" 
                    type="number" 
                    min="1"
                    class="w-16 text-center border-x-2 border-gray-300 py-2 focus:outline-none"
                  />
                  <button 
                    @click="quantity++"
                    class="px-4 py-2 text-gray-600 hover:bg-gray-100 transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                    </svg>
                  </button>
                </div>
                <p class="text-gray-600">{{ product.stock || 50 }} sản phẩm có sẵn</p>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex gap-4 mb-8">
              <button 
                class="flex-1 bg-white border-2 border-black text-black px-8 py-4 rounded-lg font-semibold hover:bg-black hover:text-white transition-all transform hover:scale-105 shadow-lg flex items-center justify-center gap-2"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                Thêm vào giỏ
              </button>
              <button 
                class="flex-1 bg-black text-white px-8 py-4 rounded-lg font-semibold hover:bg-gray-800 transition-all transform hover:scale-105 shadow-lg flex items-center justify-center gap-2"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                Mua ngay
              </button>
            </div>

            <!-- Product Features -->
            <div class="border-t pt-6">
              <h3 class="font-semibold text-gray-800 mb-4">Đặc điểm nổi bật</h3>
              <ul class="space-y-2 text-gray-600">
                <li class="flex items-start">
                  <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  Chính hãng 100%, tem check chống hàng giả
                </li>
                <li class="flex items-start">
                  <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  Miễn phí vận chuyển toàn quốc cho đơn hàng từ 500k
                </li>
                <li class="flex items-start">
                  <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  Đổi trả trong vòng 7 ngày nếu có lỗi từ nhà sản xuất
                </li>
                <li class="flex items-start">
                  <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  Bảo hành 6 tháng chính hãng
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Product Description Tabs -->
      <div class="mt-12 bg-white rounded-lg shadow-lg">
        <div class="border-b">
          <nav class="flex">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              @click="activeTab = tab.id"
              :class="[
                'px-8 py-4 font-semibold transition-colors border-b-2',
                activeTab === tab.id
                  ? 'border-blue-600 text-blue-600'
                  : 'border-transparent text-gray-600 hover:text-gray-800'
              ]"
            >
              {{ tab.label }}
            </button>
          </nav>
        </div>

        <div class="p-8">
          <!-- Description Tab -->
          <div v-if="activeTab === 'description'">
            <h3 class="text-2xl font-bold mb-4">Mô tả sản phẩm</h3>
            <div class="prose max-w-none text-gray-600 space-y-4">
              <p>
                {{ product.name }} là một trong những dòng giày thể thao đỉnh cao từ {{ product.brand }}, 
                mang đến sự kết hợp hoàn hảo giữa phong cách thời trang và hiệu suất vận động.
              </p>
              <p>
                Với thiết kế độc đáo và chất liệu cao cấp, sản phẩm này không chỉ đảm bảo sự thoải mái 
                tối đa khi mang mà còn tạo nên phong cách cá nhân nổi bật cho người sử dụng.
              </p>
              <p>
                Đế giày được thiết kế với công nghệ tiên tiến, tạo độ êm ái và độ bám tốt trên mọi địa hình.
                Phần upper làm từ chất liệu breathable giúp thoáng khí tốt, giữ cho đôi chân luôn khô ráo.
              </p>
            </div>
          </div>

          <!-- Specifications Tab -->
          <div v-if="activeTab === 'specifications'">
            <h3 class="text-2xl font-bold mb-4">Thông số kỹ thuật</h3>
            <table class="w-full">
              <tbody class="divide-y">
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Thương hiệu</td>
                  <td class="py-3 text-gray-600">{{ product.brand }}</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Loại</td>
                  <td class="py-3 text-gray-600">{{ product.category }}</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Màu sắc</td>
                  <td class="py-3 text-gray-600">{{ product.colors.join(', ') }}</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Size</td>
                  <td class="py-3 text-gray-600">{{ product.sizes.join(', ') }}</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Chất liệu</td>
                  <td class="py-3 text-gray-600">Da tổng hợp, Mesh breathable</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Đế giày</td>
                  <td class="py-3 text-gray-600">Rubber, EVA foam</td>
                </tr>
                <tr>
                  <td class="py-3 font-semibold text-gray-700">Xuất xứ</td>
                  <td class="py-3 text-gray-600">Chính hãng nhập khẩu</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Reviews Tab -->
          <div v-if="activeTab === 'reviews'">
            <h3 class="text-2xl font-bold mb-6">Đánh giá từ khách hàng</h3>
            
            <!-- Review Summary -->
            <div class="bg-gray-50 rounded-lg p-6 mb-8">
              <div class="flex items-center gap-8">
                <div class="text-center">
                  <p class="text-5xl font-bold text-blue-600 mb-2">4.8</p>
                  <div class="flex text-yellow-400 mb-2">
                    <svg v-for="star in 5" :key="star" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  </div>
                  <p class="text-gray-600">128 đánh giá</p>
                </div>
                
                <div class="flex-1">
                  <div v-for="rating in [5, 4, 3, 2, 1]" :key="rating" class="flex items-center gap-2 mb-2">
                    <span class="text-sm text-gray-600 w-12">{{ rating }} sao</span>
                    <div class="flex-1 bg-gray-200 rounded-full h-2">
                      <div 
                        class="bg-yellow-400 h-2 rounded-full" 
                        :style="{ width: `${rating === 5 ? 80 : rating === 4 ? 15 : 5}%` }"
                      ></div>
                    </div>
                    <span class="text-sm text-gray-600 w-8">{{ rating === 5 ? 102 : rating === 4 ? 19 : 7 }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Sample Reviews -->
            <div class="space-y-6">
              <div v-for="review in sampleReviews" :key="review.id" class="border-b pb-6">
                <div class="flex items-start gap-4">
                  <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                    <span class="text-blue-600 font-semibold">{{ review.author.charAt(0) }}</span>
                  </div>
                  <div class="flex-1">
                    <div class="flex items-center justify-between mb-2">
                      <h4 class="font-semibold">{{ review.author }}</h4>
                      <span class="text-sm text-gray-500">{{ review.date }}</span>
                    </div>
                    <div class="flex text-yellow-400 mb-2">
                      <svg v-for="star in review.rating" :key="star" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                      </svg>
                    </div>
                    <p class="text-gray-600 mb-2">{{ review.comment }}</p>
                    <div class="flex gap-2">
                      <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded">Đã mua hàng</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Related Products -->
      <div class="mt-12">
        <h2 class="text-3xl font-bold mb-8">Sản phẩm liên quan</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div 
            v-for="relatedProduct in relatedProducts" 
            :key="relatedProduct.id"
            @click="$router.push(`/products/${relatedProduct.id}`)"
            class="bg-white rounded-lg shadow-md overflow-hidden cursor-pointer hover:shadow-xl transition-all"
          >
            <div class="relative pt-[100%] bg-gray-100">
              <img 
                :src="relatedProduct.image" 
                :alt="relatedProduct.name"
                class="absolute inset-0 w-full h-full object-cover"
                @error="handleImageError"
              />
            </div>
            <div class="p-4">
              <p class="text-sm text-gray-500">{{ relatedProduct.brand }}</p>
              <h3 class="font-semibold text-gray-800 mb-2">{{ relatedProduct.name }}</h3>
              <p class="text-lg font-bold text-blue-600">{{ formatPrice(relatedProduct.price) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Product Not Found -->
    <div v-else class="container mx-auto px-4 py-16 text-center">
      <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <h2 class="text-2xl font-bold text-gray-700 mb-2">Không tìm thấy sản phẩm</h2>
      <router-link to="/products" class="text-blue-600 hover:underline">Quay lại trang sản phẩm</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const productId = parseInt(route.params.id);

// Active tab
const activeTab = ref('description');

// Tabs
const tabs = [
  { id: 'description', label: 'Mô tả' },
  { id: 'specifications', label: 'Thông số kỹ thuật' },
  { id: 'reviews', label: 'Đánh giá' }
];

// Sample products data (trong thực tế sẽ fetch từ API)
const allProducts = [
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
    colors: ['Trắng', 'Đen', 'Xám'],
    sizes: [39, 40, 41, 42, 43]
  },
  { 
    id: 5, 
    name: 'Nike Air Max 270', 
    brand: 'Nike',
    price: 3200000,
    image: '/images/shoes/nike-air-max-2.jpg',
    category: 'Lifestyle',
    colors: ['Xanh', 'Hồng', 'Trắng'],
    sizes: [35, 36, 37, 38, 39, 40]
  },
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
];

// Find current product
const product = computed(() => {
  return allProducts.find(p => p.id === productId);
});

// Selected options
const selectedImage = ref('');
const selectedColor = ref('');
const selectedSize = ref(null);
const quantity = ref(1);

// Product images (main + thumbnails)
const productImages = computed(() => {
  if (!product.value) return [];
  // Trong thực tế, mỗi sản phẩm sẽ có nhiều ảnh từ API
  // Ở đây tạm dùng cùng 1 ảnh cho demo
  return [
    product.value.image,
    product.value.image,
    product.value.image,
    product.value.image
  ];
});

// Related products
const relatedProducts = computed(() => {
  if (!product.value) return [];
  return allProducts
    .filter(p => p.brand === product.value.brand && p.id !== product.value.id)
    .slice(0, 4);
});

// Sample reviews
const sampleReviews = [
  {
    id: 1,
    author: 'Nguyễn Văn A',
    rating: 5,
    date: '15/09/2024',
    comment: 'Giày rất đẹp và chất lượng tốt. Đi rất êm chân, giao hàng nhanh. Sẽ ủng hộ shop lâu dài!'
  },
  {
    id: 2,
    author: 'Trần Thị B',
    rating: 5,
    date: '10/09/2024',
    comment: 'Mình rất hài lòng với sản phẩm này. Đóng gói cẩn thận, giày y hình. Recommend!'
  },
  {
    id: 3,
    author: 'Lê Văn C',
    rating: 4,
    date: '05/09/2024',
    comment: 'Giày đẹp, chất lượng ổn. Tuy nhiên ship hơi lâu. Nhưng nhìn chung ok!'
  }
];

// Initialize selections
onMounted(() => {
  if (product.value) {
    selectedImage.value = product.value.image;
    selectedColor.value = product.value.colors[0];
  }
});

// Format price
const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

// Handle image error
const handleImageError = (event) => {
  event.target.src = '/images/shoes/placeholder.jpg';
};

// Get color classes based on color name
const getColorClasses = (colorName) => {
  const lowerColor = colorName.toLowerCase();
  
  // Màu đơn
  if (lowerColor.includes('đen')) {
    return {
      dot: 'bg-black',
      active: 'border-black bg-black text-white shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('trắng')) {
    return {
      dot: 'bg-white',
      active: 'border-gray-800 bg-white text-black shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('xanh') && !lowerColor.includes('navy')) {
    return {
      dot: 'bg-blue-500',
      active: 'border-blue-600 bg-blue-500 text-white shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('đỏ')) {
    return {
      dot: 'bg-red-500',
      active: 'border-red-600 bg-red-500 text-white shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('xám')) {
    return {
      dot: 'bg-gray-500',
      active: 'border-gray-600 bg-gray-500 text-white shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('hồng')) {
    return {
      dot: 'bg-pink-400',
      active: 'border-pink-500 bg-pink-400 text-white shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('be')) {
    return {
      dot: 'bg-amber-200',
      active: 'border-amber-400 bg-amber-200 text-gray-800 shadow-md transform scale-105'
    };
  }
  if (lowerColor.includes('navy')) {
    return {
      dot: 'bg-blue-900',
      active: 'border-blue-900 bg-blue-900 text-white shadow-md transform scale-105'
    };
  }
  
  // Mặc định
  return {
    dot: 'bg-gray-400',
    active: 'border-black bg-black text-white shadow-md transform scale-105'
  };
};
</script>