import { defineStore } from 'pinia';
import { io } from 'socket.io-client';
import NotificationService from '@/api-services/NotificationService';

export const useNotificationStore = defineStore('notification', {
    state: () => ({
        notifications: [],
        unreadCount: 0,
        socket: null,
        isConnected: false,
        loading: false
    }),

    getters: {
        /**
         * Lấy unread notifications
         */
        unreadNotifications: (state) => {
            return state.notifications.filter(notification => !notification.is_read);
        },

        /**
         * Lấy notifications chưa đọc mới nhất
         */
        latestUnread: (state) => {
            const unread = state.notifications
                .filter(notification => !notification.is_read)
                .sort((notification1, notification2) => new Date(notification2.timestamp) - new Date(notification1.timestamp));
            return unread[0] || null;
        }
    },

    actions: {
        async connect(userId) {
            if (!userId) return;

            // 1. Load notifications từ database trước khi connect WebSocket
            try {
                await this.loadNotificationsFromDB();
            } catch (error) {
                console.error('Error loading notifications from DB:', error);
            }

            // 2. Connect WebSocket
            if (this.socket) {
                this.disconnect();
            }

            this.socket = io('http://localhost:8000/notifications', {
                transports: ['websocket', 'polling'],
                autoConnect: true
            });

            // Khi connect thành công
            this.socket.on('connect', () => {
                console.log('✅ Connected to notification server');
                this.isConnected = true;
                this.socket.emit('join_user_room', { user_id: userId });
            });

            // Nhận notification từ server
            this.socket.on('notification', (data) => {
                console.log('📬 Received notification:', data);
                this.addNotification(data);
            });

            // Handle disconnect
            this.socket.on('disconnect', () => {
                console.log('❌ Disconnected from notification server');
                this.isConnected = false;
            });

            // Handle errors
            this.socket.on('connect_error', (error) => {
                console.error('Socket connection error:', error);
                this.isConnected = false;
            });
        },

        async loadNotificationsFromDB() {
            try {
                const notifications = await NotificationService.getAll();
                this.notifications = notifications || [];
                this.updateUnreadCount();
                console.log('✅ Loaded notifications from DB:', this.notifications.length);
            } catch (error) {
                console.error('Error loading notifications:', error);
            }
        },

        disconnect() {
            if (this.socket) {
                this.socket.disconnect();
                this.socket = null;
                this.isConnected = false;
            }
        },

        /**
         * Thêm notification mới
         */
        addNotification(notification) {
            const newNotification = {
                ...notification,
                id: notification.id || notification._id || Date.now(),
                is_read: notification.is_read || false,
                timestamp: notification.timestamp || notification.created_at || new Date().toISOString()
            };

            this.notifications.unshift(newNotification);
            this.updateUnreadCount();

            return newNotification;
        },

        /**
         * Đánh dấu notification là đã đọc (Sync với backend)
         */
        async markAsRead(notificationId) {
            // 1. Update trong store
            const notification = this.notifications.find(n => n.id === notificationId || n._id === notificationId);
            if (notification) {
                notification.is_read = true;
                this.updateUnreadCount();
            }

            // 2. Sync với backend
            try {
                await NotificationService.markAsRead(notificationId);
            } catch (error) {
                console.error('Error marking notification as read:', error);
            }
        },

        /**
         * Đánh dấu tất cả là đã đọc (Sync với backend)
         */
        async markAllAsRead() {
            // 1. Update trong store
            this.notifications.forEach(n => n.is_read = true);
            this.updateUnreadCount();

            // 2. Sync với backend
            try {
                await NotificationService.markAllAsRead();
                console.log('✅ Marked all notifications as read');
            } catch (error) {
                console.error('Error marking all as read:', error);
            }
        },

        /**
         * Cập nhật unread count
         */
        updateUnreadCount() {
            this.unreadCount = this.unreadNotifications.length;
        },

        /**
         * Xóa notification (Sync với backend)
         */
        async removeNotification(notificationId) {
            // 1. Xóa trong store
            const index = this.notifications.findIndex(n => n.id === notificationId || n._id === notificationId);
            if (index > -1) {
                this.notifications.splice(index, 1);
                this.updateUnreadCount();
            }

            // 2. Sync với backend
            try {
                await NotificationService.delete(notificationId);
            } catch (error) {
                console.error('Error deleting notification:', error);
            }
        },

        clearNotifications() {
            this.notifications = [];
            this.unreadCount = 0;
        }
    }
});

