<template>
    <DefaultLayout>
        <div class="min-h-screen bg-white">
            <!-- Hero Section -->
            <section class="bg-gray-900 text-white py-20">
                <div class="container mx-auto px-4">
                    <div class="max-w-4xl mx-auto text-center">
                        <h1 class="text-5xl font-bold mb-6">LIÊN HỆ</h1>
                        <p class="text-xl text-gray-300 leading-relaxed">
                            Chúng tôi luôn sẵn sàng lắng nghe và hỗ trợ bạn. Hãy liên hệ với chúng tôi
                            để được tư vấn và giải đáp mọi thắc mắc.
                        </p>
                    </div>
                </div>
            </section>

            <!-- Contact Information & Form -->
            <section class="py-16 bg-white">
                <div class="container mx-auto px-4">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-6xl mx-auto">

                        <!-- Contact Information -->
                        <div>
                            <h2 class="text-3xl font-bold text-gray-900 mb-8">THÔNG TIN LIÊN HỆ</h2>

                            <div class="space-y-6">
                                <!-- Address -->
                                <div class="flex items-start space-x-4">
                                    <div
                                        class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center mt-1">
                                        <i class="fas fa-map-marker-alt text-gray-700"></i>
                                    </div>
                                    <div>
                                        <h3 class="text-lg font-semibold text-gray-900 mb-1">ĐỊA CHỈ</h3>
                                        <p class="text-gray-600">Tầng 6, 266 Đội Cần, Hà Nội</p>
                                        <p class="text-gray-600">P. Uối Cần, Phân Kế Bình</p>
                                    </div>
                                </div>

                                <!-- Phone -->
                                <div class="flex items-start space-x-4">
                                    <div
                                        class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center mt-1">
                                        <i class="fas fa-phone text-gray-700"></i>
                                    </div>
                                    <div>
                                        <h3 class="text-lg font-semibold text-gray-900 mb-1">ĐIỆN THOẠI</h3>
                                        <p class="text-gray-600">1900 6750</p>
                                    </div>
                                </div>

                                <!-- Email -->
                                <div class="flex items-start space-x-4">
                                    <div
                                        class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center mt-1">
                                        <i class="fas fa-envelope text-gray-700"></i>
                                    </div>
                                    <div>
                                        <h3 class="text-lg font-semibold text-gray-900 mb-1">EMAIL</h3>
                                        <p class="text-gray-600">heliocafein@gmail.com</p>
                                    </div>
                                </div>

                                <!-- Map -->
                                <div class="mt-8">
                                    <h3 class="text-lg font-semibold text-gray-900 mb-4">BẢN ĐỒ</h3>
                                    <div class="map-container">
                                        <div class="text-center">
                                            <i class="fas fa-map text-4xl mb-2"></i>
                                            <p>View larger map</p>
                                        </div>
                                    </div>
                                </div>

                                <!-- Social Media -->
                                <div class="mt-8">
                                    <h3 class="text-lg font-semibold text-gray-900 mb-4">THEO DÕI CHÚNG TÔI</h3>
                                    <div class="flex space-x-4">
                                        <a href="#"
                                            class="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center text-white hover:bg-gray-700 transition-colors">
                                            <i class="fab fa-facebook-f"></i>
                                        </a>
                                        <a href="#"
                                            class="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center text-white hover:bg-gray-700 transition-colors">
                                            <i class="fab fa-instagram"></i>
                                        </a>
                                        <a href="#"
                                            class="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center text-white hover:bg-gray-700 transition-colors">
                                            <i class="fab fa-youtube"></i>
                                        </a>
                                        <a href="#"
                                            class="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center text-white hover:bg-gray-700 transition-colors">
                                            <i class="fab fa-tiktok"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Contact Form -->
                        <div>
                            <h2 class="text-3xl font-bold text-gray-900 mb-8">GỬI TIN NHẮN CHO CHÚNG TÔI</h2>

                            <form @submit.prevent="submitForm" class="space-y-6">
                                <!-- Name -->
                                <div>
                                    <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Họ tên
                                        *</label>
                                    <input type="text" id="name" v-model="form.name" required
                                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors"
                                        placeholder="Nhập họ tên *">
                                </div>

                                <!-- Email -->
                                <div>
                                    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email
                                        *</label>
                                    <input type="email" id="email" v-model="form.email" required
                                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors"
                                        placeholder="Nhập Email *">
                                </div>

                                <!-- Content -->
                                <div>
                                    <label for="content" class="block text-sm font-medium text-gray-700 mb-1">Nội dung
                                        *</label>
                                    <textarea id="content" rows="6" v-model="form.content" required
                                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors"
                                        placeholder="Lời nhắn"></textarea>
                                </div>

                                <!-- Submit Button -->
                                <div>
                                    <button type="submit"
                                        class="w-full bg-gray-900 text-white py-3 px-6 rounded-lg font-semibold hover:bg-gray-700 transition-colors duration-200">
                                        GỬI TIN NHẮN
                                    </button>
                                </div>
                            </form>

                            <!-- Brand -->
                            <div class="mt-12 text-center">
                                <p class="text-2xl font-bold text-gray-900">c01LIGHT</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Additional Locations -->
            <section class="py-16 bg-gray-50">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-gray-900 text-center mb-12">CÁC CHI NHÁNH KHÁC</h2>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
                        <!-- Location 1 -->
                        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">Cung thể Hạo Quận Ngựa</h3>
                            <p class="text-gray-600 mb-2">Tổ 6B, Lúc quá</p>
                            <p class="text-gray-600">Hà Nội</p>
                        </div>

                        <!-- Location 2 -->
                        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">HỒ DÂM TRÒN</h3>
                            <p class="text-gray-600 mb-2">Tổ 1B</p>
                            <p class="text-gray-600">Hà Nội</p>
                        </div>

                        <!-- Location 3 -->
                        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">Bảo lạng Chiến thăng B-52</h3>
                            <p class="text-gray-600 mb-2">P. Đội Cần</p>
                            <p class="text-gray-900">Hà Nội</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- CTA Section -->
            <section class="py-16 bg-gray-900 text-white">
                <div class="container mx-auto px-4 text-center">
                    <h2 class="text-3xl font-bold mb-6">CẦN HỖ TRỢ NGAY?</h2>
                    <p class="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
                        Đội ngũ chăm sóc khách hàng của chúng tôi luôn sẵn sàng hỗ trợ bạn 24/7
                    </p>
                    <div class="space-x-4">
                        <a href="tel:19006750"
                            class="bg-white text-gray-900 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors duration-200 inline-block">
                            GỌI NGAY: 1900 6750
                        </a>
                        <a href="mailto:heliocafein@gmail.com"
                            class="border border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-gray-900 transition-colors duration-200 inline-block">
                            GỬI EMAIL
                        </a>
                    </div>
                </div>
            </section>
        </div>
    </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
    name: '',
    email: '',
    content: ''
})

const submitForm = () => {
    // Xử lý gửi form ở đây
    console.log('Form submitted:', form.value)
    alert('Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất có thể.')

    // Reset form
    form.value = {
        name: '',
        email: '',
        content: ''
    }
}
</script>

<style scoped>
.map-container {
    height: 300px;
    background-color: #f3f4f6;
    border-radius: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #6b7280;
}
</style>