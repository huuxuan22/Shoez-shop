<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-6 flex items-center justify-between">
      <div>
        <div class="flex items-center gap-3 mb-2">
          <div class="w-12 h-12 bg-black rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
            </svg>
          </div>
          <div>
            <h1 class="text-2xl font-semibold text-gray-900">Thương hiệu</h1>
            <p class="text-gray-600 mt-1">Quản lý thương hiệu sản phẩm của cửa hàng</p>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <div class="relative w-80">
          <input v-model="keyword" type="text" placeholder="Tìm theo tên thương hiệu..."
            class="w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black/70 bg-white" />
          <svg class="w-5 h-5 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor"
            viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m21 21-4.35-4.35M11 19a8 8 0 1 1 0-16 8 8 0 0 1 0 16z" />
          </svg>
        </div>
        <button @click="showAddModal = true"
          class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors font-medium flex items-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Thêm thương hiệu
        </button>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Tổng thương hiệu</p>
            <h3 class="text-3xl font-bold text-black">{{ brands.length }}</h3>
          </div>
          <div class="w-12 h-12 bg-black rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
            </svg>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Đang hoạt động</p>
            <h3 class="text-3xl font-bold text-black">{{ activeCount }}</h3>
          </div>
          <div class="w-12 h-12 bg-gray-800 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Đã vô hiệu hóa</p>
            <h3 class="text-3xl font-bold text-black">{{ inactiveCount }}</h3>
          </div>
          <div class="w-12 h-12 bg-gray-400 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Brands Grid -->
    <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
      </div>

      <!-- Brands List -->
      <div v-else-if="filteredBrands.length > 0" class="divide-y divide-gray-200">
        <div v-for="brand in filteredBrands" :key="brand.id"
          class="p-6 hover:bg-gray-50 transition-colors">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4 flex-1">
              <!-- Logo or Icon -->
              <div class="w-16 h-16 bg-gray-100 rounded-xl flex items-center justify-center flex-shrink-0 overflow-hidden border-2 border-gray-200 relative">
                <img 
                  v-if="brand.logo && brand.logo.trim()" 
                  :src="brand.logo.trim()" 
                  :alt="brand.name"
                  @error="handleImageError($event)"
                  @load="handleImageLoad($event)"
                  class="w-full h-full object-contain bg-white"
                  loading="lazy"
                />
                <div v-if="!brand.logo || !brand.logo.trim()" class="w-full h-full flex items-center justify-center bg-gray-100">
                  <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                  </svg>
                </div>
              </div>

              <!-- Brand Info -->
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <h3 class="text-xl font-bold text-gray-900">{{ brand.name }}</h3>
                  <span
                    :class="brand.is_active !== false ? 'bg-black text-white' : 'bg-gray-400 text-white'"
                    class="px-3 py-1 rounded-full text-xs font-semibold">
                    {{ brand.is_active !== false ? 'Hoạt động' : 'Vô hiệu hóa' }}
                  </span>
                </div>
                <p v-if="brand.description" class="text-gray-600 text-sm">{{ brand.description }}</p>
                <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                  <span>{{ formatDate(brand.created_at) }}</span>
                </div>
              </div>
            </div>

            <!-- Actions -->
            <div class="flex items-center gap-2">
              <button @click="editBrand(brand)"
                class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors font-medium">
                Sửa
              </button>
              <button @click="confirmDelete(brand.id)"
                class="px-4 py-2 border border-black bg-white text-black rounded-lg hover:bg-black hover:text-white transition-colors font-medium">
                Xoá
              </button>
              <button @click="toggleActive(brand)"
                :class="[
                  'px-4 py-2 rounded-lg transition-colors font-medium',
                  brand.is_active !== false
                    ? 'border border-gray-300 text-gray-700 hover:bg-gray-100'
                    : 'bg-black text-white hover:bg-gray-800'
                ]">
                {{ brand.is_active !== false ? 'Vô hiệu hóa' : 'Kích hoạt' }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="flex flex-col items-center justify-center py-20">
        <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mb-4">
          <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
          </svg>
        </div>
        <p class="text-gray-600 text-lg font-medium mb-2">Chưa có thương hiệu nào</p>
        <p class="text-gray-500 text-sm mb-4">Thêm thương hiệu đầu tiên để bắt đầu</p>
        <button @click="showAddModal = true"
          class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors font-medium">
          Thêm thương hiệu
        </button>
      </div>
    </div>
  </AdminLayout>

  <!-- Add/Edit Modal -->
  <transition name="modal">
    <div v-if="showAddModal || showEditModal" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4"
      @click.self="closeModal">
      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] flex flex-col transform transition-all overflow-hidden">
        <!-- Modal Header - Fixed -->
        <div class="flex items-center justify-between p-6 border-b border-gray-200 flex-shrink-0">
          <h2 class="text-2xl font-bold text-gray-900">
            {{ showEditModal ? 'Sửa thương hiệu' : 'Thêm thương hiệu mới' }}
          </h2>
          <button @click="closeModal" class="text-gray-400 hover:text-gray-600 transition-colors p-1 rounded-lg hover:bg-gray-100">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Modal Body - Scrollable -->
        <div class="overflow-y-auto flex-1 px-6 py-6">
          <form @submit.prevent="saveBrand" class="space-y-6">
          <div>
            <label class="block text-sm font-semibold text-gray-800 mb-2">
              Tên thương hiệu <span class="text-red-500">*</span>
            </label>
            <input 
              v-model.trim="formData.name" 
              type="text" 
              required
              :class="[
                'w-full px-4 py-3 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-black transition-all text-gray-900 placeholder-gray-400',
                !formData.name || !formData.name.trim() ? 'border-red-300' : 'border-gray-200 focus:border-black'
              ]"
              placeholder="Nhập tên thương hiệu"
              @blur="validateName"
            />
            <p v-if="nameError" class="mt-1 text-sm text-red-600">{{ nameError }}</p>
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-800 mb-3">Logo</label>
            
            <!-- File Upload -->
            <div class="mb-4">
              <label class="block text-xs font-medium text-gray-600 mb-2.5">Upload ảnh (tùy chọn)</label>
              <div class="relative">
                <input 
                  ref="logoFileInput"
                  type="file" 
                  accept="image/*" 
                  @change="handleLogoFileChange"
                  class="hidden"
                  id="logo-upload"
                />
                <label 
                  for="logo-upload"
                  class="flex items-center justify-center gap-2 w-full px-4 py-3 border-2 border-dashed border-gray-300 rounded-xl hover:border-black hover:bg-gray-50 transition-all cursor-pointer group"
                >
                  <svg class="w-5 h-5 text-gray-400 group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                  <span class="text-sm font-medium text-gray-600 group-hover:text-black transition-colors">
                    {{ logoFile ? logoFile.name : 'Chọn file ảnh' }}
                  </span>
                </label>
              </div>
              
              <!-- Preview với styling đẹp hơn -->
              <div v-if="logoPreview" class="mt-4 relative group">
                <div class="relative inline-block">
                  <img 
                    :src="logoPreview" 
                    alt="Logo preview" 
                    class="w-40 h-40 object-contain border-2 border-gray-200 rounded-xl shadow-sm bg-gray-50 p-2"
                  />
                  <button 
                    type="button" 
                    @click="clearLogoFile"
                    class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center shadow-lg hover:bg-red-600 transition-colors opacity-0 group-hover:opacity-100"
                    title="Xóa ảnh"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
            
            <!-- Divider -->
            <div class="flex items-center my-4">
              <div class="flex-1 border-t border-gray-200"></div>
              <span class="px-3 text-xs text-gray-500 font-medium">HOẶC</span>
              <div class="flex-1 border-t border-gray-200"></div>
            </div>
            
            <!-- Logo URL (alternative) -->
            <div>
              <label class="block text-xs font-medium text-gray-600 mb-2.5">Nhập URL logo</label>
              <input 
                v-model="formData.logo" 
                type="url"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black focus:border-black transition-all text-sm text-gray-900 placeholder-gray-400"
                placeholder="https://example.com/logo.png" 
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-800 mb-2">Mô tả</label>
            <textarea v-model="formData.description" rows="4"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-black focus:border-black transition-all text-gray-900 placeholder-gray-400 resize-none"
              placeholder="Nhập mô tả thương hiệu (tùy chọn)"></textarea>
          </div>

          <div class="flex items-center gap-3 p-4 bg-gray-50 rounded-xl border border-gray-200">
            <input 
              v-model="formData.is_active" 
              type="checkbox" 
              id="is_active"
              class="w-5 h-5 border-2 border-gray-300 rounded text-black focus:ring-2 focus:ring-black focus:ring-offset-2 cursor-pointer transition-all" 
            />
            <label for="is_active" class="text-sm font-medium text-gray-800 cursor-pointer flex-1">
              Kích hoạt thương hiệu
            </label>
          </div>
          </form>
        </div>

        <!-- Modal Footer - Fixed -->
        <div class="flex justify-end gap-3 p-6 border-t border-gray-200 bg-gray-50 flex-shrink-0">
          <button type="button" @click="closeModal"
            class="px-6 py-2.5 rounded-xl border-2 border-gray-300 text-gray-700 bg-white hover:bg-gray-50 hover:border-gray-400 font-semibold transition-all duration-200">
            Huỷ
          </button>
          <button type="button" @click="saveBrand"
            class="px-6 py-2.5 rounded-xl bg-black text-white hover:bg-gray-800 font-semibold transition-all duration-200 shadow-lg hover:shadow-xl">
            {{ showEditModal ? 'Cập nhật' : 'Thêm mới' }}
          </button>
        </div>
      </div>
    </div>
  </transition>

  <!-- Confirm Delete Modal -->
  <transition name="modal">
    <div v-if="confirm.visible" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4"
      @click.self="confirm.visible = false">
      <div class="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md transform transition-all">
        <div class="flex justify-center mb-4">
          <div class="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center">
            <svg class="w-8 h-8 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
        </div>
        <p class="text-center text-gray-900 text-xl font-semibold mb-8 leading-relaxed">
          {{ confirm.message }}
        </p>
        <div class="flex justify-center gap-4">
          <button @click="confirm.visible = false"
            class="px-8 py-3 rounded-full border-2 border-black text-black bg-white hover:bg-gray-50 font-semibold transition-all duration-200 min-w-[120px]">
            Huỷ
          </button>
          <button @click="confirm.onOk"
            class="px-8 py-3 rounded-full bg-black text-white hover:bg-gray-800 font-semibold transition-all duration-200 min-w-[120px]">
            Xác nhận
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import AdminLayout from '@/layouts/admin/AdminLayout.vue'
import BrandService from '@/api-services/BrandService'
import { useToast } from '@/composables/useToast'

const toast = useToast()

const brands = ref([])
const loading = ref(false)
const keyword = ref('')
const showAddModal = ref(false)
const showEditModal = ref(false)
const editingId = ref(null)

const formData = reactive({
  name: '',
  logo: '',
  description: '',
  is_active: true
})

const logoFile = ref(null)
const logoPreview = ref(null)
const logoFileInput = ref(null)
const nameError = ref('')

const confirm = reactive({ visible: false, message: '', onOk: null })

const activeCount = computed(() => brands.value.filter(b => b.is_active !== false).length)
const inactiveCount = computed(() => brands.value.filter(b => b.is_active === false).length)

const filteredBrands = computed(() => {
  const q = keyword.value.trim().toLowerCase()
  if (!q) return brands.value
  return brands.value.filter(b => b.name.toLowerCase().includes(q))
})

const loadBrands = async () => {
  loading.value = true
  try {
    const data = await BrandService.getAll()
    // Backend giờ trả về array trực tiếp giống Categories
    brands.value = data || []
    
    // Tự động đồng bộ logos nếu có brands không có logo
    const brandsWithoutLogo = brands.value.filter(b => !b.logo || !b.logo.trim())
    if (brandsWithoutLogo.length > 0) {
      // Tự động đồng bộ logos từ MinIO (chạy ngầm, không hiển thị loading)
      try {
        await BrandService.syncLogos()
        // Reload lại brands sau khi sync
        const updatedData = await BrandService.getAll()
        brands.value = updatedData || []
      } catch (syncError) {
        // Nếu sync thất bại thì bỏ qua, không ảnh hưởng đến hiển thị
      }
    }
  } catch (error) {
    toast.error('Không thể tải danh sách thương hiệu')
  } finally {
    loading.value = false
  }
}

const closeModal = () => {
  showAddModal.value = false
  showEditModal.value = false
  editingId.value = null
  formData.name = ''
  formData.logo = ''
  formData.description = ''
  formData.is_active = true
  logoFile.value = null
  logoPreview.value = null
  nameError.value = ''
}

const validateName = () => {
  if (!formData.name || !formData.name.trim()) {
    nameError.value = 'Tên thương hiệu là bắt buộc'
  } else {
    nameError.value = ''
  }
}

const handleLogoFileChange = (event) => {
  const file = event.target.files?.[0]
  if (file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
      toast.error('File phải là hình ảnh')
      event.target.value = ''
      return
    }
    
    // Validate file size (max 5MB)
    if (file.size > 5 * 1024 * 1024) {
      toast.error('Kích thước file không được vượt quá 5MB')
      event.target.value = ''
      return
    }
    
    logoFile.value = file
    
    // Create preview
    const reader = new FileReader()
    reader.onload = (e) => {
      logoPreview.value = e.target.result
    }
    reader.readAsDataURL(file)
    
    // Clear URL input when file is selected
    formData.logo = ''
  }
}

const clearLogoFile = () => {
  logoFile.value = null
  logoPreview.value = null
  // Reset file input
  if (logoFileInput.value) {
    logoFileInput.value.value = ''
  }
}

const editBrand = (brand) => {
  editingId.value = brand.id
  formData.name = brand.name
  formData.logo = brand.logo || ''
  formData.description = brand.description || ''
  formData.is_active = brand.is_active !== false
  logoFile.value = null
  logoPreview.value = brand.logo || null
  showEditModal.value = true
}

const saveBrand = async () => {
  try {
    // Validate form trước khi gửi
    const trimmedName = formData.name?.trim() || ''
    if (!trimmedName) {
      toast.error('Tên thương hiệu là bắt buộc')
      nameError.value = 'Tên thương hiệu là bắt buộc'
      return
    }
    
    // Reset error
    nameError.value = ''
    
    let response
    const brandName = trimmedName
    
    
    if (showEditModal.value && editingId.value) {
      // Cập nhật thương hiệu
      response = await BrandService.update(editingId.value, formData, logoFile.value)
      // Kiểm tra response thành công
      if (response && (response.message || response.data)) {
        toast.success('Cập nhật thương hiệu thành công!')
        // Load lại danh sách trước
        await loadBrands()
        // Kiểm tra brand đã có trong danh sách chưa
        const updatedBrand = brands.value.find(b => 
          b.id === editingId.value || b._id === editingId.value
        )
        if (updatedBrand) {
          closeModal()
        } else {
          await new Promise(resolve => setTimeout(resolve, 500))
          await loadBrands()
          closeModal()
        }
      } else {
        throw new Error('Không nhận được phản hồi từ server')
      }
    } else {
      // Thêm thương hiệu mới
      response = await BrandService.create(formData, logoFile.value)
      if (response && (response.message || response.data)) {
        toast.success('Thêm thương hiệu thành công!')
        
        const createdBrandData = response.data?.data || response.data
        const newBrandId = createdBrandData?.id || createdBrandData?._id
        
        await loadBrands()
        
        let brandFound = false
        let retryCount = 0
        const maxRetries = 5
        
        while (!brandFound && retryCount < maxRetries) {
          brandFound = brands.value.some(b => {
            const nameMatch = b.name && b.name.trim().toLowerCase() === brandName.toLowerCase()
            const idMatch = newBrandId && (b.id === newBrandId || b._id === newBrandId)
            return nameMatch || idMatch
          })
          
          if (!brandFound && retryCount < maxRetries - 1) {
            await new Promise(resolve => setTimeout(resolve, 300))
            await loadBrands()
            retryCount++
          } else {
            break
          }
        }
        
        if (brandFound) {
          // Brand đã có trong danh sách, đóng modal
          closeModal()
        } else {
          // Sau nhiều lần retry vẫn chưa thấy, nhưng đã thành công nên vẫn đóng modal
          closeModal()
        }
      } else {
        throw new Error('Không nhận được phản hồi từ server')
      }
    }
  } catch (error) {
    toast.error(
      error?.response?.data?.detail ||
      error?.response?.data?.message ||
      error?.message ||
      'Thao tác thất bại'
    )
    // Không đóng modal nếu có lỗi để user có thể sửa lại
  }
}

const confirmDelete = (id) => {
  confirm.message = 'Bạn có chắc muốn xoá thương hiệu này?'
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await BrandService.delete(id)
      toast.success('Đã xoá thương hiệu thành công!')
      await loadBrands()
    } catch (error) {
      toast.error(
        error?.response?.data?.detail ||
        error?.response?.data?.message ||
        'Xoá thương hiệu thất bại'
      )
    }
  }
}

const toggleActive = async (brand) => {
  try {
    const currentActive = brand.is_active !== false
    await BrandService.update(brand.id, { is_active: !currentActive })
    toast.success(currentActive ? 'Đã vô hiệu hóa thương hiệu!' : 'Đã kích hoạt thương hiệu!')
    await loadBrands()
  } catch (error) {
    toast.error(
      error?.response?.data?.detail ||
      error?.response?.data?.message ||
      'Thao tác thất bại'
    )
  }
}

const formatDate = (d) => {
  if (!d) return '-'
  try {
    return new Date(d).toLocaleDateString('vi-VN')
  } catch {
    return '-'
  }
}

const handleImageError = (event) => {
  // Khi ảnh không load được, ẩn img và hiển thị placeholder
  const img = event.target
  
  // Ẩn img element
  img.style.display = 'none'
  
  // Hiển thị placeholder thay thế
  const parent = img.parentElement
  if (parent && !parent.querySelector('svg')) {
    const placeholder = document.createElement('div')
    placeholder.className = 'w-full h-full flex items-center justify-center bg-gray-100 absolute inset-0'
    placeholder.innerHTML = `
      <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
      </svg>
    `
    parent.appendChild(placeholder)
  }
}

const handleImageLoad = (event) => {
  // Khi ảnh load thành công, đảm bảo nó hiển thị
  const img = event.target
  img.style.display = 'block'
}

onMounted(() => {
  loadBrands()
})
</script>

<style scoped>
/* Custom scrollbar for modal */
.overflow-y-auto::-webkit-scrollbar {
  width: 8px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

/* Modal transition animations */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-active .bg-white,
.modal-leave-active .bg-white {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .bg-white,
.modal-leave-to .bg-white {
  transform: scale(0.95) translateY(-10px);
  opacity: 0;
}

.modal-enter-to .bg-white,
.modal-leave-from .bg-white {
  transform: scale(1) translateY(0);
  opacity: 1;
}

/* Input focus animation */
input:focus,
textarea:focus {
  animation: focusPulse 0.3s ease;
}

@keyframes focusPulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.01);
  }
  100% {
    transform: scale(1);
  }
}
</style>
