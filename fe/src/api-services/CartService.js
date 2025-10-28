import BaseAxios from "./BaseAxios";

const PREFIX_CART = "cart";

const CartService = {
    /**
     * Lấy giỏ hàng của user
     * @param {string} userId - ID của user
     */
    async getByUser() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_CART}/user`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Thêm sản phẩm vào giỏ hàng
     * @param {Object} cartData - { user_id, product_id, quantity, size, color }
     */
    async addToCart(cartData) {
        try {
            // Backend now reads user from context; prefer /cart/item with product payload
            const response = await BaseAxios.post(`/${PREFIX_CART}/item`, cartData, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Xóa nhiều sản phẩm khỏi giỏ hàng
     * @param {Array<string>} cartIds - Danh sách IDs cần xóa
     */
    async deleteMultiple(cartIds) {
        try {
            const response = await BaseAxios.delete(`/${PREFIX_CART}/delete-multiple`, {
                data: { ids: cartIds },
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default CartService;

