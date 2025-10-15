<template>
    <section class="py-20 bg-gradient-to-br from-gray-50 to-white">
        <div class="container mx-auto px-4">
            <!-- Header bên trái -->
            <div class="text-left mb-16 max-w-2xl">
                <h2 class="text-4xl md:text-5xl font-bold text-black mb-4">
                    Thiết kế giày của riêng bạn
                </h2>
                <p class="text-xl text-gray-600">
                    Tùy chỉnh màu sắc, chất liệu và tạo đôi giày độc nhất cho phong cách cá nhân
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
                <!-- Left Column - Customization Controls -->
                <div class="space-y-8 order-2 lg:order-1">
                    <!-- Shoe Model Selection -->
                    <div>
                        <h3 class="text-lg font-semibold mb-4">Chọn kiểu giày</h3>
                        <div class="grid grid-cols-2 gap-4">
                            <button v-for="model in shoeModels" :key="model.id" @click="selectModel(model)"
                                class="p-4 border-2 rounded-xl text-left hover:border-black transition group"
                                :class="{ 'border-black bg-black text-white': currentModel.id === model.id, 'border-gray-200': currentModel.id !== model.id }">
                                <div class="font-medium group-hover:text-current">{{ model.name }}</div>
                                <div class="text-sm opacity-75 mt-1">{{ model.price }}</div>
                            </button>
                        </div>
                    </div>

                    <!-- Color Customization -->
                    <div class="pt-6">
                        <h3 class="text-lg font-semibold mb-4">Tùy chỉnh màu sắc</h3>
                        <div class="space-y-4">
                            <div v-for="part in customizableParts" :key="part.id"
                                class="flex items-center justify-between py-2">
                                <span class="font-medium text-gray-700">{{ part.name }}</span>
                                <div class="flex space-x-2">
                                    <button v-for="color in part.colors" :key="color"
                                        @click="changePartColor(part.id, color)"
                                        class="w-8 h-8 rounded-full border-2 border-white shadow-md hover:scale-110 transition transform"
                                        :style="{ backgroundColor: color }"
                                        :class="{ 'ring-2 ring-black ring-offset-2': getCurrentColor(part.id) === color }"></button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Material Selection -->
                    <div class="pt-6">
                        <h3 class="text-lg font-semibold mb-4">Chất liệu</h3>
                        <div class="flex flex-wrap gap-3">
                            <button v-for="material in materials" :key="material" @click="currentMaterial = material"
                                class="px-4 py-2 border-2 rounded-lg hover:border-black transition font-medium"
                                :class="{ 'border-black bg-black text-white': currentMaterial === material, 'border-gray-200 text-gray-700': currentMaterial !== material }">
                                {{ material }}
                            </button>
                        </div>
                        <div class="flex space-x-4 pt-8">
                            <button @click="saveDesign"
                                class="flex-1 bg-black text-white py-4 rounded-lg hover:bg-gray-800 transition font-medium text-lg">
                                💾 Lưu thiết kế
                            </button>
                        </div>
                    </div>

                    <!-- Action Buttons -->

                </div>

                <!-- Right Column - Shoe Preview với hiệu ứng 3D -->
                <div class="relative order-1 lg:order-2">
                    <div class="bg-white rounded-2xl shadow-2xl p-8 3d-container" @mousemove="handleMouseMove"
                        @mouseleave="handleMouseLeave">
                        <div class="relative h-96 flex items-center justify-center perspective">
                            <!-- Base Shoe với hiệu ứng 3D -->
                            <div class="absolute inset-0 flex items-center justify-center container-3d">
                                <img :src="currentModel.base" alt="Custom Shoe" class="max-h-80 object-contain 3d-shoe"
                                    :style="shoeTransform" />
                            </div>

                            <!-- Dynamic parts với hiệu ứng 3D -->
                            <div v-for="part in customParts" :key="part.id"
                                class="absolute inset-0 flex items-center justify-center container-3d">
                                <img :src="getPartImage(part.id)" :alt="part.name"
                                    class="max-h-80 object-contain 3d-shoe" :style="{
                                        filter: `hue-rotate(${part.hue}deg) brightness(${part.brightness}) saturate(${part.saturation})`,
                                        ...shoeTransform
                                    }" />
                            </div>

                            <!-- Hiệu ứng ánh sáng 3D -->
                            <div class="absolute inset-0 rounded-2xl pointer-events-none" :style="lightingEffect"></div>
                        </div>
                    </div>

                    <!-- Rotation controls -->
                    <div class="flex justify-center mt-6 space-x-3">
                        <button v-for="angle in [0, 45, 90, 180]" :key="angle" @click="setFixedAngle(angle)"
                            class="w-12 h-12 rounded-full bg-white border-2 border-gray-300 flex items-center justify-center hover:border-black transition font-medium"
                            :class="{ 'border-black bg-black text-white': currentFixedAngle === angle }">
                            {{ angle }}°
                        </button>
                        <button @click="toggle3DMode"
                            class="w-12 h-12 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 text-white border-2 border-transparent flex items-center justify-center hover:from-purple-600 hover:to-pink-600 transition font-medium"
                            :class="{ 'ring-2 ring-purple-300': is3DMode }">
                            {{ is3DMode ? '2D' : '3D' }}
                        </button>
                    </div>

                    <!-- Hướng dẫn 3D -->
                    <div v-if="is3DMode" class="text-center mt-4">
                        <p class="text-sm text-gray-500">✨ Di chuột để xoay giày 3D</p>
                    </div>
                </div>
            </div>

            <!-- Design Gallery -->
            <div class="mt-20">
                <h3 class="text-3xl font-bold text-center mb-12 text-gray-900">Thiết kế nổi bật từ cộng đồng</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div v-for="design in featuredDesigns" :key="design.id"
                        class="group relative bg-white rounded-2xl p-6 shadow-lg hover:shadow-2xl transition-all duration-500 cursor-pointer border border-gray-200/60 hover:border-gray-300 overflow-hidden"
                        @click="loadDesign(design)">
                        <!-- Background gradient effect -->
                        <div
                            class="absolute inset-0 bg-gradient-to-br from-white to-gray-50 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                        </div>

                        <!-- Shine effect on hover -->
                        <div
                            class="absolute inset-0 bg-gradient-to-r from-transparent via-white/50 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                        </div>

                        <!-- Content -->
                        <div class="relative z-10">
                            <!-- Image container with elegant frame -->
                            <div
                                class="relative h-40 mb-4 flex items-center justify-center bg-gradient-to-br from-gray-50 to-white rounded-xl border border-gray-100 group-hover:border-gray-200 transition-colors duration-300 overflow-hidden">
                                <!-- Image with scale effect -->
                                <img :src="design.preview" :alt="design.name"
                                    class="max-h-32 object-contain transition-transform duration-500 group-hover:scale-110" />

                                <!-- Hover overlay -->
                                <div
                                    class="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors duration-300 rounded-xl">
                                </div>

                                <!-- Corner accents -->
                                <div
                                    class="absolute top-2 left-2 w-2 h-2 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                </div>
                                <div
                                    class="absolute top-2 right-2 w-2 h-2 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                </div>
                                <div
                                    class="absolute bottom-2 left-2 w-2 h-2 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                </div>
                                <div
                                    class="absolute bottom-2 right-2 w-2 h-2 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                                </div>
                            </div>

                            <!-- Design info -->
                            <div class="space-y-3">
                                <div>
                                    <h4
                                        class="font-semibold text-gray-900 text-lg leading-tight group-hover:text-gray-800 transition-colors duration-300">
                                        {{ design.name }}
                                    </h4>
                                    <p class="text-sm text-gray-500 mt-1">by {{ design.creator }}</p>
                                </div>

                                <!-- Stats and action -->
                                <div class="flex items-center justify-between pt-2">
                                    <div class="flex items-center space-x-2">
                                        <div class="flex items-center space-x-1 bg-red-50 px-3 py-1 rounded-full">
                                            <span class="text-red-500 text-sm">❤️</span>
                                            <span class="text-xs font-medium text-gray-700">{{ design.likes }}</span>
                                        </div>
                                    </div>

                                    <button
                                        class="relative bg-gradient-to-r from-gray-900 to-black text-white px-4 py-2 rounded-lg text-sm font-medium hover:from-gray-800 hover:to-gray-900 transition-all duration-300 transform group-hover:scale-105 shadow-md hover:shadow-lg active:scale-95 overflow-hidden"
                                        @click.stop="loadDesign(design)">
                                        <!-- Button shine effect -->
                                        <div
                                            class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                                        </div>
                                        <span class="relative">Sử dụng</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Border glow effect -->
                        <div
                            class="absolute inset-0 rounded-2xl border-2 border-transparent bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10">
                            <div class="absolute inset-[2px] rounded-2xl bg-white"></div>
                        </div>
                    </div>
                </div>

                <!-- View more button -->
                <div class="text-center mt-12">
                    <button
                        class="bg-transparent border-2 border-gray-300 text-gray-700 px-8 py-3 rounded-xl hover:border-gray-400 hover:bg-gray-50 transition-all duration-300 font-medium transform hover:scale-105 active:scale-95">
                        Xem thêm thiết kế ↓
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

// Current customization state
const currentModel = ref({})
const currentFixedAngle = ref(0)
const currentMaterial = ref('Da lộn')
const customParts = reactive([])
const is3DMode = ref(true)

// 3D mouse tracking
const mouseX = ref(0)
const mouseY = ref(0)
const isMouseOver = ref(false)

// Sample data
const shoeModels = [
    {
        id: 1,
        name: 'Nike Air Max',
        base: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        price: '2.500.000 VND'
    },
    {
        id: 2,
        name: 'Adidas Ultraboost',
        base: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        price: '2.800.000 VND'
    },
    {
        id: 3,
        name: 'Converse Classic',
        base: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        price: '1.200.000 VND'
    },
    {
        id: 4,
        name: 'Puma RS-X',
        base: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        price: '1.900.000 VND'
    }
]

const customizableParts = [
    {
        id: 'upper',
        name: 'Thân giày',
        image: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        colors: ['#000000', '#FFFFFF', '#FF0000', '#0000FF', '#00FF00', '#FFFF00']
    },
    {
        id: 'sole',
        name: 'Đế giày',
        image: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        colors: ['#2C2C2C', '#FFFFFF', '#FFA500', '#800080', '#A52A2A', '#FFC0CB']
    },
    {
        id: 'laces',
        name: 'Dây giày',
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        colors: ['#000000', '#FFFFFF', '#FF0000', '#0000FF', '#FFFF00', '#FF69B4']
    },
    {
        id: 'logo',
        name: 'Logo',
        image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
        colors: ['#000000', '#FFFFFF', '#FF0000', '#0000FF', '#FFD700', '#00FF00']
    }
]

const materials = ['Da lộn', 'Da thật', 'Vải canvas', 'Knit', 'Mesh']

const featuredDesigns = [
    {
        id: 1,
        name: 'Street Style Red',
        preview: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
        creator: 'Anh Tú',
        likes: 142,
        settings: { upper: '#FF0000', sole: '#000000', laces: '#FFFFFF', logo: '#FFFFFF' }
    },
    {
        id: 2,
        name: 'Ocean Blue',
        preview: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
        creator: 'Minh Châu',
        likes: 98,
        settings: { upper: '#0000FF', sole: '#FFFFFF', laces: '#0000FF', logo: '#FFFFFF' }
    },
    {
        id: 3,
        name: 'Forest Green',
        preview: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
        creator: 'Hoàng Nam',
        likes: 76,
        settings: { upper: '#00FF00', sole: '#2C2C2C', laces: '#000000', logo: '#FFFFFF' }
    },
    {
        id: 4,
        name: 'Sunset Orange',
        preview: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
        creator: 'Thu Hà',
        likes: 113,
        settings: { upper: '#FFA500', sole: '#000000', laces: '#FFFFFF', logo: '#000000' }
    }
]

// Computed properties for 3D effects
const shoeTransform = computed(() => {
    if (!is3DMode.value) {
        return {
            transform: `rotate(${currentFixedAngle.value}deg)`
        }
    }

    const rotateX = isMouseOver.value ? (mouseY.value - 0.5) * 60 : 0
    const rotateY = isMouseOver.value ? (mouseX.value - 0.5) * 60 : 0

    return {
        transform: `
            perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            scale3d(1, 1, 1)
        `,
        transition: isMouseOver.value ? 'transform 0.1s ease' : 'transform 0.5s ease'
    }
})

const lightingEffect = computed(() => {
    if (!is3DMode.value || !isMouseOver.value) return {}

    const gradientX = mouseX.value * 100
    const gradientY = mouseY.value * 100

    return {
        background: `radial-gradient(circle at ${gradientX}% ${gradientY}%, rgba(255,255,255,0.3) 0%, transparent 50%)`
    }
})

// Initialize with first model
currentModel.value = shoeModels[0]

// Methods
const selectModel = (model) => {
    currentModel.value = model
}

const handleMouseMove = (event) => {
    if (!is3DMode.value) return

    const rect = event.currentTarget.getBoundingClientRect()
    mouseX.value = (event.clientX - rect.left) / rect.width
    mouseY.value = (event.clientY - rect.top) / rect.height
    isMouseOver.value = true
}

const handleMouseLeave = () => {
    isMouseOver.value = false
}

const setFixedAngle = (angle) => {
    currentFixedAngle.value = angle
    is3DMode.value = false
}

const toggle3DMode = () => {
    is3DMode.value = !is3DMode.value
    if (!is3DMode.value) {
        isMouseOver.value = false
    }
}

const getPartImage = (partId) => {
    return currentModel.value.base
}

const changePartColor = (partId, color) => {
    const existingPart = customParts.find(part => part.id === partId)
    if (existingPart) {
        existingPart.color = color
    } else {
        customParts.push({
            id: partId,
            color: color,
            hue: Math.random() * 360,
            brightness: '100%',
            saturation: '100%',
            image: getPartImage(partId)
        })
    }
}

const getCurrentColor = (partId) => {
    const part = customParts.find(part => part.id === partId)
    return part ? part.color : '#000000'
}

const saveDesign = () => {
    const design = {
        model: currentModel.value,
        customization: [...customParts],
        material: currentMaterial.value,
        timestamp: new Date().toISOString()
    }
    console.log('Design saved:', design)
    alert('🎉 Thiết kế đã được lưu! Bạn có thể xem trong mục "Thiết kế của tôi"')
}

const resetDesign = () => {
    customParts.splice(0, customParts.length)
    currentMaterial.value = 'Da lộn'
    currentFixedAngle.value = 0
    is3DMode.value = true
}

const loadDesign = (design) => {
    customParts.splice(0, customParts.length)
    Object.entries(design.settings).forEach(([partId, color]) => {
        customParts.push({
            id: partId,
            color: color,
            hue: Math.random() * 360,
            brightness: '100%',
            saturation: '100%',
            image: getPartImage(partId)
        })
    })
    currentFixedAngle.value = 0
    is3DMode.value = true
}
</script>

<style scoped>
/* 3D Effects */
.perspective {
    perspective: 1000px;
}

/* Container 3D */
.container-3d {
    perspective: 1000px;
    /* giúp 3D nhìn rõ hơn */
}

/* Giày 3D */
.shoe-3d {
    transform-style: preserve-3d;
    transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1),
        filter 0.5s cubic-bezier(0.23, 1, 0.32, 1);
    animation: float 6s ease-in-out infinite;
    /* hiệu ứng float mặc định */
}

/* Khi hover container */
.container-3d:hover .shoe-3d {
    filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.3));
    transform: rotateY(10deg) rotateX(5deg);
    /* hiệu ứng 3D */
    animation: none;
    /* tắt float khi hover */
}

/* Keyframes float */
@keyframes float {

    0%,
    100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }
}


/* Keyframes float */
@keyframes float {

    0%,
    100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }
}



/* Smooth transitions */
* {
    transition: all 0.3s ease;
}

/* Enhanced shadows for 3D effect */
.shadow-2xl {
    box-shadow:
        0 25px 50px -12px rgba(0, 0, 0, 0.25),
        0 0 0 1px rgba(0, 0, 0, 0.05);
}

/* Custom animations */
@keyframes float {

    0%,
    100% {
        transform: translateY(0px) rotateX(0deg) rotateY(0deg);
    }

    50% {
        transform: translateY(-10px) rotateX(5deg) rotateY(5deg);
    }
}

.shoe-3d:not(:hover) {
    animation: float 6s ease-in-out infinite;
}


/* Responsive adjustments */
@media (max-width: 1024px) {
    .container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Reduce 3D effect on mobile for better performance */
    .perspective {
        perspective: 500px;
    }
}

/* Custom scrollbar for color picker */
.color-picker {
    scrollbar-width: thin;
    scrollbar-color: #cbd5e0 #f7fafc;
}

.color-picker::-webkit-scrollbar {
    height: 6px;
}

.color-picker::-webkit-scrollbar-track {
    background: #f7fafc;
    border-radius: 3px;
}

.color-picker::-webkit-scrollbar-thumb {
    background: #cbd5e0;
    border-radius: 3px;
}
</style>