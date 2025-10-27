import { defineStore } from "pinia";
import CartService from "@/api-services/CartService";
import { useAuthStore } from "@/stores/auth";

export const useCartStore = defineStore("cart", {
    state: () => ({
        cart: null,
        items: [],
        loading: false,
        error: null
    }),

    getters: {
        /**
         * Số lượng sản phẩm trong giỏ hàng
         */
        totalItems: (state) => {
            if (!state.items || state.items.length === 0) return 0;
            return state.items.reduce((total, item) => total + (item.quantity || 0), 0);
        },

        /**
         * Tổng giá trị giỏ hàng
         */
        totalPrice: (state) => {
            if (!state.items || state.items.length === 0) return 0;
            return state.items.reduce((total, item) => {
                const price = item.product_id?.price || item.price || 0;
                const quantity = item.quantity || 0;
                return total + (price * quantity);
            }, 0);
        },

        /**
         * Kiểm tra giỏ hàng có rỗng không
         */
        isEmpty: (state) => !state.items || state.items.length === 0,

        /**
         * User ID
         */
        userId: () => {
            const authStore = useAuthStore();
            return authStore.user?.id || authStore.user?._id || null;
        }
    },

    actions: {
        /**
         * Tải giỏ hàng từ server
         */
        async loadCart() {
            const userId = this.userId;

            if (!userId) {
                this.error = "User not authenticated";
                return null;
            }

            this.loading = true;
            this.error = null;

            try {
                const cartData = await CartService.getByUser(userId);
                this.cart = cartData;
                this.items = cartData?.items || [];
                return cartData;
            } catch (error) {
                console.error("Error loading cart:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to load cart";
                return null;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Thêm sản phẩm vào giỏ hàng
         */
        async addToCart(productId, quantity, size, color) {
            const userId = this.userId;

            if (!userId) {
                this.error = "User not authenticated";
                return null;
            }

            this.loading = true;
            this.error = null;

            try {
                const cartData = await CartService.addToCart({
                    user_id: userId,
                    product_id: productId,
                    quantity,
                    size,
                    color
                });

                // Reload cart sau khi thêm
                await this.loadCart();

                return cartData;
            } catch (error) {
                console.error("Error adding to cart:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to add to cart";
                return null;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Xóa sản phẩm khỏi giỏ hàng
         */
        async removeFromCart(cartIds) {
            if (!Array.isArray(cartIds)) {
                cartIds = [cartIds];
            }

            this.loading = true;
            this.error = null;

            try {
                await CartService.deleteMultiple(cartIds);

                // Reload cart sau khi xóa
                await this.loadCart();

                return true;
            } catch (error) {
                console.error("Error removing from cart:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to remove from cart";
                return false;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Clear error
         */
        clearError() {
            this.error = null;
        },

        /**
         * Clear cart (logout)
         */
        clearCart() {
            this.cart = null;
            this.items = [];
            this.error = null;
            this.loading = false;
        }
    }
});

