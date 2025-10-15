<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-red-50 to-orange-50">
    <div class="text-center px-4">
      <!-- Animated Icon -->
      <div class="mb-8 relative">
        <div class="animate-bounce">
          <svg class="w-32 h-32 mx-auto text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <div class="absolute top-0 left-1/2 transform -translate-x-1/2 w-48 h-48 bg-red-200 rounded-full opacity-20 animate-ping"></div>
      </div>

      <!-- Error Code -->
      <h1 class="text-9xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-orange-600 mb-4 drop-shadow-lg">
        403
      </h1>

      <!-- Error Title -->
      <h2 class="text-4xl font-bold text-gray-800 mb-4">
        Truy cập bị từ chối
      </h2>

      <!-- Error Message -->
      <p class="text-xl text-gray-600 mb-2 max-w-md mx-auto">
        Bạn không có quyền truy cập vào trang này
      </p>
      <p class="text-gray-500 mb-8 max-w-md mx-auto">
        Vui lòng kiểm tra lại thông tin đăng nhập hoặc liên hệ với quản trị viên để được hỗ trợ.
      </p>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
        <router-link 
          to="/"
          class="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-blue-700 text-white px-8 py-3 rounded-lg font-semibold hover:from-blue-700 hover:to-blue-800 transition-all transform hover:scale-105 shadow-lg"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          Về trang chủ
        </router-link>

        <router-link 
          to="/login"
          class="inline-flex items-center gap-2 bg-white text-gray-700 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-all transform hover:scale-105 shadow-lg border-2 border-gray-300"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
          </svg>
          Đăng nhập
        </router-link>
      </div>

      <!-- Help Section -->
      <div class="mt-12 pt-8 border-t border-gray-200 max-w-2xl mx-auto">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Lý do có thể gây ra lỗi này:</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-left">
          <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm">
            <svg class="w-6 h-6 text-red-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
            <div>
              <h4 class="font-semibold text-gray-800">Chưa đăng nhập</h4>
              <p class="text-sm text-gray-600">Bạn cần đăng nhập để truy cập</p>
            </div>
          </div>

          <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm">
            <svg class="w-6 h-6 text-red-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
            <div>
              <h4 class="font-semibold text-gray-800">Không đủ quyền</h4>
              <p class="text-sm text-gray-600">Tài khoản không có quyền truy cập</p>
            </div>
          </div>

          <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm">
            <svg class="w-6 h-6 text-red-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
            <div>
              <h4 class="font-semibold text-gray-800">Phiên đăng nhập hết hạn</h4>
              <p class="text-sm text-gray-600">Vui lòng đăng nhập lại</p>
            </div>
          </div>

          <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm">
            <svg class="w-6 h-6 text-red-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
            <div>
              <h4 class="font-semibold text-gray-800">Tài khoản bị khóa</h4>
              <p class="text-sm text-gray-600">Liên hệ admin để mở khóa</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Contact Support -->
      <div class="mt-8 p-6 bg-white rounded-lg shadow-lg inline-block">
        <p class="text-gray-700 mb-2">Cần hỗ trợ?</p>
        <div class="flex gap-4 justify-center">
          <a href="mailto:support@shoezshop.com" class="text-blue-600 hover:text-blue-700 flex items-center gap-1">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            Email
          </a>
          <span class="text-gray-300">|</span>
          <a href="tel:1900xxxx" class="text-blue-600 hover:text-blue-700 flex items-center gap-1">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            Hotline
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 403 Forbidden page with detailed error information
</script>

<style scoped>
@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-5%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
</style>
