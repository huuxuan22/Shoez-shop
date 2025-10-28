<template>
  <div class="news-detail-container">
    <Header />
    <div class="news-content max-w-6xl mx-auto mt-12 bg-white p-10 px-16">
      <button @click="goBack"
        class="mb-8 flex items-center gap-3 text-gray-700 hover:text-black transition-colors text-base font-medium">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        Quay lại
      </button>

      <div v-if="newsItem">
        <!-- Meta information -->
        <div class="flex flex-wrap items-center gap-4 mb-6">
          <span class="bg-black text-white text-sm px-3 py-1.5 font-medium">{{ newsItem.date }}</span>
          <span v-if="newsItem.tag" class="bg-gray-100 text-gray-800 text-sm px-3 py-1.5">#{{ newsItem.tag }}</span>
          <span class="text-sm text-gray-600 flex items-center gap-2">
            <img :src="logoSrc" alt="logo" class="w-6 h-6 object-contain" /> Myshoes.vn
          </span>
          <span class="text-sm text-gray-600 flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            {{ newsItem.author || 'Tác giả: Myshoes Team' }}
          </span>
          <span class="text-sm text-gray-600 flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 10l4.553-2.276A2 2 0 0021 6.382V5a2 2 0 00-2-2H5a2 2 0 00-2 2v1.382a2 2 0 00.447 1.342L8 10m7 0v10a2 2 0 01-2 2H9a2 2 0 01-2-2V10m10 0h-4m0 0V4m0 6h-4" />
            </svg>
            {{ newsItem.views || randomViews }} lượt xem
          </span>
        </div>

        <!-- Title -->
        <h1 class="text-4xl font-bold mb-6 leading-tight text-gray-900">{{ newsItem.title }}</h1>

        <!-- Featured image -->
        <div class="relative mb-8 overflow-hidden bg-gray-100">
          <img :src="newsItem.image" alt="" class="w-full h-96 object-cover" />
          <div class="absolute bottom-0 left-0 w-full h-20 bg-gradient-to-t from-black/30 to-transparent"></div>
        </div>

        <!-- Additional images gallery -->
        <div v-if="additionalImages.length" class="mb-8">
          <h3 class="text-xl font-semibold mb-4 text-gray-900">Hình ảnh liên quan</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div v-for="(img, index) in additionalImages" :key="index"
              class="overflow-hidden bg-gray-100 cursor-pointer" @click="openImageGallery(index)">
              <img :src="img" :alt="`Hình ảnh ${index + 1}`"
                class="w-full h-32 object-cover hover:scale-105 transition-transform duration-300" />
            </div>
          </div>
        </div>

        <!-- Table of contents -->
        <div v-if="toc.length" class="mb-8 bg-gray-50 p-6 text-base">
          <div class="font-semibold mb-3 text-gray-800 text-lg">Mục lục</div>
          <ul class="space-y-2">
            <li v-for="item in toc" :key="item.text" class="flex items-start">
              <span class="text-gray-500 mr-2 mt-1">•</span>
              <a :href="'#' + item.anchor" class="text-gray-700 hover:text-black transition-colors">{{ item.text }}</a>
            </li>
          </ul>
        </div>

        <!-- Article content -->
        <div class="article-content text-gray-800 leading-relaxed whitespace-pre-line mb-10 text-lg">
          <template v-if="toc.length">
            <div v-for="(section, idx) in contentSections" :key="section.anchor" class="mb-8">
              <h2 :id="section.anchor" class="text-2xl font-semibold mt-10 mb-4 text-gray-900 pb-2">{{ section.heading
              }}</h2>

              <!-- Content image for each section -->
              <div v-if="sectionImages[idx]" class="my-6 overflow-hidden bg-gray-100">
                <img :src="sectionImages[idx]" :alt="`Hình ảnh cho ${section.heading}`"
                  class="w-full h-64 object-cover" />
              </div>

              <div class="section-body">{{ section.body }}</div>
            </div>
          </template>
          <template v-else>
            <div class="text-content">{{ newsItem.content }}</div>
          </template>
        </div>

        <!-- Share section -->
        <div class="flex items-center gap-4 mb-10 py-6">
          <span class="text-gray-600 text-base font-medium">Chia sẻ:</span>
          <button @click="share('facebook')"
            class="w-10 h-10 flex items-center justify-center bg-gray-100 text-gray-700 hover:bg-black hover:text-white transition-colors duration-300"
            aria-label="Share to Facebook">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-5 h-5" fill="currentColor">
              <path
                d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.406.593 24 1.325 24h11.495v-9.294H9.691V11.01h3.129V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.796.715-1.796 1.764v2.314h3.59l-.467 3.696h-3.123V24h6.127C23.406 24 24 23.406 24 22.676V1.325C24 .593 23.406 0 22.675 0z" />
            </svg>
          </button>
          <button @click="share('twitter')"
            class="w-10 h-10 flex items-center justify-center bg-gray-100 text-gray-700 hover:bg-black hover:text-white transition-colors duration-300"
            aria-label="Share to Twitter">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-5 h-5" fill="currentColor">
              <path
                d="M24 4.557a9.83 9.83 0 0 1-2.828.775 4.932 4.932 0 0 0 2.165-2.724 9.864 9.864 0 0 1-3.127 1.195 4.916 4.916 0 0 0-8.369 4.482A13.949 13.949 0 0 1 1.671 3.149a4.916 4.916 0 0 0 1.523 6.558A4.897 4.897 0 0 1 .964 9.1v.062a4.916 4.916 0 0 0 3.946 4.817 4.902 4.902 0 0 1-2.212.084 4.918 4.918 0 0 0 4.588 3.41A9.867 9.867 0 0 1 0 19.54a13.94 13.94 0 0 0 7.548 2.212c9.057 0 14.01-7.514 14.01-14.01 0-.213-.005-.425-.014-.636A10.012 10.012 0 0 0 24 4.557z" />
            </svg>
          </button>
          <button @click="share('copy')"
            class="w-10 h-10 flex items-center justify-center bg-gray-100 text-gray-700 hover:bg-black hover:text-white transition-colors duration-300"
            aria-label="Copy link">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-5 h-5" fill="currentColor">
              <path
                d="M3.9 12a5.1 5.1 0 0 1 5.1-5.1h3a1.5 1.5 0 1 1 0 3h-3a2.1 2.1 0 1 0 0 4.2h3a1.5 1.5 0 1 1 0 3h-3A5.1 5.1 0 0 1 3.9 12Zm11.1-6a5.1 5.1 0 0 1 0 10.2h-3a1.5 1.5 0 1 1 0-3h3a2.1 2.1 0 1 0 0-4.2h-3a1.5 1.5 0 1 1 0-3h3Z" />
            </svg>
          </button>
        </div>

        <!-- Comments section -->
        <div class="mt-12 pt-10">
          <h2 class="text-2xl font-semibold mb-6 text-gray-900">Bình luận</h2>
          <div class="mb-6">
            <textarea v-model="commentText" rows="4"
              class="w-full p-4 focus:ring-2 focus:ring-black focus:border-transparent transition-all"
              placeholder="Nhập bình luận của bạn..."></textarea>
            <button @click="submitComment"
              class="mt-3 px-6 py-2.5 bg-black text-white hover:bg-gray-800 transition-colors font-medium">Gửi bình
              luận</button>
          </div>
          <div v-if="comments.length" class="space-y-4">
            <div v-for="(cmt, idx) in comments" :key="idx" class="p-4 bg-gray-50">
              <div class="font-medium text-gray-900 text-lg">Khách</div>
              <div class="text-gray-700 mt-2 text-base">{{ cmt }}</div>
            </div>
          </div>
          <div v-else class="text-gray-500 text-base py-4 text-center">Chưa có bình luận nào.</div>
        </div>

        <!-- Related articles -->
        <div v-if="relatedNews.length" class="mt-12 pt-10">
          <h2 class="text-2xl font-semibold mb-6 text-gray-900">Bài viết liên quan</h2>
          <div class="grid grid-cols-3 gap-4">
            <div v-for="item in relatedNews" :key="item.id"
              class="flex flex-col bg-white overflow-hidden hover:shadow-lg transition-all duration-300">
              <img :src="item.image" alt="" class="w-full h-48 object-cover" />
              <div class="p-5 flex-1 flex flex-col">
                <router-link :to="{ name: 'NewsDetail', params: { id: item.id } }"
                  class="font-semibold text-gray-900 hover:text-black transition-colors text-lg mb-2 line-clamp-2">{{
                    item.title
                  }}</router-link>
                <div class="text-sm text-gray-500 mt-auto pt-3">{{ item.date }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center text-gray-500 py-16 text-xl">Bài báo không tồn tại.</div>
    </div>
    <Footer />

    <!-- Image Gallery Modal -->
    <div v-if="showImageGallery" class="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-50"
      @click="closeImageGallery">
      <div class="relative max-w-4xl max-h-full">
        <button @click="closeImageGallery" class="absolute top-4 right-4 text-white text-2xl z-10">×</button>
        <img :src="galleryImages[galleryCurrentIndex]" :alt="`Hình ảnh ${galleryCurrentIndex + 1}`"
          class="max-w-full max-h-screen object-contain" />
        <button v-if="galleryCurrentIndex > 0" @click.stop="prevImage"
          class="absolute left-4 top-1/2 transform -translate-y-1/2 text-white text-2xl">‹</button>
        <button v-if="galleryCurrentIndex < galleryImages.length - 1" @click.stop="nextImage"
          class="absolute right-4 top-1/2 transform -translate-y-1/2 text-white text-2xl">›</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { ref, watch } from 'vue';
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';

// Import images from assets
import blog1 from '@/assets/images/blog/blog1.png';
import blog2 from '@/assets/images/blog/blog2.png';
import blog3 from '@/assets/images/blog/blog3.png';
import blog4 from '@/assets/images/blog/blog4.png';
import blog5 from '@/assets/images/blog/blog5.png';
import blog6 from '@/assets/images/blog/blog6.png';

// Import additional images for the article
import runningShoes from '@/assets/images/blog/running-shoes.png';
import sneakerCollection from '@/assets/images/blog/sneaker-collection.jpg';

const logoSrc = '/images/logo-shoez.png';
const route = useRoute();
const router = useRouter();

// Additional images for gallery
const additionalImages = ref([
  blog4,
  blog5,
  blog6,
  runningShoes,
  sneakerCollection
]);

// Images for different sections
const sectionImages = ref([
  runningShoes,
  blog4,
  blog5
]);

// Image gallery state
const showImageGallery = ref(false);
const galleryCurrentIndex = ref(0);
const galleryImages = ref([]);

function openImageGallery(index) {
  galleryImages.value = additionalImages.value;
  galleryCurrentIndex.value = index;
  showImageGallery.value = true;
}

function closeImageGallery() {
  showImageGallery.value = false;
}

function nextImage() {
  if (galleryCurrentIndex.value < galleryImages.value.length - 1) {
    galleryCurrentIndex.value++;
  }
}

function prevImage() {
  if (galleryCurrentIndex.value > 0) {
    galleryCurrentIndex.value--;
  }
}

// Fake news data (should be replaced with API or store in real app)
const newsList = [
  {
    id: '1',
    image: blog1,
    date: '25 Tháng 10, 2024',
    title: 'GIÀY CHẠY BỘ NÀO ĐANG LÀ "CHIẾC VƯƠNG MIỆN" CỦA DÂN RUNNER 2025?',
    content: `I. Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025

Năm 2025 đánh dấu một bước ngoặt lớn trong ngành công nghiệp giày chạy bộ. Không chỉ là những cải tiến nhỏ lẻ, chúng ta đang chứng kiến một cuộc cách mạng thực sự về công nghệ và vật liệu. Các thương hiệu lớn đã đầu tư hàng triệu đô la vào nghiên cứu và phát triển, mang đến những sản phẩm không chỉ giúp cải thiện thành tích mà còn bảo vệ sức khỏe của runner.

Thị trường giày chạy bộ năm 2025 chứng kiến sự cạnh tranh khốc liệt giữa các ông lớn như Nike, Adidas, New Balance và Asics. Mỗi hãng đều mang đến những công nghệ độc quyền, từ hệ thống đệm siêu nhẹ cho đến cảm biến thông minh tích hợp. Người tiêu dùng giờ đây không chỉ tìm kiếm một đôi giày êm ái, mà còn cần một "trợ thủ đắc lực" có thể đồng hành trong mọi hành trình chinh phục.

II. Công Nghệ Mới Đột Phá

Carbon Fiber Plate - Tấm carbon không còn là độc quyền của giày racing: Năm 2025 chứng kiến sự phổ biến của tấm carbon trong cả giày training. Công nghệ này giúp tăng hiệu suất đẩy về phía trước lên đến 4%, đồng thời giảm thiểu chấn thương cho cơ bắp.

Foam Revolution - Cuộc cách mạng về chất liệu đệm: Các hãng đã phát triển những loại foam mới với độ đàn hồi vượt trội. Nike với ZoomX, Adidas với Lightstrike Pro, và New Balance với FuelCell đều cho thấy sự cải tiến đáng kể về độ bền và khả năng phục hồi.

Sustainable Materials - Vật liệu bền vững: Xu hướng xanh hóa ngành giày thể thao tiếp tục được đẩy mạnh. Hơn 50% giày chạy bộ năm 2025 sử dụng vật liệu tái chế, từ lưới upper làm từ chai nhựa tái chế đến midsole làm từ ngô và các nguyên liệu sinh học.

Smart Integration - Cảm biến thông minh: Nhiều mẫu giày cao cấp nay được tích hợp cảm biến theo dõi nhịp chân, lực tiếp đất và form chạy. Dữ liệu được đồng bộ hóa với ứng dụng di động, giúp runner phân tích và cải thiện kỹ thuật.

III. Top 5 Mẫu Giày Đáng Chú Ý Nhất 2025

1. Nike Alphafly 3 - "Siêu Phẩm Tốc Độ"
   • Đệm ZoomX cải tiến với độ dày tối ưu
   • Tấm carbon hình cánh cung độc quyền
   • Trọng lượng chỉ 180g cho size US 9
   • Phù hợp: Marathon, tập luyện tốc độ

2. Adidas Adizero Prime X 2
   • Công nghệ Lightstrike Pro kép
   • Độ dày midsole 50mm - giới hạn kỹ thuật
   • Thiết kế energy rods linh hoạt
   • Phù hợp: Runner kinh nghiệm tìm kiếm cảm giác mới lạ

3. New Balance FuelCell SuperComp Elite v4
   • FuelCell foam với công thức mới
   • Hệ thống tấm carbon năng lượng kép
   • Upper engineered mesh siêu nhẹ
   • Phù hợp: Cân bằng giữa tốc độ và sự ổn định

4. Asics Metaspeed Sky+
   • FlyteFoam Blast Turbo cao cấp
   • Công nghệ Guidesole giảm tiêu hao năng lượng
   • Thiết kế riêng cho runner có nhịp bước cao
   • Phù hợp: Runner chuyên nghiệp thi đấu

5. Saucony Endorphin Pro 4
   • PWRRUN HG foam đệm siêu nhẹ
   • SPEEDROLL technology tạo lực đẩy
   • Formfit upper ôm chân hoàn hảo
   • Phù hợp: Đa dạng từ beginner đến pro

IV. Tiêu Chí Lựa Chọn Giày Phù H�p

Để chọn được đôi giày "vương miện" cho riêng mình, runner cần xem xét các yếu tố:

• Loại hình chạy: Road running, trail running hay track?
• Khoảng cách: 5K, 10K, bán marathon hay full marathon?
• Dáng chạy: Neutral, overpronation hay underpronation?
• Trọng lượng cơ thể: Ảnh hưởng đến độ bền của đệm
• Ngân sách: Từ 2-6 triệu đồng tùy phân khúc
• Địa hình: Bê tông, đường đất hay địa hình phức tạp?

V. Kết Luận: Bứt Phá Mọi Giới Hạn

Năm 2025 thực sự là thời điểm vàng cho cộng đồng runner Việt Nam. Với sự đa dạng về công nghệ và mẫu mã, mỗi người chạy đều có thể tìm thấy "chiếc vương miện" phù hợp cho đôi chân của mình. Quan trọng nhất, hãy lắng nghe cơ thể và chọn giày không chỉ dựa trên công nghệ, mà còn dựa trên cảm giác thoải mái khi xỏ vào.

Hãy nhớ: Đôi giày tốt nhất không phải là đôi đắt nhất, mà là đôi phù hợp nhất với bạn. Đến với Myshoes.vn, chúng tôi cam kết mang đến những trải nghiệm mua sắm tốt nhất và tư vấn chuyên nghiệp nhất để bạn tìm được người bạn đồng hành hoàn hảo trên mọi cung đường.`,
    tag: 'Chạy bộ',
    author: 'Nguyễn Văn A - Chuyên gia giày thể thao',
    views: 1234
  },
  {
    id: '2',
    image: blog2,
    date: '25 Tháng 10, 2024',
    title: 'Đừng Hỏi Vì Sao Tôi Chỉ Mang Giày Chính Hãng – Câu Trả Lời Nằm Ở Cảm Giác Khi Xỏ Chân Vào',
    content: `I. Hành Trình Từ "Thợ Săn Sale" Đến Người Tiêu Dùng Thông Thái

Cách đây 5 năm, tôi từng là một "thợ săn sale" chính hiệu. Mục tiêu của tôi luôn là tìm kiếm những đôi giày có giá rẻ nhất, bất kể đó là hàng chính hãng hay replica. Tôi tự hào về khả năng tìm được những đôi giày "giống 99%" với giá chỉ bằng 1/3, 1/4 so với hàng thật. Nhưng rồi một sự kiện đã thay đổi hoàn toàn quan điểm của tôi.

Đó là vào một ngày mưa, khi tôi đang đi chiếc giày fake mua được với giá 400k, đế giày bất ngờ bong ra khiến tôi trượt ngã và chấn thương mắt cá chân. 2 tuần nằm bất động và chi phí y tế gấp 10 lần số tiền tôi "tiết kiệm" được đã dạy cho tôi một bài học đắt giá.

II. Sự Khác Biệt Không Thể Phủ Nhận

1. Chất Liệu: Từ Những Điều Nhỏ Nhất
   • Upper: Hàng chính hãng sử dụng engineered mesh cao cấp, có độ co giãn và thông thoáng được tính toán kỹ lưỡng. Hàng fake thường dùng vải thường, dễ rách và gây hầm nóng.
   • Đệm: Công nghệ foam độc quyền như Boost, ZoomX, React chỉ có ở hàng thật. Hàng fake sử dụng foam rẻ tiền, nhanh xẹp và không có độ đàn hồi.
   • Keo dán: Hàng thật sử dụng keo công nghiệp chuyên dụng, chịu được nhiệt độ và lực kéo cao. Hàng fake dùng keo thường, dễ bong tróc.

2. Công Nghệ Sản Xuất
   • Quy trình QC (Quality Control) nghiêm ngặt
   • Máy móc công nghệ cao từ Đức, Nhật
   • Đội ngũ kỹ sư giàu kinh nghiệm
   • Kiểm tra từng công đoạn sản xuất

3. Trải Nghiệm Sử Dụng
   • Độ ôm chân hoàn hảo
   • Phân phối lực đồng đều
   • Độ bền vượt trội (trung bình 800-1000km)
   • Bảo hành chính hãng 2 năm

III. Những Hệ Lụy Khi Sử Dụng Giày Fake

1. Nguy Cơ Sức Khỏe
   • Chấn thương khớp gối, mắt cá chân
   • Đau lưng, đau cột sống
   • Viêm cân gan chân
   • Biến dạng dáng đi

2. Thiệt Hại Kinh Tế
   • Tuổi thọ thấp, phải thay thường xuyên
   • Chi phí y tế khi xảy ra chấn thương
   • Không có giá trị bán lại

3. Vấn Đề Môi Trường
   • Sử dụng hóa chất độc hại
   • Quy trình sản xuất không kiểm soát
   • Nhanh chóng trở thành rác thải

IV. Làm Sao Phân Biệt Hàng Thật - Hàng Fake?

1. Kiểm Tra Bao Bì
   • Hộp cứng cáp, in ấn sắc nét
   • Mã QR, serial number
   • Tem chống hàng giả

2. Quan Sát Chi Tiết
   • Đường may tỉ mỉ, đều đặn
   • Logo in rõ ràng, không nhòe
   • Màu sắc đồng nhất, không lỗi

3. Cảm Nhận Khi Sử Dụng
   • Nhẹ và êm ngay lần đầu đi
   • Không có mùi hóa chất
   • Độ đàn hồi tốt

V. Lời Khuyên Chân Thành

Sau 3 năm chỉ sử dụng giày chính hãng, tôi nhận ra rằng: "Đắt một lần nhưng chất lượng mãi mãi". Mỗi buổi sáng xỏ đôi giày chính hãng vào, tôi cảm nhận được sự tin tưởng và an tâm. Không còn lo lắng về việc đế bong khi đang chạy, không còn sợ chấn thương bất ngờ.

Đặc biệt, với chính sách bảo hành của Myshoes.vn, tôi hoàn toàn yên tâm về chất lượng. Đội ngũ tư vấn chuyên nghiệp giúp tôi chọn được đôi giày phù hợp nhất với nhu cầu và túi tiền.

Hãy đầu tư cho đôi chân của bạn - nơi nâng đỡ toàn bộ cơ thể. Đừng để những khoản tiết kiệm trước mắt khiến bạn phải trả giá đắt về sau.`,
    tag: 'Trải nghiệm',
    author: 'Lê Thị B - Runner 5 năm kinh nghiệm',
    views: 567
  },
  {
    id: '3',
    image: blog3,
    date: '21 Tháng 10, 2024',
    title: 'Gợi ý 5 đôi sneaker tiện lợi và êm chân phù hợp cuối năm 2025',
    content: `I. Xu Hướng Sneaker Cuối Năm 2025: Tiện Lợi & Đa Năng

Cuối năm luôn là thời điểm bận rộn với hàng loạt sự kiện: tiệc tùng, du lịch, mua sắm và các buổi họp mặt. Một đôi sneaker êm ái, linh hoạt trở thành vật bất ly thân của mọi tín đồ thời trang. Năm 2025 chứng kiến sự lên ngôi của những mẫu sneaker "all-in-one" - có thể phối đồ từ casual đến semi-formal, từ văn phòng đến các buổi tiệc cuối năm.

Theo khảo sát mới nhất từ Myshoes.vn, 85% khách hàng tìm kiếm sneaker cuối năm ưu tiên 3 yếu tố: comfort tối đa, dễ phối đồ và giá cả hợp lý. Dưới đây là 5 cái tên nổi bật nhất đáp ứng đầy đủ các tiêu chí này.

II. Top 5 Sneaker Đáng Đồng Tiền Bát Gạo

1. Nike Air Force 1 '07 Premium
   • Ưu điểm: Thiết kế classic không bao giờ lỗi thời
   • Công nghệ: Air-Sole unit toàn bộ đế
   • Chất liệu: Leather cao cấp, dễ vệ sinh
   • Phối đồ: Quần jeans, jogger, hay cả suit
   • Giá: 2,500,000 VND
   • Đánh giá: 9.5/10 - "Basic nhưng không bao giờ nhàm chán"

2. Adidas Ultraboost Light
   • Ưu điểm: Êm ái nhất trong phân khúc
   • Công nghệ: Boost foam mới nhẹ hơn 30%
   • Chất liệu: Primeknit+ co giãn 4 chiều
   • Phối đồ: Sporty chic, streetwear
   • Giá: 4,200,000 VND
   • Đánh giá: 9.8/10 - "Như đi trên mây cả ngày"

3. New Balance 990v6
   • Ưu điểm: Support tuyệt vời cho bàn chân
   • Công nghệ: FuelCell midsole kết hợp ENCAP
   • Chất liệu: Pigskin suede và mesh cao cấp
   • Phối đồ: Smart casual, business casual
   • Giá: 5,500,000 VND
   • Đánh giá: 9.2/10 - "Đẳng cấp và thoải mái"

4. Veja Campo Leather
   • Ưu điểm: Thân thiện môi trường, thiết kế tối giản
   • Công nghệ: Đệm L-Foam từ ngô tái chế
   • Chất liệu: Leather chrome-free
   • Phối đồ: Minimalist, sustainable fashion
   • Giá: 2,800,000 VND
   • Đánh giá: 8.8/10 - "Style có trách nhiệm"

5. Converse Chuck 70 Vintage Canvas
   • Ưu điểm: Giá cả phải chăng, đa dạng màu sắc
   • Công nghệ: Đế cao su cổ điển, bền bỉ
   • Chất liệu: Canvas 12oz cao cấp
   • Phối đồ: Streetwear, retro style
   • Giá: 1,500,000 VND
   • Đánh giá: 9.0/10 - "Icon không tuổi"

III. Bí Quyết Chọn Sneaker Theo Nhu Cầu

1. Dân Văn Phòng
   • Ưu tiên: Màu trung tính (trắng, đen, be)
   • Kiểu dáng: Gọn gàng, không quá thể thao
   • Comfort: Quan trọng hàng đầu

2. Giới Trẻ Năng Động
   • Ưu tiên: Màu sắc trẻ trung, thiết kế mới lạ
   • Tính năng: Nhẹ, linh hoạt
   • Ngân sách: Linh hoạt 1-3 triệu

3. Người Trung Niên
   • Ưu tiên: Êm ái, support tốt
   • Thiết kế: Đơn giản, dễ phối đồ
   • Thương hiệu: Uy tín, bền bỉ

IV. Cách Phối Đồ Thông Minh Với Sneaker

1. Smart Casual Cuối Năm
   • Sneaker trắng + Quần chinos + Áo sơ mi
   • Thêm blazer cho các sự kiện quan trọng
   • Phụ kiện: Tất cổ thấp, đồng hồ leather

2. Streetwear Năng Động
   • Sneaker màu + Quần jogger + Hoodie
   • Layer với áo khoác denim hoặc bomber
   • Phụ kiện: Mũ bucket, backpack

3. Tiệc Tùng Festive
   • Sneaker sang trọng + Quần âu + Áo polo
   • Màu sắc: Đỏ, xanh đậm, vàng đồng
   • Phụ kiện: Dây da, ví cầm tay

V. Lời Khuyên Từ Chuyên Gia

"Đừng chạy theo số lượng, hãy đầu tư vào chất lượng" - đó là chia sẻ từ chuyên gia thời trang Nguyễn Minh Anh. Theo anh, mỗi người nên sở hữu 3-4 đôi sneaker chất lượng thay vì 10-15 đôi giá rẻ.

Cuối năm 2025, Myshoes.vn mang đến chương trình khuyến mãi đặc biệt "Year-End Comfort" với ưu đãi lên đến 30% cho các dòng sneaker cao cấp. Đặc biệt, chúng tôi cam kết:
• Bảo hành chính hãng 24 tháng
• Đổi size trong 30 ngày
• Tư vấn style miễn phí

Hãy đến với Myshoes.vn để tìm cho mình người bạn đồng hành hoàn hảo trong những ngày cuối năm bận rộn!`,
    tag: 'Sneaker',
    author: 'Trần C - Stylist & Fashion Consultant',
    views: 321
  },
  {
    id: '4',
    image: blog4,
    date: '21 Tháng 10, 2024',
    title: 'Gió Lạnh Về Rồi, Bạn Đã Có Giày Ấm Chưa?',
    content: `I. Mùa Đông 2025: Thời Tiết Khắc Nghiệt Và Nhu Cầu Giày Ấm

Theo dự báo từ Trung tâm Khí tượng Thủy văn Trung ương, mùa đông năm 2025 được dự báo sẽ lạnh hơn và kéo dài hơn so với các năm trước. Nhiệt độ tại miền Bắc có thể xuống dưới 10 độ C, trong khi miền Trung cũng chịu ảnh hưởng của các đợt gió mùa Đông Bắc. Đây chính là thời điểm cần chuẩn bị những đôi giày ấm áp để bảo vệ đôi chân - bộ phận nhạy cảm nhất với nhiệt độ thấp.

II. Công Nghệ Giữ Nhiệt Hiện Đại Trong Giày Mùa Đông

1. Công Nghệ Heat Retention
   • Sợi nhiệt Silver Ion: Kháng khuẩn và giữ nhiệt
   • Lớp lót Thinsulate™: Giữ ấm gấp 1.5 lần bông thường
   • Màng chống thấm GORE-TEX: Ngăn nước, thoát hơi ẩm

2. Vật Liệu Cách Nhiệt
   • Wool Felt: Len ép giữ nhiệt tự nhiên
   • Shearling Lining: Lớp lót lông cừu mềm mại
   • Memory Foam Insole: Đệm nhiệt định hình

3. Thiết Kế Chống Lạnh
   • Cổ giày cao ôm mắt cá
   • Đế chống trượt Winter Grip
   • Đường may kín nước

III. Top 5 Giày Ấm Đáng Mua Nhất Mùa Đông 2025

1. Timberland 6-Inch Premium Boot
   • Nhiệt độ chịu được: -20°C
   • Công nghệ: Waterproof leather, PrimaLoft insulation
   • Giá: 4,500,000 VND
   • Phù hợp: Thành phố, dã ngoại nhẹ

2. Dr. Martens 1460 Winter Grip
   • Nhiệt độ chịu được: -15°C
   • Công nghệ: Thermal sole, fur lining
   • Giá: 3,800,000 VND
   • Phù hợp: Street style, đi làm

3. UGG Classic Ultra Mini
   • Nhiệt độ chịu được: -10°C
   • Công nghệ: Twinface sheepskin, Treadlite sole
   • Giá: 3,200,000 VND
   • Phù hợp: Casual, đi chơi

4. Sorel Caribou Boot
   • Nhiệt độ chịu được: -40°C
   • Công nghệ: Waterproof nubuck, felt liner
   • Giá: 5,500,000 VND
   • Phù hợp: Tuyết, thời tiết khắc nghiệt

5. ECCO Soft 7 Winter
   • Nhiệt độ chịu được: -25°C
   • Công nghệ: Yak leather, thermal insole
   • Giá: 3,600,000 VND
   • Phù hợp: Văn phòng, smart casual

IV. Bí Quyết Chọn Giày Ấm Theo Vùng Miền

1. Miền Bắc (Hà Nội & các tỉnh lân cận)
   • Nhiệt độ: 8-15°C, độ ẩm cao
   • Ưu tiên: Chống thấm, giữ nhiệt tốt
   • Kiểu dáng: Boot cổ trung đến cao

2. Miền Trung (Đà Nẵng, Huế)
   • Nhiệt độ: 15-20°C, mưa nhiều
   • Ưu tiên: Thoáng khí, chống thấm
   • Kiểu dáng: Sneaker ấm, boot cổ thấp

3. Miền Nam (TP.HCM & các tỉnh)
   • Nhiệt độ: 20-25°C, se lạnh về đêm
   • Ưu tiên: Thoáng mát, nhẹ nhàng
   • Kiểu dáng: Sneaker mỏng, giày thể thao

V. Chăm Sóc Và Bảo Quản Giày Mùa Đông

1. Vệ Sinh Hàng Ngày
   • Dùng bàn chải mềm làm sạch bùn đất
   • Lau khô tự nhiên, tránh nhiệt cao
   • Sử dụng waterproof spray định kỳ

2. Bảo Quản Khi Không Sử Dụng
   • Nhét giấy báo giữ form giày
   • Để nơi khô ráo, thoáng mát
   • Tránh ánh nắng trực tiếp

3. "Cấp Cứu" Giày Bị Ướt
   • Tháo ngay lót giày ra ngoài
   • Nhét báo khô để hút ẩm
   • Phơi trong bóng râm 2-3 ngày

VI. Chương Trình Khuyến Mãi Đặc Biệt "Winter Ready"

Nhân dịp gió mùa về, Myshoes.vn triển khai chương trình ưu đãi đặc biệt:
• Giảm 25% toàn bộ giày boot mùa đông
• Tặng bộ chăm sóc giày trị giá 500k
• Miễn phí giao hàng toàn quốc
• Bảo hành 2 năm chính hãng

Đừng để cái lạnh làm ảnh hưởng đến sức khỏe và cuộc sống của bạn. Hãy chuẩn bị ngay những đôi giày ấm áp từ hôm nay! Ghé thăm Myshoes.vn hoặc đến trực tiếp các cửa hàng để được tư vấn miễn phí và chọn cho mình người bạn đồng hành hoàn hảết trong mùa đông này.`,
    tag: 'Thời tiết',
    author: 'Myshoes Team',
    views: 99
  },
  {
    id: '5',
    image: blog5,
    date: '20 Tháng 10, 2024',
    title: 'Top mẫu sneaker đáng sắm mùa thu 2025',
    content: `I. BST Mới Nhất Với Nhiều Màu Sắc Và Công Nghệ Êm Ái…

Mùa thu 2025 mang đến làn gió mới cho thế giới sneaker với sự kết hợp hoàn hảo giữa công nghệ hiện đại và thiết kế thời trang. Các thương hiệu lớn đã cho ra mắt những bộ sưu tập đặc biệt, tập trung vào tính năng chống thấm nước và thiết kế thông minh phù hợp với thời tiết se lạnh đặc trưng của mùa thu.

II. Tiêu Chí Lựa Chọn Sneaker Mùa Thu

Khi lựa chọn sneaker cho mùa thu, cần cân nhắc các yếu tố:

• Chất liệu: Nên chọn những chất liệu có khả năng chống nước nhẹ như leather, suede được xử lý waterproof
• Màu sắc: Tông màu trầm ấm như nâu, be, xanh rêu, burgundy
• Độ ấm: Có lớp lót mỏng giữ ấm nhưng vẫn thoáng khí
• Đế: Chống trượt tốt cho những ngày mưa ẩm

III. Top Picks Sneaker Mùa Thu 2025

1. Nike Air Max 90 "Autumn Pack"
   • Thiết kế: Màu nâu camel kết hợp gum sole
   • Công nghệ: Air Max unit visible, leather upper
   • Giá: 3,200,000 VND
   • Đặc điểm: Chống nước nhẹ, phối đồ dễ dàng

2. Adidas Stan Smith "Wool Edition"
   • Thiết kế: Upper làm từ wool blend ấm áp
   • Công nghệ: Cloudfoam comfort insole
   • Giá: 2,800,000 VND
   • Đặc điểm: Nhẹ, ấm, phù hợp tiết trời se lạnh

3. New Balance 574 "Weatherproof"
   • Thiết kế: Suede và mesh có xử lý chống nước
   • Công nghệ: ENCAP midsole, đế chống trượt
   • Giá: 2,500,000 VND
   • Đặc điểm: Bền bỉ, phù hợp đi làm hàng ngày

4. Converse Chuck 70 "Shield Canvas"
   • Thiết kế: Canvas chống nước, màu olive
   • Công nghệ: Đế cao su dày, lót êm
   • Giá: 1,800,000 VND
   • Đặc điểm: Giá cả phải chăng, unisex

5. Puma RS-X "Echo"
   • Thiết kế: Màu xám kết hợp cam burnt
   • Công nghệ: RS cushioning system
   • Giá: 2,900,000 VND
   • Đặc điểm: Êm ái, thiết kế futuristict

IV. Cách Phối Đồ Với Sneaker Mùa Thu

• Casual Style: Sneaker + Quần jeans + Áo hoodie + Áo khoác denim
• Smart Casual: Sneaker + Quần chinos + Áo sơ mi + Blazer
• Street Style: Sneaker + Quần jogger + Áo graphic tee + Bomber jacket

V. Bảo Quản Sneaker Mùa Thu

• Sử dụng waterproof spray trước khi dùng
• Vệ sinh bằng khăn ẩm sau khi đi ngoài trời
• Tránh phơi trực tiếp dưới nắng gắt
• Sử dụng shoe tree để giữ form

Myshoes.vn hiện đang có chương trình ưu đãi đặc biệt cho các mẫu sneaker mùa thu với mức giảm lên đến 30%. Đến ngay cửa hàng gần nhất hoặc đặt hàng online để sở hữu những đôi sneaker đẹp nhất mùa này!`,
    tag: 'Sneaker',
    author: 'Myshoes Team',
    views: 456
  }
];

const newsItem = ref(newsList.find(n => n.id === route.params.id));
const relatedNews = ref(newsList.filter(n => n.id !== route.params.id).slice(0, 3));

// Theo dõi id trên route để cập nhật lại newsItem và relatedNews khi chuyển bài
watch(() => route.params.id, (newId) => {
  newsItem.value = newsList.find(n => n.id === newId);
  relatedNews.value = newsList.filter(n => n.id !== newId).slice(0, 3);
  updateTocAndSections();
});

// Tạo mục lục và phân đoạn nội dung
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
.news-detail-container {
  background-color: #f8f9fa;
  min-height: 100vh;
  font-family: 'Times New Roman', Times, serif;
}

.news-content {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
}

.text-content,
.section-body {
  line-height: 1.8;
  font-size: 1.125rem;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Smooth scrolling for anchor links */
html {
  scroll-behavior: smooth;
}

/* Focus styles for accessibility */
button:focus,
textarea:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

/* Custom scrollbar for the article */
.article-content {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e0 #f1f5f9;
}

.article-content::-webkit-scrollbar {
  width: 6px;
}

.article-content::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.article-content::-webkit-scrollbar-thumb {
  background: #cbd5e0;
}

.article-content::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

/* Image gallery modal styles */
.fixed {
  position: fixed;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.bg-opacity-90 {
  --tw-bg-opacity: 0.9;
}

.z-50 {
  z-index: 50;
}

.max-h-full {
  max-height: 100%;
}

.max-h-screen {
  max-height: 100vh;
}

.object-contain {
  object-fit: contain;
}

.transform {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1\/2 {
  --tw-translate-y: -50%;
}
</style>