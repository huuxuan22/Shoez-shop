// Notification Service
import BaseAxios from "./BaseAxios";

const NotificationService = {
    /**
     * Lấy tất cả notifications của user
     */
    async getAll() {
        try {
            const response = await BaseAxios.get('/notifications', {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy unread notifications
     */
    async getUnread() {
        try {
            const response = await BaseAxios.get('/notifications/unread', {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy số lượng unread notifications
     */
    async getUnreadCount() {
        try {
            const response = await BaseAxios.get('/notifications/count', {
                withCredentials: true
            });
            return response.data.unread_count;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Đánh dấu notification là đã đọc
     */
    async markAsRead(notificationId) {
        try {
            const response = await BaseAxios.patch(`/notifications/${notificationId}/read`, {}, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Đánh dấu tất cả notifications là đã đọc
     */
    async markAllAsRead() {
        try {
            const response = await BaseAxios.patch('/notifications/read-all', {}, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Xóa notification
     */
    async delete(notificationId) {
        try {
            const response = await BaseAxios.delete(`/notifications/${notificationId}`, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default NotificationService;

