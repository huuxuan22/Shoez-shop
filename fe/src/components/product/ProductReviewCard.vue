<template>
    <div class="border-b border-gray-200 pb-6 last:border-b-0">
        <div class="flex items-start space-x-4">
            <!-- User Avatar -->
            <div
                class="w-12 h-12 bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl flex items-center justify-center flex-shrink-0">
                <span v-if="!review.user.avatar" class="text-lg font-semibold text-gray-600">
                    {{ getUserInitials(review.user.name) }}
                </span>
                <img v-else :src="review.user.avatar" :alt="review.user.name"
                    class="w-full h-full object-cover rounded-2xl">
            </div>

            <!-- Review Content -->
            <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between mb-2">
                    <div>
                        <h4 class="font-semibold text-gray-900">{{ review.user.name }}</h4>
                        <div class="flex items-center space-x-2 mt-1">
                            <StarRating :rating="review.rating" :size="16" />
                            <span class="text-sm text-gray-500">{{ formatDate(review.createdAt) }}</span>
                            <span v-if="review.verified"
                                class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">
                                {{ $t('Product.ReviewCard.verified') }}
                            </span>
                        </div>
                    </div>
                </div>

                <p class="text-gray-700 leading-relaxed mb-3">{{ review.comment }}</p>

                <!-- Review Images -->
                <div v-if="review.images && review.images.length > 0" class="flex space-x-2 mt-3">
                    <img v-for="(image, index) in review.images" :key="index" :src="image"
                        :alt="`Review image ${index + 1}`"
                        class="w-20 h-20 object-cover rounded-lg cursor-pointer hover:opacity-80 transition-opacity"
                        @click="openImageGallery(image)" />
                </div>

                <!-- Helpful Actions -->
                <div class="flex items-center space-x-4 mt-4 text-sm text-gray-500">
                    <button @click="toggleHelpful"
                        class="flex items-center space-x-1 hover:text-gray-700 transition-colors"
                        :class="{ 'text-blue-600': review.isHelpful }">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                        </svg>
                        <span>{{ $t('Product.ReviewCard.helpful') }} ({{ review.helpfulCount || 0 }})</span>
                    </button>

                    <button class="flex items-center space-x-1 hover:text-gray-700 transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                        <span>{{ $t('Product.ReviewCard.reply') }}</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import StarRating from '../shared/StarRating.vue'

const { t } = useI18n()

const props = defineProps({
    review: {
        type: Object,
        required: true
    }
})

// Methods
const getUserInitials = (name) => {
    return name.split(' ').map(n => n[0]).join('').toUpperCase()
}

const formatDate = (date) => {
    return new Date(date).toLocaleDateString('vi-VN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    })
}

const toggleHelpful = () => {
    // Xử lý đánh dấu hữu ích
    props.review.isHelpful = !props.review.isHelpful
    if (props.review.isHelpful) {
        props.review.helpfulCount = (props.review.helpfulCount || 0) + 1
    } else {
        props.review.helpfulCount = Math.max(0, (props.review.helpfulCount || 1) - 1)
    }
}

const openImageGallery = (image) => {
}
</script>