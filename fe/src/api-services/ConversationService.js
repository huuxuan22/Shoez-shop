// Conversation Service
import BaseAxios from "./BaseAxios";

const ConversationService = {
    /**
     * Lấy danh sách users đã nhắn tin với admin
     */
    async getUsersChattingWithAdmin() {
        try {
            const response = await BaseAxios.get('/conversations/users', {
                withCredentials: true
            });
            return response.data.users || [];
        } catch (error) {
            throw error;
        }
    },

    /**
     * Tìm kiếm users theo email hoặc số điện thoại
     */
    async searchUsers(query) {
        try {
            if (!query || query.trim().length < 2) {
                return [];
            }
            const response = await BaseAxios.get('/conversations/search-users', {
                params: { q: query.trim() },
                withCredentials: true
            });
            return response.data.users || [];
        } catch (error) {
            console.error('Error searching users:', error);
            throw error;
        }
    }
};

export default ConversationService;

