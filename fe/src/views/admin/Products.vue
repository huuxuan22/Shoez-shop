<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8 flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Quản lý sản phẩm</h1>
        <p class="text-gray-600 mt-2">Danh sách tất cả sản phẩm</p>
      </div>
      <button 
        @click="showAddProductModal = true"
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
          <input
            type="text"
            v-model="filters.search"
            placeholder="Tên sản phẩm..."
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Danh mục</label>
          <select
            v-model="filters.category"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
          >
            <option value="">Tất cả</option>
            <option value="running">Giày chạy</option>
            <option value="basketball">Giày bóng rổ</option>
            <option value="casual">Giày thường</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Thương hiệu</label>
          <select
            v-model="filters.brand"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
          >
            <option value="">Tất cả</option>
            <option value="nike">Nike</option>
            <option value="adidas">Adidas</option>
            <option value="puma">Puma</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Trạng thái</label>
          <select
            v-model="filters.status"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
          >
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
                SKU
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Danh mục
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Giá
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Tồn kho
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
            <tr v-for="product in products" :key="product.id" class="hover:bg-gray-50">
              <td class="px-6 py-4">
                <input type="checkbox" class="rounded border-gray-300" />
              </td>
              <td class="px-6 py-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gray-200 rounded"></div>
                  <div>
                    <p class="font-medium text-gray-900">{{ product.name }}</p>
                    <p class="text-sm text-gray-500">{{ product.brand }}</p>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ product.sku }}
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ product.category }}
              </td>
              <td class="px-6 py-4 text-sm font-medium text-gray-900">
                ${{ product.price }}
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                <span :class="product.stock < 10 ? 'text-red-600 font-medium' : ''">
                  {{ product.stock }}
                </span>
              </td>
              <td class="px-6 py-4">
                <span
                  class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': product.status === 'active',
                    'bg-gray-100 text-gray-800': product.status === 'inactive',
                    'bg-red-100 text-red-800': product.status === 'out-of-stock'
                  }"
                >
                  {{ getStatusText(product.status) }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm">
                <div class="flex items-center space-x-2">
                  <button class="text-blue-600 hover:text-blue-900">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <button class="text-gray-600 hover:text-gray-900">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                  <button class="text-red-600 hover:text-red-900">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
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
          Hiển thị <span class="font-medium">1</span> đến <span class="font-medium">10</span> trong tổng số <span class="font-medium">50</span> sản phẩm
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

    <!-- Add Product Modal -->
    <div v-if="showAddProductModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-8 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Thêm sản phẩm mới</h2>
          <button @click="closeModal" class="text-gray-400 hover:text-gray-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="createProduct" class="space-y-4">
          <!-- Tên sản phẩm -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Tên sản phẩm *</label>
            <input
              v-model="newProduct.name"
              type="text"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="VD: Nike Air Max 2024"
            />
          </div>

          <!-- Giá -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Giá (VNĐ) *</label>
            <input
              v-model.number="newProduct.price"
              type="number"
              required
              min="0"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="3500000"
            />
          </div>

          <!-- Mô tả -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Mô tả *</label>
            <textarea
              v-model="newProduct.description"
              required
              rows="3"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="Mô tả chi tiết sản phẩm..."
            ></textarea>
          </div>

          <!-- Danh mục & Thương hiệu -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Danh mục *</label>
              <select
                v-model="newProduct.category"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              >
                <option value="">Chọn danh mục</option>
                <option value="running">Giày chạy</option>
                <option value="basketball">Giày bóng rổ</option>
                <option value="lifestyle">Giày thường</option>
                <option value="football">Giày bóng đá</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Thương hiệu *</label>
              <input
                v-model="newProduct.brand"
                type="text"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
                placeholder="Nike, Adidas..."
              />
            </div>
          </div>

          <!-- Tồn kho -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Tồn kho *</label>
            <input
              v-model.number="newProduct.stock"
              type="number"
              required
              min="0"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="50"
            />
          </div>

          <!-- Size (array) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Sizes (phân cách bằng dấu phẩy) *</label>
            <input
              v-model="newProduct.sizesInput"
              type="text"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="38, 39, 40, 41, 42, 43"
            />
          </div>

          <!-- Colors (array) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Màu sắc (phân cách bằng dấu phẩy) *</label>
            <input
              v-model="newProduct.colorsInput"
              type="text"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="black, white, red"
            />
          </div>

          <!-- Images Upload -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Hình ảnh sản phẩm *</label>
            <input
              type="file"
              @change="handleImageUpload"
              accept="image/*"
              multiple
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
            />
            <p class="text-xs text-gray-500 mt-1">Có thể chọn nhiều ảnh. Ảnh đầu tiên sẽ là ảnh chính.</p>
            
            <!-- Preview images -->
            <div v-if="imagePreview.length > 0" class="mt-3 grid grid-cols-4 gap-2">
              <div v-for="(preview, index) in imagePreview" :key="index" class="relative">
                <img :src="preview" class="w-full h-24 object-cover rounded-lg border border-gray-200" />
                <button
                  type="button"
                  @click="removeImage(index)"
                  class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600"
                >
                  ×
                </button>
              </div>
            </div>
          </div>

          <!-- Error message -->
          <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg">
            {{ errorMessage }}
          </div>

          <!-- Success message -->
          <div v-if="successMessage" class="bg-green-50 border border-green-200 text-green-600 px-4 py-3 rounded-lg">
            {{ successMessage }}
          </div>

          <!-- Actions -->
          <div class="flex items-center justify-end space-x-3 pt-4">
            <button
              type="button"
              @click="closeModal"
              class="px-6 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50"
            >
              Hủy
            </button>
            <button
              type="submit"
              :disabled="isSubmitting"
              class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 disabled:opacity-50"
            >
              {{ isSubmitting ? 'Đang tạo...' : 'Tạo sản phẩm' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import axios from 'axios';

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

const products = ref([
  { id: 1, name: 'Nike Air Max 270', brand: 'Nike', sku: 'NK-AM270-BK', category: 'Running', price: 150, stock: 45, status: 'active' },
  { id: 2, name: 'Adidas Ultraboost 21', brand: 'Adidas', sku: 'AD-UB21-WH', category: 'Running', price: 180, stock: 32, status: 'active' },
  { id: 3, name: 'Puma RS-X', brand: 'Puma', sku: 'PM-RSX-RD', category: 'Casual', price: 120, stock: 8, status: 'active' },
  { id: 4, name: 'New Balance 574', brand: 'New Balance', sku: 'NB-574-GY', category: 'Casual', price: 90, stock: 0, status: 'out-of-stock' },
  { id: 5, name: 'Jordan 1 Retro High', brand: 'Nike', sku: 'NK-J1-BK', category: 'Basketball', price: 170, stock: 23, status: 'active' },
  { id: 6, name: 'Adidas Stan Smith', brand: 'Adidas', sku: 'AD-SS-WH', category: 'Casual', price: 85, stock: 56, status: 'active' },
  { id: 7, name: 'Nike Zoom Freak', brand: 'Nike', sku: 'NK-ZF-BL', category: 'Basketball', price: 130, stock: 12, status: 'active' },
  { id: 8, name: 'Puma Suede Classic', brand: 'Puma', sku: 'PM-SC-BK', category: 'Casual', price: 70, stock: 0, status: 'inactive' },
]);

const getStatusText = (status) => {
  const statusMap = {
    'active': 'Đang bán',
    'inactive': 'Ngừng bán',
    'out-of-stock': 'Hết hàng'
  };
  return statusMap[status] || status;
};

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
    
    // Thêm vào danh sách
    products.value.unshift({
      id: productId,
      name: productData.name,
      brand: productData.brand,
      sku: `SKU-${Date.now()}`,
      category: productData.category,
      price: productData.price,
      stock: productData.stock,
      status: 'active'
    });

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

<style scoped>
</style>
