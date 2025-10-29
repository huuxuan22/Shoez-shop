import { defineStore } from 'pinia'
import { ref } from 'vue'
import FavouriteService from '@/api-services/FavouriteService'
import ProductService from '@/api-services/ProductService'
import { useAuthStore } from '@/stores/auth'
import { useNotificationStore } from '@/stores/notification'

export const useFavouriteStore = defineStore('favourite', () => {
    const favourites = ref([])

    // Lấy danh sách sản phẩm yêu thích từ backend
    async function fetchFavourites(userId) {
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
        if (!uid) return
        const res = await FavouriteService.getFavourite(uid)
        const productIds = res?.product || []
        // Fetch product details in parallel
        if (productIds.length === 0) {
            favourites.value = []
            return
        }
        const details = await Promise.allSettled(
            productIds.map((pid) => ProductService.getById(pid))
        )
        favourites.value = details
            .filter(d => d.status === 'fulfilled')
            .map(d => d.value)
    }

    // Thêm sản phẩm vào danh sách yêu thích
    async function addFavourite(product, userId) {
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
        const isAlreadyFavourited = favourites.value.some(item => 
            (item._id || item.id) === productId
        )
        
        if (isAlreadyFavourited) {
            useNotificationStore().notify({ type: 'info', message: 'Sản phẩm đã có trong danh sách yêu thích!' })
            return false
        }
        
        try {
            const res = await FavouriteService.addFavourite(uid, productId)
            console.log('[Favourite] addFavourite FE - Kết quả trả về từ backend:', res)
            console.log('[Favourite] Số sản phẩm trước khi thêm:', favourites.value.length)
            
            // Fetch lại danh sách từ backend để đảm bảo đồng bộ
            await fetchFavourites(uid)
            console.log('[Favourite] Số sản phẩm sau khi thêm:', favourites.value.length)
            
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
    }

    // Xóa sản phẩm khỏi danh sách yêu thích
    async function removeFavourite(productId, userId) {
        const auth = useAuthStore()
        let uid = userId || auth.user?._id || auth.user?.id
        if (!uid) return
        try {
            await FavouriteService.removeFavourite(uid, productId)
            favourites.value = favourites.value.filter(item => (item._id || item.id) !== productId)
            // optionally refresh
            await fetchFavourites(uid)
            useNotificationStore().notify({ type: 'success', message: 'Đã xóa khỏi danh sách yêu thích!' })
        } catch (error) {
            const msg = error?.message || error?.data?.message || 'Không thể xóa khỏi danh sách yêu thích'
            useNotificationStore().notify({ type: 'error', message: msg })
        }
    }

    return { favourites, fetchFavourites, addFavourite, removeFavourite }
})
