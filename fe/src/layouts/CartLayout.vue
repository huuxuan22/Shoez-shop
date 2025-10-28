<template>
    <div class="min-h-screen bg-white">
        <Header />
        <div class="container mx-auto px-4 py-8">
            <CartHeader :item-count="cartItems.length" @continue-shopping="continueShopping" />

            <div v-if="cartItems.length > 0" class="flex flex-col lg:flex-row gap-8 mt-6">
                <!-- Cart Items -->
                <div class="lg:w-2/3">
                    <div class="space-y-4">
                        <CartItem v-for="item in cartItems" :key="item.id" :item="item"
                            @update-quantity="updateQuantity" @remove-item="removeItem" />
                    </div>
                </div>

                <!-- Order Summary -->
                <div class="lg:w-1/3">
                    <CartSummary :cart-items="cartItems" @checkout="handleCheckout" />
                </div>
            </div>

            <EmptyCart v-else @continue-shopping="continueShopping" />
        </div>
        <Footer />
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';
import CartSummary from '@/components/cart/CartSummary.vue';
import EmptyCart from '@/components/cart/EmptyCart.vue';
import CartItem from '@/components/cart/CartItem.vue';
import { onMounted, ref, computed } from 'vue';
import { useCartStore } from '@/stores/cart';

const router = useRouter();

const cartStore = useCartStore();
const cartItems = ref([]);

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

const removeItem = (itemId) => {
    cartItems.value = cartItems.value.filter(item => item.id !== itemId);
};

const continueShopping = () => {
    router.push('/products');
};

const handleCheckout = () => {
    router.push('/checkout');
};
</script>