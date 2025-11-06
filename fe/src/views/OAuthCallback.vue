<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="text-center">
            <div v-if="loading" class="space-y-4">
                <div
                    class="inline-block w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin">
                </div>
                <p class="text-gray-600">{{ $t('OAuthCallback.processing') }}</p>
            </div>
            <div v-else-if="error" class="space-y-4">
                <p class="text-red-600">{{ error }}</p>
                <button @click="closeWindow" class="px-4 py-2 bg-gray-600 text-white rounded">{{ $t('OAuthCallback.close') }}</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { hydrateFromOAuthRedirect } from '@/api-services/AuthService';

const { t } = useI18n();

const route = useRoute();
const loading = ref(true);
const error = ref(null);

const closeWindow = () => {
    if (window.opener) {
        window.close();
    } else {
        window.location.href = '/login';
    }
};

onMounted(async () => {
    try {
        debugger;
        const oauth = route.query?.oauth || new URLSearchParams(window.location.search).get('oauth');
        const status = route.query?.status || new URLSearchParams(window.location.search).get('status');

        if (status === 'success' && oauth) {
            // Nếu đây là popup, redirect parent về login với query params và đóng popup
            if (window.opener) {
                // Redirect parent window về login với query params
                window.opener.location.href = `${window.location.origin}/login?oauth=${oauth}&status=${status}`;
                // Đóng popup
                setTimeout(() => {
                    window.close();
                }, 100);
            } else {
                window.location.href = '/login';
            }
        } else {
            throw new Error('OAuth callback failed');
        }
    } catch (err) {
        error.value = err.message || t('OAuthCallback.error');
        loading.value = false;
    }
});
</script>
