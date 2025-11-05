<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold text-gray-900">{{$t('Admin.Customers.title')}}</h1>
        <p class="text-gray-600 mt-1">{{$t('Admin.Customers.subtitle')}}</p>
      </div>
      <div class="relative w-80">
        <input v-model="keyword" type="text" :placeholder="$t('Admin.Customers.searchPlaceholder')"
               class="w-full pl-10 pr-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-black/70"
        />
        <svg class="w-5 h-5 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m21 21-4.35-4.35M11 19a8 8 0 1 1 0-16 8 8 0 0 1 0 16z" />
        </svg>
      </div>
    </div>

    <!-- Actions -->
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-2">
        <button
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-red-200 text-red-700 bg-red-50 hover:bg-red-100 hover:border-red-300 disabled:opacity-50"
          :disabled="selectedIds.length === 0"
          @click="confirmDeleteSelected"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7V4a1 1 0 011-1h4a1 1 0 011 1v3m4 0H5"/></svg>
          {{$t('Admin.Customers.actions.deleteSelected')}} ({{ selectedIds.length }})
        </button>
        <button
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-gray-300 text-gray-800 bg-white hover:bg-gray-50 disabled:opacity-50"
          :disabled="selectedIds.length === 0"
          @click="confirmLockSelected(true)"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 11V7a4 4 0 118 0v4m-9 4h10a2 2 0 002-2v-2a2 2 0 00-2-2H7a2 2 0 00-2 2v2a2 2 0 002 2z"/></svg>
          {{$t('Admin.Customers.actions.lockSelected')}}
        </button>
        <button
          class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-green-300 text-green-700 bg-green-50 hover:bg-green-100 disabled:opacity-50"
          :disabled="selectedIds.length === 0"
          @click="confirmLockSelected(false)"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11V7a4 4 0 118 0m-9 8h10a2 2 0 002-2v-2a2 2 0 00-2-2H7a2 2 0 00-2 2v2a2 2 0 002 2z"/></svg>
          {{$t('Admin.Customers.actions.unlockSelected')}}
        </button>
      </div>
      <div class="flex items-center space-x-2">
        <label class="text-sm text-gray-600">{{$t('Admin.Customers.actions.perPage')}}</label>
        <select v-model.number="pageSize" @change="reload" class="border rounded px-2 py-1">
          <option :value="10">10</option>
          <option :value="20">20</option>
          <option :value="50">50</option>
        </select>
      </div>
    </div>

    <!-- Table -->
    <div class="bg-white rounded-xl shadow-sm ring-1 ring-gray-200/70 overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50 sticky top-0 z-10">
          <tr>
            <th class="px-4 py-3">
              <input type="checkbox" :checked="allChecked" @change="toggleAll" />
            </th>
            <th class="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">{{$t('Admin.Customers.table.fullName')}}</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Customers.table.email')}}</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Customers.table.status')}}</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Customers.table.role')}}</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Customers.table.createdAt')}}</th>
            <th class="px-4 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">{{$t('Admin.Customers.table.actions')}}</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-100">
          <tr v-if="loading">
            <td colspan="7" class="px-4 py-10 text-center text-gray-500">
              <svg class="animate-spin h-5 w-5 inline-block mr-2 text-gray-600" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
              </svg>
              {{$t('Admin.Customers.table.loading')}}
            </td>
          </tr>
          <tr v-for="u in filteredUsers" :key="u.id" class="hover:bg-gray-50/80">
            <td class="px-4 py-3 align-middle">
              <input type="checkbox" :value="u.id" v-model="selectedIds" />
            </td>
            <td class="px-4 py-3">
              <div class="flex items-center space-x-3">
                <div class="h-9 w-9 rounded-full bg-gray-200 flex items-center justify-center text-gray-700 text-sm font-semibold">
                  {{ initials(u.full_name || u.name || u.email) }}
                </div>
                <div>
                  <div class="font-medium text-gray-900">{{ u.full_name || u.name || '-' }}</div>
                </div>
              </div>
            </td>
            <td class="px-4 py-3 text-gray-700">{{ u.email }}</td>
            <td class="px-4 py-3">
              <span class="inline-flex items-center px-2 py-1 rounded text-xs font-semibold"
                    :class="u.is_active === false ? 'bg-red-100 text-red-800' : 'bg-green-100 text-green-800'">
                {{ u.is_active === false ? $t('Admin.Customers.table.locked') : $t('Admin.Customers.table.active') }}
              </span>
            </td>
            <td class="px-4 py-3">
              <span class="inline-flex items-center px-2 py-1 rounded text-xs font-semibold"
                    :class="u.role === 'ADMIN' ? 'bg-yellow-100 text-yellow-800' : 'bg-green-100 text-green-800'">
                {{ u.role || 'USER' }}
              </span>
            </td>
            <td class="px-4 py-3 text-gray-600">{{ formatDate(u.created_at) }}</td>
            <td class="px-4 py-3 text-right space-x-2">
              <button class="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-full border border-slate-300 text-slate-700 bg-white hover:bg-slate-50" @click="resetDraft(u)">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12a9 9 0 119 9m0-18A9 9 0 003 12h6"/></svg>
                {{$t('Admin.Customers.table.undo')}}
              </button>
              <button class="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-full border border-red-200 text-red-700 bg-red-50 hover:bg-red-100" @click="confirmDelete(u.id)">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7V4a1 1 0 011-1h4a1 1 0 011 1v3m4 0H5"/></svg>
                {{$t('Admin.Customers.table.delete')}}
              </button>
              <button v-if="u.is_active !== false" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-full border border-gray-300 text-gray-800 bg-white hover:bg-gray-50" @click="confirmLock(u, true)">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 11V7a4 4 0 118 0v4m-9 4h10a2 2 0 002-2v-2a2 2 0 00-2-2H7a2 2 0 00-2 2v2a2 2 0 002 2z"/></svg>
                {{$t('Admin.Customers.table.lock')}}
              </button>
              <button v-else class="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-full border border-green-300 text-green-700 bg-green-50 hover:bg-green-100" @click="confirmLock(u, false)">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11V7a4 4 0 118 0m-9 8h10a2 2 0 002-2v-2a2 2 0 00-2-2H7a2 2 0 00-2 2v2a2 2 0 002 2z"/></svg>
                {{$t('Admin.Customers.table.unlock')}}
              </button>
            </td>
          </tr>
          <tr v-if="!loading && filteredUsers.length === 0">
            <td colspan="7" class="px-4 py-10 text-center text-gray-500">
              {{$t('Admin.Customers.table.noData')}}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="flex items-center justify-between mt-4">
      <div class="text-sm text-gray-600">{{$t('Admin.Customers.pagination.page')}} {{ page }}</div>
      <div class="space-x-2">
        <button class="px-3 py-1 border rounded disabled:opacity-50" :disabled="page === 1" @click="prevPage">{{$t('Admin.Customers.pagination.prev')}}</button>
        <button class="px-3 py-1 border rounded" @click="nextPage">{{$t('Admin.Customers.pagination.next')}}</button>
      </div>
    </div>
  </AdminLayout>
  
  <!-- Simple confirm dialogs -->
  <transition name="modal">
    <div v-if="confirm.visible" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4" @click.self="confirm.visible = false">
      <div class="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md transform transition-all">
        <!-- Icon or visual indicator -->
        <div class="flex justify-center mb-4">
          <div class="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center">
            <svg class="w-8 h-8 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
        </div>
        
        <!-- Message -->
        <p class="text-center text-gray-900 text-xl font-semibold mb-8 leading-relaxed">
          {{ confirm.message }}
        </p>
        
        <!-- Buttons -->
        <div class="flex justify-center gap-4">
          <button 
            class="px-8 py-3 rounded-full border-2 border-black text-black bg-white hover:bg-gray-50 hover:border-gray-700 font-semibold transition-all duration-200 shadow-sm hover:shadow-md min-w-[120px]" 
            @click="confirm.visible = false">
            {{$t('Admin.Customers.confirm.cancel')}}
          </button>
          <button 
            class="px-8 py-3 rounded-full bg-black text-white hover:bg-gray-800 font-semibold transition-all duration-200 shadow-md hover:shadow-lg min-w-[120px]" 
            @click="confirm.onOk">
            {{$t('Admin.Customers.confirm.confirm')}}
          </button>
        </div>
      </div>
    </div>
  </transition>
  
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import AdminLayout from '@/layouts/admin/AdminLayout.vue'
import UserService from '@/api-services/UserService'
import { useToast } from '@/composables/useToast'

const { t: $t } = useI18n()
// Toast notifications
const toast = useToast()

const users = ref([])
const page = ref(1)
const pageSize = ref(10)
const selectedIds = ref([])
const roleDraft = reactive({})
const keyword = ref('')
const loading = ref(false)

const confirm = reactive({ visible: false, message: '', onOk: null })

const load = async () => {
  loading.value = true
  const list = await UserService.listUsers({ page: page.value, page_size: pageSize.value })
  // Chỉ hiển thị tài khoản khách hàng (USER)
  users.value = (list || []).filter(u => (u.role || 'USER') === 'USER')
  // init role draft
  roleDraftReset()
  // clear selections on reload
  selectedIds.value = []
  loading.value = false
}

const roleDraftReset = () => {
  for (const u of users.value) {
    roleDraft[u.id] = u.role || 'USER'
  }
}

const reload = () => {
  page.value = 1
  load()
}

const prevPage = () => {
  if (page.value > 1) {
    page.value -= 1
    load()
  }
}
const nextPage = () => {
  page.value += 1
  load()
}

const allChecked = computed(() => users.value.length > 0 && selectedIds.value.length === users.value.length)
const toggleAll = (e) => {
  if (e.target.checked) selectedIds.value = users.value.map(u => u.id)
  else selectedIds.value = []
}

const formatDate = (d) => {
  if (!d) return '-'
  try { return new Date(d).toLocaleString() } catch { return '-' }
}

// Vô hiệu hoá việc đổi role tại trang Khách hàng
const updateRole = async () => {}

const confirmDelete = (id) => {
  confirm.message = $t('Admin.Customers.confirm.deleteUser')
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await UserService.deleteUsers([id])
      toast.success($t('Admin.Customers.messages.deleteSuccess'))
      await load()
    } catch (e) {
      console.error('Delete user failed', e)
      toast.error(e?.message || $t('Admin.Customers.messages.deleteFailed'))
    }
  }
}

const confirmDeleteSelected = () => {
  confirm.message = $t('Admin.Customers.confirm.deleteUsers', { count: selectedIds.value.length })
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await UserService.deleteUsers(selectedIds.value)
      toast.success($t('Admin.Customers.messages.deleteUsersSuccess', { count: selectedIds.value.length }))
      await load()
    } catch (e) {
      console.error('Delete users failed', e)
      toast.error(e?.message || $t('Admin.Customers.messages.deleteFailed'))
    }
  }
}

const setActive = async (ids, active) => {
  // use batch lock API
  await UserService.lockUsers(ids, active)
}

const confirmLock = (u, lock) => {
  confirm.message = lock ? $t('Admin.Customers.confirm.lockAccount') : $t('Admin.Customers.confirm.unlockAccount')
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await setActive([u.id], !lock ? true : false)
      toast.success(lock ? $t('Admin.Customers.messages.lockSuccess') : $t('Admin.Customers.messages.unlockSuccess'))
      await load()
    } catch (e) {
      console.error('Lock user failed', e)
      toast.error(e?.message || $t('Admin.Customers.messages.lockFailed'))
    }
  }
}

const confirmLockSelected = (lock) => {
  confirm.message = lock ? $t('Admin.Customers.confirm.lockAccounts', { count: selectedIds.value.length }) : $t('Admin.Customers.confirm.unlockAccounts', { count: selectedIds.value.length })
  confirm.visible = true
  confirm.onOk = async () => {
    confirm.visible = false
    try {
      await setActive(selectedIds.value, !lock ? true : false)
      toast.success(lock ? $t('Admin.Customers.messages.lockUsersSuccess', { count: selectedIds.value.length }) : $t('Admin.Customers.messages.unlockUsersSuccess', { count: selectedIds.value.length }))
      await load()
    } catch (e) {
      console.error('Batch lock users failed', e)
      toast.error(e?.message || $t('Admin.Customers.messages.actionFailed'))
    }
  }
}

const filteredUsers = computed(() => {
  const q = keyword.value.trim().toLowerCase()
  if (!q) return users.value
  return users.value.filter(u => (
    (u.full_name || u.name || '').toLowerCase().includes(q) ||
    (u.email || '').toLowerCase().includes(q)
  ))
})

const initials = (str) => {
  if (!str) return 'U'
  const parts = String(str).split(/\s+/).filter(Boolean)
  const chars = parts.length >= 2 ? parts[0][0] + parts[parts.length - 1][0] : parts[0].slice(0, 2)
  return chars.toUpperCase()
}

onMounted(load)
</script>

<style scoped>
/* Modal transition animations */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-active .bg-white,
.modal-leave-active .bg-white {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .bg-white,
.modal-leave-to .bg-white {
  transform: scale(0.9) translateY(-20px);
  opacity: 0;
}

.modal-enter-to .bg-white,
.modal-leave-from .bg-white {
  transform: scale(1) translateY(0);
  opacity: 1;
}
</style>


