<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">{{$t('Admin.Analytics.title')}}</h1>
      <p class="text-gray-600 mt-2">{{$t('Admin.Analytics.subtitle')}}</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
      <p class="text-red-800">{{ error }}</p>
      <button @click="fetchData" class="mt-2 text-red-600 hover:text-red-800 underline">
        {{$t('Admin.Analytics.retry')}}
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
              <p class="text-sm text-gray-600 mb-1">{{$t('Admin.Analytics.cards.totalRevenue')}}</p>
              <h3 class="text-2xl font-bold text-gray-900">
                {{ formatCurrency(overview.total_revenue) }}
              </h3>
              <p
                class="text-sm mt-2"
                :class="overview.revenue_change >= 0 ? 'text-green-600' : 'text-red-600'"
              >
                {{ overview.revenue_change >= 0 ? '+' : '' }}{{ overview.revenue_change }}{{$t('Admin.Analytics.cards.revenueChangeSuffix')}}
              </p>
            </div>
            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Orders -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-gray-600 mb-1">{{$t('Admin.Analytics.cards.totalOrders')}}</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_orders) }}</h3>
              <p
                class="text-sm mt-2"
                :class="overview.orders_change >= 0 ? 'text-blue-600' : 'text-red-600'"
              >
                {{ overview.orders_change >= 0 ? '+' : '' }}{{ overview.orders_change }}{{$t('Admin.Analytics.cards.revenueChangeSuffix')}}
              </p>
            </div>
            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Products -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-gray-600 mb-1">{{$t('Admin.Analytics.cards.totalProducts')}}</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_products) }}</h3>
              <p class="text-sm text-purple-600 mt-2">{{$t('Admin.Analytics.cards.active')}}</p>
            </div>
            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Customers -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-gray-600 mb-1">{{$t('Admin.Analytics.cards.totalCustomers')}}</p>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatNumber(overview.total_customers) }}</h3>
              <p class="text-sm text-orange-600 mt-2">{{$t('Admin.Analytics.cards.registeredUsers')}}</p>
            </div>
            <div class="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Charts Row -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Revenue Chart -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-gray-900">{{$t('Admin.Analytics.chart.revenueTitle', { days: chartDays })}}</h3>
            <select v-model="chartDays" @change="fetchChartData" class="text-sm border rounded px-2 py-1">
              <option :value="7">{{$t('Admin.Analytics.chart.option7')}}</option>
              <option :value="14">{{$t('Admin.Analytics.chart.option14')}}</option>
              <option :value="30">{{$t('Admin.Analytics.chart.option30')}}</option>
            </select>
          </div>
          <div class="h-64 overflow-hidden">
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
          <div class="mt-4 pt-4 border-t border-gray-200">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">{{$t('Admin.Analytics.chart.totalRevenue')}}</span>
              <span class="font-semibold text-gray-900">
                {{ formatCurrency(getTotalRevenue(chartData)) }}
              </span>
            </div>
          </div>
        </div>

        <!-- Top Products -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.topProducts.title')}}</h3>
          <div class="space-y-4">
            <div v-if="topProducts.length === 0" class="text-center text-gray-500 py-8">
              {{$t('Admin.Analytics.topProducts.noData')}}
            </div>
            <div v-for="(product, index) in topProducts" :key="product.product_id"
              class="flex items-center justify-between">
              <div class="flex items-center space-x-3 flex-1">
                <div class="w-10 h-10 bg-gray-200 rounded flex items-center justify-center text-gray-600 font-bold">
                  {{ index + 1 }}
                </div>
                <div class="flex-1 min-w-0">
                  <p class="font-medium text-gray-900 truncate">{{ product.name }}</p>
                  <p class="text-sm text-gray-500">{{ formatNumber(product.sold) }} {{$t('Admin.Analytics.topProducts.soldSuffix')}}</p>
                </div>
              </div>
              <div class="text-right">
                <span class="font-semibold text-gray-900">{{ formatCurrency(product.revenue) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Status Distribution & Recent Orders -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Order Status Distribution -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.statusDistribution.title')}}</h3>
          <div class="space-y-3">
            <div v-for="(count, status) in overview.status_counts" :key="status" class="flex items-center">
              <div class="flex-1">
                <div class="flex items-center justify-between mb-1">
                  <span class="text-sm font-medium text-gray-700">{{ getStatusLabel(status) }}</span>
                  <span class="text-sm text-gray-600">{{ formatNumber(count) }}</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                  <div
                    class="h-2 rounded-full transition-all duration-300"
                    :class="getStatusColor(status)"
                    :style="{ width: `${getStatusPercentage(count, overview.total_orders)}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Recent Orders -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.recentOrders.title')}}</h3>
          <div class="space-y-3">
            <div v-if="recentOrders.length === 0" class="text-center text-gray-500 py-8">
              {{$t('Admin.Analytics.recentOrders.empty')}}
            </div>
            <div v-for="order in recentOrders" :key="order.id"
              class="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
              <div class="flex-1">
                <p class="font-medium text-gray-900">#{{ order.id.slice(-6) }}</p>
                <p class="text-sm text-gray-500">{{ order.customer }}</p>
                <p class="text-xs text-gray-400">{{ formatDate(order.date) }}</p>
              </div>
              <div class="text-right">
                <p class="font-semibold text-gray-900">{{ formatCurrency(order.total) }}</p>
                <span
                  class="inline-block px-2 py-1 text-xs font-semibold rounded-full mt-1"
                  :class="getStatusBadgeClass(order.status)"
                >
                  {{ getStatusLabel(order.status) }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Detailed Statistics Section -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <!-- Detailed Revenue Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.detailedRevenue.title')}}</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedRevenue.today')}}</span>
              <div class="text-right">
                <p class="font-semibold text-gray-900">{{ formatCurrency(detailedRevenue.today?.revenue || 0) }}</p>
                <p class="text-xs text-gray-500">{{ formatNumber(detailedRevenue.today?.orders || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}</p>
              </div>
            </div>
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedRevenue.thisWeek')}}</span>
              <div class="text-right">
                <p class="font-semibold text-gray-900">{{ formatCurrency(detailedRevenue.this_week?.revenue || 0) }}</p>
                <p class="text-xs text-gray-500">{{ formatNumber(detailedRevenue.this_week?.orders || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}</p>
              </div>
            </div>
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedRevenue.thisMonth')}}</span>
              <div class="text-right">
                <p class="font-semibold text-gray-900">{{ formatCurrency(detailedRevenue.this_month?.revenue || 0) }}</p>
                <p class="text-xs text-gray-500">{{ formatNumber(detailedRevenue.this_month?.orders || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}</p>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedRevenue.thisYear')}}</span>
              <div class="text-right">
                <p class="font-semibold text-gray-900">{{ formatCurrency(detailedRevenue.this_year?.revenue || 0) }}</p>
                <p class="text-xs text-gray-500">{{ formatNumber(detailedRevenue.this_year?.orders || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Detailed Order Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.detailedOrders.title')}}</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedOrders.today')}}</span>
              <span class="font-semibold text-gray-900">{{ formatNumber(detailedOrders.today || 0) }}</span>
            </div>
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedOrders.thisWeek')}}</span>
              <span class="font-semibold text-gray-900">{{ formatNumber(detailedOrders.this_week || 0) }}</span>
            </div>
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedOrders.thisMonth')}}</span>
              <span class="font-semibold text-gray-900">{{ formatNumber(detailedOrders.this_month || 0) }}</span>
            </div>
            <div class="flex items-center justify-between pb-3 border-b border-gray-200">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.detailedOrders.total')}}</span>
              <span class="font-semibold text-gray-900">{{ formatNumber(detailedOrders.total || 0) }}</span>
            </div>
            <div class="pt-2">
              <p class="text-xs text-gray-500 mb-2">{{$t('Admin.Analytics.detailedOrders.byStatus')}}</p>
              <div class="space-y-1">
                <div v-for="(count, status) in detailedOrders.by_status" :key="status" class="flex items-center justify-between text-xs">
                  <span class="text-gray-600">{{ getStatusLabel(status) }}:</span>
                  <span class="font-medium">{{ formatNumber(count) }} ({{ detailedOrders.status_percentages?.[status] || 0 }}%)</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Cancellation Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.cancellations.title')}}</h3>
          <div class="space-y-4">
            <div class="bg-red-50 rounded-lg p-4">
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-red-800">{{$t('Admin.Analytics.cancellations.totalCancelled')}}</span>
                <span class="text-xl font-bold text-red-900">{{ formatNumber(cancellationStats.total_cancelled || 0) }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-xs text-red-600">{{$t('Admin.Analytics.cancellations.cancellationRate')}}</span>
                <span class="text-sm font-semibold text-red-700">{{ cancellationStats.cancellation_rate || 0 }}%</span>
              </div>
            </div>
            <div class="pb-3 border-b border-gray-200">
              <p class="text-sm font-medium text-gray-700 mb-2">{{$t('Admin.Analytics.cancellations.lostRevenue')}}</p>
              <p class="text-xl font-bold text-red-600">{{ formatCurrency(cancellationStats.lost_revenue || 0) }}</p>
            </div>
            <div class="space-y-2">
              <div class="flex items-center justify-between text-sm">
                <span class="text-gray-600">{{$t('Admin.Analytics.cancellations.today')}}:</span>
                <span class="font-medium">{{ formatNumber(cancellationStats.today?.count || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}
                  ({{ formatCurrency(cancellationStats.today?.lost_revenue || 0) }})</span>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="text-gray-600">{{$t('Admin.Analytics.cancellations.thisWeek')}}:</span>
                <span class="font-medium">{{ formatNumber(cancellationStats.this_week?.count || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}
                  ({{ formatCurrency(cancellationStats.this_week?.lost_revenue || 0) }})</span>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="text-gray-600">{{$t('Admin.Analytics.cancellations.thisMonth')}}:</span>
                <span class="font-medium">{{ formatNumber(cancellationStats.this_month?.count || 0) }} {{$t('Admin.Analytics.detailedRevenue.ordersSuffix')}}
                  ({{ formatCurrency(cancellationStats.this_month?.lost_revenue || 0) }})</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Cancelled Orders -->
      <div class="bg-white rounded-lg shadow p-6 mb-8" v-if="cancellationStats.recent_cancelled?.length > 0">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.recentCancelled.title')}}</h3>
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50 border-b border-gray-200">
              <tr>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">{{$t('Admin.Analytics.table.orderId')}}</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">{{$t('Admin.Analytics.table.customer')}}</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">{{$t('Admin.Analytics.table.date')}}</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">{{$t('Admin.Analytics.table.value')}}</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr v-for="order in cancellationStats.recent_cancelled" :key="order.id" class="hover:bg-gray-50">
                <td class="px-4 py-3 text-sm font-medium text-gray-900">#{{ order.id.slice(-6) }}</td>
                <td class="px-4 py-3 text-sm text-gray-900">{{ order.customer }}</td>
                <td class="px-4 py-3 text-sm text-gray-500">{{ formatDate(order.date) }}</td>
                <td class="px-4 py-3 text-sm font-semibold text-red-600">{{ formatCurrency(order.total) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Additional Statistics: Users, Categories, Brands, Products -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <!-- Users Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-gray-900">{{$t('Admin.Analytics.entities.users')}}</h3>
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
          </div>
          <div class="space-y-2">
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.total')}}</span>
              <span class="text-sm font-semibold text-gray-900">{{ formatNumber(userStats.total_users) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.active')}}</span>
              <span class="text-sm font-semibold text-green-600">{{ formatNumber(userStats.active_users) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.inactive')}}</span>
              <span class="text-sm font-semibold text-red-600">{{ formatNumber(userStats.inactive_users) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.newThisMonth')}}</span>
              <span class="text-sm font-semibold text-blue-600">{{ formatNumber(userStats.new_users_this_month) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.newThisWeek')}}</span>
              <span class="text-sm font-semibold text-blue-600">{{ formatNumber(userStats.new_users_this_week) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.admins')}}</span>
              <span class="text-sm font-semibold text-purple-600">{{ formatNumber(userStats.total_admins) }}</span>
            </div>
          </div>
        </div>

        <!-- Categories Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-gray-900">{{$t('Admin.Analytics.entities.categories')}}</h3>
            <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
              </svg>
            </div>
          </div>
          <div class="space-y-2">
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.total')}}</span>
              <span class="text-sm font-semibold text-gray-900">{{ formatNumber(categoryStats.total_categories) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.active')}}</span>
              <span class="text-sm font-semibold text-green-600">{{ formatNumber(categoryStats.active_categories) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.inactive')}}</span>
              <span class="text-sm font-semibold text-red-600">{{ formatNumber(categoryStats.inactive_categories) }}</span>
            </div>
          </div>
        </div>

        <!-- Brands Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-gray-900">{{$t('Admin.Analytics.entities.brands')}}</h3>
            <div class="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
              </svg>
            </div>
          </div>
          <div class="space-y-2">
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.total')}}</span>
              <span class="text-sm font-semibold text-gray-900">{{ formatNumber(brandStats.total_brands) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.active')}}</span>
              <span class="text-sm font-semibold text-green-600">{{ formatNumber(brandStats.active_brands) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.inactive')}}</span>
              <span class="text-sm font-semibold text-red-600">{{ formatNumber(brandStats.inactive_brands) }}</span>
            </div>
          </div>
        </div>

        <!-- Products Stats -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-gray-900">{{$t('Admin.Analytics.entities.products')}}</h3>
            <div class="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
              </svg>
            </div>
          </div>
          <div class="space-y-2">
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.total')}}</span>
              <span class="text-sm font-semibold text-gray-900">{{ formatNumber(productStats.total_products) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.active')}}</span>
              <span class="text-sm font-semibold text-green-600">{{ formatNumber(productStats.active_products) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.inactive')}}</span>
              <span class="text-sm font-semibold text-red-600">{{ formatNumber(productStats.inactive_products) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.newThisMonth')}}</span>
              <span class="text-sm font-semibold text-blue-600">{{ formatNumber(productStats.new_products_this_month) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.newThisWeek')}}</span>
              <span class="text-sm font-semibold text-blue-600">{{ formatNumber(productStats.new_products_this_week) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.lowStock')}}</span>
              <span class="text-sm font-semibold text-yellow-600">{{ formatNumber(productStats.low_stock_count) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-gray-600">{{$t('Admin.Analytics.entities.outOfStock')}}</span>
              <span class="text-sm font-semibold text-red-600">{{ formatNumber(productStats.out_of_stock_count) }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Top Categories and Brands -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Top Categories -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.topCategoriesTitle')}}</h3>
          <div class="space-y-3">
            <div v-if="categoryStats.categories_with_products.length === 0" class="text-center text-gray-500 py-4">
              {{$t('Admin.Analytics.topProducts.noData')}}
            </div>
            <div v-for="(category, index) in categoryStats.categories_with_products.slice(0, 10)" :key="category.id" 
              class="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-purple-100 rounded flex items-center justify-center text-purple-600 font-bold text-sm">
                  {{ index + 1 }}
                </div>
                <div>
                  <p class="font-medium text-gray-900">{{ category.name }}</p>
                  <p class="text-xs text-gray-500" :class="category.is_active ? 'text-green-600' : 'text-red-600'">
                    {{ category.is_active ? $t('Admin.Analytics.entities.active').replace(':','') : $t('Admin.Analytics.entities.inactive').replace(':','') }}
                  </p>
                </div>
              </div>
              <div class="text-right">
                <span class="font-semibold text-gray-900">{{ formatNumber(category.products_count) }}</span>
                <p class="text-xs text-gray-500">{{$t('Admin.Analytics.entities.productsUnit')}}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Top Brands -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{$t('Admin.Analytics.topBrandsTitle')}}</h3>
          <div class="space-y-3">
            <div v-if="brandStats.brands_with_products.length === 0" class="text-center text-gray-500 py-4">
              {{$t('Admin.Analytics.topProducts.noData')}}
            </div>
            <div v-for="(brand, index) in brandStats.brands_with_products.slice(0, 10)" :key="brand.id" 
              class="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-indigo-100 rounded flex items-center justify-center text-indigo-600 font-bold text-sm">
                  {{ index + 1 }}
                </div>
                <div>
                  <p class="font-medium text-gray-900">{{ brand.name }}</p>
                  <p class="text-xs text-gray-500" :class="brand.is_active ? 'text-green-600' : 'text-red-600'">
                    {{ brand.is_active ? $t('Admin.Analytics.entities.active').replace(':','') : $t('Admin.Analytics.entities.inactive').replace(':','') }}
                  </p>
                </div>
              </div>
              <div class="text-right">
                <span class="font-semibold text-gray-900">{{ formatNumber(brand.products_count) }}</span>
                <p class="text-xs text-gray-500">{{$t('Admin.Analytics.entities.productsUnit')}}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import AdminLayout from '@/layouts/admin/AdminLayout.vue';
import StatisticsService from '@/api-services/StatisticsService';

const { t: $t } = useI18n();

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
const chartDays = ref(7);
const detailedRevenue = ref({
  today: { revenue: 0, orders: 0 },
  this_week: { revenue: 0, orders: 0 },
  this_month: { revenue: 0, orders: 0 },
  this_year: { revenue: 0, orders: 0 }
});
const detailedOrders = ref({
  by_status: {},
  total: 0,
  today: 0,
  this_week: 0,
  this_month: 0,
  status_percentages: {}
});
const cancellationStats = ref({
  total_cancelled: 0,
  total_orders: 0,
  cancellation_rate: 0,
  lost_revenue: 0,
  today: { count: 0, lost_revenue: 0 },
  this_week: { count: 0, lost_revenue: 0 },
  this_month: { count: 0, lost_revenue: 0 },
  recent_cancelled: []
});
const userStats = ref({
  total_users: 0,
  active_users: 0,
  inactive_users: 0,
  new_users_this_month: 0,
  new_users_this_week: 0,
  total_admins: 0
});
const categoryStats = ref({
  total_categories: 0,
  active_categories: 0,
  inactive_categories: 0,
  categories_with_products: []
});
const brandStats = ref({
  total_brands: 0,
  active_brands: 0,
  inactive_brands: 0,
  brands_with_products: []
});
const productStats = ref({
  total_products: 0,
  active_products: 0,
  inactive_products: 0,
  new_products_this_month: 0,
  new_products_this_week: 0,
  total_stock: 0,
  low_stock_count: 0,
  out_of_stock_count: 0
});

// Fetch all data
const fetchData = async () => {
  try {
    loading.value = true;
    error.value = null;

    // Fetch all data in parallel
    const [
      overviewData,
      chartDataRes,
      topProductsRes,
      recentOrdersRes,
      detailedRevenueRes,
      detailedOrdersRes,
      cancellationStatsRes,
      userStatsRes,
      categoryStatsRes,
      brandStatsRes,
      productStatsRes
    ] = await Promise.all([
      StatisticsService.getOverview(),
      StatisticsService.getRevenueChart(chartDays.value),
      StatisticsService.getTopProducts(5),
      StatisticsService.getRecentOrders(5),
      StatisticsService.getDetailedRevenue(),
      StatisticsService.getDetailedOrders(),
      StatisticsService.getCancellationStats(),
      StatisticsService.getUserStats(),
      StatisticsService.getCategoryStats(),
      StatisticsService.getBrandStats(),
      StatisticsService.getProductStats()
    ]);

    overview.value = overviewData;
    chartData.value = chartDataRes;
    topProducts.value = topProductsRes;
    recentOrders.value = recentOrdersRes;
    detailedRevenue.value = detailedRevenueRes;
    detailedOrders.value = detailedOrdersRes;
    cancellationStats.value = cancellationStatsRes;
    userStats.value = userStatsRes;
    categoryStats.value = categoryStatsRes;
    brandStats.value = brandStatsRes;
    productStats.value = productStatsRes;
  } catch (err) {
    error.value = err.response?.data?.detail || err.message || $t('Admin.Analytics.errors.loadFailed');
  } finally {
    loading.value = false;
  }
};

// Fetch chart data when days change
const fetchChartData = async () => {
  try {
    const data = await StatisticsService.getRevenueChart(chartDays.value);
    chartData.value = data;
  } catch (err) {
    // Silent error handling
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
  // If it's already in Vietnamese format from backend, return as is
  if (dayName.includes('Thứ') || dayName === 'Chủ Nhật') {
    // Extract short form: "Thứ Hai" -> "T2"
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
  // Fallback for English or date format
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
  const key = String(status).toLowerCase();
  try {
    return $t(`Admin.Status.${key}`);
  } catch {
    return status;
  }
};

const getStatusColor = (status) => {
  const colors = {
    'pending': 'bg-yellow-500',
    'confirmed': 'bg-blue-500',
    'shipping': 'bg-purple-500',
    'complete': 'bg-green-500',
    'cancelled': 'bg-red-500'
  };
  return colors[status] || 'bg-gray-500';
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

const getStatusPercentage = (count, total) => {
  if (total === 0) return 0;
  return (count / total) * 100;
};

// Lifecycle
onMounted(() => {
  fetchData();
});
</script>

<style scoped>
/* Additional styles if needed */
</style>

