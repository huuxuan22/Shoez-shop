import { defineStore } from 'pinia';
import ConversationService from '@/api-services/ConversationService';

export const useConversationStore = defineStore('conversation', {
    state: () => ({
        userChatList: [],
        loading: false,
        error: null
    }),

    getters: {
        /**
         * Lấy danh sách users đã chat
         */
        users: (state) => state.userChatList,

        /**
         * Lấy tổng số unread messages
         */
        totalUnread: (state) => {
            return state.userChatList.reduce((total, user) => total + (user.unread || 0), 0);
        }
    },

    actions: {
        /**
         * Lấy danh sách users đã nhắn tin với admin
         */
        async fetchUsersChattingWithAdmin() {
            this.loading = true;
            this.error = null;
            try {
                const users = await ConversationService.getUsersChattingWithAdmin();
                // Map data để phù hợp với format của component
                this.userChatList = users.map(user => ({
                    id: user.userId || user.id,
                    conversationId: user.conversationId || user.id,
                    name: user.name || 'Unknown',
                    avatar: user.avatar || '',
                    unread: user.unread || 0,
                    lastMessage: user.lastMessage || '',
                    lastMessageTime: user.lastMessageTime || null
                }));
                console.log('✅ Loaded conversation users:', this.userChatList.length);
            } catch (error) {
                console.error('Error fetching conversation users:', error);
                this.error = error.message || 'Failed to load conversation users';
                this.userChatList = [];
            } finally {
                this.loading = false;
            }
        },

        /**
         * Reset unread count cho một user
         */
        resetUnread(userId) {
            const user = this.userChatList.find(u => u.id === userId);
            if (user) {
                user.unread = 0;
            }
        },

        /**
         * Clear store
         */
        clear() {
            this.userChatList = [];
            this.error = null;
        }
    }
});

