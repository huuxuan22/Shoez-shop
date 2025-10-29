// src/api-services/OrderService.js
import BaseAxios from "./BaseAxios";

const PREFIX_ORDER = "orders";

const OrderService = {
    /**
     * Lấy tất cả đơn hàng với filter và pagination
     * @param {Object} params - { page, limit, starttime, endtime, valueSearch }
     */
    async getAll(params = {}) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/admin/orders`, {
                params: {
                    page: params.page || 1,
                    limit: params.limit || 20,
                    starttime: params.starttime || null,
                    endtime: params.endtime || null,
                    valueSearch: params.valueSearch || null
                },
                withCredentials: true,
            });

            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Tìm kiếm đơn hàng theo từ khóa
     * @param {string} query - Từ khóa tìm kiếm
     * @param {Object} params - { page, limit }
     */
    async search(query, params = {}) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/admin/search`, {
                params: {
                    q: query,
                    page: params.page || 1,
                    limit: params.limit || 20
                },
                withCredentials: true,
            });
            return response;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy đơn hàng theo status
     * @param {string} status - Trạng thái đơn hàng
     * @param {Object} params - { page, limit }
     */
    async getByStatus(status, params = {}) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/admin/by-status`, {
                params: {
                    status: status,
                    page: params.page || 1,
                    limit: params.limit || 20
                },
                withCredentials: true,
            });
            return response;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy đơn hàng theo khoảng thời gian
     * @param {string} startDate - Ngày bắt đầu (ISO format)
     * @param {string} endDate - Ngày kết thúc (ISO format)
     * @param {Object} params - { page, limit }
     */
    async getByDateRange(startDate, endDate, params = {}) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/admin/by-date-range`, {
                params: {
                    start_date: startDate,
                    end_date: endDate,
                    page: params.page || 1,
                    limit: params.limit || 20
                },
                withCredentials: true,
            });
            return response;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy tất cả đơn hàng (không phân trang) - cho admin
     */
    async getAllWithoutPagination() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/admin/all`, {
                withCredentials: true,
            });
            return response;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy đơn hàng theo user hiện tại (dùng user_context từ backend)
     * Không cần truyền userId nữa, backend tự lấy từ context
     */
    async getByUser() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/user`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy chi tiết một đơn hàng theo ID
     * @param {string} orderId - ID của đơn hàng
     */
    async getById(orderId) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_ORDER}/${orderId}`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Cập nhật trạng thái đơn hàng
     * @param {string} orderId - ID của đơn hàng
     * @param {string} status - Trạng thái mới
     */
    async updateStatus(orderId, status) {
        try {
            const response = await BaseAxios.patch(`/${PREFIX_ORDER}/admin/update-status`, {
                order_id: orderId,
                status: status
            }, {
                withCredentials: true,
            });
            return response;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Tạo đơn hàng mới
     * @param {Object} orderData - Dữ liệu đơn hàng
     */
    async create(orderData) {
        try {
            const response = await BaseAxios.post(`/${PREFIX_ORDER}/`, orderData, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default OrderService;
