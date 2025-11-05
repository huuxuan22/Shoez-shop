<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">{{$t('Admin.Orders.title')}}</h1>
      <p class="text-gray-600 mt-2">{{$t('Admin.Orders.subtitle')}}</p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-2 md:grid-cols-6 gap-4 mb-6">
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">{{$t('Admin.Orders.stats.pending')}}</p>
            <h3 class="text-2xl font-bold text-yellow-600 mt-1">{{ statusCounts.pending }}</h3>
          </div>
          <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">{{$t('Admin.Orders.stats.confirmed')}}</p>
            <h3 class="text-2xl font-bold text-blue-600 mt-1">{{ statusCounts.confirmed }}</h3>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">{{$t('Admin.Orders.stats.shipping')}}</p>
            <h3 class="text-2xl font-bold text-purple-600 mt-1">{{ statusCounts.shipping }}</h3>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">{{$t('Admin.Orders.stats.complete')}}</p>
            <h3 class="text-2xl font-bold text-green-600 mt-1">{{ statusCounts.complete }}</h3>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">{{$t('Admin.Orders.stats.cancelled')}}</p>
            <h3 class="text-2xl font-bold text-red-600 mt-1">{{ statusCounts.cancelled }}</h3>
          </div>
          <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="bg-white rounded-lg shadow p-6 mb-6">
      <!-- Active Filters Display -->
      <div v-if="searchQuery || statusFilter || startDate || endDate" class="mb-4 pb-4 border-b border-gray-200">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="text-sm font-medium text-gray-700">{{$t('Admin.Orders.filters.activeFilters')}}</span>

          <!-- Search filter tag -->
          <span v-if="searchQuery"
            class="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
            <span>{{$t('Admin.Orders.filters.customer')}}: "{{ searchQuery }}"</span>
            <button @click="searchQuery = ''" class="hover:bg-blue-200 rounded-full p-0.5">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </button>
          </span>

          <!-- Status filter tag -->
          <span v-if="statusFilter"
            class="inline-flex items-center gap-1 px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm">
            <span>{{$t('Admin.Orders.filters.status')}}: {{ getStatusText(statusFilter) }}</span>
            <button @click="statusFilter = ''" class="hover:bg-purple-200 rounded-full p-0.5">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </button>
          </span>

          <!-- Date filter tag -->
          <span v-if="startDate || endDate"
            class="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">
            <span>
              {{ startDate ? formatDateFilter(startDate) : '...' }} → {{ endDate ? formatDateFilter(endDate) : '...' }}
            </span>
            <button @click="startDate = ''; endDate = ''" class="hover:bg-green-200 rounded-full p-0.5">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </button>
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            <svg class="inline w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            {{$t('Admin.Orders.filters.searchLabel')}}
          </label>
          <input type="text" :placeholder="$t('Admin.Orders.filters.searchPlaceholder')" v-model="searchQuery"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            <svg class="inline w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            {{$t('Admin.Orders.filters.statusLabel')}}
          </label>
          <select v-model="statusFilter"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black">
            <option value="">{{$t('Admin.Orders.filters.all')}}</option>
            <option value="pending">{{$t('Admin.Orders.filters.pending')}}</option>
            <option value="confirmed">{{$t('Admin.Orders.filters.confirmed')}}</option>
            <option value="shipping">{{$t('Admin.Orders.filters.shipping')}}</option>
            <option value="delivered">{{$t('Admin.Orders.filters.delivered')}}</option>
            <option value="complete">{{$t('Admin.Orders.filters.complete')}}</option>
            <option value="cancelled">{{$t('Admin.Orders.filters.cancelled')}}</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            <svg class="inline w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            {{$t('Admin.Orders.filters.fromDate')}}
          </label>
          <input type="date" v-model="startDate"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            <svg class="inline w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            {{$t('Admin.Orders.filters.toDate')}}
          </label>
          <input type="date" v-model="endDate"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div class="flex items-end space-x-2">
          <button @click="applyFilters"
            class="flex-1 bg-black text-white px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors font-medium">
            {{$t('Admin.Orders.filters.apply')}}
          </button>
          <button @click="clearFilters"
            class="px-4 py-2 border-2 border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 hover:border-gray-400 transition-colors">
            {{$t('Admin.Orders.filters.clear')}}
          </button>
          <button @click="exportOrders" :title="$t('Admin.Orders.filters.exportCsv')"
            class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Orders Table -->
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
      </div>

      <!-- Empty State -->
        <div v-else-if="orders.length === 0" class="flex flex-col items-center justify-center py-12">
        <svg class="w-24 h-24 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
          <h3 class="text-lg font-medium text-gray-900 mb-2">{{$t('Admin.Orders.empty.title')}}</h3>
          <p class="text-gray-500 text-center max-w-md">{{$t('Admin.Orders.empty.subtitle')}}</p>
      </div>

      <!-- Orders List -->
      <div v-else class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b border-gray-200">
            <tr>
              <th class="px-6 py-3 text-left">
                <input type="checkbox" class="rounded border-gray-300" />
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Orders.table.orderId')}}</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.customer')}}
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.phone')}}
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.date')}}
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.products')}}
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.status')}}
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{$t('Admin.Orders.table.actions')}}
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="order in orders" :key="order.id" class="hover:bg-gray-50">
              <td class="px-6 py-4">
                <input type="checkbox" class="rounded border-gray-300" />
              </td>
              <td class="px-6 py-4 text-sm font-medium text-gray-900">
                #{{ order.id.slice(-8) }}
              </td>
              <td class="px-6 py-4">
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ order?.fullName || 'N/A' }}</p>
                  <p class="text-sm text-gray-500">{{ order?.email || 'N/A' }}</p>
                </div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ order?.phone || 'N/A' }}
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ formatDate(order.created_at) }}
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">
                {{ order.products?.length || 0 }} {{$t('Admin.Orders.table.itemsSuffix')}}
              </td>
              <td class="px-6 py-4">
                <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="getStatusClass(order.status)">
                  {{ getStatusText(order.status) }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm">
                <div class="flex items-center space-x-2">
                  <button class="text-blue-600 hover:text-blue-900" @click="viewOrder(order)" :title="$t('Admin.Orders.table.view')">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>

                  <!-- Status Update Buttons -->
                  <!-- Giải thích: pending -> confirmed (Admin xác nhận) -->
                  <div class="relative inline-block text-left" v-if="order.status === 'pending'">
                    <button class="text-green-600 hover:text-green-900" @click="markAsConfirmed(order)"
                      :title="$t('Admin.Orders.table.confirm')">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </button>
                  </div>

                  <!-- Giải thích: confirmed -> shipping (Admin bắt đầu giao) -->
                  <div class="relative inline-block text-left" v-if="order.status === 'confirmed'">
                    <button class="text-blue-600 hover:text-blue-900" @click="markAsShipping(order)"
                      :title="$t('Admin.Orders.table.ship')">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0" />
                      </svg>
                    </button>
                  </div>

                  <!-- Admin có thể hoàn thành từ bất kỳ status nào (trừ complete và cancelled) -->
                  <div class="relative inline-block text-left"
                    v-if="order.status !== 'complete' && order.status !== 'cancelled'">
                    <button class="text-green-600 hover:text-green-900" @click="markAsComplete(order)"
                      :title="$t('Admin.Orders.table.complete')">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                    </button>
                  </div>

                  <button class="text-red-600 hover:text-red-900" @click="markAsCancelled(order)" :title="$t('Admin.Orders.table.cancel')"
                    v-if="order.status !== 'cancelled' && order.status !== 'complete'">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>

                  <button class="text-gray-600 hover:text-gray-900" @click="printOrder(order)" :title="$t('Admin.Orders.table.print')">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div v-if="orders.length > 0"
        class="bg-gray-50 px-6 py-4 border-t border-gray-200 flex items-center justify-between">
        <div class="text-sm text-gray-700">
          {{$t('Admin.Orders.pagination.showing')}} <span class="font-medium">{{ startIndex + 1 }}</span> {{$t('Admin.Orders.pagination.to')}}
          <span class="font-medium">{{ endIndex }}</span> {{$t('Admin.Orders.pagination.of')}}
          <span class="font-medium">{{ totalOrders }}</span> {{$t('Admin.Orders.pagination.orders')}}
        </div>
        <div class="flex items-center space-x-2">
          <button @click="prevPage" :disabled="currentPage === 1"
            class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
            {{$t('Admin.Orders.pagination.prev')}}
          </button>

          <!-- Page numbers -->
          <template v-for="page in Math.min(5, totalPages)" :key="page">
            <button @click="goToPage(page)" class="px-3 py-2 border border-gray-300 rounded-lg text-sm"
              :class="page === currentPage ? 'bg-black text-white' : 'text-gray-700 hover:bg-gray-100'">
              {{ page }}
            </button>
          </template>

          <button @click="nextPage" :disabled="currentPage === totalPages"
            class="px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed">
            {{$t('Admin.Orders.pagination.next')}}
          </button>
        </div>
      </div>
    </div>

    <!-- Order Detail Modal -->
    <OrderDetailModal :isOpen="isModalOpen" :order="selectedOrder" @close="closeModal" />

    <!-- Order Status Update Modal -->
    <OrderStatusUpdateModal :isOpen="isStatusModalOpen" :order="orderToUpdate" @close="closeStatusModal"
      @updated="handleStatusUpdate" />
  </AdminLayout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useI18n } from 'vue-i18n';
import { io } from 'socket.io-client';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import OrderService from '@/api-services/OrderService';
import OrderDetailModal from '@/components/admin/OrderDetailModal.vue';
import OrderStatusUpdateModal from '@/components/admin/OrderStatusUpdateModal.vue';
import { useToast } from '@/composables/useToast';
const { t: $t } = useI18n();

// Toast
const toast = useToast();

const orders = ref([]);
const loading = ref(true);
const totalOrders = ref(0);
const currentPage = ref(1);
const totalPages = ref(1);
const itemsPerPage = ref(20);

// Filters
const searchQuery = ref('');
const statusFilter = ref('');
const startDate = ref('');
const endDate = ref('');

// Status counts for stats cards
const statusCounts = ref({
  pending: 0,
  confirmed: 0,
  shipping: 0,
  delivered: 0,
  complete: 0,
  cancelled: 0
});

// Modal state
const selectedOrder = ref(null);
const isModalOpen = ref(false);
const isStatusModalOpen = ref(false);
const orderToUpdate = ref(null);

// Socket.IO for real-time notifications
const socket = ref(null);

// Computed properties
const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value);
const endIndex = computed(() => Math.min(startIndex.value + itemsPerPage.value, totalOrders.value));

// Fetch orders with filters
const fetchOrders = async (page = 1) => {
  try {
    loading.value = true;

    // Prepare filter parameters
    const params = {
      page: page,
      limit: itemsPerPage.value
    };

    // Add filters if they exist
    if (searchQuery.value) {
      params.valueSearch = searchQuery.value;
    }
    if (statusFilter.value) {
      params.status = statusFilter.value;
    }
    if (startDate.value) {
      params.starttime = new Date(startDate.value).toISOString();
    }
    if (endDate.value) {
      params.endtime = new Date(endDate.value + 'T23:59:59').toISOString();
    }

    const response = await OrderService.getAll(params);

    orders.value = response.orders || [];
    totalOrders.value = response.total_orders || 0;
    currentPage.value = response.current_page || 1;
    totalPages.value = response.total_pages || 1;

    // Update status counts
    updateStatusCounts();

  } catch (error) {
    orders.value = [];
    totalOrders.value = 0;
  } finally {
    loading.value = false;
  }
};

const updateStatusCounts = () => {
  const counts = {
    pending: 0,
    confirmed: 0,
    shipping: 0,
    delivered: 0,
    complete: 0,
    cancelled: 0
  };

  orders.value.forEach(order => {
    if (counts[order.status] !== undefined) {
      counts[order.status]++;
    }
  });

  statusCounts.value = counts;
};

const applyFilters = () => {
  currentPage.value = 1;
  fetchOrders(1);
};

// Pagination functions
const prevPage = () => {
  if (currentPage.value > 1) {
    fetchOrders(currentPage.value - 1);
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    fetchOrders(currentPage.value + 1);
  }
};

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    fetchOrders(page);
  }
};

// Watch for filter changes and auto-apply
watch([searchQuery, statusFilter, startDate, endDate], () => {
  // Debounce search
  if (searchQuery.value) {
    clearTimeout(searchTimeout.value);
    searchTimeout.value = setTimeout(() => {
      applyFilters();
    }, 500);
  } else {
    applyFilters();
  }
});

const searchTimeout = ref(null);

const getStatusText = (status) => {
  const statusMap = {
    'pending': $t('Admin.Orders.statusMap.pending'),
    'confirmed': $t('Admin.Orders.statusMap.confirmed'),
    'shipping': $t('Admin.Orders.statusMap.shipping'),
    'complete': $t('Admin.Orders.statusMap.complete'),
    'cancelled': $t('Admin.Orders.statusMap.cancelled')
  };
  return statusMap[status] || status;
};

const getStatusClass = (status) => {
  const classMap = {
    'pending': 'bg-yellow-100 text-yellow-800',
    'confirmed': 'bg-blue-100 text-blue-800',
    'shipping': 'bg-purple-100 text-purple-800',
    'complete': 'bg-green-100 text-green-800',
    'cancelled': 'bg-red-100 text-red-800'
  };
  return classMap[status] || 'bg-gray-100 text-gray-800';
};

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

const formatDateFilter = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  });
};

// Actions
const viewOrder = (order) => {
  selectedOrder.value = order;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedOrder.value = null;
};

const printOrder = (order) => {
  // TODO: Logic in đơn hàng
};

// Update order status
const updateOrderStatus = async (orderId, newStatus) => {
  try {
    await OrderService.updateStatus(orderId, newStatus);
    // Refresh current page
    await fetchOrders(currentPage.value);
  } catch (error) {
    toast.error('Có lỗi xảy ra khi cập nhật trạng thái đơn hàng');
  }
};

// Quick actions for status updates
const markAsConfirmed = (order) => {
  orderToUpdate.value = order;
  isStatusModalOpen.value = true;
};

const markAsShipping = (order) => {
  orderToUpdate.value = order;
  isStatusModalOpen.value = true;
};

const markAsComplete = (order) => {
  orderToUpdate.value = order;
  isStatusModalOpen.value = true;
};

const markAsCancelled = (order) => {
  orderToUpdate.value = order;
  isStatusModalOpen.value = true;
};

const closeStatusModal = () => {
  isStatusModalOpen.value = false;
  orderToUpdate.value = null;
};

const handleStatusUpdate = async (updateData) => {
  try {
    await OrderService.updateStatus(updateData.orderId, updateData.newStatus);
    // Refresh current page
    await fetchOrders(currentPage.value);
    toast.success('Cập nhật trạng thái thành công!');
  } catch (error) {
    toast.error(`Có lỗi xảy ra: ${error.response?.data?.detail || error.message}`);
  }
};

// Export orders
const exportOrders = async () => {
  try {
    // Get all orders without pagination for export
    const response = await OrderService.getAllWithoutPagination();
    const allOrders = response.orders || [];

    // Convert to CSV format
    const csvContent = convertToCSV(allOrders);
    downloadCSV(csvContent, `orders_${new Date().toISOString().split('T')[0]}.csv`);
    toast.success('Xuất đơn hàng thành công!');
  } catch (error) {
    toast.error('Có lỗi xảy ra khi xuất đơn hàng');
  }
};

const convertToCSV = (orders) => {
  const headers = ['Mã đơn', 'Khách hàng', 'Email', 'SĐT', 'Ngày đặt', 'Trạng thái', 'Số sản phẩm'];
  const rows = orders.map(order => [
    order.id.slice(-8),
    order.user_id?.full_name || '',
    order.user_id?.email || '',
    order.user_id?.numberphone || '',
    formatDate(order.created_at),
    getStatusText(order.status),
    order.products?.length || 0
  ]);

  return [headers, ...rows].map(row => row.join(',')).join('\n');
};

const downloadCSV = (content, filename) => {
  const blob = new Blob([content], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  const url = URL.createObjectURL(blob);
  link.setAttribute('href', url);
  link.setAttribute('download', filename);
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

// Clear all filters
// Giải thích: Khi clear, quay về Tất cả (không filter)
const clearFilters = () => {
  searchQuery.value = '';
  statusFilter.value = ''; // Quay về tất cả
  startDate.value = '';
  endDate.value = '';
  applyFilters();
};

// Giải thích: Connect Socket.IO để nhận notification đơn hàng mới
const connectSocket = () => {
  console.log('🔌 Connecting to notification server for admin...');

  socket.value = io('http://localhost:8000/notifications', {
    transports: ['websocket', 'polling'],
    autoConnect: true
  });

  // Khi connect thành công, join admin room
  socket.value.on('connect', () => {
    console.log('✅ Admin connected to notification server');
    socket.value.emit('join_room', { room: 'admin' });
  });

  // Nhận notification đơn hàng mới
  socket.value.on('notification', (data) => {
    console.log('📬 Admin received notification:', data);

    // Kiểm tra nếu là đơn hàng mới
    if (data.type === 'new_order') {
      // Hiển thị notification bằng toast
      toast.info(data.message, '🆕 Đơn hàng mới');

      // Reload orders tự động
      fetchOrders();
    }
  });

  // Handle disconnect
  socket.value.on('disconnect', () => {
    console.log('❌ Admin disconnected from notification server');
  });

  // Handle errors
  socket.value.on('connect_error', (error) => {
    console.error('Socket connection error:', error);
  });
};

// Disconnect socket
const disconnectSocket = () => {
  if (socket.value) {
    socket.value.disconnect();
    socket.value = null;
  }
};

onMounted(() => {
  fetchOrders();
  // Giải thích: Connect socket để nhận notifications
  connectSocket();
});

onUnmounted(() => {
  // Giải thích: Cleanup socket connection
  disconnectSocket();
});
</script>

<style scoped></style>