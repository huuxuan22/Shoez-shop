<template>
    <Transition name="modal">
        <div v-if="isOpen" class="fixed inset-0 z-50 overflow-y-auto">
            <div class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
                <!-- Backdrop -->
                <div class="fixed inset-0 bg-black bg-opacity-50 transition-opacity" @click="closeModal"></div>

                <!-- Modal -->
                <div
                    class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full">

                    <!-- Header -->
                    <div class="bg-black px-6 py-4">
                        <h3 class="text-lg font-bold text-white">Đánh giá sản phẩm</h3>
                    </div>

                    <!-- Body -->
                    <div class="bg-white px-6 py-4">
                        <!-- Product Info -->
                        <div v-if="product" class="flex items-center gap-4 mb-6 pb-4 border-b">
                            <img :src="product.image" :alt="product.name" class="w-20 h-20 object-cover rounded-lg" />
                            <div>
                                <h4 class="font-semibold text-gray-900">{{ product.name }}</h4>
                                <p class="text-sm text-gray-600">Size: {{ product.size }} - Màu: {{ product.color }}</p>
                            </div>
                        </div>

                        <!-- Rating Stars -->
                        <div class="mb-6">
                            <label class="block text-sm font-medium text-gray-700 mb-2">Đánh giá của bạn *</label>
                            <div class="flex gap-1">
                                <button v-for="star in 5" :key="star" @click="selectedRating = star"
                                    class="text-4xl transition-colors"
                                    :class="star <= selectedRating ? 'text-yellow-400' : 'text-gray-300'">
                                    ★
                                </button>
                            </div>
                            <p v-if="!selectedRating" class="text-sm text-red-500 mt-2">Vui lòng chọn số sao</p>
                        </div>

                        <!-- Comment -->
                        <div class="mb-6">
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                Nhận xét của bạn *
                            </label>
                            <textarea v-model="comment" placeholder="Chia sẻ trải nghiệm của bạn về sản phẩm..."
                                rows="4"
                                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
                            </textarea>
                            <p class="text-xs text-gray-500 mt-1">Tối thiểu 10 ký tự</p>
                            <p v-if="comment.length > 0 && comment.length < 10" class="text-sm text-red-500 mt-1">
                                Cần ít nhất {{ 10 - comment.length }} ký tự nữa
                            </p>
                        </div>

                        <!-- Image/Video Upload -->
                        <div class="mb-6">
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                Thêm hình ảnh hoặc video (tùy chọn)
                            </label>
                            <input ref="fileInput" type="file" accept="image/*,video/*" multiple class="hidden"
                                @change="handleFileUpload" />
                            <button type="button" @click="fileInput?.click()" :disabled="uploadedFiles.length >= 5"
                                class="inline-flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-sm text-gray-700 disabled:opacity-50 disabled:cursor-not-allowed">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2">
                                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12" />
                                </svg>
                                Chọn ảnh/video
                            </button>
                            <p class="text-xs text-gray-500 mt-1">Tối đa 5 tệp (ảnh/video)</p>

                            <!-- Preview Grid -->
                            <div v-if="uploadedFiles.length > 0" class="mt-4 grid grid-cols-5 gap-3">
                                <div v-for="(item, idx) in uploadedFiles" :key="idx" class="relative group">
                                    <div
                                        class="aspect-square bg-gray-100 rounded-lg overflow-hidden border border-gray-200">
                                        <img v-if="item.type.startsWith('image/')" :src="item.preview"
                                            :alt="`Preview ${idx + 1}`" class="w-full h-full object-cover" />
                                        <video v-else-if="item.type.startsWith('video/')" :src="item.preview"
                                            class="w-full h-full object-cover" muted>
                                        </video>
                                        <div
                                            class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                                            <button type="button" @click="removeFile(idx)"
                                                class="w-8 h-8 rounded-full bg-red-500 text-white flex items-center justify-center hover:bg-red-600">
                                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none"
                                                    stroke="currentColor" stroke-width="2">
                                                    <path d="M6 18L18 6M6 6l12 12" />
                                                </svg>
                                            </button>
                                        </div>
                                        <div v-if="item.type.startsWith('video/')"
                                            class="absolute top-1 right-1 bg-black/70 text-white text-xs px-1.5 py-0.5 rounded">
                                            Video
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Error Message -->
                        <div v-if="error" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
                            <p class="text-sm text-red-600">{{ error }}</p>
                        </div>
                    </div>

                    <!-- Footer -->
                    <div class="bg-gray-50 px-6 py-4 flex justify-end gap-3">
                        <button @click="closeModal"
                            class="px-6 py-2 border-2 border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
                            Hủy
                        </button>
                        <button @click="submitReview" :disabled="!canSubmit" @keyup.enter="submitReview"
                            class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed">
                            Gửi đánh giá
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </Transition>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import ReviewService from '@/api-services/ReviewService';
import { useToast } from '@/composables/useToast';
// Use ReviewService to upload media instead of updating product images

const props = defineProps({
    isOpen: Boolean,
    product: Object,
    orderId: String
});

const emit = defineEmits(['close', 'submitted']);

const toast = useToast();
const selectedRating = ref(0);
const comment = ref('');
const loading = ref(false);
const error = ref('');
const fileInput = ref(null);
const uploadedFiles = ref([]);

const canSubmit = computed(() => {
    return selectedRating.value > 0 && comment.value.length >= 10;
});

watch(() => props.isOpen, (newVal) => {
    if (newVal) {
        // Reset form khi mở modal
        selectedRating.value = 0;
        comment.value = '';
        error.value = '';
        uploadedFiles.value = [];
        if (fileInput.value) fileInput.value.value = '';
    }
});

const closeModal = () => {
    if (!loading.value) {
        emit('close');
    }
};

const handleFileUpload = (event) => {
    const files = Array.from(event.target.files || []);
    const remainingSlots = 5 - uploadedFiles.value.length;
    const filesToAdd = files.slice(0, remainingSlots);

    filesToAdd.forEach(file => {
        const reader = new FileReader();
        reader.onload = (e) => {
            uploadedFiles.value.push({
                file: file,
                preview: e.target.result,
                type: file.type
            });
        };
        if (file.type.startsWith('image/')) {
            reader.readAsDataURL(file);
        } else if (file.type.startsWith('video/')) {
            reader.readAsDataURL(file);
        }
    });

    if (event.target) event.target.value = '';
};

const removeFile = (index) => {
    uploadedFiles.value.splice(index, 1);
};

const uploadFiles = async () => {
    if (uploadedFiles.value.length === 0) return [];

    const formData = new FormData();
    uploadedFiles.value.forEach(item => {
        formData.append('files', item.file);
    });

    try {
        const result = await ReviewService.uploadMedia(formData);
        return result.images || [];
    } catch (err) {
        console.error('Upload images error:', err);
        throw new Error('Không thể upload ảnh/video. Vui lòng thử lại.');
    }
};

const submitReview = async () => {
    if (!canSubmit.value) return;

    loading.value = true;
    error.value = '';

    try {
        const productId = props.product.productId || props.product._id;
        let imageUrls = [];

        // Upload files if any
        if (uploadedFiles.value.length > 0) {
            imageUrls = await uploadFiles();
        }

        const reviewData = {
            product_id: productId,
            order_id: props.orderId,
            rating: selectedRating.value,
            comment: comment.value,
            images: imageUrls
        };

        await ReviewService.create(reviewData);
        toast.success('Cảm ơn bạn đã đánh giá!');
        emit('submitted');
        closeModal();
    } catch (err) {
        error.value = err.response?.data?.detail || err.message || 'Có lỗi xảy ra khi gửi đánh giá';
        toast.error(error.value);
    } finally {
        loading.value = false;
    }
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
    transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
    opacity: 0;
}
</style>
