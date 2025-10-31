import BaseAxios from "./BaseAxios";

const PREFIX_REVIEW = "reviews";

const ReviewService = {
    /**
     * Tạo review mới
     * @param {Object} reviewData - { product_id, order_id, rating, comment, images }
     */
    async create(reviewData) {
        try {
            const response = await BaseAxios.post(`/${PREFIX_REVIEW}/`, reviewData, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy reviews của sản phẩm
     * @param {string} productId 
     * @param {Object} params - { page, limit }
     */
    async getByProduct(productId, params = {}) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_REVIEW}/product/${productId}`, {
                params: {
                    page: params.page || 1,
                    limit: params.limit || 20
                },
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy reviews của user hiện tại
     */
    async getByUser() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_REVIEW}/user`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy reviews theo order_id
     * @param {string} orderId 
     */
    async getByOrder(orderId) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_REVIEW}/order/${orderId}`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Update review
     * @param {string} reviewId 
     * @param {Object} updateData - { rating, comment, images }
     */
    async update(reviewId, updateData) {
        try {
            const response = await BaseAxios.put(`/${PREFIX_REVIEW}/${reviewId}`, updateData, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Xóa review
     * @param {string} reviewId 
     */
    async delete(reviewId) {
        try {
            const response = await BaseAxios.delete(`/${PREFIX_REVIEW}/${reviewId}`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Toggle helpful
     * @param {string} reviewId 
     * @param {boolean} helpful 
     */
    async toggleHelpful(reviewId, helpful = true) {
        try {
            const response = await BaseAxios.post(`/${PREFIX_REVIEW}/${reviewId}/helpful`, null, {
                params: { helpful },
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy danh sách sản phẩm cần đánh giá
     */
    async getPending() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_REVIEW}/pending`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy danh sách reviews cần chú ý (rating <= 3) - Chỉ admin
     */
    async getNeedsAttention() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_REVIEW}/admin/needs-attention`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Upload media (images/videos) for reviews/comments
     * @param {FormData} formData - contains files under key 'files'
     */
    async uploadMedia(formData) {
        try {
            const response = await BaseAxios.post(`/${PREFIX_REVIEW}/upload-media`, formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
                withCredentials: true
            });
            return response.data; // { images: [url, ...] }
        } catch (error) {
            throw error;
        }
    },

    /**
     * Admin comment vào review
     */
    async addAdminComment(reviewId, comment) {
        try {
            const response = await BaseAxios.post(
                `/${PREFIX_REVIEW}/${reviewId}/admin-comment`,
                { comment },
                { withCredentials: true }
            );
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default ReviewService;

