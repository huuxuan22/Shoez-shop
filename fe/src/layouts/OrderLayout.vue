<template>
    <Header />
    <div class="min-h-screen bg-gray-50 py-8">
        <div class="container mx-auto px-4">
            <!-- Header -->
            <OrdersHeader :total-orders="filteredOrders.length" :active-filter="activeFilter"
                @filter-change="handleFilterChange" />

            <!-- Loading State -->
            <OrdersLoading v-if="loading" />

            <!-- Empty State -->
            <OrdersEmpty v-else-if="!loading && filteredOrders.length === 0" :filter="activeFilter"
                @reset-filter="resetFilter" />

            <!-- Orders List -->
            <div v-else class="space-y-6">
                <OrderCard v-for="order in paginatedOrders" :key="order.id || order._id" :order="order"
                    @view-detail="viewOrderDetail" @cancel-order="cancelOrder" @reorder="handleReorder" />
            </div>

            <!-- Pagination -->
            <OrdersPagination v-if="totalPages > 1" :current-page="currentPage" :total-pages="totalPages"
                @page-change="handlePageChange" />
        </div>
    </div>
    <Footer />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useOrderStore } from '@/stores/order'
import { useToast } from '@/composables/useToast'
import OrdersHeader from '@/components/orders/OrdersHeader.vue'
import OrdersLoading from '@/components/orders/OrdersLoading.vue'
import OrdersEmpty from '@/components/orders/OrdersEmpty.vue'
import OrderCard from '@/components/orders/OrderCard.vue'
import OrdersPagination from '@/components/orders/OrdersPagination.vue'
import Footer from '@/templates/Footer.vue'
import Header from '@/templates/Header.vue'

const router = useRouter()
const orderStore = useOrderStore()
const toast = useToast()

// Reactive data
const loading = ref(true)
const activeFilter = ref('all')
const currentPage = ref(1)
const itemsPerPage = 5

// Computed properties
const orders = computed(() => orderStore.orders || [])

const filteredOrders = computed(() => {
    if (activeFilter.value === 'all') {
        return orders.value
    }
    return orders.value.filter(order => order.status === activeFilter.value)
})

const paginatedOrders = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return filteredOrders.value.slice(start, end)
})

const totalPages = computed(() => {
    return Math.ceil(filteredOrders.value.length / itemsPerPage)
})

// Methods
const fetchOrders = async () => {
    loading.value = true
    try {
        await orderStore.loadOrders()
    } catch (error) {
        console.error('Error loading orders:', error)
    } finally {
        loading.value = false
    }
}

const handleFilterChange = (filter) => {
    activeFilter.value = filter
    currentPage.value = 1
}

const resetFilter = () => {
    activeFilter.value = 'all'
}

const handlePageChange = (page) => {
    currentPage.value = page
    window.scrollTo({ top: 0, behavior: 'smooth' })
}

const viewOrderDetail = (orderId) => {
    router.push(`/orders/${orderId}`)
}

const cancelOrder = async (orderId) => {
    const order = orders.value.find(o => (o.id || o._id) === orderId)

    // CHỈ cho phép hủy khi order đang "pending" (chưa admin xác nhận)
    if (order && order.status !== 'pending') {
        toast.warning('Không thể hủy đơn hàng này. Đơn hàng đã được xác nhận bởi admin. Vui lòng liên hệ admin để hủy.')
        return
    }

    if (confirm('Bạn có chắc chắn muốn hủy đơn hàng này?')) {
        try {
            // Update order status
            await orderStore.updateOrderStatus(orderId, 'cancelled')
            // Reload orders
            await fetchOrders()
            toast.success('Đơn hàng đã được hủy thành công!')
        } catch (error) {
            console.error('Error cancelling order:', error)
            toast.error('Không thể hủy đơn hàng')
        }
    }
}

const handleReorder = (orderId) => {
    const order = orders.value.find(order => order.id === orderId || order._id === orderId)
    if (order && order.items) {
        toast.success('Sản phẩm đã được thêm vào giỏ hàng!')
    }
}

// Lifecycle
onMounted(() => {
    fetchOrders()
})
</script>