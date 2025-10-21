<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Quản lý sản phẩm</h1>
        <p class="text-gray-600 mt-2">Danh sách tất cả sản phẩm</p>
      </div>
      <button @click="showAddProductModal = true"
        class="bg-black text-white px-6 py-3 rounded-lg hover:bg-gray-800 transition-colors flex items-center space-x-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        <span>Thêm sản phẩm mới</span>
      </button>
    </div>

    <!-- Filters -->
    <div class="bg-white rounded-lg shadow p-6 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
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
      </div>
    </div>

    <!-- Products Table -->
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <div class="overflow-x-auto">
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
                  <div class="w-12 h-12 bg-gray-200 rounded flex items-center justify-center">
                    <span class="text-xs text-gray-500">Ảnh</span>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">{{ product.name }}</p>
                    <p class="text-sm text-gray-500">{{ product.brand }}</p>
                    <p class="text-xs text-gray-400 mt-1">ID: {{ product._id }}</p>
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
                <div class="flex items-center space-x-1">
                  <span class="text-sm font-medium text-gray-900">{{ product.rating }}</span>
                  <svg class="w-4 h-4 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <span class="text-xs text-gray-500">({{ product.totalReviews }})</span>
                </div>
              </td>
              <td class="px-6 py-4">
                <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="getStatusClass(product)">
                  {{ getStatusText(product) }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm">
                <div class="flex items-center space-x-2">
                  <button class="text-blue-600 hover:text-blue-900" title="Xem chi tiết">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <button class="text-gray-600 hover:text-gray-900" title="Chỉnh sửa">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                  <button class="text-red-600 hover:text-red-900" title="Xóa">
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

      <!-- Pagination -->
      <div class="bg-gray-50 px-6 py-4 border-t border-gray-200 flex items-center justify-between">
        <div class="text-sm text-gray-700">
          Hiển thị <span class="font-medium">{{ products.length }}</span> sản phẩm
        </div>
        <div class="flex items-center space-x-2">
          <button class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100">
            Trước
          </button>
          <button class="px-3 py-2 bg-black text-white rounded-lg text-sm">1</button>
          <button class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100">2</button>
          <button class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100">3</button>
          <button class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100">
            Sau
          </button>
        </div>
      </div>
    </div>

    <!-- Add Product Modal (giữ nguyên) -->
    <!-- ... -->
  </AdminLayout>
</template>

<script setup>
import { watch, onMounted, ref, computed } from 'vue';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import axios from 'axios';
import ProductService from "@/api-services/ProductService";

const filters = ref({
  search: '',
  category: '',
  brand: '',
  status: ''
});

const showAddProductModal = ref(false);
const isSubmitting = ref(false);
const errorMessage = ref('');
const successMessage = ref('');
const imageFiles = ref([]);
const imagePreview = ref([]);
const products = ref([]);
const newProduct = ref({
  name: '',
  price: 0,
  description: '',
  category: '',
  brand: '',
  stock: 0,
  sizesInput: '',
  colorsInput: '',
  images: []
});

// Format price to VND
const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND'
  }).format(price);
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
      skip: 0,
      limit: 20,
    });
    console.log(response);

    products.value = response;
  } catch (error) {
    console.error("Fetch products error:", error);
  }
};

onMounted(() => {
  fetchProducts();
});

watch(filters, fetchProducts, { deep: true });

const closeModal = () => {
  showAddProductModal.value = false;
  errorMessage.value = '';
  successMessage.value = '';
  imageFiles.value = [];
  imagePreview.value = [];
  // Reset form
  newProduct.value = {
    name: '',
    price: 0,
    description: '',
    category: '',
    brand: '',
    stock: 0,
    sizesInput: '',
    colorsInput: '',
    images: []
  };
};

const handleImageUpload = (event) => {
  const files = Array.from(event.target.files);
  imageFiles.value = files;

  // Create preview URLs
  imagePreview.value = [];
  files.forEach(file => {
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.value.push(e.target.result);
    };
    reader.readAsDataURL(file);
  });
};

const removeImage = (index) => {
  imageFiles.value.splice(index, 1);
  imagePreview.value.splice(index, 1);
};

const createProduct = async () => {
  try {
    isSubmitting.value = true;
    errorMessage.value = '';
    successMessage.value = '';

    // Validate có ít nhất 1 ảnh
    if (imageFiles.value.length === 0) {
      errorMessage.value = 'Vui lòng chọn ít nhất 1 ảnh sản phẩm';
      isSubmitting.value = false;
      return;
    }

    // Parse sizes và tạo SizeItem objects
    const sizesArray = newProduct.value.sizesInput.split(',').map(s => parseInt(s.trim())).filter(s => !isNaN(s));
    const sizes = sizesArray.map(size => ({
      size: size,
      stock: Math.floor(newProduct.value.stock / sizesArray.length) // Chia đều stock cho mỗi size
    }));

    // Parse colors
    const colors = newProduct.value.colorsInput.split(',').map(c => c.trim()).filter(c => c);

    // Bước 1: Tạo sản phẩm trước
    const productData = {
      name: newProduct.value.name,
      price: newProduct.value.price,
      description: newProduct.value.description,
      category: newProduct.value.category,
      brand: newProduct.value.brand,
      stock: newProduct.value.stock,
      sizes: sizes, // Format: [{size: 39, stock: 10}, {size: 40, stock: 15}]
      colors: colors,
      images: ['placeholder.jpg'], // Tạm thời dùng placeholder
      discount: 0
    };

    const response = await axios.post('http://localhost:8000/api/products/create', productData, {
      withCredentials: true
    });

    const productId = response.data.id;

    // Bước 2: Upload hình ảnh
    if (imageFiles.value.length > 0) {
      const formData = new FormData();
      imageFiles.value.forEach(file => {
        formData.append('files', file);
      });

      try {
        const uploadResponse = await axios.post(
          `http://localhost:8000/api/products/${productId}/upload-images`,
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
            withCredentials: true
          }
        );

        successMessage.value = 'Tạo sản phẩm và upload hình ảnh thành công!';
      } catch (uploadError) {
        console.error('Upload images error:', uploadError);
        successMessage.value = 'Tạo sản phẩm thành công nhưng upload hình ảnh thất bại!';
      }
    } else {
      successMessage.value = 'Tạo sản phẩm thành công!';
    }

    // Refresh danh sách sản phẩm
    await fetchProducts();

    setTimeout(() => {
      closeModal();
    }, 1500);

  } catch (error) {
    console.error('Create product error:', error);
    errorMessage.value = error.response?.data?.detail || 'Có lỗi xảy ra khi tạo sản phẩm';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped></style>