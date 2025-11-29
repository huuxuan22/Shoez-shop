// Message Service
import BaseAxios from "./BaseAxios";

const MessageService = {
    /**
     * Admin gửi tin nhắn cho user
     */
    async adminSendMessage(payload) {
        try {
            const response = await BaseAxios.post('/messages/admin-send', payload, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy danh sách messages theo conversation_id
     */
    async getMessages(conversationId, limit = 100) {
        try {
            const response = await BaseAxios.get(`/messages/${conversationId}`, {
                params: { limit },
                withCredentials: true
            });
            return response.data.messages || [];
        } catch (error) {
            throw error;
        }
    },

    /**
     * User gửi tin nhắn cho admin
     */
    async userSendMessage(payload) {
        try {
            const response = await BaseAxios.post('/messages/user-send', payload, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Lấy toàn bộ messages của user hiện tại (theo userId)
     * Tự động tìm conversation và trả về messages
     */
    async getUserMessages(limit = 1000) {
        try {
            const response = await BaseAxios.get('/messages/user/my-messages', {
                params: { limit },
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    /**
     * Đánh dấu messages là đã đọc
     */
    async markAsRead(conversationId) {
        try {
            const response = await BaseAxios.post(`/messages/${conversationId}/mark-read`, {}, {
                withCredentials: true
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default MessageService;

