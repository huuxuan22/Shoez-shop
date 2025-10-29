import { ref } from 'vue'

const toasts = ref([])

/**
 * Toast Composable
 * Giải thích: Quản lý toast notifications trong toàn bộ app
 * 
 * Types: 'success', 'error', 'info', 'warning'
 */
export function useToast() {
    /**
     * Show toast notification
     * @param {Object} config - Toast configuration
     * @param {string} config.message - Toast message
     * @param {string} config.type - Toast type (success, error, info, warning)
     * @param {string} config.title - Optional title
     * @param {number} config.duration - Duration in ms (default: 3000)
     */
    const showToast = (config) => {
        const toast = {
            id: Date.now(),
            message: config.message || '',
            type: config.type || 'info',
            title: config.title || getDefaultTitle(config.type),
            duration: config.duration || 3000
        }

        toasts.value.push(toast)

        // Auto dismiss
        setTimeout(() => {
            removeToast(toast.id)
        }, toast.duration)

        return toast
    }

    /**
     * Helper functions
     */
    const success = (message, title) => showToast({ message, type: 'success', title })
    const error = (message, title) => showToast({ message, type: 'error', title })
    const info = (message, title) => showToast({ message, type: 'info', title })
    const warning = (message, title) => showToast({ message, type: 'warning', title })

    /**
     * Remove toast
     */
    const removeToast = (id) => {
        const index = toasts.value.findIndex(t => t.id === id)
        if (index > -1) {
            toasts.value.splice(index, 1)
        }
    }

    /**
     * Get default title based on type
     */
    const getDefaultTitle = (type) => {
        const titles = {
            success: 'Thành công',
            error: 'Lỗi',
            info: 'Thông báo',
            warning: 'Cảnh báo'
        }
        return titles[type] || 'Thông báo'
    }

    return {
        toasts,
        showToast,
        success,
        error,
        info,
        warning,
        removeToast
    }
}

