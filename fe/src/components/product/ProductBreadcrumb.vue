<template>
    <nav class="flex mb-8" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-1 md:space-x-3">
            <li class="inline-flex items-center">
                <router-link to="/" class="text-gray-700 hover:text-black transition-colors">
                    Trang chủ
                </router-link>
            </li>
            <li>
                <div class="flex items-center">
                    <span class="mx-2 text-gray-400">/</span>
                    <router-link to="/products" class="text-gray-700 hover:text-black transition-colors">
                        Sản phẩm
                    </router-link>
                </div>
            </li>
            <li aria-current="page">
                <div class="flex items-center">
                    <span class="mx-2 text-gray-400">/</span>
                    <span class="text-gray-600">{{ productName }}</span>
                </div>
            </li>
        </ol>
    </nav>
</template>

<script setup>
defineProps({
    productName: {
        type: String,
        required: true
    }
})
</script>