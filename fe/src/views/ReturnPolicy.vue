<template>
  <div class="max-w-5xl mx-auto mt-12">
    <div class="bg-white text-gray-900 rounded-xl p-8 shadow-lg">
      <h1 class="text-4xl font-extrabold">Chính sách đổi trả</h1>
      <p class="mt-2 text-gray-700 max-w-2xl">Chúng tôi luôn nỗ lực để đem lại trải nghiệm mua sắm tốt nhất. Dưới đây là các điều kiện và quy trình đổi trả tại Shoez Shop.</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-8">
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-xl font-semibold mb-3">Điều kiện đổi trả</h3>
        <ul class="space-y-2 text-gray-700">
          <li>• Sản phẩm còn nguyên tem, mác, chưa qua sử dụng.</li>
          <li>• Yêu cầu trong vòng <strong>7 ngày</strong> kể từ ngày nhận hàng.</li>
          <li>• Kèm hóa đơn hoặc mã đơn hàng để đối chiếu.</li>
        </ul>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-xl font-semibold mb-3">Quy trình đổi trả</h3>
        <ol class="list-decimal ml-5 space-y-2 text-gray-700">
          <li>Liên hệ CSKH với mã đơn hàng và lý do.</li>
          <li>Gửi trả hàng theo hướng dẫn của Shoez Shop.</li>
          <li>Nhận hàng, kiểm tra và tiến hành đổi/hoàn tiền.</li>
        </ol>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-xl font-semibold mb-3">Hoàn tiền & Lưu ý</h3>
        <p class="text-gray-700 mb-2">Hoàn tiền tùy phương thức thanh toán: <strong>3–14 ngày</strong> làm việc.</p>
        <p class="text-gray-600 text-sm">Phí vận chuyển đổi trả sẽ được xử lý theo chính sách. Sản phẩm giảm giá có thể không áp dụng đổi trả.</p>
      </div>
    </div>

    <div class="bg-white rounded-lg shadow p-6 mt-6">
      <h3 class="text-2xl font-semibold mb-4">Hướng dẫn chi tiết</h3>
      <div class="prose max-w-none text-gray-700">
        <p>1. Liên hệ chăm sóc khách hàng qua <router-link to="/contact" class="text-blue-600 underline">Liên hệ</router-link> hoặc hotline; cung cấp mã đơn hàng và mô tả lỗi.</p>
        <p>2. Nhân viên sẽ gửi hướng dẫn gửi trả và xác nhận điều kiện.</p>
        <p>3. Sau khi nhận hàng và kiểm tra, Shoez Shop sẽ hoàn tiền hoặc đổi sản phẩm theo yêu cầu.</p>
      </div>
    </div>

    <div class="mt-6 text-right">
      <router-link to="/contact" class="inline-block bg-indigo-600 text-white px-6 py-2 rounded-lg shadow hover:bg-indigo-700">Liên hệ hỗ trợ</router-link>
    </div>
  </div>
</template>

<script setup>
// Static page — no script needed for now
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
