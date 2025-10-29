<template>
    <!-- Toast Notification -->
    <Teleport to="body">
        <Transition name="toast">
            <div v-if="toast.show" class="fixed top-4 right-4 z-[9999]">
                <ToastNotification :message="toast.message" :type="toast.type" @close="toast.show = false" />
            </div>
        </Transition>
    </Teleport>
    <Header />

    <div class="bg-white min-h-[80vh]">
        <div class="container mx-auto px-4 py-8">
            <CartHeader :item-count="cartItems.length" @continue-shopping="continueShopping" />

            <div v-if="cartItems.length > 0" class="flex flex-col lg:flex-row gap-6 mt-6">
                <!-- Cart Items -->
                <div class="lg:w-3/4">
                    <div class="space-y-4">
                        <div v-for="item in cartItems" :key="item.id" class="flex items-start gap-3">
                            <input type="checkbox" v-model="selectedIds" :value="item.id"
                                class="mt-2 w-5 h-5 rounded border-gray-300 text-black focus:ring-black" />
                            <CartItem class="flex-1 min-w-0" :item="item" @update-quantity="updateQuantity"
                                @remove-item="removeItem" />
                        </div>
                    </div>
                </div>
                <!-- Order Summary -->
                <div class="lg:w-1/4">
                    <CartSummary :cart-items="cartItems" :selected-count="selectedIds.length" @checkout="handleCheckout"
                        @checkout-selected="checkoutSelected" />
                </div>
            </div>
            <EmptyCart v-else @continue-shopping="continueShopping" />
        </div>
    </div>
    <Footer />
</template>

<script setup>
import { useRouter } from 'vue-router';
import { reactive } from 'vue'
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';
import CartSummary from '@/components/cart/CartSummary.vue';
import EmptyCart from '@/components/cart/EmptyCart.vue';
import CartItem from '@/components/cart/CartItem.vue';
import { onMounted, ref, computed } from 'vue';
import { useCartStore } from '@/stores/cart';
import { useOrderStore } from '@/stores/order';
import ToastNotification from '@/components/ToastNotification.vue'

const router = useRouter();

const cartStore = useCartStore();
const orderStore = useOrderStore();
const cartItems = ref([]);
const selectedIds = ref([]);

// Toast state
let toastTimer = null;
const toast = reactive({ show: false, message: '', type: 'info' })
function showToast(message, type = 'info', duration = 2500) {
    if (toastTimer) clearTimeout(toastTimer)
    toast.show = true
    toast.message = message
    toast.type = type
    toastTimer = setTimeout(() => { toast.show = false }, duration)
}

function mapCartItems(items) {
    if (!Array.isArray(items)) return [];
    return items.map((i, idx) => {
        const p = i.product || {};
        const images = Array.isArray(p.images) ? p.images : [];
        return {
            id: idx + 1,
            productId: p.id || p._id,
            name: p.name,
            brand: p.brand,
            price: p.price,
            originalPrice: p.originalPrice || p.price,
            image: images[0] || '',
            size: i.size,
            color: i.color,
            quantity: i.quality || i.quantity || 1,
            maxQuantity: p.stock || 99
        };
    });
}

onMounted(async () => {
    const data = await cartStore.loadCart();
    const items = data?.items || [];
    cartItems.value = mapCartItems(items);
});

// Computed
const totalItems = computed(() => cartItems.value.reduce((t, i) => t + (i.quantity || 0), 0));

// Methods
const updateQuantity = (itemId, newQuantity) => {
    const item = cartItems.value.find(item => item.id === itemId);
    if (item) {
        item.quantity = Math.max(1, Math.min(newQuantity, item.maxQuantity));
    }
};

const removeItem = async (itemId) => {
    const item = cartItems.value.find(i => i.id === itemId);
    if (!item) return;
    try {
        await cartStore.removeItem({
            productId: item.productId,
            size: item.size,
            color: item.color
        });
        cartItems.value = mapCartItems(cartStore.items || []);
        showToast('Đã xoá sản phẩm khỏi giỏ hàng', 'success')
    } catch (e) {
        showToast('Xoá sản phẩm thất bại', 'error')
    }
};

const continueShopping = () => {
    router.push('/products');
};

const handleCheckout = () => {
    router.push('/checkout');
};

const checkoutSelected = async () => {
    const chosen = cartItems.value.filter(i => selectedIds.value.includes(i.id))
        .map(i => ({
            productId: i.productId,
            size: i.size,
            color: i.color,
            quantity: i.quantity,
            meta: { name: i.name, price: i.price, image: i.image }
        }));
    orderStore.setCheckoutItems(chosen);
    router.push('/checkout');
};
</script>