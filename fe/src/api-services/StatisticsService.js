// src/api-services/StatisticsService.js
import BaseAxios from "./BaseAxios";

const PREFIX_STATISTICS = "statistics";

const StatisticsService = {
    /**
     * Lấy thống kê tổng quan
     */
    async getOverview() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/overview`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy dữ liệu biểu đồ doanh thu
     * @param {number} days - Số ngày (mặc định 7)
     */
    async getRevenueChart(days = 7) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/revenue-chart`, {
                params: { days },
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy top sản phẩm bán chạy
     * @param {number} limit - Số lượng sản phẩm (mặc định 5)
     */
    async getTopProducts(limit = 5) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/top-products`, {
                params: { limit },
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy các đơn hàng gần đây
     * @param {number} limit - Số lượng đơn hàng (mặc định 5)
     */
    async getRecentOrders(limit = 5) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/recent-orders`, {
                params: { limit },
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê doanh thu chi tiết (hôm nay, tuần này, tháng này, năm này)
     */
    async getDetailedRevenue() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/detailed-revenue`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê đơn hàng chi tiết
     */
    async getDetailedOrders() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/detailed-orders`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê hủy hàng
     */
    async getCancellationStats() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/cancellation`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê người dùng
     */
    async getUserStats() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/users`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê danh mục
     */
    async getCategoryStats() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/categories`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê thương hiệu
     */
    async getBrandStats() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/brands`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy thống kê sản phẩm
     */
    async getProductStats() {
        try {
            const response = await BaseAxios.get(`/${PREFIX_STATISTICS}/products`, {
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default StatisticsService;

