<template>
    <!-- Toast Container -->
    <Teleport to="body">
        <TransitionGroup name="toast" tag="div" class="fixed top-4 right-4 z-[9999] space-y-3">
            <!-- Toast Item -->
            <div v-for="toast in toasts" :key="toast.id"
                class="min-w-80 max-w-md bg-white rounded-lg shadow-2xl border p-4 flex items-start gap-3 animate-in slide-in-from-right"
                :class="getToastClass(toast.type)">

                <!-- Icon -->
                <div class="flex-shrink-0">
                    <!-- Success Icon -->
                    <svg v-if="toast.type === 'success'" class="w-6 h-6 text-green-600" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>

                    <!-- Error Icon -->
                    <svg v-else-if="toast.type === 'error'" class="w-6 h-6 text-red-600" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>

                    <!-- Info Icon -->
                    <svg v-else-if="toast.type === 'info'" class="w-6 h-6 text-blue-600" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>

                    <!-- Warning Icon -->
                    <svg v-else class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                </div>

                <!-- Content -->
                <div class="flex-1 min-w-0">
                    <h3 class="font-semibold text-gray-900 text-sm">{{ toast.title }}</h3>
                    <p class="text-sm text-gray-600 mt-1">{{ toast.message }}</p>
                </div>

                <!-- Close Button -->
                <button @click="removeToast(toast.id)"
                    class="flex-shrink-0 text-gray-400 hover:text-gray-600 transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        </TransitionGroup>
    </Teleport>
</template>

<script setup>
import { useToast } from '@/composables/useToast'

const { toasts, removeToast } = useToast()

/**
 * Get CSS class cho toast
 */
const getToastClass = (type) => {
    const classes = {
        success: 'border-green-200 bg-green-50',
        error: 'border-red-200 bg-red-50',
        info: 'border-blue-200 bg-blue-50',
        warning: 'border-yellow-200 bg-yellow-50'
    }
    return classes[type] || classes.info
}
</script>

<style scoped>
/* Transition animations */
.toast-enter-active {
    transition: all 0.3s ease-out;
}

.toast-enter-from {
    transform: translateX(100%);
    opacity: 0;
}

.toast-leave-active {
    transition: all 0.3s ease-in;
}

.toast-leave-to {
    transform: translateX(100%);
    opacity: 0;
}
</style>
