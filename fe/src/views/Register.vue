<template>
  <div class="min-h-screen flex flex-col md:flex-row bg-white">
    <!-- Slideshow ảnh -->
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

          <!-- Indicator -->
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

    <!-- Form đăng ký -->
    <div class="w-full md:w-1/2 flex items-center justify-center p-6 md:p-12">
      <div class="w-full max-w-md space-y-6">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900">Đăng ký</h1>
          <p class="mt-2 text-gray-600">Tạo tài khoản mới để trải nghiệm</p>
        </div>

        <form class="mt-6 space-y-4">
          <FormInput
            v-model="form.name"
            label="Họ và tên"
            id="name"
            placeholder="Nhập họ và tên"
          />

          <FormInput
            v-model="form.age"
            label="Tuổi"
            id="age"
            type="number"
            placeholder="Nhập tuổi"
          />

          <!-- Giới tính -->
          <div class="space-y-1">
            <label for="gender" class="block text-sm font-medium text-gray-700"
              >Giới tính</label
            >
            <select
              v-model="form.gender"
              id="gender"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
            >
              <option disabled value="">-- Chọn giới tính --</option>
              <option value="male">Nam</option>
              <option value="female">Nữ</option>
              <option value="other">Khác</option>
            </select>
          </div>

          <FormInput
            v-model="form.email"
            label="Email"
            id="email"
            type="email"
            placeholder="Nhập email"
          />

          <FormInput
            v-model="form.password"
            label="Mật khẩu"
            id="password"
            type="password"
            placeholder="Nhập mật khẩu"
          />

          <div>
            <FormButton
              label="Đăng ký"
              type="submit"
              variant="black"
              @click="onSubmit"
              class="w-full"
            />
          </div>
        </form>

        <p class="text-center text-sm text-gray-500">
          Đã có tài khoản?
          <a href="/login" class="font-medium text-blue-600 hover:text-blue-500"
            >Đăng nhập ngay</a
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

const form = reactive({
  name: "",
  age: "",
  gender: "",
  email: "",
  password: "",
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

// Cách 2: Sử dụng link từ Internet
// const images = [
//   {
//     id: 1,
//     url: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
//   },
//   {
//     id: 2,
//     url: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=800&q=80",
//   },
//   {
//     id: 3,
//     url: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=80",
//   },
// ];

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

const onSubmit = (e) => {
  e.preventDefault();
  console.log("Register form submitted:", form);
};
</script>

<style scoped>
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
