<template>
    <div class="space-y-6" :aria-label="$t('Orders.Loading.text')" role="status">
        <span class="sr-only">{{ $t('Orders.Loading.text') }}</span>
        <div v-for="n in 3" :key="n" class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 animate-pulse">
            <!-- Header Skeleton -->
            <div class="flex justify-between items-center mb-4">
                <div class="space-y-2">
                    <div class="h-4 bg-gray-200 rounded w-32"></div>
                    <div class="h-3 bg-gray-200 rounded w-24"></div>
                </div>
                <div class="h-6 bg-gray-200 rounded w-20"></div>
            </div>

            <!-- Items Skeleton -->
            <div class="space-y-3">
                <div v-for="n in 2" :key="n" class="flex items-center space-x-4">
                    <div class="w-16 h-16 bg-gray-200 rounded-lg"></div>
                    <div class="flex-1 space-y-2">
                        <div class="h-4 bg-gray-200 rounded w-3/4"></div>
                        <div class="h-3 bg-gray-200 rounded w-1/4"></div>
                    </div>
                    <div class="h-4 bg-gray-200 rounded w-16"></div>
                </div>
            </div>

            <!-- Footer Skeleton -->
            <div class="flex justify-between items-center mt-4">
                <div class="h-3 bg-gray-200 rounded w-48"></div>
                <div class="flex space-x-2">
                    <div class="h-8 bg-gray-200 rounded w-20"></div>
                    <div class="h-8 bg-gray-200 rounded w-20"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
// Loading skeleton component
</script>