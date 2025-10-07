<template>
  <div class="min-h-screen flex flex-col md:flex-row bg-white">
    <!-- Phần hình ảnh với slideshow 3D -->
    <div
      class="w-full md:w-1/2 relative overflow-hidden bg-gray-100 h-[400px] md:h-auto"
    >
      <div class="absolute inset-0 flex items-center justify-center">
        <div class="relative w-full h-full">
          <div class="slideshow-3d h-full w-full perspective-1000">
            <transition-group
              name="slide"
              tag="div"
              class="relative h-full w-full"
            >
              <div
                v-for="(image, index) in images"
                :key="image.id"
                v-show="currentSlide === index"
                class="slide-3d absolute inset-0 flex items-center justify-center transform-style-preserve-3d"
                :class="{
                  'slide-active': currentSlide === index,
                  'slide-prev':
                    currentSlide ===
                    (index - 1 + images.length) % images.length,
                  'slide-next': currentSlide === (index + 1) % images.length,
                }"
              >
                <img
                  :src="image.url"
                  :alt="'Slide ' + (index + 1)"
                  class="object-cover w-full h-full rounded-lg shadow-xl"
                />
                <div
                  class="absolute inset-0 bg-black bg-opacity-20 rounded-lg"
                ></div>
              </div>
            </transition-group>
          </div>

          <!-- Slide indicators -->
          <div
            class="absolute bottom-8 left-0 right-0 flex justify-center space-x-2"
          >
            <button
              v-for="(image, index) in images"
              :key="'indicator-' + image.id"
              @click="goToSlide(index)"
              class="w-3 h-3 rounded-full transition-all"
              :class="
                currentSlide === index
                  ? 'bg-white w-6'
                  : 'bg-white bg-opacity-50'
              "
            ></button>
          </div>
        </div>
      </div>
    </div>

    <!-- Phần form đăng nhập -->
    <div class="w-full md:w-1/2 flex items-center justify-center p-6 md:p-12">
      <div class="w-full max-w-md space-y-6">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900">Chào mừng</h1>
          <p class="mt-2 text-gray-600">Đăng nhập để trải nghiệm dịch vụ</p>
        </div>

        <form class="mt-6 space-y-4" @submit.prevent="onSubmit">
          <FormInput
            v-model="username"
            label="Tài khoản"
            id="username"
            placeholder="Nhập tài khoản"
          />
          <span class="text-red-500 text-sm">{{ usernameError }}</span>

          <FormInput
            v-model="password"
            label="Mật khẩu"
            id="password"
            type="password"
            placeholder="Nhập mật khẩu"
          />
          <span class="text-red-500 text-sm">{{ passwordError }}</span>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <label for="remember-me" class="ml-2 block text-sm text-gray-700">
                Ghi nhớ đăng nhập
              </label>
            </div>

            <a
              href="#"
              class="text-sm font-medium text-blue-600 hover:text-blue-500"
            >
              Quên mật khẩu?
            </a>
          </div>

          <div>
            <FormButton
              label="Đăng nhập"
              type="submit"
              variant="black"
              @click="onSubmit"
              class="w-full"
            />
          </div>
        </form>

        <div class="relative">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-white text-gray-500">Hoặc tiếp tục với</span>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <!-- Nút đăng nhập bằng Google -->
          <button
            type="button"
            class="w-full flex items-center justify-center px-4 py-2 border border-gray-200 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-all"
            :onclick="loginWithGoogle"
            >
            <svg
              class="w-5 h-5 mr-2"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 48 48"
            >
              <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/>
              <path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/>
              <path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/>
              <path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/>
            </svg>
            Google
          </button>
          
          <!-- Nút đăng nhập bằng Facebook -->
          <button
            type="button"
            class="w-full flex items-center justify-center px-4 py-2 border border-gray-200 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-all"
            :onClick="loginWithFacebook"
          >
            <svg
              class="w-5 h-5 mr-2 text-blue-600"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 320 512"
            >
              <path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/>
            </svg>
            Facebook
          </button>
        </div>

        <p class="text-center text-sm text-gray-500">
          Chưa có tài khoản?
          <a href="/register" class="font-medium text-blue-600 hover:text-blue-500"
            >Đăng ký ngay</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted, onBeforeUnmount } from "vue";
import FormInput from "../components/FormInput.vue";
import FormButton from "../components/FormButton.vue";
import { useRoute, useRouter } from "vue-router";
import * as yup from 'yup'
import { useForm } from "vee-validate";
import AuthService from "@/api-services/AuthService";

const route = useRoute();
const router = useRouter();

const schema = yup.object({
  username: yup.string().required("Vui lòng nhập tài khoản"),
  password: yup.string().required("Vui lòng nhập mật khẩu").min(6, "Mật khẩu tối thiểu 6 ký tự"),
})

const { handleSubmit } = useForm({
  validationSchema: schema,
});

const currentSlide = ref(0);
const images = [
  {
    id: 1,
    url: "https://images.unsplash.com/photo-1600269452121-4f2416e55c28?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
  },
  {
    id: 2,
    url: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
  },
  {
    id: 3,
    url: "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
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

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + images.length) % images.length;
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

const onSubmit =async () => {
  console.log("Vào đây rồi ");
  
  const response = await AuthService.login({username:username.value,password:password.value})
};

const loginWithGoogle = () => {
  console.log("vafo dday roi nah");
  AuthService.loginWithGoogle();
}
 const loginWithFacebook = () => {
  AuthService.loginWithFacebook()
 }
</script>

<style scoped>
/* Slideshow 3D animations */
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .min-h-screen {
    flex-direction: column;
  }

  .w-full.md\:w-1\/2 {
    width: 100%;
    height: 300px;
  }

  .p-6.md\:p-12 {
    padding: 2rem 1rem;
  }

  .slideshow-3d {
    perspective: none;
  }

  .slide-prev {
    transform: translateX(-100%);
    opacity: 0;
  }

  .slide-next {
    transform: translateX(100%);
    opacity: 0;
  }
}
</style>