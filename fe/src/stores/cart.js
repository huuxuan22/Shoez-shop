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
            this.loading = true;
            this.error = null;

            try {
                const cartData = await CartService.getByUser();
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
         * Lấy toàn bộ danh sách items trong giỏ (getAll)
         */
        async fetchAll() {
            const data = await this.loadCart();
            return this.items || [];
        },

        /**
         * Thêm sản phẩm vào giỏ hàng (optimistic UI)
         * Chỉ nhận 1 đối tượng product:
         * addToCart({ id, quantity, size, color, name, image, price })
         */
        async addToCart(product) {
            const payload = {
                product_id: product?.id,
                quantity: product?.quantity,
                size: product?.size,
                color: product?.color
            };
            const meta = {
                name: product?.name,
                image: product?.image,
                price: product?.price
            };

            if (!payload.product_id || !payload.quantity || !payload.size || !payload.color) {
                this.error = "Thiếu dữ liệu bắt buộc (product.id, size, color, quantity)";
                return null;
            }

            this.loading = true;
            this.error = null;

            const optimisticKey = `${payload.product_id}-${payload.color}-${payload.size}-optimistic-${Date.now()}`;
            const optimisticItem = {
                key: optimisticKey,
                product_id: { id: payload.product_id, name: meta.name, price: meta.price, image: meta.image },
                price: meta.price,
                quantity: payload.quantity,
                size: payload.size,
                color: payload.color,
                _optimistic: true
            };
            this.items = [...this.items, optimisticItem];

            try {
                const cartData = await CartService.addToCart(payload);
                await this.loadCart();
                return cartData;
            } catch (error) {
                console.error("Error adding to cart:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to add to cart";
                // Rollback optimistic item
                this.items = this.items.filter(i => i.key !== optimisticKey);
                return null;
            } finally {
                this.loading = false;
            }
        },


        async removeFromCart(cartIds) {
            if (!Array.isArray(cartIds)) {
                cartIds = [cartIds];
            }
            debugger;
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
         * Xoá 1 item khỏi giỏ theo product/size/color
         */
        async removeItem({ productId, size, color }) {
            if (!productId || size === undefined || color === undefined) {
                this.error = "Thiếu dữ liệu bắt buộc (productId, size, color)";
                return false;
            }

            this.loading = true;
            this.error = null;

            try {
                await CartService.deleteItem({ product_id: productId, size, color });
                await this.loadCart();
                return true;
            } catch (error) {
                console.error("Error removing item:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to remove item";
                return false;
            } finally {
                this.loading = false;
            }
        },

        clearError() {
            this.error = null;
        },


        clearCart() {
            this.cart = null;
            this.items = [];
            this.error = null;
            this.loading = false;
        }
    }
});

