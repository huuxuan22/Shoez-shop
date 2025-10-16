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
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import Header from '@/templates/Header.vue';
import Footer from '@/templates/Footer.vue';
import CartSummary from '@/components/cart/CartSummary.vue';
import EmptyCart from '@/components/cart/EmptyCart.vue';
import CartItem from '@/components/cart/CartItem.vue';

const router = useRouter();

// Sample cart data
const cartItems = ref([
    {
        id: 1,
        productId: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        originalPrice: 2500000,
        image: '/images/shoes/nike-air-max-3.jpg',
        size: 42,
        color: 'Trắng',
        quantity: 1,
        maxQuantity: 10
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
        quantity: 2,
        maxQuantity: 8
    },
    {
        id: 3,
        productId: 3,
        name: 'Converse Chuck Taylor',
        brand: 'Converse',
        price: 1500000,
        originalPrice: 1800000,
        image: '/images/shoes/converse-chuck-taylor-1.jpg',
        size: 40,
        color: 'Đen',
        quantity: 1,
        maxQuantity: 12
    }
]);

// Computed
const totalItems = computed(() => {
    return cartItems.value.reduce((total, item) => total + item.quantity, 0);
});

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