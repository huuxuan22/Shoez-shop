<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
      <p class="text-gray-600 mt-2">Tổng quan về hệ thống</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
      <p class="text-red-800">{{ error }}</p>
      <button @click="fetchData" class="mt-2 text-red-600 hover:text-red-800 underline">
        Thử lại
      </button>
    </div>

    <!-- Content -->
    <div v-else>
    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total Revenue -->
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Doanh thu</p>
              <h3 class="text-2xl font-bold text-gray-900">
                {{ formatCurrency(overview.total_revenue) }}
              </h3>
              <p
                class="text-sm mt-2"
                :class="overview.revenue_change >= 0 ? 'text-green-600' : 'text-red-600'"
              >
                {{ overview.revenue_change >= 0 ? '+' : '' }}{{ overview.revenue_change }}% từ tháng trước
              </p>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Total Orders -->
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Đơn hàng</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_orders) }}</h3>
              <p
                class="text-sm mt-2"
                :class="overview.orders_change >= 0 ? 'text-blue-600' : 'text-red-600'"
              >
                {{ overview.orders_change >= 0 ? '+' : '' }}{{ overview.orders_change }}% từ tháng trước
              </p>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Total Products -->
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Sản phẩm</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_products) }}</h3>
              <p class="text-sm text-purple-600 mt-2">Đang hoạt động</p>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Total Customers -->
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Khách hàng</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_customers) }}</h3>
              <p class="text-sm text-orange-600 mt-2">Người dùng đã đăng ký</p>
          </div>
          <div class="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Charts Row -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      <!-- Sales Chart -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Doanh thu 7 ngày qua</h3>
          <div v-if="chartData.length === 0" class="h-64 flex items-center justify-center text-gray-500">
            Chưa có dữ liệu
          </div>
          <div v-else class="h-64 overflow-hidden">
            <div class="h-full w-full flex items-end" style="gap: 2px;">
              <div
                v-for="(day, index) in chartData"
                :key="index"
                class="flex-1 flex flex-col items-center"
              >
              <div
                class="w-full bg-gradient-to-t from-blue-600 to-blue-400 rounded-t transition-all duration-300 hover:from-blue-700 hover:to-blue-500"
                :style="{ height: `${getChartHeight(day.revenue)}%`, minHeight: '4px' }"
                :title="`${day.day_name}: ${formatCurrency(day.revenue)}`"
              ></div>
              <span class="text-xs text-gray-500 mt-1">{{ getDayLabel(day.day_name) }}</span>
              </div>
            </div>
          </div>
          <div class="flex justify-between mt-4 text-xs text-gray-600" v-if="chartData.length > 0">
            <span v-for="(day, index) in chartData" :key="index">{{ getDayLabel(day.day_name) }}</span>
          </div>
          <div class="mt-4 pt-4 border-t border-gray-200" v-if="chartData.length > 0">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">Tổng doanh thu:</span>
              <span class="font-semibold text-gray-900">
                {{ formatCurrency(getTotalRevenue(chartData)) }}
              </span>
            </div>
        </div>
      </div>

      <!-- Top Products -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Sản phẩm bán chạy</h3>
        <div class="space-y-4">
            <div v-if="topProducts.length === 0" class="text-center text-gray-500 py-8">
              Chưa có dữ liệu
            </div>
            <div v-for="(product, index) in topProducts" :key="product.product_id || index" 
              class="flex items-center justify-between">
              <div class="flex items-center space-x-3 flex-1">
                <div class="w-10 h-10 bg-gray-200 rounded flex items-center justify-center text-gray-600 font-bold">
                  {{ index + 1 }}
                </div>
                <div class="flex-1 min-w-0">
                  <p class="font-medium text-gray-900 truncate">{{ product.name }}</p>
                  <p class="text-sm text-gray-500">{{ formatNumber(product.sold) }} đã bán</p>
                </div>
              </div>
              <div class="text-right">
                <span class="font-semibold text-gray-900">{{ formatCurrency(product.revenue) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Orders -->
    <div class="bg-white rounded-lg shadow">
      <div class="p-6 border-b border-gray-200">
        <h3 class="text-lg font-semibold text-gray-900">Đơn hàng gần đây</h3>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b border-gray-200">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Mã đơn
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Khách hàng
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Ngày
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Tổng tiền
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Trạng thái
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Hành động
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
              <tr v-if="recentOrders.length === 0">
                <td colspan="6" class="px-6 py-8 text-center text-gray-500">
                  Chưa có đơn hàng
                </td>
              </tr>
            <tr v-for="order in recentOrders" :key="order.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  #{{ order.id.slice(-6) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ order.customer }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(order.date) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  {{ formatCurrency(order.total) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                    :class="getStatusBadgeClass(order.status)"
                  >
                    {{ getStatusLabel(order.status) }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <router-link :to="`/admin/orders`" class="text-blue-600 hover:text-blue-900 mr-3">
                    Xem
                  </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import StatisticsService from '@/api-services/StatisticsService';

const router = useRouter();

// State
const loading = ref(true);
const error = ref(null);
const overview = ref({
  total_revenue: 0,
  total_orders: 0,
  total_products: 0,
  total_customers: 0,
  monthly_revenue: 0,
  monthly_orders: 0,
  revenue_change: 0,
  orders_change: 0,
  status_counts: {}
});
const chartData = ref([]);
const topProducts = ref([]);
const recentOrders = ref([]);

// Fetch all data - chỉ lấy dữ liệu tổng quan
const fetchData = async () => {
  try {
    loading.value = true;
    error.value = null;

    // Chỉ fetch dữ liệu tổng quan cần thiết
    const [overviewData, chartDataRes, topProductsRes, recentOrdersRes] = await Promise.all([
      StatisticsService.getOverview(),
      StatisticsService.getRevenueChart(7),
      StatisticsService.getTopProducts(5),
      StatisticsService.getRecentOrders(5)
    ]);

    overview.value = overviewData;
    chartData.value = chartDataRes;
    topProducts.value = topProductsRes;
    recentOrders.value = recentOrdersRes;
  } catch (err) {
    error.value = err.response?.data?.detail || err.message || 'Không thể tải dữ liệu dashboard';
  } finally {
    loading.value = false;
  }
};

// Helper functions
const formatCurrency = (amount) => {
  return new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND'
  }).format(amount || 0);
};

const formatNumber = (num) => {
  return new Intl.NumberFormat('vi-VN').format(num || 0);
};

const formatDate = (dateStr) => {
  if (!dateStr) return '';
  const date = new Date(dateStr);
  return date.toLocaleDateString('vi-VN');
};

const getDayLabel = (dayName) => {
  if (dayName.includes('Thứ') || dayName === 'Chủ Nhật') {
    if (dayName === 'Chủ Nhật') return 'CN';
    const numMap = {
      'Thứ Hai': 'T2',
      'Thứ Ba': 'T3',
      'Thứ Tư': 'T4',
      'Thứ Năm': 'T5',
      'Thứ Sáu': 'T6',
      'Thứ Bảy': 'T7'
    };
    return numMap[dayName] || dayName;
  }
  const days = {
    'Monday': 'T2',
    'Tuesday': 'T3',
    'Wednesday': 'T4',
    'Thursday': 'T5',
    'Friday': 'T6',
    'Saturday': 'T7',
    'Sunday': 'CN'
  };
  return days[dayName] || dayName;
};

const getChartHeight = (revenue) => {
  if (chartData.value.length === 0) return 0;
  const maxRevenue = Math.max(...chartData.value.map(d => d.revenue));
  if (maxRevenue === 0) return 0;
  return (revenue / maxRevenue) * 100;
};

// No scrolling helpers (restored to classic layout)

const getTotalRevenue = (data) => {
  return data.reduce((sum, day) => sum + day.revenue, 0);
};

const getStatusLabel = (status) => {
  const labels = {
    'pending': 'Chờ xử lý',
    'confirmed': 'Đã xác nhận',
    'shipping': 'Đang giao',
    'complete': 'Hoàn thành',
    'completed': 'Hoàn thành',
    'delivered': 'Đã giao',
    'cancelled': 'Đã hủy',
    'canceled': 'Đã hủy'
  };
  return labels[status] || status;
};

const getStatusBadgeClass = (status) => {
  const classes = {
    'pending': 'bg-yellow-100 text-yellow-800',
    'confirmed': 'bg-blue-100 text-blue-800',
    'shipping': 'bg-purple-100 text-purple-800',
    'complete': 'bg-green-100 text-green-800',
    'completed': 'bg-green-100 text-green-800',
    'delivered': 'bg-green-100 text-green-800',
    'cancelled': 'bg-red-100 text-red-800',
    'canceled': 'bg-red-100 text-red-800'
  };
  return classes[status] || 'bg-gray-100 text-gray-800';
};

// Lifecycle
onMounted(() => {
  fetchData();
});
</script>

<style scoped>
</style>
