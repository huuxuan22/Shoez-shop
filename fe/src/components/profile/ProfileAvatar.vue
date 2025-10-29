<template>
    <div class="text-center">
        <div class="relative inline-block">
            <!-- Avatar Image -->
            <div class="w-32 h-32 rounded-full overflow-hidden border-4 border-white shadow-lg mx-auto">
                <img :src="avatarSrc" :alt="avatarSrc" class="w-full h-full object-cover" />
            </div>

            <!-- Upload Overlay -->
            <label :class="[
                'absolute inset-0 rounded-full bg-black bg-opacity-50 flex items-center justify-center cursor-pointer transition-opacity',
                isUploading ? 'opacity-100' : 'opacity-0 hover:opacity-100'
            ]">
                <input type="file" accept="image/*" @change="handleFileSelect" class="hidden" :disabled="isUploading" />

                <div v-if="isUploading" class="text-white">
                    <!-- Spinner -->
                    <svg class="w-8 h-8 animate-spin mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                </div>

                <div v-else class="text-white text-center">
                    <!-- Camera Icon -->
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    <span class="text-xs font-medium">Đổi ảnh</span>
                </div>
            </label>
        </div>

        <!-- User Info -->
        <div class="mt-4">
            <h3 class="font-semibold text-black text-lg">{{ user.fullName }}</h3>
            <p class="text-gray-600 text-sm">{{ user.email }}</p>
        </div>

        <!-- Upload Guidelines -->
        <div class="mt-4 p-3 bg-blue-50 rounded-lg">
            <p class="text-xs text-blue-700 text-left">
                <strong>Lưu ý:</strong> Ảnh đại diện nên có định dạng JPG, PNG hoặc GIF.
                Kích thước tối đa 5MB.
            </p>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

// Props nhận từ parent
const props = defineProps({
    user: {
        type: Object,
        required: true
    },
    isUploading: {
        type: Boolean,
        default: false
    }
});

// Emit sự kiện thay đổi avatar
const emit = defineEmits(['avatar-change']);

// Computed: nếu avatar rỗng thì dùng default
const avatarSrc = computed(() => {
    if (props.user.avatar) {
        return props.user.avatar;
    }
    return new URL('../../assets/icons/user_icon.png', import.meta.url).href;
});

// Xử lý upload file
const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    // Kiểm tra định dạng file
    const validTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (!validTypes.includes(file.type)) {
        alert('Chỉ chấp nhận file ảnh (JPG, PNG, GIF)');
        return;
    }

    // Kiểm tra dung lượng file (5MB)
    if (file.size > 5 * 1024 * 1024) {
        alert('Kích thước file không được vượt quá 5MB');
        return;
    }

    emit('avatar-change', file);
};
</script>