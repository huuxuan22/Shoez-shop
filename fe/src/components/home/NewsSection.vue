<template>
  <section class="max-w-6xl mx-auto mt-12 px-4">
    <div class="text-center mb-6">
      <h2 class="text-2xl font-bold">TIN TỨC SHOEZ.VN</h2>
      <p class="text-sm text-gray-500">#BLOG</p>
      <div class="w-16 h-1 bg-red-500 mx-auto mt-2 rounded"></div>
    </div>
    <div ref="container" class="overflow-x-auto scroll-smooth snap-x snap-mandatory -mx-4 px-4 py-2 no-scrollbar grab" 
      @pointerdown="onPointerDown" @pointermove="onPointerMove" @pointerup="onPointerUp" @pointercancel="onPointerUp" @pointerleave="onPointerUp">
      <div class="flex gap-6 items-stretch">
        <article v-for="(item, idx) in news" :key="idx" class="snap-center flex-none w-[92%] sm:w-1/2 lg:w-1/4 bg-white rounded-lg overflow-hidden shadow hover:shadow-xl transition-shadow">
          <div class="relative h-44 bg-gray-100">
            <img :src="item.image" alt="" class="w-full h-full object-cover bg-gray-100" />
            <div class="absolute top-3 left-3 bg-blue-600 text-white text-xs px-2 py-1 rounded">{{ item.date }}</div>
          </div>
          <div class="p-4 flex flex-col justify-between h-40">
            <div>
              <h3 class="text-base font-semibold mb-2 line-clamp-2">{{ item.title }}</h3>
              <p class="text-sm text-gray-600 mb-3 line-clamp-2">{{ item.excerpt }}</p>
            </div>
            <div class="text-xs text-gray-400 mt-auto flex items-center gap-1">
              <span class="inline-block w-4 h-4"><img :src="logoSrc" alt="logo" class="w-full h-full object-contain" /></span>
              Myshoes.vn
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const container = ref(null);
const isDragging = ref(false);
const dragStartX = ref(0);
const dragStartScroll = ref(0);

const onPointerDown = (e) => {
  if (!container.value) return;
  try { e.preventDefault && e.preventDefault(); } catch {}
  isDragging.value = true;
  dragStartX.value = e.pageX;
  dragStartScroll.value = container.value.scrollLeft;
  try { container.value.setPointerCapture && container.value.setPointerCapture(e.pointerId); } catch {}
  container.value.classList.add('grabbing');
};

const onPointerMove = (e) => {
  if (!isDragging.value || !container.value) return;
  try { e.preventDefault && e.preventDefault(); } catch {}
  const dx = e.pageX - dragStartX.value;
  container.value.scrollLeft = dragStartScroll.value - dx;
};

const onPointerUp = (e) => {
  if (!container.value) return;
  isDragging.value = false;
  try { container.value.releasePointerCapture && container.value.releasePointerCapture(e.pointerId); } catch {}
  container.value.classList.remove('grabbing');
};
const logoSrc = '/images/myshoes-logo.png';
const news = [
  {
    image: '/images/news1.jpg',
    date: '25 Oct',
    title: 'GIÀY CHẠY BỘ NÀO ĐANG LÀ “CHIẾC VƯƠNG MIỆN” CỦA DÂN RUNNER 2025?',
    excerpt: 'Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025…',
  },
  {
    image: '/images/news2.jpg',
    date: '25 Oct',
    title: 'Đừng Hỏi Vì Sao Tôi Chỉ Mang Giày Chính Hãng – Câu Trả Lời Nằm Ở Cảm Giác Khi Xỏ Chân Vào',
    excerpt: 'Tôi đã từng là một “thợ săn sale” giày fake…',
  },
  {
    image: '/images/news3.jpg',
    date: '21 Oct',
    title: 'Gợi ý 5 đôi sneaker tiện lợi và êm chân phù hợp cuối năm 2025',
    excerpt: 'Cuối năm luôn là thời điểm lý tưởng để sắm sửa…',
  },
  {
    image: '/images/news4.jpg',
    date: '21 Oct',
    title: 'Gió Lạnh Về Rồi, Bạn Đã Có Giày Ấm Chưa?',
    excerpt: 'Mở đầu Khi những cơn gió lạnh đầu mùa bắt đầu len lỏi…',
  },
  {
    image: '/images/news1.jpg',
    date: '20 Oct',
    title: 'Top mẫu sneaker đáng sắm mùa thu 2025',
    excerpt: 'BST mới nhất với nhiều màu sắc và công nghệ êm ái…',
  },
  {
    image: '/images/news2.jpg',
    date: '18 Oct',
    title: 'Cách chọn size giày online: mẹo từ chuyên gia',
    excerpt: 'Hướng dẫn đo chuẩn, tránh đổi trả phiền phức.',
  },
  {
    image: '/images/news3.jpg',
    date: '15 Oct',
    title: 'Bảo quản giày da đúng cách: 7 bước đơn giản',
    excerpt: 'Giữ giày luôn mới với mẹo bảo quản từ nhà sản xuất.',
  },
  {
    image: '/images/news4.jpg',
    date: '12 Oct',
    title: 'Khuyến mãi cuối tuần: Mua 1 tặng 1 một số mẫu',
    excerpt: 'Chương trình giảm giá lớn, số lượng có hạn.',
  },
  {
    image: '/images/news1.jpg',
    date: '10 Oct',
    title: 'Phong cách phối đồ với sneaker trắng',
    excerpt: 'Gợi ý outfit casual + tips giữ giày trắng sạch.',
  },
  {
    image: '/images/news2.jpg',
    date: '08 Oct',
    title: 'Sự khác biệt giữa foam A và foam B trong đế giày',
    excerpt: 'So sánh cảm giác, độ đàn hồi và độ bền.',
  },
  {
    image: '/images/news3.jpg',
    date: '05 Oct',
    title: 'Top 10 mẫu running shoes cho người mới bắt đầu',
    excerpt: 'Chọn giày chạy phù hợp để tránh chấn thương.',
  }
];
</script>

<style scoped>
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; line-clamp: 2; }

.snap-center { scroll-snap-align: center; }
.snap-x { scroll-snap-type: x mandatory; }
.scroll-smooth { scroll-behavior: smooth; }

.no-scrollbar::-webkit-scrollbar { height: 8px; }
.no-scrollbar::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.12); border-radius: 9999px; }
.no-scrollbar { scrollbar-width: thin; }

.grab { cursor: grab; touch-action: pan-y; }
.grabbing { cursor: grabbing; touch-action: pan-y; }
</style>
