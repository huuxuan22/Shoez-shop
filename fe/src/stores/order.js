import { defineStore } from "pinia";
import OrderService from "@/api-services/OrderService";
import { useAuthStore } from "@/stores/auth";

export const useOrderStore = defineStore("order", {
    state: () => ({
        orders: [],
        currentOrder: null,
        checkoutItems: [],
        loading: false,
        error: null
    }),

    getters: {
        orderCount: (state) => state.orders.length,

        getOrdersByStatus: (state) => (status) => {
            return state.orders.filter(order => order.status === status);
        }
    },

    actions: {
        async loadOrders() {
            this.loading = true;
            this.error = null;

            try {
                const ordersData = await OrderService.getByUser();
                this.orders = ordersData || [];
                return this.orders;
            } catch (error) {
                this.error = error.response?.data?.detail || error.message || "Failed to load orders";
                return null;
            } finally {
                this.loading = false;
            }
        },

        async loadOrderDetail(orderId) {
            this.loading = true;
            this.error = null;

            try {
                const orderData = await OrderService.getById(orderId);
                this.currentOrder = orderData;

                // Update trong orders array nếu order đã tồn tại để đảm bảo sync
                const index = this.orders.findIndex(order =>
                    (order.id || order._id) === (orderData.id || orderData._id)
                );
                if (index !== -1) {
                    this.orders[index] = orderData;
                }

                return orderData;
            } catch (error) {
                this.error = error.response?.data?.detail || error.message || "Failed to load order detail";
                return null;
            } finally {
                this.loading = false;
            }
        },


        async createOrder(orderData) {
            this.loading = true;
            this.error = null;

            try {
                const newOrder = await OrderService.create(orderData);

                if (newOrder) {
                    this.orders.unshift(newOrder);
                }

                return newOrder;
            } catch (error) {
                this.error = error.response?.data?.detail || error.message || "Failed to create order";
                throw error;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Thiết lập danh sách items sẽ thanh toán (từ giỏ hàng hoặc trang chi tiết)
         */
        setCheckoutItems(items) {
            this.checkoutItems = Array.isArray(items) ? items : [];
        },

        async updateOrderStatus(orderId, status) {
            try {
                const updatedOrder = await OrderService.updateStatus(orderId, status);

                const index = this.orders.findIndex(order =>
                    (order.id || order._id) === orderId ||
                    (order.id || order._id) === (updatedOrder.id || updatedOrder._id)
                );
                if (index !== -1) {
                    this.orders[index] = updatedOrder;
                }

                const currentOrderId = this.currentOrder?.id || this.currentOrder?._id;
                const updatedOrderId = updatedOrder?.id || updatedOrder?._id;
                if (currentOrderId && currentOrderId === updatedOrderId) {
                    this.currentOrder = updatedOrder;
                }

                return updatedOrder;
            } catch (error) {
                console.error("Error updating order status:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to update order status";
                return null;
            }
        },

        clearError() {
            this.error = null;
        },

        /**
         * Thiết lập checkout từ 1 sản phẩm (mua ngay)
         */
        setCheckoutFromProduct(product) {
            if (!product) {
                this.checkoutItems = [];
                return;
            }

            // Tạo item từ product với meta info
            const singleItem = {
                productId: product.id || product._id,
                size: product.size,
                color: product.color,
                quantity: product.quantity || 1,
                meta: {
                    name: product.name,
                    price: product.price,
                    image: Array.isArray(product.images) ? product.images[0] : (product.image || ''),
                    brand: product.brand
                }
            };

            this.checkoutItems = [singleItem];
        },

        clearOrders() {
            this.orders = [];
            this.currentOrder = null;
            this.error = null;
            this.loading = false;
        }
    }
});

