<template>
  <div>
    <Header />
    <div class="max-w-3xl mx-auto mt-10 bg-white rounded-xl shadow p-8">
      <div v-if="newsItem">
        <div class="flex items-center gap-3 mb-4">
          <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded">{{ newsItem.date }}</span>
          <span class="text-xs text-gray-400 flex items-center gap-1">
            <img :src="logoSrc" alt="logo" class="w-5 h-5 object-contain" /> Myshoes.vn
          </span>
        </div>
        <h1 class="text-2xl font-bold mb-4">{{ newsItem.title }}</h1>
        <img :src="newsItem.image" alt="" class="w-full h-64 object-cover rounded mb-6 bg-gray-100" />
        <div class="text-gray-700 leading-relaxed whitespace-pre-line">{{ newsItem.content }}</div>
      </div>
      <div v-else class="text-center text-gray-500 py-12">Bài báo không tồn tại.</div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';

const logoSrc = '/images/myshoes-logo.png';
const route = useRoute();

// Fake news data (should be replaced with API or store in real app)
const newsList = [
  {
    id: '1',
    image: '/images/news1.jpg',
    date: '25 Oct',
    title: 'GIÀY CHẠY BỘ NÀO ĐANG LÀ “CHIẾC VƯƠNG MIỆN” CỦA DÂN RUNNER 2025?',
    content: 'Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025...\nNăm 2025 không chỉ là một mốc năm của những kỷ lục, mà còn là năm của những đôi giày chạy bộ với công nghệ vượt trội, giúp runner chinh phục mọi thử thách.'
  },
  {
    id: '2',
    image: '/images/news2.jpg',
    date: '25 Oct',
    title: 'Đừng Hỏi Vì Sao Tôi Chỉ Mang Giày Chính Hãng – Câu Trả Lời Nằm Ở Cảm Giác Khi Xỏ Chân Vào',
    content: 'Tôi đã từng là một “thợ săn sale” giày fake...\nNhưng cảm giác khi xỏ chân vào đôi giày chính hãng thật sự khác biệt, từ chất liệu đến sự tự tin.'
  },
  {
    id: '3',
    image: '/images/news3.jpg',
    date: '21 Oct',
    title: 'Gợi ý 5 đôi sneaker tiện lợi và êm chân phù hợp cuối năm 2025',
    content: 'Cuối năm luôn là thời điểm lý tưởng để sắm sửa...\nDưới đây là 5 mẫu sneaker được đánh giá cao về sự tiện lợi và êm ái.'
  },
  {
    id: '4',
    image: '/images/news4.jpg',
    date: '21 Oct',
    title: 'Gió Lạnh Về Rồi, Bạn Đã Có Giày Ấm Chưa?',
    content: 'Mở đầu Khi những cơn gió lạnh đầu mùa bắt đầu len lỏi...\nĐừng quên chuẩn bị cho mình một đôi giày thật ấm áp.'
  }
  // ...add more if needed
];

const newsItem = newsList.find(n => n.id === route.params.id);
</script>

<style scoped>
.text-gray-700 { color: #374151; }
</style>
