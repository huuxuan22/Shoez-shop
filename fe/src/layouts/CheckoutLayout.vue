<template>
    <div class="min-h-screen bg-white">
        <div class="container mx-auto px-4 py-8">
            <!-- Header -->
            <div class="text-center mb-8">
                <h1 class="text-4xl font-bold text-black mb-4">Thanh toán</h1>
                <p class="text-gray-600 text-lg">Hoàn tất đơn hàng của bạn</p>
            </div>

            <!-- Checkout Steps -->
            <div class="flex justify-center mb-8">
                <div class="flex items-center space-x-8">
                    <div v-for="step in steps" :key="step.number" class="flex items-center">
                        <!-- Step Circle -->
                        <div :class="[
                            'w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold transition-all',
                            getStepClass(step.number)
                        ]">
                            <span v-if="step.number < currentStep">✓</span>
                            <span v-else>{{ step.number }}</span>
                        </div>

                        <!-- Step Label -->
                        <span :class="[
                            'ml-3 font-medium transition-colors',
                            step.number <= currentStep ? 'text-black' : 'text-gray-400'
                        ]">
                            {{ step.label }}
                        </span>

                        <!-- Connector Line -->
                        <div v-if="step.number < steps.length" :class="[
                            'w-16 h-0.5 ml-8 transition-colors',
                            step.number < currentStep ? 'bg-black' : 'bg-gray-300'
                        ]"></div>
                    </div>
                </div>
            </div>

            <div class="flex flex-col lg:flex-row gap-8">
                <!-- Left Column - Checkout Form -->
                <div class="lg:w-2/3">
                    <!-- Shipping Information -->
                    <div v-if="currentStep === 1" class="space-y-6">
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-6">Thông tin giao hàng</h2>

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <InputField label="Họ và tên *" name="fullName" v-model="shippingForm.fullName"
                                    placeholder="Nhập họ và tên" :required="true" />

                                <InputField label="Số điện thoại *" name="phone" type="tel" v-model="shippingForm.phone"
                                    placeholder="Nhập số điện thoại" :required="true" />

                                <InputField label="Email *" name="email" type="email" v-model="shippingForm.email"
                                    placeholder="Nhập email" :required="true" />

                                <div class="md:col-span-2">
                                    <InputField label="Địa chỉ *" name="address" v-model="shippingForm.address"
                                        placeholder="Nhập địa chỉ chi tiết" :required="true" />
                                </div>

                                <InputField label="Tỉnh/Thành phố *" name="city" v-model="shippingForm.city"
                                    placeholder="Nhập tỉnh/thành phố" :required="true" />

                                <InputField label="Quận/Huyện *" name="district" v-model="shippingForm.district"
                                    placeholder="Nhập quận/huyện" :required="true" />

                                <InputField label="Phường/Xã *" name="ward" v-model="shippingForm.ward"
                                    placeholder="Nhập phường/xã" :required="true" />
                            </div>

                            <!-- Shipping Method -->
                            <div class="mt-6">
                                <h3 class="font-semibold text-black mb-4">Phương thức giao hàng</h3>
                                <div class="space-y-3">
                                    <label v-for="option in shippingOptions" :key="option.value" :class="[
                                        'flex items-start p-4 border-2 rounded-lg cursor-pointer transition-all',
                                        shippingForm.shippingMethod === option.value
                                            ? 'border-black bg-gray-50'
                                            : 'border-gray-200 hover:border-gray-300'
                                    ]">
                                        <input type="radio" :value="option.value" v-model="shippingForm.shippingMethod"
                                            class="mt-1 text-black focus:ring-black" />
                                        <div class="ml-3 flex-1">
                                            <div class="flex justify-between items-start">
                                                <span class="font-medium text-black">{{ option.label }}</span>
                                                <span v-if="option.price" class="text-black font-semibold">{{
                                                    option.price }}</span>
                                            </div>
                                            <p v-if="option.description" class="text-sm text-gray-600 mt-1">{{
                                                option.description }}</p>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <!-- Note -->
                            <div class="mt-6">
                                <label class="block text-sm font-medium text-gray-700 mb-2">Ghi chú (tuỳ chọn)</label>
                                <textarea v-model="shippingForm.note" rows="3"
                                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-black focus:border-transparent"
                                    placeholder="Ghi chú cho đơn hàng..."></textarea>
                            </div>
                        </div>
                    </div>

                    <!-- Payment Method -->
                    <div v-else-if="currentStep === 2" class="space-y-6">
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-6">Phương thức thanh toán</h2>

                            <div class="space-y-3">
                                <label v-for="option in paymentOptions" :key="option.value" :class="[
                                    'flex items-start p-4 border-2 rounded-lg cursor-pointer transition-all',
                                    paymentMethod === option.value
                                        ? 'border-black bg-gray-50'
                                        : 'border-gray-200 hover:border-gray-300'
                                ]">
                                    <input type="radio" :value="option.value" v-model="paymentMethod"
                                        class="mt-1 text-black focus:ring-black" />
                                    <div class="ml-3 flex-1">
                                        <div class="flex justify-between items-start">
                                            <span class="font-medium text-black">{{ option.label }}</span>
                                        </div>
                                        <p v-if="option.description" class="text-sm text-gray-600 mt-1">{{
                                            option.description }}</p>
                                    </div>
                                </label>
                            </div>

                            <!-- Credit Card Form -->
                            <div v-if="paymentMethod === 'credit_card'"
                                class="mt-6 p-4 border border-gray-200 rounded-lg">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <InputField label="Số thẻ" name="cardNumber" v-model="cardInfo.number"
                                        placeholder="1234 5678 9012 3456" :maxlength="19" />

                                    <InputField label="Tên chủ thẻ" name="cardName" v-model="cardInfo.name"
                                        placeholder="NGUYEN VAN A" />

                                    <InputField label="Ngày hết hạn" name="cardExpiry" v-model="cardInfo.expiry"
                                        placeholder="MM/YY" :maxlength="5" />

                                    <InputField label="CVV" name="cardCvv" v-model="cardInfo.cvv" placeholder="123"
                                        :maxlength="3" />
                                </div>
                            </div>

                            <!-- Security Notice -->
                            <div class="mt-4 p-4 bg-gray-50 rounded-lg">
                                <div class="flex items-start gap-3">
                                    <svg class="w-5 h-5 text-gray-600 mt-0.5 flex-shrink-0" fill="none"
                                        stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                    </svg>
                                    <p class="text-sm text-gray-600">
                                        Thông tin thẻ của bạn được bảo mật và mã hóa. Chúng tôi không lưu trữ thông tin
                                        thẻ của bạn.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Order Review -->
                    <div v-else-if="currentStep === 3" class="space-y-6">
                        <!-- Shipping Info Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">Thông tin giao hàng</h2>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                <div>
                                    <p class="text-gray-600">Họ tên</p>
                                    <p class="font-semibold text-black">{{ shippingForm.fullName }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">Số điện thoại</p>
                                    <p class="font-semibold text-black">{{ shippingForm.phone }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">Email</p>
                                    <p class="font-semibold text-black">{{ shippingForm.email }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">Địa chỉ</p>
                                    <p class="font-semibold text-black">
                                        {{ shippingForm.address }}, {{ shippingForm.ward }}, {{ shippingForm.district
                                        }}, {{ shippingForm.city }}
                                    </p>
                                </div>
                                <div v-if="shippingForm.note">
                                    <p class="text-gray-600">Ghi chú</p>
                                    <p class="font-semibold text-black">{{ shippingForm.note }}</p>
                                </div>
                            </div>
                        </div>

                        <!-- Payment Method Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">Phương thức thanh toán</h2>
                            <div class="flex items-center justify-between">
                                <div>
                                    <p class="font-semibold text-black">{{ getPaymentMethodLabel(paymentMethod) }}</p>
                                    <p class="text-sm text-gray-600">{{ getPaymentMethodDescription(paymentMethod) }}
                                    </p>
                                </div>
                                <button @click="currentStep = 2"
                                    class="text-black hover:text-gray-700 transition-colors">
                                    Chỉnh sửa
                                </button>
                            </div>
                        </div>

                        <!-- Order Items Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">Sản phẩm</h2>
                            <div class="space-y-4">
                                <div v-for="item in cartItems" :key="item.id"
                                    class="flex items-center gap-4 py-3 border-b border-gray-100 last:border-b-0">
                                    <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded-lg" />
                                    <div class="flex-1">
                                        <h3 class="font-semibold text-black">{{ item.name }}</h3>
                                        <p class="text-sm text-gray-600">{{ item.brand }}</p>
                                        <p class="text-sm text-gray-600">Size: {{ item.size }} | Màu: {{ item.color }}
                                        </p>
                                    </div>
                                    <div class="text-right">
                                        <p class="font-semibold text-black">{{ formatPrice(item.price * item.quantity)
                                            }}</p>
                                        <p class="text-sm text-gray-600">Số lượng: {{ item.quantity }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column - Order Summary -->
                <div class="lg:w-1/3">
                    <div class="bg-white border border-gray-200 rounded-lg p-6 sticky top-4">
                        <h2 class="text-xl font-bold text-black mb-6">Tóm tắt đơn hàng</h2>

                        <!-- Order Items -->
                        <div class="space-y-3 mb-6">
                            <div v-for="item in cartItems" :key="item.id" class="flex items-center gap-3">
                                <img :src="item.image" :alt="item.name" class="w-12 h-12 object-cover rounded" />
                                <div class="flex-1 min-w-0">
                                    <p class="font-medium text-black text-sm truncate">{{ item.name }}</p>
                                    <p class="text-gray-600 text-xs">Size {{ item.size }} | SL: {{ item.quantity }}</p>
                                </div>
                                <p class="font-semibold text-black text-sm whitespace-nowrap">
                                    {{ formatPrice(item.price * item.quantity) }}
                                </p>
                            </div>
                        </div>

                        <!-- Pricing -->
                        <div class="space-y-2 border-t border-gray-200 pt-4">
                            <div class="flex justify-between text-sm">
                                <span class="text-gray-600">Tạm tính</span>
                                <span class="text-black">{{ formatPrice(subtotal) }}</span>
                            </div>

                            <div class="flex justify-between text-sm">
                                <span class="text-gray-600">Phí vận chuyển</span>
                                <span class="text-black">{{ shippingFee > 0 ? formatPrice(shippingFee) : 'Miễn phí'
                                    }}</span>
                            </div>

                            <div class="flex justify-between text-lg font-bold border-t border-gray-200 pt-3 mt-2">
                                <span class="text-black">Tổng cộng</span>
                                <span class="text-black">{{ formatPrice(total) }}</span>
                            </div>
                        </div>

                        <!-- Action Button -->
                        <Button :variant="'primary'" @click="handleAction" class="w-full mt-6">
                            {{ actionButtonText }}
                        </Button>

                        <!-- Back Button -->
                        <button v-if="currentStep > 1" @click="goToPreviousStep"
                            class="w-full mt-3 text-center text-gray-600 hover:text-black transition-colors">
                            ← Quay lại
                        </button>

                        <!-- Security Badge -->
                        <div class="mt-4 text-center">
                            <div class="flex items-center justify-center gap-2 text-sm text-gray-600">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                </svg>
                                <span>Thanh toán an toàn & bảo mật</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Success Modal -->
        <div v-if="showSuccessModal" class="fixed inset-0 z-50 overflow-y-auto">
            <div class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
                <!-- Background -->
                <div class="fixed inset-0 bg-black bg-opacity-50 transition-opacity" @click="handleSuccessModalClose">
                </div>

                <!-- Modal Panel -->
                <div
                    class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div class="text-center p-8">
                            <div
                                class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                                <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                            </div>

                            <h2 class="text-2xl font-bold text-black mb-4">Đặt hàng thành công!</h2>
                            <p class="text-gray-600 mb-2">Cảm ơn bạn đã đặt hàng. Đơn hàng của bạn đã được xác nhận.</p>
                            <p class="text-gray-600 mb-6">Mã đơn hàng: <strong class="text-black">{{ orderResult?.id
                                    }}</strong></p>

                            <div class="bg-gray-50 rounded-lg p-4 mb-6 text-left">
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-gray-600">Tổng thanh toán:</span>
                                    <span class="text-xl font-bold text-black">{{ formatPrice(orderResult?.total || 0)
                                        }}</span>
                                </div>
                                <div class="flex justify-between items-center text-sm">
                                    <span class="text-gray-600">Dự kiến giao hàng:</span>
                                    <span class="text-black">{{ formatDate(orderResult?.estimatedDelivery) }}</span>
                                </div>
                            </div>

                            <div class="flex gap-4 justify-center">
                                <Button :variant="'outline'" @click="handleSuccessModalClose">
                                    Tiếp tục mua sắm
                                </Button>
                                <Button :variant="'primary'" @click="viewOrder">
                                    Xem đơn hàng
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

// Import các component UI
import InputField from '@/components/FormInput.vue';
import Button from '@/components/Button.vue';

const router = useRouter();

// Step management
const currentStep = ref(1);

// Form data
const shippingForm = ref({
    fullName: '',
    phone: '',
    email: '',
    address: '',
    city: '',
    district: '',
    ward: '',
    note: '',
    shippingMethod: 'standard'
});

const paymentMethod = ref('cod');
const cardInfo = ref({
    number: '',
    name: '',
    expiry: '',
    cvv: ''
});

// Cart data
const cartItems = ref([
    {
        id: 1,
        productId: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        image: '/images/shoes/nike-air-max-3.jpg',
        size: 42,
        color: 'Trắng',
        quantity: 1
    },
    {
        id: 2,
        productId: 2,
        name: 'Adidas Ultraboost 22',
        brand: 'Adidas',
        price: 4500000,
        image: '/images/shoes/adidas-ultraboost-1.jpg',
        size: 41,
        color: 'Đen',
        quantity: 2
    }
]);

// UI state
const showSuccessModal = ref(false);
const orderResult = ref(null);

// Constants
const steps = [
    { number: 1, label: 'Giao hàng' },
    { number: 2, label: 'Thanh toán' },
    { number: 3, label: 'Xác nhận' }
];

const shippingOptions = [
    {
        value: 'standard',
        label: 'Giao hàng tiêu chuẩn',
        description: 'Nhận hàng trong 3-5 ngày',
        price: '30.000đ'
    },
    {
        value: 'express',
        label: 'Giao hàng nhanh',
        description: 'Nhận hàng trong 1-2 ngày',
        price: '50.000đ'
    },
    {
        value: 'pickup',
        label: 'Nhận tại cửa hàng',
        description: 'Nhận hàng trực tiếp',
        price: 'Miễn phí'
    }
];

const paymentOptions = [
    {
        value: 'cod',
        label: 'Thanh toán khi nhận hàng (COD)',
        description: 'Trả tiền mặt khi nhận được hàng'
    },
    {
        value: 'credit_card',
        label: 'Thẻ tín dụng/Ghi nợ',
        description: 'Thanh toán an toàn bằng thẻ Visa, MasterCard'
    },
    {
        value: 'bank_transfer',
        label: 'Chuyển khoản ngân hàng',
        description: 'Chuyển khoản trực tiếp đến tài khoản ngân hàng'
    },
    {
        value: 'momo',
        label: 'Ví MoMo',
        description: 'Thanh toán nhanh qua ví điện tử MoMo'
    }
];

// Computed
const shippingFee = computed(() => {
    return subtotal.value > 5000000 ? 0 : 30000;
});

const subtotal = computed(() => {
    return cartItems.value.reduce((total, item) => total + (item.price * item.quantity), 0);
});

const total = computed(() => {
    return subtotal.value + shippingFee.value;
});

const actionButtonText = computed(() => {
    switch (currentStep.value) {
        case 1: return 'Tiếp tục thanh toán';
        case 2: return 'Tiếp tục xác nhận';
        case 3: return 'Đặt hàng';
        default: return 'Tiếp tục';
    }
});

// Methods
const getStepClass = (stepNumber) => {
    if (stepNumber < currentStep.value) {
        return 'bg-black border-black text-white';
    } else if (stepNumber === currentStep.value) {
        return 'border-black bg-white text-black';
    } else {
        return 'border-gray-300 bg-white text-gray-400';
    }
};

const validateShipping = () => {
    const required = ['fullName', 'phone', 'email', 'address', 'city', 'district', 'ward'];
    return required.every(field => shippingForm.value[field].trim() !== '');
};

const goToNextStep = () => {
    if (currentStep.value === 1 && !validateShipping()) {
        alert('Vui lòng điền đầy đủ thông tin giao hàng');
        return;
    }

    if (currentStep.value < 3) {
        currentStep.value++;
    } else {
        placeOrder();
    }
};

const goToPreviousStep = () => {
    if (currentStep.value > 1) {
        currentStep.value--;
    }
};

const handleAction = () => {
    if (currentStep.value === 3) {
        placeOrder();
    } else {
        goToNextStep();
    }
};

const placeOrder = async () => {
    try {
        // Simulate API call
        const orderData = {
            id: 'ORD' + Date.now(),
            shipping: shippingForm.value,
            payment: paymentMethod.value,
            items: cartItems.value,
            total: total.value,
            orderDate: new Date().toISOString(),
            estimatedDelivery: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString()
        };

        // Here would be your API call
        // const result = await api.placeOrder(orderData);

        orderResult.value = orderData;
        showSuccessModal.value = true;
    } catch (error) {
        alert('Có lỗi xảy ra khi đặt hàng. Vui lòng thử lại.');
    }
};

const handleSuccessModalClose = () => {
    showSuccessModal.value = false;
    router.push('/');
};

const viewOrder = () => {
    // Navigate to order detail page
    router.push(`/orders/${orderResult.value.id}`);
};

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString('vi-VN');
};

const getPaymentMethodLabel = (method) => {
    const methods = {
        cod: 'Thanh toán khi nhận hàng',
        credit_card: 'Thẻ tín dụng/Ghi nợ',
        bank_transfer: 'Chuyển khoản ngân hàng',
        momo: 'Ví MoMo'
    };
    return methods[method] || method;
};

const getPaymentMethodDescription = (method) => {
    const descriptions = {
        cod: 'Trả tiền mặt khi nhận hàng',
        credit_card: 'Thanh toán an toàn bằng thẻ',
        bank_transfer: 'Chuyển khoản trực tiếp',
        momo: 'Thanh toán qua ví điện tử'
    };
    return descriptions[method] || '';
};

// Lifecycle
onMounted(() => {
    if (cartItems.value.length === 0) {
        router.push('/cart');
    }
});
</script>