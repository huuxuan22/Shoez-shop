<template>
    <section class="py-12 bg-gray-50 border-t border-gray-200">
        <div class="container mx-auto px-4">
            <div class="max-w-2xl mx-auto text-center">
                <h2 class="text-2xl md:text-3xl font-bold text-black mb-2">{{ $t('Home.Newsletter.title') }}</h2>
                <p class="text-gray-600 mb-6">{{ $t('Home.Newsletter.subtitle') }}</p>

                <form class="flex gap-2">
                    <input v-model="email" type="email" :placeholder="$t('Home.Newsletter.emailPlaceholder')"
                        class="flex-1 px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-black" />
                    <button type="submit" @click.prevent="subscribeNewsletter"
                        class="bg-black text-white px-6 py-3 rounded hover:bg-gray-800 transition">
                        {{ $t('Home.Newsletter.subscribeButton') }}
                    </button>
                </form>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const email = ref('')

const subscribeNewsletter = () => {
    if (!email.value) {
        alert(t('Home.Newsletter.emailRequired'));
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        alert(t('Home.Newsletter.emailInvalid'));
        return;
    }

    alert(t('Home.Newsletter.success', { email: email.value }));
    email.value = '';
}
</script>