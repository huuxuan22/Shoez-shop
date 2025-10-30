import { defineStore } from 'pinia'
import FavouriteService from '@/api-services/FavouriteService'
import ProductService from '@/api-services/ProductService'
import { useAuthStore } from '@/stores/auth'
import { useNotificationStore } from '@/stores/notification'

// Helper functions for localStorage persistence
const loadFavourites = () => {
    try {
        const stored = localStorage.getItem('favourites')
        return stored ? JSON.parse(stored) : []
    } catch {
        return []
    }
}

const saveFavourites = (favourites) => {
    try {
        localStorage.setItem('favourites', JSON.stringify(favourites))
    } catch (error) {
        console.error('[Favourite] Error saving to localStorage:', error)
    }
}

export const useFavouriteStore = defineStore('favourite', {
    state: () => ({
        favourites: loadFavourites()
    }),

    getters: {
        count: (state) => state.favourites.length
    },

    actions: {

        // Lấy danh sách sản phẩm yêu thích từ backend
        async fetchFavourites(userId) {
            const auth = useAuthStore()
            if (!auth.user) {
                await auth.initializeAuth()
            }
            let uid = userId || auth.user?._id || auth.user?.id
            if (!uid) {
                const userStr = localStorage.getItem('user')
                if (userStr) {
                    try {
                        const u = JSON.parse(userStr)
                        uid = u?._id || u?.id
                    } catch { }
                }
            }
            if (!uid) {
                console.log('[Favourite] No user ID found, skipping fetch')
                return
            }

            try {
                const res = await FavouriteService.getFavourite(uid)
                const productIds = res?.product || []
                // Fetch product details in parallel
                if (productIds.length === 0) {
                    this.favourites = []
                    return
                }
                const details = await Promise.allSettled(
                    productIds.map((pid) => ProductService.getById(pid))
                )
                this.favourites = details
                    .filter(d => d.status === 'fulfilled')
                    .map(d => d.value)

                // Save to localStorage after fetching
                saveFavourites(this.favourites)

                console.log('[Favourite] Fetched favourites:', this.favourites.length)
            } catch (error) {
                console.error('[Favourite] Error fetching favourites:', error)
                // Keep existing favourites on error
            }
        },

        // Thêm sản phẩm vào danh sách yêu thích
        async addFavourite(product, userId) {
            console.log('[Favourite] addFavourite FE - product:', product)
            console.log('[Favourite] addFavourite FE - product_id gửi lên:', product._id || product.id)

            const auth = useAuthStore()
            let uid = userId || auth.user?._id || auth.user?.id
            if (!uid) {
                useNotificationStore().notify({ type: 'error', message: 'Chưa đăng nhập!' })
                return false
            }

            // Check nếu đã có trong danh sách hiện tại để hiển thị thông báo
            const productId = product._id || product.id
            const isAlreadyFavourited = this.favourites.some(item =>
                (item._id || item.id) === productId
            )

            if (isAlreadyFavourited) {
                useNotificationStore().notify({ type: 'info', message: 'Sản phẩm đã có trong danh sách yêu thích!' })
                return false
            }

            try {
                const res = await FavouriteService.addFavourite(uid, productId)
                console.log('[Favourite] addFavourite FE - Kết quả trả về từ backend:', res)
                console.log('[Favourite] Số sản phẩm trước khi thêm:', this.favourites.length)

                // Fetch lại danh sách từ backend để đảm bảo đồng bộ
                await this.fetchFavourites(uid)
                console.log('[Favourite] Số sản phẩm sau khi thêm:', this.favourites.length)

                // Save to localStorage
                saveFavourites(this.favourites)

                useNotificationStore().notify({ type: 'success', message: 'Đã thêm vào danh sách yêu thích!' })
                return true
            } catch (error) {
                console.error('[Favourite] Error adding favourite:', error)
                const msg = error?.response?.data?.detail || error?.message || 'Không thể thêm vào danh sách yêu thích'

                // Nếu backend trả về lỗi "đã có", hiển thị thông báo khác
                if (msg.includes('đã có trong danh sách')) {
                    useNotificationStore().notify({ type: 'info', message: msg })
                } else {
                    useNotificationStore().notify({ type: 'error', message: msg })
                }
                return false
            }
        },

        // Xóa sản phẩm khỏi danh sách yêu thích
        async removeFavourite(productId, userId) {
            const auth = useAuthStore()
            let uid = userId || auth.user?._id || auth.user?.id
            if (!uid) return
            try {
                await FavouriteService.removeFavourite(uid, productId)
                this.favourites = this.favourites.filter(item => (item._id || item.id) !== productId)

                // Save to localStorage after removal
                saveFavourites(this.favourites)

                // optionally refresh
                await this.fetchFavourites(uid)
                useNotificationStore().notify({ type: 'success', message: 'Đã xóa khỏi danh sách yêu thích!' })
            } catch (error) {
                const msg = error?.message || error?.data?.message || 'Không thể xóa khỏi danh sách yêu thích'
                useNotificationStore().notify({ type: 'error', message: msg })
            }
        }
    }
})
