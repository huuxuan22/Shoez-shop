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
    }
};

export default ConversationService;

