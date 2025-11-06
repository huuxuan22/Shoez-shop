<template>
    <div class="mt-12 bg-white rounded-lg shadow-lg border border-gray-200">
        <div class="border-b border-gray-200">
            <nav class="flex">
                <button v-for="tab in tabs" :key="tab.id" @click="activeTab = tab.id" :class="[
                    'px-8 py-4 font-semibold transition-colors border-b-2',
                    activeTab === tab.id
                        ? 'border-black text-black'
                        : 'border-transparent text-gray-600 hover:text-gray-800'
                ]">
                    {{ tab.label }}
                </button>
            </nav>
        </div>

        <div class="p-8">
            <!-- Description Tab -->
            <div v-if="activeTab === 'description'">
                <h3 class="text-2xl font-bold mb-4 text-gray-800">{{ $t('Product.Tabs.descriptionTitle') }}</h3>
                <div class="prose max-w-none text-gray-600 space-y-4">
                    <p>
                        {{ product.name }} {{ $t('Product.Tabs.descriptionText') }} {{ product.brand }},
                        {{ $t('Product.Tabs.descriptionText2') }}
                    </p>
                    <p>
                        {{ $t('Product.Tabs.descriptionText3') }}
                    </p>
                </div>
            </div>

            <!-- Specifications Tab -->
            <div v-if="activeTab === 'specifications'">
                <h3 class="text-2xl font-bold mb-4 text-gray-800">{{ $t('Product.Tabs.specificationsTitle') }}</h3>
                <table class="w-full">
                    <tbody class="divide-y divide-gray-200">
                        <tr>
                            <td class="py-3 font-semibold text-gray-700">{{ $t('Product.Tabs.brand') }}</td>
                            <td class="py-3 text-gray-600">{{ product.brand }}</td>
                        </tr>
                        <tr>
                            <td class="py-3 font-semibold text-gray-700">{{ $t('Product.Tabs.type') }}</td>
                            <td class="py-3 text-gray-600">{{ product.category }}</td>
                        </tr>
                        <tr>
                            <td class="py-3 font-semibold text-gray-700">{{ $t('Product.Tabs.color') }}</td>
                            <td class="py-3 text-gray-600">{{ product.colors.join(', ') }}</td>
                        </tr>
                        <tr>
                            <td class="py-3 font-semibold text-gray-700">{{ $t('Product.Tabs.size') }}</td>
                            <td class="py-3 text-gray-600">{{ formatSizes(product.sizes) }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Reviews Tab -->
            <div v-if="activeTab === 'reviews'">
                <h3 class="text-2xl font-bold mb-6 text-gray-800">{{ $t('Product.Tabs.reviewsTitle') }}</h3>

                <!-- Review Summary -->
                <div class="bg-gray-50 rounded-lg p-6 mb-8 border border-gray-200">
                    <div class="flex items-center gap-8">
                        <div class="text-center">
                            <p class="text-5xl font-bold text-black mb-2">4.8</p>
                            <div class="flex text-yellow-400 mb-2">
                                <svg v-for="star in 5" :key="star" class="w-5 h-5" fill="currentColor"
                                    viewBox="0 0 20 20">
                                    <path
                                        d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                </svg>
                            </div>
                            <p class="text-gray-600">128 {{ $t('Product.Info.reviews') }}</p>
                        </div>

                        <div class="flex-1">
                            <div v-for="rating in [5, 4, 3, 2, 1]" :key="rating" class="flex items-center gap-2 mb-2">
                                <span class="text-sm text-gray-600 w-12">{{ rating }} {{ $t('Product.Reviews.star') }}</span>
                                <div class="flex-1 bg-gray-200 rounded-full h-2">
                                    <div class="bg-gray-600 h-2 rounded-full"
                                        :style="{ width: `${rating === 5 ? 80 : rating === 4 ? 15 : 5}%` }"></div>
                                </div>
                                <span class="text-sm text-gray-600 w-8">{{ rating === 5 ? 102 : rating === 4 ? 19 : 7
                                    }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

defineProps({
    product: {
        type: Object,
        required: true
    }
})

const { t } = useI18n()
const activeTab = ref('description')

const tabs = computed(() => [
    { id: 'description', label: t('Product.Tabs.description') },
    { id: 'specifications', label: t('Product.Tabs.specifications') },
    { id: 'reviews', label: t('Product.Tabs.reviews') }
])

const formatSizes = (sizes) => {
    if (!sizes || !Array.isArray(sizes)) return ''
    return sizes.map(size => {
        if (typeof size === 'object' && size.size !== undefined) {
            return size.size
        }
        return size
    }).join(', ')
}
</script>