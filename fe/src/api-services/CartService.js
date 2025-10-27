import BaseAxios from "./BaseAxios";

const PREFIX_CART = "cart";

const CartService = {
    /**
     * Lấy giỏ hàng của user
     * @param {string} userId - ID của user
     */
    async getByUser(userId) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_CART}/user/${userId}`, {
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
            const response = await BaseAxios.post(`/${PREFIX_CART}/`, cartData, {
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

