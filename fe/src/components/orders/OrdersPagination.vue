<template>
    <div class="flex justify-center mt-8">
        <nav class="flex items-center space-x-2">
            <!-- Previous Button -->
            <button @click="handlePageChange(currentPage - 1)" :disabled="currentPage === 1" :class="[
                'px-3 py-2 rounded-lg border text-sm font-medium transition-colors',
                currentPage === 1
                    ? 'bg-gray-100 text-gray-400 border-gray-200 cursor-not-allowed'
                    : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                </svg>
            </button>

            <!-- Page Numbers -->
            <button v-for="page in visiblePages" :key="page" @click="handlePageChange(page)" :class="[
                'px-4 py-2 rounded-lg border text-sm font-medium transition-colors',
                currentPage === page
                    ? 'bg-black text-white border-black'
                    : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]">
                {{ page }}
            </button>

            <!-- Next Button -->
            <button @click="handlePageChange(currentPage + 1)" :disabled="currentPage === totalPages" :class="[
                'px-3 py-2 rounded-lg border text-sm font-medium transition-colors',
                currentPage === totalPages
                    ? 'bg-gray-100 text-gray-400 border-gray-200 cursor-not-allowed'
                    : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
            </button>
        </nav>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
    currentPage: {
        type: Number,
        required: true
    },
    totalPages: {
        type: Number,
        required: true
    }
})

const emit = defineEmits(['page-change'])

const visiblePages = computed(() => {
    const pages = []
    const maxVisible = 5

    let start = Math.max(1, props.currentPage - Math.floor(maxVisible / 2))
    let end = Math.min(props.totalPages, start + maxVisible - 1)

    // Adjust start if we're near the end
    start = Math.max(1, end - maxVisible + 1)

    for (let i = start; i <= end; i++) {
        pages.push(i)
    }

    return pages
})

const handlePageChange = (page) => {
    if (page >= 1 && page <= props.totalPages) {
        emit('page-change', page)
    }
}
</script>