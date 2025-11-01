<template>
    <!-- Product Form Modal -->
    <div v-if="isVisible" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-2 sm:p-4 z-50">
        <div class="bg-white rounded-lg w-full max-w-4xl max-h-[95vh] overflow-y-auto">
            <div class="p-6 border-b border-gray-200">
                <h2 class="text-2xl font-bold text-gray-900">{{ isEditMode ? 'Chỉnh sửa sản phẩm' : 'Thêm sản phẩm mới'
                }}
                </h2>
            </div>

            <form @submit.prevent="submitProduct" class="p-4 sm:p-6 space-y-6">
                <!-- Thông báo lỗi và thành công -->
                <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
                    {{ errorMessage }}
                </div>
                <div v-if="successMessage"
                    class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded">
                    {{ successMessage }}
                </div>

                <!-- Thông tin cơ bản -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Tên sản phẩm *</label>
                        <input v-model="productForm.name" type="text" required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Giá *</label>
                        <input v-model.number="productForm.price" type="number" min="0" required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Danh mục *</label>
                        <select v-model="productForm.category" required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
                            <option value="">Chọn danh mục</option>
                            <option v-for="c in categoryOptions" :key="c.id || c.name" :value="c.name">
                                {{ c.name }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Thương hiệu *</label>
                        <select v-model="productForm.brand" required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
                            <option value="">Chọn thương hiệu</option>
                            <option value="Nike">Nike</option>
                            <option value="Adidas">Adidas</option>
                            <option value="Puma">Puma</option>
                        </select>
                    </div>
                </div>

                <!-- Mô tả -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Mô tả sản phẩm</label>
                    <textarea v-model="productForm.description" rows="3"
                        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"></textarea>
                </div>

                <!-- Kích thước và màu sắc -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Kích thước (phân cách bằng dấu phẩy)
                            *</label>
                        <input v-model="productForm.sizesInput" type="text" placeholder="Ví dụ: 39, 40, 41, 42" required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Màu sắc (phân cách bằng dấu phẩy)
                            *</label>
                        <input v-model="productForm.colorsInput" type="text" placeholder="Ví dụ: Đen, Trắng, Xanh"
                            required
                            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
                    </div>
                </div>

                <!-- Tồn kho -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Số lượng tồn kho *</label>
                    <input v-model.number="productForm.stock" type="number" min="0" required
                        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
                </div>

                <!-- Upload hình ảnh -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">
                        Hình ảnh sản phẩm {{ isEditMode ? '(chọn thêm ảnh mới)' : '*' }}
                    </label>
                    <input type="file" multiple accept="image/*" @change="handleImageUpload"
                        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />

                    <!-- Existing images (for edit mode) -->
                    <div v-if="isEditMode && productForm.images && productForm.images.length > 0" class="mt-4">
                        <h4 class="text-sm font-medium text-gray-700 mb-2">Ảnh hiện tại:</h4>
                        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
                            <div v-for="(image, index) in productForm.images" :key="`existing-${index}`"
                                class="relative">
                                <img :src="image" :alt="`Existing ${index + 1}`"
                                    class="w-full h-32 object-cover rounded-lg" />
                                <div
                                    class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 hover:opacity-100 transition-opacity">
                                    <span class="text-white text-sm">Ảnh hiện tại</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Preview new images -->
                    <div v-if="imagePreview.length" class="mt-4">
                        <h4 class="text-sm font-medium text-gray-700 mb-2">Ảnh mới:</h4>
                        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
                            <div v-for="(preview, index) in imagePreview" :key="`new-${index}`" class="relative">
                                <img :src="preview" :alt="`Preview ${index + 1}`"
                                    class="w-full h-32 object-cover rounded-lg" />
                                <button type="button" @click="removeImage(index)"
                                    class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs cursor-pointer">
                                    ×
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Actions -->
                <div
                    class="flex flex-col sm:flex-row sm:justify-end space-y-2 sm:space-y-0 sm:space-x-4 pt-6 border-t border-gray-200">
                    <button type="button" @click="closeModal"
                        class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer">
                        Hủy
                    </button>
                    <button type="submit" :disabled="isSubmitting"
                        class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer">
                        {{ isSubmitting ? (isEditMode ? 'Đang cập nhật...' : 'Đang tạo...') : (isEditMode ? 'Cập nhật sản phẩm' : 'Tạo Sản Phẩm') }}
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, computed, onMounted } from 'vue'
import ProductService from "@/api-services/ProductService"
import CategoryService from "@/api-services/CategoryService"

// Props
const props = defineProps({
    isVisible: {
        type: Boolean,
        default: false
    },
    isEditMode: {
        type: Boolean,
        default: false
    },
    editingProduct: {
        type: Object,
        default: null
    }
})

// Emits
const emit = defineEmits(['close', 'success', 'error'])

// Reactive data
const isSubmitting = ref(false)
const errorMessage = ref('')
const successMessage = ref('')
const imageFiles = ref([])
const imagePreview = ref([])
const categoryOptions = ref([])

// Product form data
const productForm = ref({
    name: '',
    price: 0,
    description: '',
    category: '',
    brand: '',
    stock: 0,
    sizesInput: '',
    colorsInput: '',
    images: []
})

// Computed
const editingProductId = computed(() => {
    return props.editingProduct?._id || props.editingProduct?.id || ''
})

// Methods
const resetForm = () => {
    productForm.value = {
        name: '',
        price: 0,
        description: '',
        category: '',
        brand: '',
        stock: 0,
        sizesInput: '',
        colorsInput: '',
        images: []
    }
    imageFiles.value = []
    imagePreview.value = []
    errorMessage.value = ''
    successMessage.value = ''
}

const populateForm = (product) => {
    productForm.value = {
        name: product.name || '',
        price: product.price || 0,
        description: product.description || '',
        category: product.category || '',
        brand: product.brand || '',
        stock: product.stock || 0,
        sizesInput: product.sizes ? product.sizes.map(s => s.size).join(', ') : '',
        colorsInput: product.colors ? product.colors.join(', ') : '',
        images: product.images || []
    }

    // Set existing images as preview
    imagePreview.value = product.images || []
    imageFiles.value = [] // Clear new files
}

const handleImageUpload = (event) => {
    const files = Array.from(event.target.files)
    imageFiles.value = files

    // Create preview URLs
    imagePreview.value = []
    files.forEach(file => {
        const reader = new FileReader()
        reader.onload = (e) => {
            imagePreview.value.push(e.target.result)
        }
        reader.readAsDataURL(file)
    })
}

const removeImage = (index) => {
    imageFiles.value.splice(index, 1)
    imagePreview.value.splice(index, 1)
}

const submitProduct = async () => {
    try {
        isSubmitting.value = true
        errorMessage.value = ''
        successMessage.value = ''

        // Validate có ít nhất 1 ảnh (chỉ khi tạo mới hoặc có ảnh mới)
        if (!props.isEditMode && imageFiles.value.length === 0) {
            errorMessage.value = 'Vui lòng chọn ít nhất 1 ảnh sản phẩm'
            isSubmitting.value = false
            return
        }

        // Parse sizes và tạo SizeItem objects
        const sizesArray = productForm.value.sizesInput.split(',').map(s => parseInt(s.trim())).filter(s => !isNaN(s))
        const sizes = sizesArray.map(size => ({
            size: size,
            stock: Math.floor(productForm.value.stock / sizesArray.length) // Chia đều stock cho mỗi size
        }))

        // Parse colors
        const colors = productForm.value.colorsInput.split(',').map(c => c.trim()).filter(c => c)

        const productData = {
            name: productForm.value.name,
            price: productForm.value.price,
            description: productForm.value.description,
            category: productForm.value.category,
            brand: productForm.value.brand,
            stock: productForm.value.stock,
            sizes: sizes,
            colors: colors,
            images: props.isEditMode ? productForm.value.images : ['placeholder.jpg'],
            discount: 0
        }

        let response

        if (props.isEditMode) {
            // Update existing product
            response = await ProductService.update(editingProductId.value, productData)

            // Upload new images if any
            if (imageFiles.value.length > 0) {
                const formData = new FormData()
                imageFiles.value.forEach(file => {
                    formData.append('files', file)
                })

                try {
                    const uploadResponse = await ProductService.uploadImages(editingProductId.value, formData)
                    response.images = uploadResponse.images
                } catch (uploadError) {
                }
            }

            successMessage.value = 'Cập nhật sản phẩm thành công!'
            emit('success', { type: 'update', product: response })
        } else {
            // Create new product
            response = await ProductService.create(productData)
            const productId = response.id

            // Upload images
            if (imageFiles.value.length > 0) {
                const formData = new FormData()
                imageFiles.value.forEach(file => {
                    formData.append('files', file)
                })

                try {
                    const uploadResponse = await ProductService.uploadImages(productId, formData)
                    response.images = uploadResponse.images
                    successMessage.value = 'Tạo sản phẩm và upload hình ảnh thành công!'
                } catch (uploadError) {
                    successMessage.value = 'Tạo sản phẩm thành công nhưng upload hình ảnh thất bại!'
                }
            } else {
                successMessage.value = 'Tạo sản phẩm thành công!'
            }

            emit('success', { type: 'create', product: response })
        }

        setTimeout(() => {
            closeModal()
        }, 1500)

    } catch (error) {
        const errorMsg = error.response?.data?.detail || `Có lỗi xảy ra khi ${props.isEditMode ? 'cập nhật' : 'tạo'} sản phẩm`
        errorMessage.value = errorMsg
        emit('error', errorMsg)
    } finally {
        isSubmitting.value = false
    }
}

const closeModal = () => {
    resetForm()
    emit('close')
}

// Watch for editing product changes
watch(() => props.editingProduct, (newProduct) => {
    if (newProduct && props.isEditMode) {
        populateForm(newProduct)
    } else if (!props.isEditMode) {
        resetForm()
    }
}, { immediate: true })

// Watch for visibility changes
watch(() => props.isVisible, (isVisible) => {
    if (!isVisible) {
        resetForm()
    }
})

// Load categories when modal mounts (or when first opened)
onMounted(async () => {
    try {
        const list = await CategoryService.getAll()
        // Accept both array and wrapped response
        const categories = Array.isArray(list) ? list : (list?.categories || [])
        categoryOptions.value = categories
            .filter(c => c && c.name)
            .sort((a, b) => a.name.localeCompare(b.name))
    } catch (e) {
        // fallback: keep empty; user can type category manually if needed
        categoryOptions.value = []
    }
})
</script>

<style scoped>
/* Custom scrollbar for modal */
.overflow-y-auto::-webkit-scrollbar {
    width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}
</style>
