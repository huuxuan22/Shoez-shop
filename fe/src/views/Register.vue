<template>
  <!-- Toast Notification -->
  <Teleport to="body">
    <Transition name="toast">
      <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
        <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
      </div>
    </Transition>
  </Teleport>

  <div class="min-h-screen flex flex-col md:flex-row bg-white">
    <!-- Slideshow ảnh -->
    <div class="w-full md:w-1/2 relative overflow-hidden bg-gray-100 h-[400px] md:h-auto">
      <div class="absolute inset-0 flex items-center justify-center">
        <div class="relative w-full h-full">
          <div class="slideshow-3d h-full w-full perspective-1000">
            <transition-group name="slide" tag="div" class="relative h-full w-full">
              <div v-for="(image, index) in images" :key="image.id" v-show="currentSlide === index"
                class="slide-3d absolute inset-0 flex items-center justify-center transform-style-preserve-3d" :class="{
                  'slide-active': currentSlide === index,
                  'slide-prev':
                    currentSlide ===
                    (index - 1 + images.length) % images.length,
                  'slide-next': currentSlide === (index + 1) % images.length,
                }">
                <img :src="image.url" :alt="'Slide ' + (index + 1)"
                  class="object-cover w-full h-full rounded-lg shadow-xl" />
                <div class="absolute inset-0 bg-black bg-opacity-20 rounded-lg"></div>
              </div>
            </transition-group>
          </div>

          <!-- Indicator -->
          <div class="absolute bottom-8 left-0 right-0 flex justify-center space-x-2">
            <button v-for="(image, index) in images" :key="'indicator-' + image.id" @click="goToSlide(index)"
              class="w-3 h-3 rounded-full transition-all" :class="currentSlide === index
                ? 'bg-white w-6'
                : 'bg-white bg-opacity-50'
                "></button>
          </div>
        </div>
      </div>
    </div>

    <!-- Form đăng ký -->
    <div class="w-full md:w-1/2 flex items-center justify-center p-6 md:p-12">
      <div class="w-full max-w-md space-y-6">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900">Đăng ký</h1>
          <p class="mt-2 text-gray-600">Tạo tài khoản mới để trải nghiệm</p>
        </div>

        <Form @submit="onSubmit" :validation-schema="schema" class="mt-6 space-y-4">
          <!-- Họ và tên -->
          <div>
            <label for="full_name" class="block text-sm font-medium text-gray-700 mb-1">
              Họ và tên
            </label>
            <Field name="full_name" type="text" id="full_name"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border"
              placeholder="Nhập họ và tên" />
            <ErrorMessage name="full_name" class="text-red-500 text-sm mt-1 block" />
          </div>

          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-1">
              Email
            </label>
            <Field name="email" type="email" id="email"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border"
              placeholder="Nhập email" />
            <ErrorMessage name="email" class="text-red-500 text-sm mt-1 block" />
          </div>

          <!-- Mật khẩu -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 mb-1">
              Mật khẩu
            </label>
            <Field name="password" type="password" id="password"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border"
              placeholder="Nhập mật khẩu" />
            <ErrorMessage name="password" class="text-red-500 text-sm mt-1 block" />
          </div>

          <!-- Số điện thoại -->
          <div>
            <label for="numberphone" class="block text-sm font-medium text-gray-700 mb-1">
              Số điện thoại
            </label>
            <Field name="numberphone" type="tel" id="numberphone"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border"
              placeholder="Nhập số điện thoại (VD: 0912345678)" />
            <ErrorMessage name="numberphone" class="text-red-500 text-sm mt-1 block" />
          </div>

          <div>
            <FormButton label="Đăng ký" type="submit" variant="black" class="w-full" />
          </div>
        </Form>

        <p class="text-center text-sm text-gray-500">
          Đã có tài khoản?
          <a href="/login" class="font-medium text-black-600 hover:text-gray-500">Đăng nhập ngay</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import FormButton from "../components/FormButton.vue";
import ToastNotification from '@/components/ToastNotification.vue';
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';

const router = useRouter();
const authStore = useAuthStore();

// Toast notification
let timer = null;
const toast = ref({
  show: false,
  message: '',
  type: 'info',
});

// Show toast function
function showToast(message, type = 'info') {
  if (timer) {
    clearTimeout(timer);
  }
  toast.value.show = true;
  toast.value.message = message;
  toast.value.type = type;

  timer = setTimeout(() => {
    toast.value.show = false;
  }, 3000);
}

// Validation schema với yup
const schema = yup.object({
  full_name: yup
    .string()
    .required("Vui lòng nhập họ và tên")
    .min(2, "Họ và tên phải có ít nhất 2 ký tự")
    .max(64, "Họ và tên không được quá 64 ký tự"),

  email: yup
    .string()
    .required("Vui lòng nhập email")
    .email("Email không hợp lệ")
    .min(6, "Email phải từ 6 đến 64 ký tự")
    .max(64, "Email phải từ 6 đến 64 ký tự"),

  password: yup
    .string()
    .required("Vui lòng nhập mật khẩu")
    .min(6, "Mật khẩu phải có ít nhất 6 ký tự")
    .max(64, "Mật khẩu không được quá 64 ký tự"),

  numberphone: yup
    .string()
    .required("Vui lòng nhập số điện thoại")
    .matches(
      /^(0|\+84)\d{9}$/,
      "Số điện thoại không hợp lệ (VD: 0912345678 hoặc +84912345678)"
    ),
});

const currentSlide = ref(0);

// Cách 1: Sử dụng ảnh từ thư mục public (Khuyến nghị)
const images = [
  {
    id: 1,
    url: "/images/register/slide-1.jpg",
  },
  {
    id: 2,
    url: "/images/register/slide-2.jpg",
  },
  {
    id: 3,
    url: "/images/register/slide-3.jpg",
  },
];

let slideInterval;

const goToSlide = (index) => {
  currentSlide.value = index;
  resetInterval();
};

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % images.length;
  resetInterval();
};

const startInterval = () => {
  slideInterval = setInterval(() => {
    nextSlide();
  }, 5000);
};

const resetInterval = () => {
  clearInterval(slideInterval);
  startInterval();
};

onMounted(() => {
  startInterval();
});

onBeforeUnmount(() => {
  clearInterval(slideInterval);
});

// Submit handler - VeeValidate sẽ tự động validate trước khi gọi hàm này
const onSubmit = async (values) => {
  try {
    console.log('Register form data:', values);

    const response = await authStore.register({
      full_name: values.full_name,
      email: values.email,
      password: values.password,
      numberphone: values.numberphone,
    });

    showToast('Đăng ký thành công!', 'success');

    // Delay chuyển trang 1.5 giây để user thấy toast
    setTimeout(() => {
      router.push('/');
    }, 1500);
  } catch (error) {
    console.error('Register error:', error);
    const errorMessage = error.data?.detail || error.message || 'Đăng ký thất bại!';
    showToast(errorMessage, 'error');
  }
};
</script>

<style scoped>
/* Toast animations */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

/* Slideshow animations */
.slideshow-3d {
  perspective: 1000px;
}

.slide-3d {
  transition: all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  backface-visibility: hidden;
  transform-style: preserve-3d;
  opacity: 0;
  z-index: 0;
}

.slide-active {
  opacity: 1;
  transform: translateX(0) scale(1);
  z-index: 10;
}

.slide-prev {
  opacity: 0.5;
  transform: translateX(-30%) scale(0.9);
  z-index: 5;
}

.slide-next {
  opacity: 0.5;
  transform: translateX(30%) scale(0.9);
  z-index: 5;
}
</style>
