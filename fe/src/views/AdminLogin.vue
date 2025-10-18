<template>
  <!-- Toast Notification -->
  <Teleport to="body">
    <Transition name="toast">
      <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
        <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
      </div>
    </Transition>
  </Teleport>

  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-gray-800 to-black relative overflow-hidden">
    <!-- Animated Background Elements -->
    <div class="absolute inset-0 overflow-hidden">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"></div>
      <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
      <div class="absolute top-40 left-40 w-80 h-80 bg-pink-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
    </div>

    <!-- Login Card -->
    <div class="relative z-10 w-full max-w-md px-6">
      <div class="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl border border-white/20 p-8">
        <!-- Logo & Title -->
        <div class="text-center mb-8">
          <div class="inline-flex items-center justify-center w-20 h-20 bg-white rounded-2xl shadow-lg mb-4">
            <svg class="w-12 h-12 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
          <h1 class="text-3xl font-bold text-white mb-2">Admin Portal</h1>
          <p class="text-gray-300">Shoez Management System</p>
        </div>

        <!-- Login Form -->
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Email Field -->
          <div>
            <label class="block text-sm font-medium text-gray-200 mb-2">
              Email hoặc Tên đăng nhập
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </div>
              <input
                v-model="loginForm.email"
                type="text"
                required
                class="w-full pl-10 pr-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all"
                placeholder="admin@shoez.com"
              />
            </div>
          </div>

          <!-- Password Field -->
          <div>
            <label class="block text-sm font-medium text-gray-200 mb-2">
              Mật khẩu
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
              </div>
              <input
                v-model="loginForm.password"
                :type="showPassword ? 'text' : 'password'"
                required
                class="w-full pl-10 pr-12 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all"
                placeholder="••••••••"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-white transition-colors"
              >
                <svg v-if="!showPassword" class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                <svg v-else class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <label class="flex items-center cursor-pointer">
              <input
                v-model="loginForm.rememberMe"
                type="checkbox"
                class="w-4 h-4 bg-white/10 border-white/20 rounded text-white focus:ring-2 focus:ring-white/50 cursor-pointer"
              />
              <span class="ml-2 text-sm text-gray-300">Ghi nhớ đăng nhập</span>
            </label>
            <a href="#" class="text-sm text-gray-300 hover:text-white transition-colors">
              Quên mật khẩu?
            </a>
          </div>

          <!-- Login Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full bg-white text-gray-900 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-all transform hover:scale-[1.02] active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-lg"
          >
            <span v-if="!isLoading" class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
              </svg>
              Đăng nhập
            </span>
            <span v-else class="flex items-center justify-center">
              <svg class="animate-spin h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Đang xử lý...
            </span>
          </button>
        </form>

        <!-- Divider -->
        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-white/20"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-transparent text-gray-400">hoặc</span>
          </div>
        </div>

        <!-- Back to Customer Login -->
        <router-link
          to="/login"
          class="block w-full text-center py-3 border-2 border-white/20 rounded-lg text-white hover:bg-white/10 transition-all font-medium"
        >
          <div class="flex items-center justify-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Đăng nhập với tài khoản khách hàng
          </div>
        </router-link>

        <!-- Security Notice -->
        <div class="mt-6 p-4 bg-yellow-500/10 border border-yellow-500/20 rounded-lg">
          <div class="flex items-start">
            <svg class="w-5 h-5 text-yellow-400 mr-2 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <p class="text-xs text-yellow-200">
              Đây là khu vực quản trị hệ thống. Chỉ dành cho người quản lý được ủy quyền. Mọi hành động đều được ghi nhận.
            </p>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="text-center mt-6">
        <p class="text-gray-400 text-sm">
          © 2025 Shoez Shop. All rights reserved.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import ToastNotification from '@/components/ToastNotification.vue';

const router = useRouter();
const authStore = useAuthStore();

// State
const isLoading = ref(false);
const showPassword = ref(false);

const loginForm = reactive({
  email: '',
  password: '',
  rememberMe: false
});

const toast = reactive({
  show: false,
  message: '',
  type: 'success'
});

// Methods
const showToast = (message, type = 'success') => {
  toast.message = message;
  toast.type = type;
  toast.show = true;
  setTimeout(() => {
    toast.show = false;
  }, 3000);
};

const handleLogin = async () => {
  if (!loginForm.email || !loginForm.password) {
    showToast('Vui lòng nhập đầy đủ thông tin', 'error');
    return;
  }

  isLoading.value = true;

  try {
    // Call API login
    const response = await authStore.login({
      email: loginForm.email,
      password: loginForm.password
    });

    // Check if user is admin
    if (response.user_principal.role !== 'admin' && response.user_principal.role !== 'ADMIN') {
      showToast('Bạn không có quyền truy cập vào khu vực quản trị', 'error');
      authStore.logout();
      isLoading.value = false;
      return;
    }

    showToast('Đăng nhập thành công! Đang chuyển hướng...', 'success');

    // Save remember me preference
    if (loginForm.rememberMe) {
      localStorage.setItem('adminRememberMe', 'true');
    }

    // Redirect to admin dashboard
    setTimeout(() => {
      router.push('/admin');
    }, 1000);

  } catch (error) {
    console.error('Login error:', error);
    const errorMessage = error.response?.data?.detail || 'Email hoặc mật khẩu không đúng';
    showToast(errorMessage, 'error');
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
/* Toast Animation */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100px);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100px);
}

/* Blob Animation */
@keyframes blob {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  33% {
    transform: translate(30px, -50px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
}

.animate-blob {
  animation: blob 7s infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}
</style>
