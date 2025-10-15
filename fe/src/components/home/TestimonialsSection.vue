<template>
    <section class="py-12 bg-white border-t border-gray-200">
        <div class="container mx-auto px-4">
            <div class="text-center mb-8">
                <h2 class="text-2xl md:text-3xl font-bold text-black">Đánh giá</h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
                <div v-for="(review, index) in testimonials" :key="index">
                    <div class="border border-gray-200 rounded p-6 hover:border-black transition">
                        <!-- Stars -->
                        <div class="flex gap-1 mb-3">
                            <span v-for="i in 5" :key="i" class="text-yellow-400">★</span>
                        </div>

                        <!-- Review text -->
                        <p class="text-sm text-gray-700 mb-4">"{{ review.text }}"</p>

                        <!-- Author -->
                        <div class="text-sm">
                            <div class="font-medium text-black">{{ review.author }}</div>
                            <div class="text-gray-500">{{ review.role }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
const testimonials = [
    {
        text: 'Giày rất đẹp và chất lượng, đi rất êm chân. Giao hàng nhanh, đóng gói cẩn thận. Sẽ ủng hộ shop lâu dài!',
        author: 'Nguyễn Văn An',
        role: 'Khách hàng thân thiết'
    },
    {
        text: 'Mình đã mua 3 đôi giày ở đây rồi, tất cả đều chính hãng 100%. Giá cả hợp lý, nhân viên tư vấn nhiệt tình!',
        author: 'Trần Thị Bình',
        role: 'Đã mua 3 lần'
    },
    {
        text: 'Shop uy tín, hàng chính hãng, giá tốt. Freeship nhanh chóng. Rất hài lòng với dịch vụ. Recommend!',
        author: 'Lê Hoàng Minh',
        role: 'Khách hàng mới'
    }
]
</script>