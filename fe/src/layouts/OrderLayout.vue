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
                <OrderCard v-for="order in paginatedOrders" :key="order.id" :order="order"
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
import OrdersHeader from '@/components/orders/OrdersHeader.vue'
import OrdersLoading from '@/components/orders/OrdersLoading.vue'
import OrdersEmpty from '@/components/orders/OrdersEmpty.vue'
import OrderCard from '@/components/orders/OrderCard.vue'
import OrdersPagination from '@/components/orders/OrdersPagination.vue'
import Footer from '@/templates/Footer.vue'
import Header from '@/templates/Header.vue'

const router = useRouter()

// Reactive data
const loading = ref(true)
const orders = ref([])
const activeFilter = ref('all')
const currentPage = ref(1)
const itemsPerPage = 5

// Mock data - trong thực tế sẽ lấy từ API
const mockOrders = [
    {
        id: 'ORD-001',
        orderNumber: 'ORD-2024-001',
        createdAt: new Date('2024-01-15'),
        status: 'delivered',
        items: [
            { id: 1, name: 'Nike Air Force 1', price: 2200000, quantity: 1, image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' },
            { id: 2, name: 'Nike Socks', price: 150000, quantity: 2, image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' }
        ],
        totalAmount: 2500000,
        shippingAddress: {
            name: 'Nguyễn Văn A',
            phone: '0123456789',
            address: '123 Đường ABC, Quận 1, TP.HCM'
        },
        paymentMethod: 'credit_card',
        trackingNumber: 'TRK123456789'
    },
    {
        id: 'ORD-002',
        orderNumber: 'ORD-2024-002',
        createdAt: new Date('2024-01-10'),
        status: 'shipped',
        items: [
            { id: 3, name: 'Adidas Ultraboost', price: 4500000, quantity: 1, image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' }
        ],
        totalAmount: 4500000,
        shippingAddress: {
            name: 'Nguyễn Văn A',
            phone: '0123456789',
            address: '123 Đường ABC, Quận 1, TP.HCM'
        },
        paymentMethod: 'cod',
        trackingNumber: 'TRK987654321'
    },
    {
        id: 'ORD-003',
        orderNumber: 'ORD-2024-003',
        createdAt: new Date('2024-01-05'),
        status: 'pending',
        items: [
            { id: 4, name: 'Converse Chuck Taylor', price: 1500000, quantity: 1, image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60' }
        ],
        totalAmount: 1500000,
        shippingAddress: {
            name: 'Nguyễn Văn A',
            phone: '0123456789',
            address: '123 Đường ABC, Quận 1, TP.HCM'
        },
        paymentMethod: 'credit_card'
    },
    {
        id: 'ORD-004',
        orderNumber: 'ORD-2024-004',
        createdAt: new Date('2024-01-01'),
        status: 'cancelled',
        items: [
            { id: 5, name: 'Puma RS-X', price: 2800000, quantity: 1, image: 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80' }
        ],
        totalAmount: 2800000,
        shippingAddress: {
            name: 'Nguyễn Văn A',
            phone: '0123456789',
            address: '123 Đường ABC, Quận 1, TP.HCM'
        },
        paymentMethod: 'credit_card'
    }
]

// Computed properties
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
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        orders.value = mockOrders
    } catch (error) {
        console.error('Error fetching orders:', error)
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
    if (confirm('Bạn có chắc chắn muốn hủy đơn hàng này?')) {
        try {
            // Call API to cancel order
            console.log('Cancelling order:', orderId)
            // Update local state
            const order = orders.value.find(o => o.id === orderId)
            if (order) {
                order.status = 'cancelled'
            }
        } catch (error) {
            console.error('Error cancelling order:', error)
        }
    }
}

const handleReorder = (orderId) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order) {
        // Add items to cart
        console.log('Reordering:', order.items)
        alert('Sản phẩm đã được thêm vào giỏ hàng!')
    }
}

// Lifecycle
onMounted(() => {
    fetchOrders()
})
</script>