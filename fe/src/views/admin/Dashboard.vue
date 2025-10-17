<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
      <p class="text-gray-600 mt-2">Tổng quan về hệ thống</p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total Revenue -->
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 mb-1">Doanh thu</p>
            <h3 class="text-2xl font-bold text-gray-900">$45,231</h3>
            <p class="text-sm text-green-600 mt-2">+12.5% từ tháng trước</p>
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
            <h3 class="text-2xl font-bold text-gray-900">1,234</h3>
            <p class="text-sm text-blue-600 mt-2">+8.2% từ tháng trước</p>
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
            <h3 class="text-2xl font-bold text-gray-900">456</h3>
            <p class="text-sm text-purple-600 mt-2">32 sản phẩm mới</p>
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
            <h3 class="text-2xl font-bold text-gray-900">8,234</h3>
            <p class="text-sm text-orange-600 mt-2">+15.3% từ tháng trước</p>
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
        <div class="h-64 flex items-end justify-between space-x-2">
          <div class="flex-1 bg-black rounded-t" style="height: 70%"></div>
          <div class="flex-1 bg-black rounded-t" style="height: 85%"></div>
          <div class="flex-1 bg-black rounded-t" style="height: 60%"></div>
          <div class="flex-1 bg-black rounded-t" style="height: 75%"></div>
          <div class="flex-1 bg-black rounded-t" style="height: 90%"></div>
          <div class="flex-1 bg-black rounded-t" style="height: 65%"></div>
          <div class="flex-1 bg-gray-300 rounded-t" style="height: 50%"></div>
        </div>
        <div class="flex justify-between mt-4 text-xs text-gray-600">
          <span>CN</span>
          <span>T2</span>
          <span>T3</span>
          <span>T4</span>
          <span>T5</span>
          <span>T6</span>
          <span>T7</span>
        </div>
      </div>

      <!-- Top Products -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Sản phẩm bán chạy</h3>
        <div class="space-y-4">
          <div v-for="product in topProducts" :key="product.id" class="flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <div class="w-12 h-12 bg-gray-200 rounded"></div>
              <div>
                <p class="font-medium text-gray-900">{{ product.name }}</p>
                <p class="text-sm text-gray-500">{{ product.sold }} đã bán</p>
              </div>
            </div>
            <span class="font-semibold text-gray-900">${{ product.price }}</span>
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
            <tr v-for="order in recentOrders" :key="order.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                #{{ order.id }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ order.customer }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ order.date }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                ${{ order.total }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': order.status === 'Hoàn thành',
                    'bg-yellow-100 text-yellow-800': order.status === 'Đang xử lý',
                    'bg-blue-100 text-blue-800': order.status === 'Đang giao',
                    'bg-red-100 text-red-800': order.status === 'Đã hủy'
                  }"
                >
                  {{ order.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <button class="text-blue-600 hover:text-blue-900 mr-3">Xem</button>
                <button class="text-gray-600 hover:text-gray-900">Sửa</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';

const topProducts = ref([
  { id: 1, name: 'Nike Air Max 270', sold: 234, price: 150 },
  { id: 2, name: 'Adidas Ultraboost', sold: 189, price: 180 },
  { id: 3, name: 'Puma RS-X', sold: 156, price: 120 },
  { id: 4, name: 'New Balance 574', sold: 142, price: 90 },
]);

const recentOrders = ref([
  { id: '10234', customer: 'Nguyễn Văn A', date: '17/10/2025', total: 299, status: 'Hoàn thành' },
  { id: '10233', customer: 'Trần Thị B', date: '17/10/2025', total: 450, status: 'Đang giao' },
  { id: '10232', customer: 'Lê Văn C', date: '16/10/2025', total: 180, status: 'Đang xử lý' },
  { id: '10231', customer: 'Phạm Thị D', date: '16/10/2025', total: 320, status: 'Hoàn thành' },
  { id: '10230', customer: 'Hoàng Văn E', date: '15/10/2025', total: 550, status: 'Đã hủy' },
]);
</script>

<style scoped>
</style>
