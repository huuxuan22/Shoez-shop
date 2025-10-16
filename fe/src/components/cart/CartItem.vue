<template>
    <div class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
        <div class="flex gap-4">
            <!-- Product Image -->
            <div class="w-24 h-24 flex-shrink-0">
                <img :src="item.image" :alt="item.name" class="w-full h-full object-cover rounded-lg" />
            </div>

            <!-- Product Info -->
            <div class="flex-1">
                <div class="flex justify-between">
                    <div>
                        <h3 class="font-semibold text-black text-lg">{{ item.name }}</h3>
                        <p class="text-gray-600 text-sm">{{ item.brand }}</p>
                    </div>
                    <button @click="$emit('remove-item', item.id)"
                        class="text-gray-400 hover:text-black transition-colors">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <div class="mt-2 flex items-center gap-4 text-sm">
                    <span class="text-gray-600">Size: <strong class="text-black">{{ item.size }}</strong></span>
                    <span class="text-gray-600">Màu: <strong class="text-black">{{ item.color }}</strong></span>
                </div>

                <div class="mt-4 flex items-center justify-between">
                    <!-- Price -->
                    <div class="flex items-center gap-2">
                        <span class="text-xl font-bold text-black">{{ formatPrice(item.price * item.quantity) }}</span>
                        <span v-if="item.originalPrice" class="text-sm text-gray-400 line-through">
                            {{ formatPrice(item.originalPrice * item.quantity) }}
                        </span>
                    </div>

                    <!-- Quantity Selector -->
                    <QuantitySelector :quantity="item.quantity" :max-quantity="item.maxQuantity"
                        @update:quantity="$emit('update-quantity', item.id, $event)" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import QuantitySelector from '../QuantitySelector.vue';


const props = defineProps({
    item: Object
});

defineEmits(['update-quantity', 'remove-item']);

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};
</script>