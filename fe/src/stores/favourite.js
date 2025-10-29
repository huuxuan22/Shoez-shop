import { defineStore } from 'pinia'
import { ref } from 'vue'
import { useNotificationStore } from './notification'
import { useAuthStore } from './auth'
import { getFavouritesApi, addFavouriteApi, removeFavouriteApi } from '@/api-services/FavouriteService'
import ProductService from '@/api-services/ProductService'

export const useFavouriteStore = defineStore('favourite', () => {
    const favourites = ref([])

    // Lấy danh sách sản phẩm yêu thích từ backend
    async function fetchFavourites(userId) {
        const auth = useAuthStore()
        if (!auth.user) {
            auth.initializeAuth()
        }
        let uid = userId || auth.user?._id || auth.user?.id
        if (!uid) {
            const userStr = localStorage.getItem('user')
            if (userStr) {
                try {
                    const u = JSON.parse(userStr)
                    uid = u?._id || u?.id
                } catch {}
            }
        }
        if (!uid) return
        const res = await getFavouritesApi(uid)
        const productIds = res?.data?.product || []
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
        if (favourites.value.find(item => item._id === product._id)) {
            useNotificationStore().notify('Sản phẩm đã có trong danh sách yêu thích!', 'error')
            return false
        }
        const uid = userId || useAuthStore().user?._id || useAuthStore().user?.id
        if (!uid) return false
        try {
            await addFavouriteApi(uid, product._id || product.id)
            // refresh from backend to ensure consistency
            await fetchFavourites(uid)
            useNotificationStore().notify('Đã thêm vào danh sách yêu thích!', 'success')
            return true
        } catch (error) {
            const msg = error?.message || error?.data?.message || 'Không thể thêm vào danh sách yêu thích'
            useNotificationStore().notify(msg, 'error')
            return false
        }
    }

    // Xóa sản phẩm khỏi danh sách yêu thích
    async function removeFavourite(productId, userId) {
        const uid = userId || useAuthStore().user?._id || useAuthStore().user?.id
        if (uid) {
            await removeFavouriteApi(uid, productId)
        }
        favourites.value = favourites.value.filter(item => (item._id || item.id) !== productId)
        // optionally refresh
        await fetchFavourites(uid)
        useNotificationStore().notify('Đã xóa khỏi danh sách yêu thích!', 'success')
    }

    return { favourites, fetchFavourites, addFavourite, removeFavourite }
})
