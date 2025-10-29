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

const canSubmit = computed(() => {
    return selectedRating.value > 0 && comment.value.length >= 10;
});

watch(() => props.isOpen, (newVal) => {
    if (newVal) {
        // Reset form khi mở modal
        selectedRating.value = 0;
        comment.value = '';
        error.value = '';
    }
});

const closeModal = () => {
    if (!loading.value) {
        emit('close');
    }
};

const submitReview = async () => {
    if (!canSubmit.value) return;

    loading.value = true;
    error.value = '';

    try {
        const reviewData = {
            product_id: props.product.productId || props.product._id,
            order_id: props.orderId,
            rating: selectedRating.value,
            comment: comment.value,
            images: []
        };

        await ReviewService.create(reviewData);
        toast.success('Cảm ơn bạn đã đánh giá!');
        emit('submitted');
        closeModal();
    } catch (err) {
        error.value = err.response?.data?.detail || 'Có lỗi xảy ra khi gửi đánh giá';
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
