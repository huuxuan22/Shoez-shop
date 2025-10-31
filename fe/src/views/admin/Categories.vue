<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-6 flex items-center justify-between">
      <div>
        <div class="flex items-center gap-3 mb-2">
          <div class="w-12 h-12 bg-black rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
            </svg>
          </div>
          <div>
            <h1 class="text-2xl font-semibold text-gray-900">Danh mục</h1>
            <p class="text-gray-600 mt-1">Quản lý danh mục sản phẩm của cửa hàng</p>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <div class="relative w-80">
          <input v-model="keyword" type="text" placeholder="Tìm theo tên danh mục..."
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
          Thêm danh mục
        </button>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Tổng danh mục</p>
            <h3 class="text-3xl font-bold text-black">{{ categories.length }}</h3>
          </div>
          <div class="w-12 h-12 bg-black rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
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

    <!-- Categories Grid -->
    <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
      </div>

      <!-- Categories List -->
      <div v-else-if="filteredCategories.length > 0" class="divide-y divide-gray-200">
        <div v-for="category in filteredCategories" :key="category.id"
          class="p-6 hover:bg-gray-50 transition-colors">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4 flex-1">
              <!-- Icon -->
              <div class="w-16 h-16 bg-black rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                </svg>
              </div>

              <!-- Category Info -->
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <h3 class="text-xl font-bold text-gray-900">{{ category.name }}</h3>
                  <span
                    :class="category.is_active ? 'bg-black text-white' : 'bg-gray-400 text-white'"
                    class="px-3 py-1 rounded-full text-xs font-semibold">
                    {{ category.is_active ? 'Hoạt động' : 'Vô hiệu hóa' }}
                  </span>
                </div>
                <p v-if="category.description" class="text-gray-600 text-sm">{{ category.description }}</p>
                <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                  <span v-if="category.product_count !== undefined">
                    {{ category.product_count }} sản phẩm
                  </span>
                  <span>•</span>
                  <span>{{ formatDate(category.created_at) }}</span>
                </div>
              </div>
            </div>

            <!-- Actions -->
            <div class="flex items-center gap-2">
              <button @click="editCategory(category)"
                class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors font-medium">
                Sửa
              </button>
              <button @click="confirmDelete(category.id)"
                class="px-4 py-2 border border-black bg-white text-black rounded-lg hover:bg-black hover:text-white transition-colors font-medium">
                Xoá
              </button>
              <button @click="toggleActive(category)"
                :class="[
                  'px-4 py-2 rounded-lg transition-colors font-medium',
                  category.is_active
                    ? 'border border-gray-300 text-gray-700 hover:bg-gray-100'
                    : 'bg-black text-white hover:bg-gray-800'
                ]">
                {{ category.is_active ? 'Vô hiệu hóa' : 'Kích hoạt' }}
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
              d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
          </svg>
        </div>
        <p class="text-gray-600 text-lg font-medium mb-2">Chưa có danh mục nào</p>
        <p class="text-gray-500 text-sm mb-4">Thêm danh mục đầu tiên để bắt đầu</p>
        <button @click="showAddModal = true"
          class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors font-medium">
          Thêm danh mục
        </button>
      </div>
    </div>
  </AdminLayout>

  <!-- Add/Edit Modal -->
  <transition name="modal">
    <div v-if="showAddModal || showEditModal" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4"
      @click.self="closeModal">
      <div class="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md transform transition-all">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gray-900">
            {{ showEditModal ? 'Sửa danh mục' : 'Thêm danh mục mới' }}
          </h2>
          <button @click="closeModal" class="text-gray-400 hover:text-gray-600 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="saveCategory" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Tên danh mục *</label>
            <input v-model="formData.name" type="text" required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black/70"
              placeholder="Nhập tên danh mục" />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Mô tả</label>
            <textarea v-model="formData.description" rows="3"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black/70"
              placeholder="Nhập mô tả danh mục"></textarea>
          </div>

          <div class="flex items-center gap-2">
            <input v-model="formData.is_active" type="checkbox" id="is_active"
              class="w-4 h-4 border-gray-300 rounded focus:ring-black" />
            <label for="is_active" class="text-sm font-medium text-gray-700">Kích hoạt danh mục</label>
          </div>

          <div class="flex justify-end gap-3 pt-4">
            <button type="button" @click="closeModal"
              class="px-6 py-3 rounded-full border-2 border-black text-black bg-white hover:bg-gray-50 font-semibold transition-all duration-200">
              Huỷ
            </button>
            <button type="submit"
              class="px-6 py-3 rounded-full bg-black text-white hover:bg-gray-800 font-semibold transition-all duration-200">
              {{ showEditModal ? 'Cập nhật' : 'Thêm mới' }}
            </button>
          </div>
        </form>
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
import CategoryService from '@/api-services/CategoryService'
import { useToast } from '@/composables/useToast'

const toast = useToast()

const categories = ref([])
const loading = ref(false)
const keyword = ref('')
const showAddModal = ref(false)
const showEditModal = ref(false)
const editingId = ref(null)

const formData = reactive({
  name: '',
  description: '',
  is_active: true
})

const confirm = reactive({ visible: false, message: '', onOk: null })

const activeCount = computed(() => categories.value.filter(c => c.is_active).length)
const inactiveCount = computed(() => categories.value.filter(c => !c.is_active).length)

const filteredCategories = computed(() => {
  const q = keyword.value.trim().toLowerCase()
  if (!q) return categories.value
  return categories.value.filter(c => c.name.toLowerCase().includes(q))
})

const loadCategories = async () => {
  loading.value = true
  try {
    const data = await CategoryService.getAll()
    categories.value = data || []
  } catch (error) {
    console.error('Load categories failed', error)
    toast.error('Không thể tải danh sách danh mục')
  } finally {
    loading.value = false
  }
}

const closeModal = () => {
  showAddModal.value = false
  showEditModal.value = false
  editingId.value = null
  formData.name = ''
  formData.description = ''
  formData.is_active = true
}

const editCategory = (category) => {
  editingId.value = category.id
  formData.name = category.name
  formData.description = category.description || ''
  formData.is_active = category.is_active !== false
  showEditModal.value = true
}

const saveCategory = async () => {
  try {
    if (showEditModal.value && editingId.value) {
      await CategoryService.update(editingId.value, formData)
      toast.success('Cập nhật danh mục thành công!')
    } else {
      await CategoryService.create(formData)
      toast.success('Thêm danh mục thành công!')
    }
    closeModal()
    await loadCategories()
  } catch (error) {
    console.error('Save category failed', error)
    toast.error(
      error?.response?.data?.detail ||
      error?.response?.data?.message ||
      'Thao tác thất bại'
    )
  }
}

const confirmDelete = (id) => {
  confirm.message = 'Bạn có chắc muốn xoá danh mục này?'
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await CategoryService.delete(id)
      toast.success('Đã xoá danh mục thành công!')
      await loadCategories()
    } catch (error) {
      console.error('Delete category failed', error)
    toast.error(
      error?.response?.data?.detail ||
      error?.response?.data?.message ||
      'Xoá danh mục thất bại'
    )
    }
  }
}

const toggleActive = async (category) => {
  try {
    await CategoryService.update(category.id, { is_active: !category.is_active })
    toast.success(category.is_active ? 'Đã vô hiệu hóa danh mục!' : 'Đã kích hoạt danh mục!')
    await loadCategories()
  } catch (error) {
    console.error('Toggle active failed', error)
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

onMounted(() => {
  loadCategories()
})
</script>

<style scoped>
/* Modal transition animations */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-active .bg-white,
.modal-leave-active .bg-white {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .bg-white,
.modal-leave-to .bg-white {
  transform: scale(0.9) translateY(-20px);
  opacity: 0;
}

.modal-enter-to .bg-white,
.modal-leave-from .bg-white {
  transform: scale(1) translateY(0);
  opacity: 1;
}
</style>

