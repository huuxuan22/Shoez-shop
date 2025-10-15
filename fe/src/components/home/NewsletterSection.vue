<template>
    <section class="py-12 bg-gray-50 border-t border-gray-200">
        <div class="container mx-auto px-4">
            <div class="max-w-2xl mx-auto text-center">
                <h2 class="text-2xl md:text-3xl font-bold text-black mb-2">Nhận ưu đãi</h2>
                <p class="text-gray-600 mb-6">Đăng ký để nhận mã giảm giá 100K</p>

                <form class="flex gap-2">
                    <input v-model="email" type="email" placeholder="Email của bạn"
                        class="flex-1 px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-black" />
                    <button type="submit" @click.prevent="subscribeNewsletter"
                        class="bg-black text-white px-6 py-3 rounded hover:bg-gray-800 transition">
                        Đăng ký
                    </button>
                </form>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')

const subscribeNewsletter = () => {
    if (!email.value) {
        alert('Vui lòng nhập email!');
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        alert('Email không hợp lệ!');
        return;
    }

    alert(`🎉 Đăng ký thành công! Mã giảm giá 100K đã được gửi đến ${email.value}`);
    email.value = '';
}
</script>