<template>
  <div class="min-h-screen bg-gray-50">
    <AdminSidebar />
    <AdminHeader />
    
    <!-- Main Content -->
    <main class="ml-64 pt-16">
      <div class="p-8">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup>
import AdminSidebar from '@/components/admin/AdminSidebar.vue';
import AdminHeader from '@/components/admin/AdminHeader.vue';
</script>

<style scoped>
</style>
