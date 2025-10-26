<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Quản lý sản phẩm</h1>
        <p class="text-gray-600 mt-2">Danh sách tất cả sản phẩm</p>
      </div>
      <button @click="showAddProductModal = true"
        class="bg-black text-white px-6 py-3 rounded-lg hover:bg-gray-800 transition-colors flex items-center space-x-2 cursor-pointer">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        <span>Thêm sản phẩm mới</span>
      </button>
    </div>

    <!-- Filters -->
    <div class="bg-white rounded-lg shadow p-6 mb-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Tìm kiếm</label>
          <input type="text" v-model="filters.search" placeholder="Tên sản phẩm..."
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Danh mục</label>
          <select v-model="filters.category"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
            <option value="">Tất cả</option>
            <option value="Sneaker">Sneaker</option>
            <option value="Running">Running</option>
            <option value="Basketball">Basketball</option>
            <option value="Lifestyle">Lifestyle</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Thương hiệu</label>
          <select v-model="filters.brand"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
            <option value="">Tất cả</option>
            <option value="Nike">Nike</option>
            <option value="Adidas">Adidas</option>
            <option value="Puma">Puma</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Trạng thái</label>
          <select v-model="filters.status"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
            <option value="">Tất cả</option>
            <option value="active">Đang bán</option>
            <option value="inactive">Ngừng bán</option>
            <option value="out-of-stock">Hết hàng</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Sắp xếp</label>
          <select v-model="sortBy" @change="fetchProducts"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
            <option value="created_at">Ngày tạo</option>
            <option value="name">Tên sản phẩm</option>
            <option value="price">Giá</option>
            <option value="stock">Số lượng</option>
          </select>
        </div>
      </div>

      <div class="mt-4 flex items-center space-x-4">
        <div class="flex items-center space-x-2">
          <label class="text-sm font-medium text-gray-700">Thứ tự:</label>
          <select v-model="sortOrder" @change="fetchProducts"
            class="px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-black">
            <option value="desc">Mới nhất</option>
            <option value="asc">Cũ nhất</option>
          </select>
        </div>
      </div>

      <!-- Rating Filter -->
      <div class="mt-4 flex items-center space-x-4">
        <div class="flex items-center space-x-2">
          <label class="text-sm font-medium text-gray-700">Đánh giá từ:</label>
          <input type="number" v-model="filters.min_rating" placeholder="0" min="0" max="5" step="0.1"
            class="w-20 px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-black" />
          <span class="text-sm text-gray-500">⭐</span>
        </div>
        <div class="flex items-center space-x-2">
          <label class="text-sm font-medium text-gray-700">Đến:</label>
          <input type="number" v-model="filters.max_rating" placeholder="5" min="0" max="5" step="0.1"
            class="w-20 px-3 py-1 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-black" />
          <span class="text-sm text-gray-500">⭐</span>
        </div>
        <button @click="clearRatingFilter"
          class="px-3 py-1 text-sm text-gray-600 hover:text-gray-800 underline cursor-pointer">
          Xóa filter đánh giá
        </button>
      </div>

      <!-- Rating Presets -->
      <div class="mt-2 flex items-center space-x-2">
        <span class="text-sm text-gray-500">Nhanh:</span>
        <button @click="setRatingFilter(4, 5)"
          class="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 rounded hover:bg-yellow-200 cursor-pointer">
          ⭐⭐⭐⭐+ (4-5 sao)
        </button>
        <button @click="setRatingFilter(3, 4)"
          class="px-2 py-1 text-xs bg-orange-100 text-orange-800 rounded hover:bg-orange-200 cursor-pointer">
          ⭐⭐⭐+ (3-4 sao)
        </button>
        <button @click="setRatingFilter(2, 3)"
          class="px-2 py-1 text-xs bg-red-100 text-red-800 rounded hover:bg-red-200 cursor-pointer">
          ⭐⭐+ (2-3 sao)
        </button>
        <button @click="setRatingFilter(0, 2)"
          class="px-2 py-1 text-xs bg-gray-100 text-gray-800 rounded hover:bg-gray-200 cursor-pointer">
          ⭐+ (0-2 sao)
        </button>
      </div>
    </div>

    <!-- Products Table -->
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <!-- Desktop Table View -->
      <div class="hidden lg:block overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b border-gray-200">
            <tr>
              <th class="px-6 py-3 text-left">
                <input type="checkbox" class="rounded border-gray-300" />
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Sản phẩm
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Danh mục
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Giá
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Giảm giá
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Tồn kho
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Đánh giá
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Trạng thái
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Ngày tạo
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Hành động
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="product in products" :key="product._id" class="hover:bg-gray-50">
              <td class="px-6 py-4">
                <input type="checkbox" class="rounded border-gray-300" />
              </td>
              <td class="px-6 py-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gray-200 rounded flex items-center justify-center overflow-hidden">
                    <img v-if="product.images && product.images.length > 0" :src="product.images[0]" :alt="product.name"
                      class="w-full h-full object-cover" />
                    <span v-else class="text-xs text-gray-500">Ảnh</span>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">{{ product.name }}</p>
                    <p class="text-sm text-gray-500">{{ product.brand }}</p>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ product.category }}
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">
                  {{ formatPrice(product.price) }}
                </div>
                <div v-if="product.discount > 0" class="text-sm text-green-600">
                  {{ formatPrice(calculateDiscountedPrice(product.price, product.discount)) }}
                </div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                <span v-if="product.discount > 0" class="bg-red-100 text-red-800 px-2 py-1 rounded-full text-xs">
                  -{{ product.discount }}%
                </span>
                <span v-else class="text-gray-400">Không</span>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm text-gray-900">
                  {{ product.stock }} sản phẩm
                </div>
                <div class="text-xs text-gray-500">
                  {{ getAvailableSizes(product.sizes) }} size
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="flex flex-col items-start space-y-1">
                  <span class="text-sm font-medium text-gray-900">{{ formatRating(product.rating) }}</span>
                  <span class="text-xs text-gray-500">({{ product.totalReviews }} đánh giá)</span>
                </div>
              </td>
              <td class="px-6 py-4">
                <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="getStatusClass(product)">
                  {{ getStatusText(product) }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm text-gray-500">
                {{ formatDate(product.created_at) }}
              </td>
              <td class="px-6 py-4 text-sm">
                <div class="flex items-center space-x-2">
                  <button @click="showProductDetail(product._id)"
                    class="text-blue-600 hover:text-blue-900 cursor-pointer" title="Xem chi tiết">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <button @click="editProduct(product)" class="text-gray-600 hover:text-gray-900 cursor-pointer"
                    title="Chỉnh sửa">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                  <button @click="showDeleteConfirmModal(product)"
                    class="text-red-600 hover:text-red-900 cursor-pointer" title="Xóa">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Mobile Card View -->
      <div class="lg:hidden">
        <div class="p-4 space-y-4">
          <div v-for="product in products" :key="product.id" class="border border-gray-200 rounded-lg p-4">
            <div class="flex items-start justify-between mb-3">
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-gray-200 rounded flex items-center justify-center overflow-hidden">
                  <img v-if="product.images && product.images.length > 0" :src="product.images[0]" :alt="product.name"
                    class="w-full h-full object-cover" />
                  <span v-else class="text-xs text-gray-500">Ảnh</span>
                </div>
                <div>
                  <h3 class="font-medium text-gray-900">{{ product.name }}</h3>
                  <p class="text-sm text-gray-500">{{ product.brand }}</p>
                </div>
              </div>
              <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                :class="getStatusClass(product)">
                {{ getStatusText(product) }}
              </span>
            </div>

            <div class="grid grid-cols-2 gap-3 text-sm mb-3">
              <div>
                <span class="text-gray-500">Danh mục:</span>
                <span class="ml-1 font-medium">{{ product.category }}</span>
              </div>
              <div>
                <span class="text-gray-500">Giá:</span>
                <span class="ml-1 font-medium">{{ formatPrice(product.price) }}</span>
              </div>
              <div>
                <span class="text-gray-500">Tồn kho:</span>
                <span class="ml-1 font-medium">{{ product.stock }}</span>
              </div>
              <div>
                <span class="text-gray-500">Đánh giá:</span>
                <span class="ml-1 font-medium">{{ formatRating(product.rating) }}</span>
              </div>
            </div>

            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500">{{ formatDate(product.created_at) }}</span>
              <div class="flex items-center space-x-2">
                <button @click="showProductDetail(product._id)"
                  class="text-blue-600 hover:text-blue-900 cursor-pointer p-1" title="Xem chi tiết">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
                <button @click="editProduct(product)" class="text-gray-600 hover:text-gray-900 cursor-pointer p-1"
                  title="Chỉnh sửa">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
                <button @click="showDeleteConfirmModal(product)"
                  class="text-red-600 hover:text-red-900 cursor-pointer p-1" title="Xóa">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Pagination -->
      <div class="bg-gray-50 px-4 lg:px-6 py-4 border-t border-gray-200">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between space-y-4 lg:space-y-0">
          <div class="flex flex-col sm:flex-row sm:items-center space-y-2 sm:space-y-0 sm:space-x-4">
            <div class="text-sm text-gray-700">
              Hiển thị <span class="font-medium">{{ products.length }}</span> trong tổng số <span class="font-medium">{{
                totalProducts }}</span> sản phẩm
            </div>
            <div class="flex items-center space-x-2">
              <label class="text-sm text-gray-700">Hiển thị:</label>
              <select v-model="itemsPerPage" @change="fetchProducts"
                class="border border-gray-300 rounded-lg px-3 py-1 text-sm">
                <option value="5">5</option>
                <option value="10">10</option>
                <option value="20">20</option>
                <option value="50">50</option>
              </select>
            </div>
          </div>
          <div class="flex items-center justify-center lg:justify-end space-x-2">
            <button @click="prevPage" :disabled="currentPage === 1"
              class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer">
              Trước
            </button>

            <!-- Page numbers - hide some on mobile -->
            <template v-for="page in getPageNumbers()" :key="page">
              <button @click="goToPage(page)" :class="[
                'px-3 py-2 border rounded-lg text-sm cursor-pointer',
                currentPage === page
                  ? 'bg-black text-white border-black'
                  : 'border-gray-300 text-gray-700 hover:bg-gray-100'
              ]">
                {{ page }}
              </button>
            </template>

            <button @click="nextPage" :disabled="currentPage === totalPages"
              class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer">
              Sau
            </button>
          </div>
        </div>
      </div>
    </div>

    <transition name="fade">
      <Notification v-if="showNotificationError" :message="messageError" :type="typeNotification"
        @close="closeNotification" />
    </transition>


    <!-- Product Form Modal -->
    <ProductFormModal :is-visible="showAddProductModal" :is-edit-mode="isEditMode" :editing-product="editingProduct"
      @close="closeModal" @success="handleProductSuccess" @error="handleProductError" />

    <!-- Product Detail Modal -->
    <ProductDetailModal :product="selectedProduct" :is-visible="showProductDetailModal" @close="closeProductDetailModal"
      @edit="editProductFromDetail" @delete="deleteProductFromDetail" />

    <!-- Delete Confirm Modal -->
    <ConfirmModal :show="showDeleteConfirm" :message="deleteConfirmMessage" @confirm="confirmDeleteProduct"
      @cancel="cancelDeleteProduct" />
  </AdminLayout>
</template>


<script setup>
import { watch, onMounted, ref, computed } from 'vue';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import ProductDetailModal from '@/components/admin/ProductDetailModal.vue';
import ProductFormModal from '@/components/admin/ProductFormModal.vue';
import ConfirmModal from '@/components/ConfirmModal.vue';
import ProductService from "@/api-services/ProductService";
import ToastNotification from '@/components/ToastNotification.vue';
// Khi thêm sản phẩm thành công từ modal
const onProductCreated = () => {
  fetchProducts();
  closeModal();
};

const filters = ref({
  search: '',
  category: '',
  brand: '',
  status: '',
  min_rating: '',
  max_rating: ''
});

const sortBy = ref('created_at');
const sortOrder = ref('desc');

const showAddProductModal = ref(false);
const showNotificationError = ref(false);
const messageError = ref("");
const typeNotification = ref("")
const isEditMode = ref(false);
const editingProduct = ref(null);
const products = ref([]);
const currentPage = ref(1);
const itemsPerPage = ref(10);
const totalProducts = ref(0);
const totalPages = ref(0);

// Product Detail Modal
const showProductDetailModal = ref(false);
const selectedProduct = ref(null);

// close notification error 
const closeNotificationError = () => {
  showNotificationError.value = false;
}

// Delete Confirm Modal
const showDeleteConfirm = ref(false);
const productToDelete = ref(null);

// Computed property for delete confirm message
const deleteConfirmMessage = computed(() => {
  if (!productToDelete.value) return 'Bạn có chắc chắn muốn xóa sản phẩm này?';
  return `Bạn có chắc chắn muốn xóa sản phẩm "${productToDelete.value.name}"? Hành động này không thể hoàn tác.`;
});

const handleProductSuccess = (data) => {
  fetchProducts();
};

const handleProductError = (error) => {
  showNotificationError.value = true;
  messageError.value = error.detail;
  typeNotification.value = "error"
};

// Format price to VND
const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND'
  }).format(price);
};

// Format date
const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleDateString('vi-VN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
};

// Format rating stars
const formatRating = (rating) => {
  if (!rating) return 'Chưa đánh giá';
  const stars = '⭐'.repeat(Math.floor(rating));
  const halfStar = rating % 1 >= 0.5 ? '⭐' : '';
  return `${stars}${halfStar} ${rating.toFixed(1)}`;
};

// Calculate discounted price
const calculateDiscountedPrice = (price, discount) => {
  return price * (1 - discount / 100);
};

// Get available sizes text
const getAvailableSizes = (sizes) => {
  if (!sizes || !Array.isArray(sizes)) return '0';
  return sizes.map(size => size.size).join(', ');
};

// Get status text based on product data
const getStatusText = (product) => {
  if (product.stock === 0) return 'Hết hàng';
  if (product.stock < 10) return 'Sắp hết';
  return 'Đang bán';
};

// Get status class based on product data
const getStatusClass = (product) => {
  if (product.stock === 0) return 'bg-red-100 text-red-800';
  if (product.stock < 10) return 'bg-yellow-100 text-yellow-800';
  return 'bg-green-100 text-green-800';
};

const fetchProducts = async () => {
  try {
    const response = await ProductService.getAll({
      name: filters.value.search,
      brand: filters.value.brand,
      category: filters.value.category,
      status: filters.value.status,
      min_rating: filters.value.min_rating ? parseFloat(filters.value.min_rating) : null,
      max_rating: filters.value.max_rating ? parseFloat(filters.value.max_rating) : null,
      skip: (currentPage.value - 1) * itemsPerPage.value,
      limit: itemsPerPage.value,
      sort_by: sortBy.value,
      sort_order: sortOrder.value
    });

    products.value = response.products;
    totalProducts.value = response.total;
    totalPages.value = response.total_pages;
  } catch (error) {

  }
};

// Pagination methods
const getPageNumbers = () => {
  const pages = [];
  const maxVisiblePages = 5;
  const startPage = Math.max(1, currentPage.value - Math.floor(maxVisiblePages / 2));
  const endPage = Math.min(totalPages.value, startPage + maxVisiblePages - 1);

  for (let i = startPage; i <= endPage; i++) {
    pages.push(i);
  }

  return pages;
};

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
    fetchProducts();
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchProducts();
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchProducts();
  }
};

// Clear rating filter
const clearRatingFilter = () => {
  filters.value.min_rating = '';
  filters.value.max_rating = '';
  fetchProducts();
};

// Set rating filter
const setRatingFilter = (min, max) => {
  filters.value.min_rating = min;
  filters.value.max_rating = max;
  fetchProducts();
};

// Reset pagination when filters or sort change
watch([filters, sortBy, sortOrder], () => {
  currentPage.value = 1;
  fetchProducts();
}, { deep: true });

onMounted(() => {
  fetchProducts();
});

const closeModal = () => {
  showAddProductModal.value = false;
  isEditMode.value = false;
  editingProduct.value = null;
};

const showProductDetail = (productId) => {
  // Tìm sản phẩm từ danh sách đã có
  const product = products.value.find(p => p._id === productId);
  if (product) {
    selectedProduct.value = product;
    showProductDetailModal.value = true;
  }
};

const closeProductDetailModal = () => {
  showProductDetailModal.value = false;
  selectedProduct.value = null;
};

const editProduct = (product) => {
  // Set edit mode
  isEditMode.value = true;
  editingProduct.value = product;

  // Show modal
  showAddProductModal.value = true;
};

const editProductFromDetail = (product) => {
  // Set edit mode
  isEditMode.value = true;
  editingProduct.value = product;

  // Show modal
  showAddProductModal.value = true;

  // Close detail modal
  closeProductDetailModal();
};

// Delete Product Functions
const showDeleteConfirmModal = (product) => {
  productToDelete.value = product;
  showDeleteConfirm.value = true;
};

const cancelDeleteProduct = () => {
  showDeleteConfirm.value = false;
  productToDelete.value = null;
};

const confirmDeleteProduct = async () => {
  if (!productToDelete.value) return;

  try {
    await ProductService.delete(productToDelete.value._id || productToDelete.value.id);

    // Refresh products list to get updated data from server
    await fetchProducts();

    // Close modals
    showDeleteConfirm.value = false;
    productToDelete.value = null;

    // Show success message
    successMessage.value = 'Xóa sản phẩm thành công!';
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Có lỗi xảy ra khi xóa sản phẩm';
    setTimeout(() => {
      errorMessage.value = '';
    }, 3000);
  }
};

const deleteProductFromDetail = async (product) => {
  try {
    await ProductService.delete(product.id);

    // Refresh products list to get updated data from server
    await fetchProducts();

    closeProductDetailModal();
    // Show success message
    successMessage.value = 'Xóa sản phẩm thành công!';
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Có lỗi xảy ra khi xóa sản phẩm';
    setTimeout(() => {
      errorMessage.value = '';
    }, 3000);
  }
};
</script>

<style scoped></style>