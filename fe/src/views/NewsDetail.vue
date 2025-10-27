<template>
  <div>
    <Header />
    <div class="max-w-3xl mx-auto mt-10 bg-white rounded-xl shadow p-8">
      <button @click="goBack" class="mb-6 flex items-center gap-2 text-blue-600 hover:underline text-sm font-medium">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
        Quay lại
      </button>
      <div v-if="newsItem">
        <div class="flex flex-wrap items-center gap-3 mb-4">
          <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded">{{ newsItem.date }}</span>
          <span v-if="newsItem.tag" class="bg-gray-200 text-gray-700 text-xs px-2 py-1 rounded">#{{ newsItem.tag }}</span>
          <span class="text-xs text-gray-400 flex items-center gap-1">
            <img :src="logoSrc" alt="logo" class="w-5 h-5 object-contain" /> Myshoes.vn
          </span>
          <span class="text-xs text-gray-400 flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            {{ newsItem.author || 'Tác giả: Myshoes Team' }}
          </span>
          <span class="text-xs text-gray-400 flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A2 2 0 0021 6.382V5a2 2 0 00-2-2H5a2 2 0 00-2 2v1.382a2 2 0 00.447 1.342L8 10m7 0v10a2 2 0 01-2 2H9a2 2 0 01-2-2V10m10 0h-4m0 0V4m0 6h-4" /></svg>
            {{ newsItem.views || randomViews }} lượt xem
          </span>
        </div>
        <h1 class="text-2xl font-bold mb-4">{{ newsItem.title }}</h1>
        <img :src="newsItem.image" alt="" class="w-full h-64 object-cover rounded mb-6 bg-gray-100" />
        <!-- Mục lục nếu bài dài -->
        <div v-if="toc.length" class="mb-6 bg-gray-50 rounded p-4 border text-sm">
          <div class="font-semibold mb-2 text-gray-700">Mục lục</div>
          <ul class="list-disc pl-5">
            <li v-for="item in toc" :key="item.text">
              <a :href="'#' + item.anchor" class="text-blue-600 hover:underline">{{ item.text }}</a>
            </li>
          </ul>
        </div>
        <div class="text-gray-700 leading-relaxed whitespace-pre-line mb-8">
          <template v-if="toc.length">
            <span v-for="(section, idx) in contentSections" :key="section.anchor">
              <h2 :id="section.anchor" class="text-lg font-semibold mt-6 mb-2">{{ section.heading }}</h2>
              <span>{{ section.body }}</span>
            </span>
          </template>
          <template v-else>
            {{ newsItem.content }}
          </template>
        </div>
        <!-- Chia sẻ -->
        <div class="flex items-center gap-3 mb-8">
          <span class="text-gray-500 text-sm">Chia sẻ:</span>
          <button @click="share('facebook')" class="hover:opacity-80"><img src="/images/facebook.svg" alt="fb" class="w-6 h-6" /></button>
          <button @click="share('twitter')" class="hover:opacity-80"><img src="/images/twitter.svg" alt="tw" class="w-6 h-6" /></button>
          <button @click="share('copy')" class="hover:opacity-80"><img src="/images/link.svg" alt="copy" class="w-6 h-6" /></button>
        </div>
        <!-- Bình luận mockup -->
        <div class="mt-10 border-t pt-8">
          <h2 class="text-lg font-semibold mb-4 text-gray-700">Bình luận</h2>
          <div class="mb-4">
            <textarea v-model="commentText" rows="3" class="w-full border rounded p-2" placeholder="Nhập bình luận..."></textarea>
            <button @click="submitComment" class="mt-2 px-4 py-1 bg-blue-600 text-white rounded hover:bg-blue-700">Gửi</button>
          </div>
          <div v-if="comments.length">
            <div v-for="(cmt, idx) in comments" :key="idx" class="mb-3 p-3 bg-gray-50 rounded">
              <div class="font-medium text-gray-800">Khách</div>
              <div class="text-gray-600 text-sm mt-1">{{ cmt }}</div>
            </div>
          </div>
          <div v-else class="text-gray-400 text-sm">Chưa có bình luận nào.</div>
        </div>
        <!-- Gợi ý bài viết liên quan -->
        <div v-if="relatedNews.length" class="mt-10 border-t pt-8">
          <h2 class="text-lg font-semibold mb-4 text-gray-700">Bài viết liên quan</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div v-for="item in relatedNews" :key="item.id" class="flex gap-3 items-center bg-gray-50 rounded p-3 hover:bg-gray-100 transition">
              <img :src="item.image" alt="" class="w-16 h-16 object-cover rounded" />
              <div>
                <router-link :to="{ name: 'NewsDetail', params: { id: item.id } }" class="font-medium text-blue-700 hover:underline">{{ item.title }}</router-link>
                <div class="text-xs text-gray-400 mt-1">{{ item.date }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="text-center text-gray-500 py-12">Bài báo không tồn tại.</div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { ref, watch } from 'vue';
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';

const logoSrc = '/images/myshoes-logo.png';
const route = useRoute();
const router = useRouter();

// Fake news data (should be replaced with API or store in real app)
const newsList = [
  {
    id: '1',
    image: '/images/news1.jpg',
    date: '25 Oct',
    title: 'GIÀY CHẠY BỘ NÀO ĐANG LÀ “CHIẾC VƯƠNG MIỆN” CỦA DÂN RUNNER 2025?',
    content: 'I. Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025\nNăm 2025 không chỉ là một mốc năm của những kỷ lục, mà còn là năm của những đôi giày chạy bộ với công nghệ vượt trội, giúp runner chinh phục mọi thử thách.\n\nII. Công Nghệ Mới\nCác hãng lớn đã ra mắt những dòng sản phẩm với đệm siêu nhẹ, vật liệu tái chế và cảm biến thông minh.\n\nIII. Kết Luận\nChọn giày phù hợp sẽ giúp bạn bứt phá mọi giới hạn.',
    tag: 'Chạy bộ',
    author: 'Nguyễn Văn A',
    views: 1234
  },
  {
    id: '2',
    image: '/images/news2.jpg',
    date: '25 Oct',
    title: 'Đừng Hỏi Vì Sao Tôi Chỉ Mang Giày Chính Hãng – Câu Trả Lời Nằm Ở Cảm Giác Khi Xỏ Chân Vào',
    content: 'I. Trải Nghiệm Cá Nhân\nTôi đã từng là một “thợ săn sale” giày fake...\n\nII. Sự Khác Biệt\nNhưng cảm giác khi xỏ chân vào đôi giày chính hãng thật sự khác biệt, từ chất liệu đến sự tự tin.',
    tag: 'Trải nghiệm',
    author: 'Lê Thị B',
    views: 567
  },
  {
    id: '3',
    image: '/images/news3.jpg',
    date: '21 Oct',
    title: 'Gợi ý 5 đôi sneaker tiện lợi và êm chân phù hợp cuối năm 2025',
    content: 'I. Giới Thiệu\nCuối năm luôn là thời điểm lý tưởng để sắm sửa...\n\nII. Top 5 Sneaker\nDưới đây là 5 mẫu sneaker được đánh giá cao về sự tiện lợi và êm ái.',
    tag: 'Sneaker',
    author: 'Trần C',
    views: 321
  },
  {
    id: '4',
    image: '/images/news4.jpg',
    date: '21 Oct',
    title: 'Gió Lạnh Về Rồi, Bạn Đã Có Giày Ấm Chưa?',
    content: 'I. Mở đầu\nKhi những cơn gió lạnh đầu mùa bắt đầu len lỏi...\n\nII. Gợi Ý Chọn Giày Ấm\nĐừng quên chuẩn bị cho mình một đôi giày thật ấm áp.',
    tag: 'Thời tiết',
    author: 'Myshoes Team',
    views: 99
  },
  {
    id: '5',
    image: '/images/news1.jpg',
    date: '20 Oct',
    title: 'Top mẫu sneaker đáng sắm mùa thu 2025',
    content: 'I. Giới Thiệu\nBST mới nhất với nhiều màu sắc và công nghệ êm ái…\n\nII. Tiêu Chí Lựa Chọn\nLựa chọn sneaker phù hợp cần cân nhắc về kiểu dáng, chất liệu và tính ứng dụng trong cuộc sống hàng ngày.\n\nIII. Top Picks\nMột số mẫu sneaker đáng chú ý mùa thu này có tính năng chống thấm nước và thiết kế thông minh.',
    tag: 'Sneaker',
    author: 'Myshoes Team',
    views: 456
  },
  {
    id: '6',
    image: '/images/news2.jpg',
    date: '18 Oct',
    title: 'Cách chọn size giày online: mẹo từ chuyên gia',
    content: 'I. Vấn Đề Phổ Biến\nHướng dẫn đo chuẩn, tránh đổi trả phiền phức.\n\nII. Cách Đo Chân Đúng\nSử dụng thước dây và đo vào buổi tối khi chân đã hơi phù.\n\nIII. Lưu Ý Khi Mua Online\nĐọc kỹ bảng size, xem review về độ chật và mô tả chân.',
    tag: 'Mẹo vặt',
    author: 'Myshoes Team',
    views: 723
  },
  {
    id: '7',
    image: '/images/news3.jpg',
    date: '15 Oct',
    title: 'Bảo quản giày da đúng cách: 7 bước đơn giản',
    content: 'I. Tầm Quan Trọng\nGiữ giày luôn mới với mẹo bảo quản từ nhà sản xuất.\n\nII. Các Bước Cơ Bản\nLàm sạch bụi, lau chùi kỹ, phơi khô đúng cách và sử dụng sản phẩm bảo dưỡng phù hợp.\n\nIII. Lưu Ý\nTránh ánh nắng trực tiếp và giữ giày trong túi kín khi không dùng.',
    tag: 'Chăm sóc',
    author: 'Myshoes Team',
    views: 312
  },
  {
    id: '8',
    image: '/images/news4.jpg',
    date: '12 Oct',
    title: 'Khuyến mãi cuối tuần: Mua 1 tặng 1 một số mẫu',
    content: 'I. Thông Báo Khuyến Mãi\nChương trình giảm giá lớn, số lượng có hạn.\n\nII. Điều Kiện\nÁp dụng cho các mẫu sneaker, không áp dụng cho các sản phẩm sale và có thể thay đổi theo từng thời điểm.\n\nIII. Cách Tham Gia\nĐăng ký nhận thông báo qua email hoặc theo dõi fanpage để không bỏ lỡ cơ hội.',
    tag: 'Khuyến mãi',
    author: 'Myshoes Team',
    views: 1089
  },
  {
    id: '9',
    image: '/images/news1.jpg',
    date: '10 Oct',
    title: 'Phong cách phối đồ với sneaker trắng',
    content: 'I. Sneaker Trắng - Classic\nGợi ý outfit casual + tips giữ giày trắng sạch.\n\nII. Phối Đồ\nSneaker trắng kết hợp được với hầu hết mọi outfit từ quần jeans đến váy maxi.\n\nIII. Bảo Quản\nVệ sinh thường xuyên bằng khăn ướt, tránh xịt chất bảo vệ lên giày trắng.',
    tag: 'Style',
    author: 'Myshoes Team',
    views: 567
  },
  {
    id: '10',
    image: '/images/news2.jpg',
    date: '08 Oct',
    title: 'Sự khác biệt giữa foam A và foam B trong đế giày',
    content: 'I. Foam Technology\nSo sánh cảm giác, độ đàn hồi và độ bền.\n\nII. Foam A\nCảm giác êm ái, độ đàn hồi tốt, phù hợp cho đi bộ và hoạt động nhẹ nhàng.\n\nIII. Foam B\nĐộ bền cao hơn, phù hợp cho chạy bộ và các hoạt động có cường độ cao.',
    tag: 'Công nghệ',
    author: 'Myshoes Team',
    views: 234
  },
  {
    id: '11',
    image: '/images/news3.jpg',
    date: '05 Oct',
    title: 'Top 10 mẫu running shoes cho người mới bắt đầu',
    content: 'I. Bắt Đầu Chạy Bộ\nChọn giày chạy phù hợp để tránh chấn thương.\n\nII. Tiêu Chí Quan Trọng\nĐệm êm, hỗ trợ chân tốt, nhẹ và có độ bền cao.\n\nIII. Top 10 Gợi Ý\nDanh sách các mẫu running shoes được đánh giá cao bởi các runner chuyên nghiệp.',
    tag: 'Running',
    author: 'Myshoes Team',
    views: 890
  }
];

const newsItem = ref(newsList.find(n => n.id === route.params.id));
const relatedNews = ref(newsList.filter(n => n.id !== route.params.id).slice(0, 3));

// Theo dõi id trên route để cập nhật lại newsItem và relatedNews khi chuyển bài
watch(() => route.params.id, (newId) => {
  newsItem.value = newsList.find(n => n.id === newId);
  relatedNews.value = newsList.filter(n => n.id !== newId).slice(0, 3);
  // Cập nhật lại mục lục và contentSections nếu cần
  updateTocAndSections();
});

// Tạo mục lục và phân đoạn nội dung nếu bài có nhiều phần
const toc = ref([]);
const contentSections = ref([]);
function updateTocAndSections() {
  toc.value = [];
  contentSections.value = [];
  if (newsItem.value && newsItem.value.content) {
    const regex = /([IVXLCDM]+\.) (.+)/g;
    let lastIndex = 0;
    let match;
    let idx = 0;
    while ((match = regex.exec(newsItem.value.content)) !== null) {
      if (idx > 0) {
        const prev = toc.value[idx - 1];
        contentSections.value.push({
          anchor: prev.anchor,
          heading: prev.text,
          body: newsItem.value.content.slice(lastIndex, match.index).replace(/^[\n]+|[\n]+$/g, '')
        });
      }
      const anchor = `section-${idx}`;
      toc.value.push({ text: match[2], anchor });
      lastIndex = match.index + match[0].length;
      idx++;
    }
    if (toc.value.length) {
      const prev = toc.value[toc.value.length - 1];
      contentSections.value.push({
        anchor: prev.anchor,
        heading: prev.text,
        body: newsItem.value.content.slice(lastIndex).replace(/^[\n]+|[\n]+$/g, '')
      });
    }
  }
}
// Khởi tạo mục lục ban đầu
updateTocAndSections();


// Lượt xem random nếu không có
const randomViews = Math.floor(Math.random() * 1000) + 100;

// Bình luận mockup
import { ref } from 'vue';
const commentText = ref('');
const comments = ref([]);
function submitComment() {
  if (commentText.value.trim()) {
    comments.value.unshift(commentText.value.trim());
    commentText.value = '';
  }
}

function goBack() {
  router.back();
}

function share(type) {
  const url = window.location.href;
  if (type === 'facebook') {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`);
  } else if (type === 'twitter') {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`);
  } else if (type === 'copy') {
    navigator.clipboard.writeText(url);
    alert('Đã copy liên kết bài viết!');
  }
}
</script>

<style scoped>
.text-gray-700 { color: #374151; }
button:focus { outline: 2px solid #2563eb; }
</style>
