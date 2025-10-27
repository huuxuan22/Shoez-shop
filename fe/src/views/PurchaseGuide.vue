<template>
  <div class="max-w-5xl mx-auto mt-12">
    <div class="bg-white text-gray-900 rounded-xl shadow p-8">
      <h1 class="text-3xl font-extrabold mb-4">Hướng dẫn mua hàng</h1>
      <p class="text-gray-700 mb-6">Các bước mua hàng đơn giản, nhanh chóng — theo dõi hướng dẫn bên dưới để hoàn tất đơn hàng một cách an toàn.</p>

      <div class="grid gap-6 md:grid-cols-3">
        <div class="p-4 border rounded-lg hover:shadow-lg transition">
          <div class="text-indigo-600 text-2xl mb-3">🛒</div>
          <h3 class="font-semibold mb-2">Chọn sản phẩm</h3>
          <p class="text-gray-700 text-sm">Chọn size, màu và số lượng rồi thêm vào giỏ hàng.</p>
        </div>

        <div class="p-4 border rounded-lg hover:shadow-lg transition">
          <div class="text-green-600 text-2xl mb-3">💳</div>
          <h3 class="font-semibold mb-2">Thanh toán</h3>
          <p class="text-gray-700 text-sm">Chọn phương thức thanh toán phù hợp: COD, thẻ, chuyển khoản hoặc ví điện tử.</p>
        </div>

        <div class="p-4 border rounded-lg hover:shadow-lg transition">
          <div class="text-blue-600 text-2xl mb-3">🚚</div>
          <h3 class="font-semibold mb-2">Giao hàng & Theo dõi</h3>
          <p class="text-gray-700 text-sm">Theo dõi trạng thái trong trang Hồ sơ hoặc liên hệ CSKH để biết chi tiết.</p>
        </div>
      </div>

      <div class="mt-6 bg-gray-50 border rounded-lg p-4">
        <h3 class="font-semibold mb-2">Mẹo</h3>
        <ul class="list-disc ml-6 text-gray-700">
          <li>Kiểm tra kỹ size và mô tả sản phẩm trước khi mua.</li>
          <li>Lưu lại mã đơn hàng để tra cứu nhanh.</li>
        </ul>
      </div>

      <div class="mt-6 text-right">
        <router-link to="/contact" class="inline-block bg-indigo-600 text-white px-6 py-2 rounded-lg shadow hover:bg-indigo-700">Liên hệ hỗ trợ</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
// Static informational page
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
