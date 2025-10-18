<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100 px-4">
    <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 max-w-7xl w-full">
      <!-- Left Side -->
      <div class="text-center lg:text-left lg:w-1/2 flex flex-col justify-center">
        <!-- Icon and Error Code on same row -->
        <div class="flex items-center justify-center lg:justify-start gap-6 mb-8 relative">
          <!-- Animated Icon -->
          <div class="animate-bounce">
            <svg class="w-32 h-32 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>

          <!-- Error Code -->
          <h1
            class="text-9xl font-black text-transparent bg-clip-text bg-gradient-to-r from-gray-800 to-gray-600 drop-shadow-lg">
            403
          </h1>

          <!-- Ping Animation Background -->
          <div
            class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-48 h-48 bg-gray-300 rounded-full opacity-20 animate-ping">
          </div>
        </div>

        <!-- Error Title -->
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          Truy cập bị từ chối
        </h2>

        <!-- Error Message -->
        <p class="text-xl text-gray-700 mb-2">
          Bạn không có quyền truy cập vào trang này
        </p>
        <p class="text-gray-600 mb-8">
          Vui lòng kiểm tra lại thông tin đăng nhập hoặc liên hệ với quản trị viên để được hỗ trợ.
        </p>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start items-center">
          <router-link to="/"
            class="inline-flex items-center gap-2 bg-gradient-to-r from-gray-800 to-gray-900 text-white px-8 py-3 rounded-lg font-semibold hover:from-gray-900 hover:to-black transition-all transform hover:scale-105 shadow-lg">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            Về trang chủ
          </router-link>

          <router-link to="/login"
            class="inline-flex items-center gap-2 bg-white text-gray-800 px-8 py-3 rounded-lg font-semibold hover:bg-gray-50 transition-all transform hover:scale-105 shadow-lg border-2 border-gray-300">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
            </svg>
            Đăng nhập
          </router-link>
        </div>
      </div>

      <!-- Right Side -->
      <div class="lg:w-1/2 flex flex-col justify-center">
        <!-- Help Section -->
        <div class="mb-8">
          <h3 class="text-lg font-semibold text-gray-900 mb-6">Lý do có thể gây ra lỗi này:</h3>

          <!-- Row 1 -->
          <div class="flex flex-col md:flex-row gap-4 mb-4">
            <!-- Item 1 -->
            <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex-1">
              <svg class="w-6 h-6 text-gray-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clip-rule="evenodd" />
              </svg>
              <div>
                <h4 class="font-semibold text-gray-900">Chưa đăng nhập</h4>
                <p class="text-sm text-gray-700">Bạn cần đăng nhập để truy cập</p>
              </div>
            </div>

            <!-- Item 2 -->
            <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex-1">
              <svg class="w-6 h-6 text-gray-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clip-rule="evenodd" />
              </svg>
              <div>
                <h4 class="font-semibold text-gray-900">Không đủ quyền</h4>
                <p class="text-sm text-gray-700">Tài khoản không có quyền truy cập</p>
              </div>
            </div>
          </div>

          <!-- Row 2 -->
          <div class="flex flex-col md:flex-row gap-4">
            <!-- Item 3 -->
            <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex-1">
              <svg class="w-6 h-6 text-gray-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clip-rule="evenodd" />
              </svg>
              <div>
                <h4 class="font-semibold text-gray-900">Phiên đăng nhập hết hạn</h4>
                <p class="text-sm text-gray-700">Vui lòng đăng nhập lại</p>
              </div>
            </div>

            <!-- Item 4 -->
            <div class="flex items-start gap-3 bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex-1">
              <svg class="w-6 h-6 text-gray-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clip-rule="evenodd" />
              </svg>
              <div>
                <h4 class="font-semibold text-gray-900">Tài khoản bị khóa</h4>
                <p class="text-sm text-gray-700">Liên hệ admin để mở khóa</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Support -->
        <div class="p-6 bg-white rounded-lg shadow-lg border border-gray-200">
          <p class="text-gray-800 mb-4 font-semibold">Cần hỗ trợ?</p>

          <!-- Contact Info -->
          <div class="flex gap-4 justify-center lg:justify-start mb-4">
            <a href="mailto:support@shoezshop.com"
              class="text-gray-700 hover:text-gray-900 flex items-center gap-1 transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              Email
            </a>
            <span class="text-gray-400">|</span>
            <a href="tel:1900xxxx" class="text-gray-700 hover:text-gray-900 flex items-center gap-1 transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              Hotline
            </a>
          </div>

          <!-- Social Media -->
          <div class="flex gap-3 justify-center lg:justify-start">
            <!-- Zalo -->
            <a href="https://zalo.me/your-zalo" target="_blank" rel="noopener noreferrer"
              class="w-10 h-10 bg-blue-500 hover:bg-blue-600 rounded-full flex items-center justify-center transition-colors shadow-md">
              <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="currentColor">
                <path
                  d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z" />
                <path
                  d="M12 6c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z" />
              </svg>
            </a>

            <!-- Facebook -->
            <a href="https://facebook.com/your-page" target="_blank" rel="noopener noreferrer"
              class="w-10 h-10 bg-blue-600 hover:bg-blue-700 rounded-full flex items-center justify-center transition-colors shadow-md">
              <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
              </svg>
            </a>

            <!-- Instagram -->
            <a href="https://instagram.com/your-account" target="_blank" rel="noopener noreferrer"
              class="w-10 h-10 bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 rounded-full flex items-center justify-center transition-colors shadow-md">
              <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 403 Forbidden page with monochrome color scheme
</script>

<style scoped>
@keyframes ping {

  75%,
  100% {
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes bounce {

  0%,
  100% {
    transform: translateY(-5%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }

  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
</style>
