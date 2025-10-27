import { defineStore } from "pinia";
import OrderService from "@/api-services/OrderService";
import { useAuthStore } from "@/stores/auth";

export const useOrderStore = defineStore("order", {
    state: () => ({
        orders: [],
        currentOrder: null,
        loading: false,
        error: null
    }),

    getters: {
        /**
         * User ID
         */
        userId: () => {
            const authStore = useAuthStore();
            return authStore.user?.id || authStore.user?._id || null;
        },

        /**
         * Số lượng đơn hàng
         */
        orderCount: (state) => state.orders.length,

        /**
         * Đơn hàng theo status
         */
        getOrdersByStatus: (state) => (status) => {
            return state.orders.filter(order => order.status === status);
        }
    },

    actions: {
        /**
         * Tải tất cả đơn hàng của user
         */
        async loadOrders() {
            const userId = this.userId;

            if (!userId) {
                this.error = "User not authenticated";
                return null;
            }

            this.loading = true;
            this.error = null;

            try {
                const ordersData = await OrderService.getByUser(userId);
                this.orders = ordersData || [];
                return this.orders;
            } catch (error) {
                console.error("Error loading orders:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to load orders";
                return null;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Tải chi tiết một đơn hàng
         */
        async loadOrderDetail(orderId) {
            this.loading = true;
            this.error = null;

            try {
                const orderData = await OrderService.getById(orderId);
                this.currentOrder = orderData;
                return orderData;
            } catch (error) {
                console.error("Error loading order detail:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to load order detail";
                return null;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Tạo đơn hàng mới
         */
        async createOrder(orderData) {
            this.loading = true;
            this.error = null;

            try {
                const newOrder = await OrderService.create(orderData);

                // Thêm vào danh sách orders
                if (newOrder) {
                    this.orders.unshift(newOrder);
                }

                return newOrder;
            } catch (error) {
                console.error("Error creating order:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to create order";
                return null;
            } finally {
                this.loading = false;
            }
        },

        /**
         * Cập nhật trạng thái đơn hàng
         */
        async updateOrderStatus(orderId, status) {
            try {
                const updatedOrder = await OrderService.updateStatus(orderId, status);

                // Update trong danh sách orders
                const index = this.orders.findIndex(order => order.id === orderId);
                if (index !== -1) {
                    this.orders[index] = updatedOrder;
                }

                // Update currentOrder nếu đang xem
                if (this.currentOrder && this.currentOrder.id === orderId) {
                    this.currentOrder = updatedOrder;
                }

                return updatedOrder;
            } catch (error) {
                console.error("Error updating order status:", error);
                this.error = error.response?.data?.detail || error.message || "Failed to update order status";
                return null;
            }
        },

        /**
         * Clear error
         */
        clearError() {
            this.error = null;
        },

        /**
         * Clear orders (logout)
         */
        clearOrders() {
            this.orders = [];
            this.currentOrder = null;
            this.error = null;
            this.loading = false;
        }
    }
});

