<template>
  <div class="max-w-5xl mx-auto mt-12">
    <div class="bg-white text-gray-900 rounded-xl shadow p-8">
      <h1 class="text-3xl font-extrabold mb-4">Câu hỏi thường gặp (FAQ)</h1>
      <p class="text-gray-700 mb-6">Tổng hợp các câu hỏi thường gặp giúp bạn nhanh chóng tìm được câu trả lời.</p>

      <div class="space-y-6">
        <div class="bg-gray-50 border rounded-lg p-6">
          <h3 class="font-semibold text-lg">1. Làm thế nào để đổi size?</h3>
          <p class="text-gray-700 mt-2">Bạn có thể liên hệ CSKH trong vòng 7 ngày kể từ ngày nhận hàng và làm theo hướng dẫn đổi trả. Vui lòng giữ nguyên tem mác và tình trạng sản phẩm.</p>
        </div>

        <div class="bg-gray-50 border rounded-lg p-6">
          <h3 class="font-semibold text-lg">2. Thời gian giao hàng mất bao lâu?</h3>
          <p class="text-gray-700 mt-2">Thời gian giao hàng phụ thuộc vào khu vực và đơn vị vận chuyển, thông thường 2–5 ngày làm việc cho khu vực nội thành.</p>
        </div>

        <div class="bg-gray-50 border rounded-lg p-6">
          <h3 class="font-semibold text-lg">3. Tôi có thể trả hàng nếu sản phẩm lỗi?</h3>
          <p class="text-gray-700 mt-2">Có. Nếu sản phẩm lỗi do nhà sản xuất, vui lòng liên hệ CSKH và gửi bằng chứng (ảnh/ video). Shoez Shop sẽ hướng dẫn quy trình đổi trả hoặc bảo hành.</p>
        </div>

        <div class="bg-gray-50 border rounded-lg p-6">
          <h3 class="font-semibold text-lg">4. Làm sao để theo dõi đơn hàng?</h3>
          <p class="text-gray-700 mt-2">Bạn có thể kiểm tra trạng thái đơn trong trang Hồ sơ > Đơn hàng hoặc liên hệ hotline để được hỗ trợ nhanh.</p>
        </div>

        <div class="text-right">
          <router-link to="/contact" class="inline-block bg-indigo-600 text-white px-6 py-2 rounded-lg shadow hover:bg-indigo-700">Liên hệ hỗ trợ</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Static FAQ page
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
