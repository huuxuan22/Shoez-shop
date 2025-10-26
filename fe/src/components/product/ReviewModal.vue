<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
        <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
            <!-- Header -->
            <div class="border-b border-gray-200 p-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-2xl font-bold text-gray-900 font-serif">Đánh giá sản phẩm</h3>
                    <button @click="$emit('close')" class="text-gray-400 hover:text-gray-600 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!-- Product Info -->
                <div class="flex items-center space-x-4 mt-4">
                    <img :src="product.image" :alt="product.name" class="w-16 h-16 object-cover rounded-2xl">
                    <div>
                        <h4 class="font-semibold text-gray-900">{{ product.name }}</h4>
                        <p class="text-gray-600 text-sm">{{ product.brand }}</p>
                    </div>
                </div>
            </div>

            <!-- Form -->
            <form @submit.prevent="submitReview" class="p-6 space-y-6">
                <!-- Rating -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-3">Đánh giá của bạn *</label>
                    <div class="flex items-center space-x-2">
                        <button v-for="star in 5" :key="star" type="button" @click="form.rating = star"
                            class="text-3xl transition-transform hover:scale-110"
                            :class="star <= form.rating ? 'text-yellow-400' : 'text-gray-300'">
                            ★
                        </button>
                    </div>
                </div>

                <!-- Comment -->
                <div>
                    <label for="comment" class="block text-sm font-medium text-gray-700 mb-3">Nhận xét *</label>
                    <textarea id="comment" v-model="form.comment" rows="5" required
                        class="w-full px-4 py-3 border-2 border-gray-200 rounded-2xl focus:ring-2 focus:ring-gray-900 focus:border-gray-900 transition-all duration-300 resize-none"
                        placeholder="Chia sẻ trải nghiệm của bạn về sản phẩm này..."></textarea>
                </div>

                <!-- Image Upload -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-3">Hình ảnh (tối đa 3 ảnh)</label>
                    <div class="flex space-x-4">
                        <!-- Image Preview -->
                        <div v-for="(image, index) in form.images" :key="index" class="relative w-20 h-20">
                            <img :src="image.url" class="w-full h-full object-cover rounded-lg">
                            <button type="button" @click="removeImage(index)"
                                class="absolute -top-2 -right-2 w-6 h-6 bg-red-500 text-white rounded-full flex items-center justify-center text-sm hover:bg-red-600 transition-colors">
                                ×
                            </button>
                        </div>

                        <!-- Upload Button -->
                        <label v-if="form.images.length < 3"
                            class="w-20 h-20 border-2 border-dashed border-gray-300 rounded-lg flex items-center justify-center cursor-pointer hover:border-gray-400 transition-colors">
                            <input type="file" multiple accept="image/*" @change="handleImageUpload" class="hidden">
                            <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                            </svg>
                        </label>
                    </div>
                </div>

                <!-- Submit Button -->
                <div class="flex space-x-4 pt-4">
                    <button type="button" @click="$emit('close')"
                        class="flex-1 border-2 border-gray-300 text-gray-700 py-3 rounded-2xl font-semibold hover:border-gray-900 hover:text-gray-900 transition-all duration-300">
                        Hủy
                    </button>
                    <button type="submit" :disabled="!form.rating || !form.comment"
                        class="flex-1 bg-gradient-to-r from-gray-900 to-black text-white py-3 rounded-2xl font-semibold hover:from-gray-800 hover:to-gray-900 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed">
                        Gửi đánh giá
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
    product: {
        type: Object,
        required: true
    }
})

const emit = defineEmits(['submit', 'close'])

const form = ref({
    rating: 0,
    comment: '',
    images: []
})

// Methods
const handleImageUpload = (event) => {
    const files = Array.from(event.target.files)
    const remainingSlots = 3 - form.value.images.length

    files.slice(0, remainingSlots).forEach(file => {
        const reader = new FileReader()
        reader.onload = (e) => {
            form.value.images.push({
                file: file,
                url: e.target.result
            })
        }
        reader.readAsDataURL(file)
    })
}

const removeImage = (index) => {
    form.value.images.splice(index, 1)
}

const submitReview = () => {
    const reviewData = {
        rating: form.value.rating,
        comment: form.value.comment,
        images: form.value.images.map(img => img.url)
    }

    emit('submit', reviewData)

    // Reset form
    form.value = {
        rating: 0,
        comment: '',
        images: []
    }
}
</script>