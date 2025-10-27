<template>
  <div class="max-w-5xl mx-auto mt-12">
    <div class="bg-white text-gray-900 rounded-xl p-8 shadow-lg">
      <h1 class="text-3xl font-extrabold">Bảo hành sản phẩm</h1>
      <p class="mt-2 text-gray-700 max-w-2xl">Thông tin bảo hành rõ ràng giúp bạn yên tâm khi mua sắm tại Shoez Shop. Dưới đây là những điều cần biết khi yêu cầu bảo hành.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-xl font-semibold mb-3">Thời hạn & Điều kiện</h3>
        <p class="text-gray-700 mb-2">Mỗi sản phẩm có thời hạn bảo hành khác nhau; kiểm tra trang sản phẩm hoặc phiếu bảo hành kèm theo.</p>
        <ul class="list-disc ml-6 text-gray-700">
          <li>Sản phẩm trong thời hạn bảo hành.</li>
          <li>Lỗi do nhà sản xuất (không áp dụng do va chạm, ngấm nước).</li>
          <li>Kèm hóa đơn hoặc mã bảo hành.</li>
        </ul>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-xl font-semibold mb-3">Trường hợp không được bảo hành</h3>
        <ul class="list-disc ml-6 text-gray-700">
          <li>Sử dụng sai cách, va chạm, rơi vỡ.</li>
          <li>Sản phẩm hỏng do tác động môi trường hoặc hao mòn tự nhiên.</li>
          <li>Thiếu tem/phiếu bảo hành hoặc chứng từ mua hàng.</li>
        </ul>
      </div>
    </div>

    <div class="bg-white rounded-lg shadow p-6 mt-6">
      <h3 class="text-2xl font-semibold mb-4">Quy trình bảo hành</h3>
      <ol class="list-decimal ml-6 space-y-2 text-gray-700">
        <li>Liên hệ CSKH hoặc mang sản phẩm tới trung tâm bảo hành.</li>
        <li>Nhân viên kiểm tra và đánh giá nguyên nhân hỏng hóc.</li>
        <li>Sửa chữa hoặc thay thế theo chính sách nếu đủ điều kiện.</li>
      </ol>
    </div>

    <div class="mt-6 text-right">
      <router-link to="/contact" class="inline-block bg-indigo-600 text-white px-6 py-2 rounded-lg shadow hover:bg-indigo-700">Liên hệ bảo hành</router-link>
    </div>
  </div>
</template>

<script setup>
// Static informational page
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
