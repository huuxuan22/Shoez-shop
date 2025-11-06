<template>
    <DefaultLayout>
        <div class="min-h-screen bg-white">
            <!-- Hero Section -->
            <section
                class="relative bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white py-24 overflow-hidden">
                <div class="absolute inset-0 bg-black/50"></div>
                <div class="absolute top-0 left-0 w-full h-full">
                    <div class="absolute top-10 left-10 w-20 h-20 bg-blue-500/10 rounded-full blur-xl"></div>
                    <div class="absolute top-1/2 right-10 w-32 h-32 bg-purple-500/10 rounded-full blur-2xl"></div>
                    <div class="absolute bottom-10 left-1/3 w-24 h-24 bg-emerald-500/10 rounded-full blur-xl"></div>
                </div>
                <div class="container mx-auto px-4 relative z-10">
                    <div class="max-w-4xl mx-auto text-center">
                        <h1
                            class="text-6xl font-bold mb-6 bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                            {{ $t('ContactTemplate.title') }}
                        </h1>
                        <div class="w-24 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-8 rounded-full">
                        </div>
                        <p class="text-xl text-gray-300 leading-relaxed font-light">
                            {{ $t('ContactTemplate.subtitle') }}
                        </p>
                    </div>
                </div>
            </section>

            <!-- Contact Information & Form -->
            <section class="py-20 bg-white">
                <div class="container mx-auto px-4">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 max-w-6xl mx-auto">

                        <!-- Contact Information -->
                        <div class="relative">
                            <div class="absolute -top-4 -left-4 w-8 h-8 border-t-2 border-l-2 border-gray-900"></div>
                            <div class="absolute -bottom-4 -right-4 w-8 h-8 border-b-2 border-r-2 border-gray-900">
                            </div>

                            <h2 class="text-4xl font-bold text-gray-900 mb-12 font-serif">{{ $t('ContactTemplate.contactInfo') }}</h2>

                            <div class="space-y-8">
                                <!-- Address -->
                                <div
                                    class="flex items-start space-x-6 group hover:transform hover:-translate-y-1 transition-all duration-300">
                                    <div
                                        class="w-14 h-14 bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl flex items-center justify-center mt-1 shadow-lg group-hover:shadow-xl transition-shadow">
                                        <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor"
                                            viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                                d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                                d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                        </svg>
                                    </div>
                                    <div>
                                        <h3 class="text-xl font-semibold text-gray-900 mb-2 tracking-wide">{{ $t('ContactTemplate.address') }}</h3>
                                        <p class="text-gray-600 font-light text-lg">{{ $t('ContactTemplate.addressLine1') }}</p>
                                        <p class="text-gray-600 font-light text-lg">{{ $t('ContactTemplate.addressLine2') }}</p>
                                    </div>
                                </div>

                                <!-- Phone -->
                                <div
                                    class="flex items-start space-x-6 group hover:transform hover:-translate-y-1 transition-all duration-300">
                                    <div
                                        class="w-14 h-14 bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl flex items-center justify-center mt-1 shadow-lg group-hover:shadow-xl transition-shadow">
                                        <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor"
                                            viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                                d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                        </svg>
                                    </div>
                                    <div>
                                        <h3 class="text-xl font-semibold text-gray-900 mb-2 tracking-wide">{{ $t('ContactTemplate.phone') }}
                                        </h3>
                                        <p class="text-gray-600 font-light text-lg">1900 6750</p>
                                    </div>
                                </div>

                                <!-- Email -->
                                <div
                                    class="flex items-start space-x-6 group hover:transform hover:-translate-y-1 transition-all duration-300">
                                    <div
                                        class="w-14 h-14 bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl flex items-center justify-center mt-1 shadow-lg group-hover:shadow-xl transition-shadow">
                                        <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor"
                                            viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                        </svg>
                                    </div>
                                    <div>
                                        <h3 class="text-xl font-semibold text-gray-900 mb-2 tracking-wide">{{ $t('ContactTemplate.email') }}</h3>
                                        <p class="text-gray-600 font-light text-lg">heliocafein@gmail.com</p>
                                    </div>
                                </div>

                                <div class="mt-12 pt-8 border-t border-gray-200">
                                    <h3 class="text-xl font-semibold text-gray-900 mb-6 tracking-wide">{{ $t('ContactTemplate.followUs') }}
                                    </h3>
                                    <div class="flex space-x-4">
                                        <a href="#"
                                            class="w-12 h-12 bg-[#1877F2] rounded-2xl flex items-center justify-center text-white hover:bg-[#166FE5] hover:transform hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-xl">
                                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                                <path
                                                    d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                                            </svg>
                                        </a>

                                        <a href="#"
                                            class="w-12 h-12 bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl flex items-center justify-center text-white hover:from-purple-600 hover:to-pink-600 hover:transform hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-xl">
                                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                                <path
                                                    d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 6.62 5.367 11.987 11.988 11.987 6.62 0 11.987-5.367 11.987-11.987C24.014 5.367 18.637.001 12.017.001zM8.449 16.988c-1.297 0-2.448-.49-3.323-1.297C4.22 14.815 3.73 13.664 3.73 12.367s.49-2.448 1.396-3.323c.875-.807 2.026-1.297 3.323-1.297s2.448.49 3.323 1.297c.906.875 1.396 2.026 1.396 3.323s-.49 2.448-1.396 3.323c-.875.807-2.026 1.297-3.323 1.297z" />
                                            </svg>
                                        </a>

                                        <a href="#"
                                            class="w-12 h-12 bg-gradient-to-br from-gray-900 to-black rounded-2xl flex items-center justify-center text-white hover:bg-gray-800 hover:transform hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-xl">
                                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                                <path
                                                    d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z" />
                                            </svg>
                                        </a>

                                        <a href="#"
                                            class="w-12 h-12 bg-[#1DA1F2] rounded-2xl flex items-center justify-center text-white hover:bg-[#1A91DA] hover:transform hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-xl">
                                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                                <path
                                                    d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" />
                                            </svg>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Contact Form -->
                        <div class="relative">
                            <div
                                class="bg-gradient-to-br from-white to-gray-50 rounded-3xl p-8 shadow-2xl border border-gray-100">
                                <div class="absolute -top-4 -right-4 w-8 h-8 border-t-2 border-r-2 border-gray-900">
                                </div>
                                <div class="absolute -bottom-4 -left-4 w-8 h-8 border-b-2 border-l-2 border-gray-900">
                                </div>

                                <h2 class="text-4xl font-bold text-gray-900 mb-12 font-serif">{{ $t('ContactTemplate.sendMessage') }}
                                </h2>

                                <form @submit.prevent="submitForm" class="space-y-8">
                                    <!-- Name -->
                                    <div class="group">
                                        <label for="name"
                                            class="block text-sm font-medium text-gray-700 mb-3 tracking-wide">{{ $t('ContactTemplate.fullName') }}
                                            *</label>
                                        <input type="text" id="name" v-model="form.name" required
                                            class="w-full px-6 py-4 border-2 border-gray-200 rounded-2xl focus:ring-2 focus:ring-gray-900 focus:border-gray-900 transition-all duration-300 bg-white/80 backdrop-blur-sm placeholder-gray-400 text-lg font-light group-hover:border-gray-300"
                                            :placeholder="$t('ContactTemplate.fullNamePlaceholder')">
                                    </div>

                                    <!-- Email -->
                                    <div class="group">
                                        <label for="email"
                                            class="block text-sm font-medium text-gray-700 mb-3 tracking-wide">{{ $t('ContactTemplate.emailLabel') }}
                                            *</label>
                                        <input type="email" id="email" v-model="form.email" required
                                            class="w-full px-6 py-4 border-2 border-gray-200 rounded-2xl focus:ring-2 focus:ring-gray-900 focus:border-gray-900 transition-all duration-300 bg-white/80 backdrop-blur-sm placeholder-gray-400 text-lg font-light group-hover:border-gray-300"
                                            :placeholder="$t('ContactTemplate.emailPlaceholder')">
                                    </div>

                                    <!-- Content -->
                                    <div class="group">
                                        <label for="content"
                                            class="block text-sm font-medium text-gray-700 mb-3 tracking-wide">{{ $t('ContactTemplate.content') }}
                                            *</label>
                                        <textarea id="content" rows="6" v-model="form.content" required
                                            class="w-full px-6 py-4 border-2 border-gray-200 rounded-2xl focus:ring-2 focus:ring-gray-900 focus:border-gray-900 transition-all duration-300 bg-white/80 backdrop-blur-sm placeholder-gray-400 text-lg font-light resize-none group-hover:border-gray-300"
                                            :placeholder="$t('ContactTemplate.messagePlaceholder')"></textarea>
                                    </div>

                                    <!-- Submit Button -->
                                    <div>
                                        <button type="submit"
                                            class="w-full bg-gradient-to-r from-gray-900 to-black text-white py-4 px-8 rounded-2xl font-semibold text-lg hover:from-gray-800 hover:to-gray-900 transform hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-xl">
                                            {{ $t('ContactTemplate.sendButton') }}
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Additional Locations -->
            <section class="py-20 bg-gradient-to-b from-white to-gray-50">
                <div class="container mx-auto px-4">
                    <h2 class="text-4xl font-bold text-gray-900 text-center mb-16 font-serif">{{ $t('ContactTemplate.otherBranches') }}</h2>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
                        <!-- Location 1 -->
                        <div
                            class="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 hover:transform hover:-translate-y-2 transition-all duration-300 group">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-500 rounded-2xl flex items-center justify-center mb-6 group-hover:rotate-12 transition-transform duration-300">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                            </div>
                            <h3 class="text-2xl font-semibold text-gray-900 mb-4">{{ $t('ContactTemplate.location1Name') }}</h3>
                            <p class="text-gray-600 mb-2 text-lg font-light">{{ $t('ContactTemplate.location1Address') }}</p>
                            <p class="text-gray-600 text-lg font-light">{{ $t('ContactTemplate.location1City') }}</p>
                        </div>

                        <!-- Location 2 -->
                        <div
                            class="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 hover:transform hover:-translate-y-2 transition-all duration-300 group">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-500 rounded-2xl flex items-center justify-center mb-6 group-hover:rotate-12 transition-transform duration-300">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                            </div>
                            <h3 class="text-2xl font-semibold text-gray-900 mb-4">{{ $t('ContactTemplate.location2Name') }}</h3>
                            <p class="text-gray-600 mb-2 text-lg font-light">{{ $t('ContactTemplate.location2Address') }}</p>
                            <p class="text-gray-600 text-lg font-light">{{ $t('ContactTemplate.location2City') }}</p>
                        </div>

                        <!-- Location 3 -->
                        <div
                            class="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 hover:transform hover:-translate-y-2 transition-all duration-300 group">
                            <div
                                class="w-12 h-12 bg-gradient-to-br from-orange-500 to-red-500 rounded-2xl flex items-center justify-center mb-6 group-hover:rotate-12 transition-transform duration-300">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                            </div>
                            <h3 class="text-2xl font-semibold text-gray-900 mb-4">{{ $t('ContactTemplate.location3Name') }}</h3>
                            <p class="text-gray-600 mb-2 text-lg font-light">{{ $t('ContactTemplate.location3Address') }}</p>
                            <p class="text-gray-900 text-lg font-light">{{ $t('ContactTemplate.location3City') }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- CTA Section -->
            <section
                class="relative py-24 bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white overflow-hidden">
                <div class="absolute inset-0">
                    <div class="absolute top-0 left-0 w-full h-full opacity-10">
                        <div class="absolute top-20 left-20 w-40 h-40 bg-white rounded-full blur-3xl"></div>
                        <div class="absolute bottom-20 right-20 w-60 h-60 bg-blue-500 rounded-full blur-3xl"></div>
                    </div>
                </div>
                <div class="container mx-auto px-4 text-center relative z-10">
                    <h2
                        class="text-5xl font-bold mb-8 font-serif bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                        {{ $t('ContactTemplate.needSupportNow') }}
                    </h2>
                    <div class="w-32 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-12 rounded-full"></div>
                    <p class="text-xl text-gray-300 mb-12 max-w-2xl mx-auto font-light leading-relaxed">
                        {{ $t('ContactTemplate.supportTeam') }}
                    </p>
                    <div class="space-x-6">
                        <a href="tel:19006750"
                            class="bg-gradient-to-r from-white to-gray-100 text-gray-900 px-10 py-4 rounded-2xl font-semibold text-lg hover:from-gray-100 hover:to-white transform hover:-translate-y-1 transition-all duration-300 shadow-2xl hover:shadow-3xl inline-block">
                            📞 {{ $t('ContactTemplate.callNow') }}: 1900 6750
                        </a>
                        <a href="mailto:heliocafein@gmail.com"
                            class="border-2 border-white text-white px-10 py-4 rounded-2xl font-semibold text-lg hover:bg-white hover:text-gray-900 transform hover:-translate-y-1 transition-all duration-300 shadow-2xl hover:shadow-3xl inline-block">
                            ✉️ {{ $t('ContactTemplate.sendEmail') }}
                        </a>
                    </div>
                </div>
            </section>
        </div>
    </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const form = ref({
    name: '',
    email: '',
    content: ''
})

const submitForm = () => {
    // Xử lý gửi form ở đây
    alert(t('ContactTemplate.thankYouContact'))

    // Reset form
    form.value = {
        name: '',
        email: '',
        content: ''
    }
}
</script>

<style scoped>
/* Custom scrollbar for textarea */
textarea::-webkit-scrollbar {
    width: 6px;
}

textarea::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

textarea::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 10px;
}

textarea::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}

/* Smooth transitions for all interactive elements */
* {
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 300ms;
}
</style>