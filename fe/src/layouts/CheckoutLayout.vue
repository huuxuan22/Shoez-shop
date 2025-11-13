<template>
    <div class="min-h-screen bg-white">
        <div class="container mx-auto px-4 py-8">
            <!-- Header -->
            <div class="text-center mb-8">
                <h1 class="text-4xl font-bold text-black mb-4">{{ t('Views.Checkout.header.title') }}</h1>
                <p class="text-gray-600 text-lg">{{ t('Views.Checkout.header.subtitle') }}</p>
            </div>

            <!-- Checkout Steps -->
            <div class="flex justify-center mb-8">
                <div class="flex items-center space-x-8">
                    <div v-for="step in steps" :key="step.number" class="flex items-center">
                        <!-- Step Circle -->
                        <div :class="[
                            'w-10 h-10 rounded-full border-2 flex items-center justify-center font-semibold transition-all',
                            getStepClass(step.number)
                        ]">
                            <span v-if="step.number < currentStep">✓</span>
                            <span v-else>{{ step.number }}</span>
                        </div>

                        <!-- Step Label -->
                        <span :class="[
                            'ml-3 font-medium transition-colors',
                            step.number <= currentStep ? 'text-black' : 'text-gray-400'
                        ]">
                            {{ step.label }}
                        </span>

                        <!-- Connector Line -->
                        <div v-if="step.number < steps.length" :class="[
                            'w-16 h-0.5 ml-8 transition-colors',
                            step.number < currentStep ? 'bg-black' : 'bg-gray-300'
                        ]"></div>
                    </div>
                </div>
            </div>

            <div class="flex flex-col lg:flex-row gap-8">
                <!-- Left Column - Checkout Form -->
                <div class="lg:w-2/3">
                    <!-- Shipping Information -->
                    <div v-if="currentStep === 1" class="space-y-6">
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-6">{{ t('Views.Checkout.shipping.title') }}</h2>

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <InputField :label="t('Views.Checkout.shipping.fields.fullName.label')" name="fullName"
                                    v-model="shippingForm.fullName"
                                    :placeholder="t('Views.Checkout.shipping.fields.fullName.placeholder')"
                                    :required="true" />

                                <InputField :label="t('Views.Checkout.shipping.fields.phone.label')" name="phone"
                                    type="tel" v-model="shippingForm.phone"
                                    :placeholder="t('Views.Checkout.shipping.fields.phone.placeholder')"
                                    :required="true" />

                                <InputField :label="t('Views.Checkout.shipping.fields.email.label')" name="email"
                                    type="email" v-model="shippingForm.email"
                                    :placeholder="t('Views.Checkout.shipping.fields.email.placeholder')"
                                    :required="true" />

                                <div class="md:col-span-2">
                                    <InputField :label="t('Views.Checkout.shipping.fields.address.label')"
                                        name="address" v-model="shippingForm.address"
                                        :placeholder="t('Views.Checkout.shipping.fields.address.placeholder')"
                                        :required="true" />
                                </div>

                                <InputField :label="t('Views.Checkout.shipping.fields.city.label')" name="city"
                                    v-model="shippingForm.city"
                                    :placeholder="t('Views.Checkout.shipping.fields.city.placeholder')"
                                    :required="true" />

                                <InputField :label="t('Views.Checkout.shipping.fields.district.label')" name="district"
                                    v-model="shippingForm.district"
                                    :placeholder="t('Views.Checkout.shipping.fields.district.placeholder')"
                                    :required="true" />

                                <InputField :label="t('Views.Checkout.shipping.fields.ward.label')" name="ward"
                                    v-model="shippingForm.ward"
                                    :placeholder="t('Views.Checkout.shipping.fields.ward.placeholder')"
                                    :required="true" />
                            </div>

                            <!-- Shipping Method -->
                            <div class="mt-6">
                                <h3 class="font-semibold text-black mb-4">{{ t('Views.Checkout.shipping.methodTitle') }}
                                </h3>
                                <div class="space-y-3">
                                    <label v-for="option in shippingOptions" :key="option.value" :class="[
                                        'flex items-start p-4 border-2 rounded-lg cursor-pointer transition-all',
                                        shippingForm.shippingMethod === option.value
                                            ? 'border-black bg-gray-50'
                                            : 'border-gray-200 hover:border-gray-300'
                                    ]">
                                        <input type="radio" :value="option.value" v-model="shippingForm.shippingMethod"
                                            class="mt-1 text-black focus:ring-black" />
                                        <div class="ml-3 flex-1">
                                            <div class="flex justify-between items-start">
                                                <span class="font-medium text-black">{{ option.label }}</span>
                                                <span v-if="option.price" class="text-black font-semibold">{{
                                                    option.price }}</span>
                                            </div>
                                            <p v-if="option.description" class="text-sm text-gray-600 mt-1">{{
                                                option.description }}</p>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <!-- Note -->
                            <div class="mt-6">
                                <label class="block text-sm font-medium text-gray-700 mb-2">
                                    {{ t('Views.Checkout.shipping.noteLabel') }}
                                </label>
                                <textarea v-model="shippingForm.note" rows="3"
                                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-black focus:border-transparent"
                                    :placeholder="t('Views.Checkout.shipping.notePlaceholder')"></textarea>
                            </div>
                        </div>
                    </div>

                    <!-- Payment Method -->
                    <div v-else-if="currentStep === 2" class="space-y-6">
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-6">{{ t('Views.Checkout.payment.title') }}</h2>

                            <div class="space-y-3">
                                <label v-for="option in paymentOptions" :key="option.value" :class="[
                                    'flex items-start p-4 border-2 rounded-lg cursor-pointer transition-all',
                                    paymentMethod === option.value
                                        ? 'border-black bg-gray-50'
                                        : 'border-gray-200 hover:border-gray-300'
                                ]">
                                    <input type="radio" :value="option.value" v-model="paymentMethod"
                                        class="mt-1 text-black focus:ring-black" />
                                    <div class="ml-3 flex-1">
                                        <div class="flex justify-between items-start">
                                            <span class="font-medium text-black">{{ option.label }}</span>
                                        </div>
                                        <p v-if="option.description" class="text-sm text-gray-600 mt-1">{{
                                            option.description }}</p>
                                    </div>
                                </label>
                            </div>

                            <!-- Credit Card Form -->
                            <div v-if="paymentMethod === 'credit_card'"
                                class="mt-6 p-4 border border-gray-200 rounded-lg">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <InputField :label="t('Views.Checkout.payment.creditCardForm.numberLabel')"
                                        name="cardNumber" v-model="cardInfo.number"
                                        :placeholder="t('Views.Checkout.payment.creditCardForm.numberPlaceholder')"
                                        :maxlength="19" />

                                    <InputField :label="t('Views.Checkout.payment.creditCardForm.nameLabel')"
                                        name="cardName" v-model="cardInfo.name"
                                        :placeholder="t('Views.Checkout.payment.creditCardForm.namePlaceholder')" />

                                    <InputField :label="t('Views.Checkout.payment.creditCardForm.expiryLabel')"
                                        name="cardExpiry" v-model="cardInfo.expiry"
                                        :placeholder="t('Views.Checkout.payment.creditCardForm.expiryPlaceholder')"
                                        :maxlength="5" />

                                    <InputField :label="t('Views.Checkout.payment.creditCardForm.cvvLabel')"
                                        name="cardCvv" v-model="cardInfo.cvv"
                                        :placeholder="t('Views.Checkout.payment.creditCardForm.cvvPlaceholder')"
                                        :maxlength="3" />
                                </div>
                            </div>

                            <!-- MoMo Payment Form -->
                            <div v-if="paymentMethod === 'momo'"
                                class="mt-6 border border-gray-200 rounded-lg overflow-hidden">
                                <!-- MoMo Header -->
                                <div class="bg-gradient-to-r from-[#A50064] to-[#D82D8B] px-6 py-4">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center">
                                            <svg class="w-6 h-6 text-[#A50064]" fill="currentColor" viewBox="0 0 24 24">
                                                <path
                                                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z" />
                                            </svg>
                                        </div>
                                        <div>
                                            <h3 class="text-white font-bold text-lg">{{
                                                t('Views.Checkout.payment.momo.headerTitle') }}</h3>
                                            <p class="text-white/80 text-sm">{{
                                                t('Views.Checkout.payment.momo.headerDescription') }}</p>
                                        </div>
                                    </div>
                                </div>

                                <!-- MoMo Content -->
                                <div class="p-6 bg-white">
                                    <!-- Phone Input -->
                                    <div class="mb-6">
                                        <label class="block text-sm font-semibold text-gray-700 mb-2">
                                            {{ t('Views.Checkout.payment.momo.phoneLabel') }}
                                        </label>
                                        <div class="relative">
                                            <div
                                                class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor"
                                                    viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                                </svg>
                                            </div>
                                            <input type="tel" v-model="momoInfo.phoneNumber"
                                                :placeholder="t('Views.Checkout.payment.momo.phonePlaceholder')"
                                                class="w-full pl-12 pr-4 py-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-[#A50064] focus:border-[#A50064] transition-colors"
                                                :maxlength="10" @input="formatPhoneNumber" />
                                        </div>
                                        <p class="mt-2 text-xs text-gray-500">
                                            {{ t('Views.Checkout.payment.momo.phoneHint') }}
                                        </p>
                                    </div>

                                    <!-- QR Code Section -->
                                    <div class="mb-6 p-4 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
                                        <div class="text-center">
                                            <div class="inline-block p-4 bg-white rounded-lg shadow-sm mb-3">
                                                <div :class="[
                                                    'w-48 h-48 mx-auto rounded flex items-center justify-center transition-all',
                                                    momoInfo.phoneNumber.length === 10
                                                        ? 'bg-gradient-to-br from-[#FFF5F9] to-[#FFE0EB] border-2 border-[#A50064]'
                                                        : 'bg-gray-200'
                                                ]">
                                                    <div class="text-center px-4">
                                                        <svg v-if="momoInfo.phoneNumber.length !== 10"
                                                            class="w-20 h-20 mx-auto text-gray-400 mb-2" fill="none"
                                                            stroke="currentColor" viewBox="0 0 24 24">
                                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                                stroke-width="2"
                                                                d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm12 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z" />
                                                        </svg>
                                                        <div v-else class="space-y-2">
                                                            <div
                                                                class="w-32 h-32 mx-auto bg-white rounded border-2 border-gray-300 flex items-center justify-center">
                                                                <div class="text-center">
                                                                    <svg class="w-16 h-16 mx-auto text-[#A50064] mb-1"
                                                                        fill="currentColor" viewBox="0 0 24 24">
                                                                        <path
                                                                            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z" />
                                                                    </svg>
                                                                </div>
                                                            </div>
                                                            <p class="text-xs font-medium text-[#A50064]">
                                                                {{ t('Views.Checkout.payment.momo.qrPending') }}
                                                            </p>
                                                        </div>
                                                        <p v-if="momoInfo.phoneNumber.length !== 10"
                                                            class="text-xs text-gray-500">
                                                            {{ t('Views.Checkout.payment.momo.qrInstructionPending') }}
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="text-sm font-medium text-gray-700 mb-1">
                                                {{ t('Views.Checkout.payment.momo.qrTitle') }}
                                            </p>
                                            <p class="text-xs text-gray-500">
                                                {{ t('Views.Checkout.payment.momo.qrDescription') }}
                                            </p>
                                            <p v-if="momoInfo.phoneNumber.length === 10"
                                                class="text-xs text-[#A50064] font-medium mt-2">
                                                {{ t('Views.Checkout.payment.momo.phoneVerified') }}
                                            </p>
                                        </div>
                                    </div>

                                    <!-- Payment Instructions -->
                                    <div class="mb-6">
                                        <h4 class="text-sm font-semibold text-gray-700 mb-3">
                                            {{ t('Views.Checkout.payment.momo.instructionsTitle') }}
                                        </h4>
                                        <div class="space-y-2">
                                            <div class="flex items-start gap-3" v-for="step in momoInstructionSteps"
                                                :key="`momo-step-${step}`">
                                                <div
                                                    class="w-6 h-6 bg-[#A50064] text-white rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">
                                                    {{ step }}
                                                </div>
                                                <p class="text-sm text-gray-600">
                                                    {{ t(`Views.Checkout.payment.momo.instructions.step${step}`) }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Security & Info -->
                                    <div
                                        class="bg-gradient-to-r from-[#FFF5F9] to-[#FFF0F6] border border-[#FFE0EB] rounded-lg p-4">
                                        <div class="flex items-start gap-3">
                                            <svg class="w-5 h-5 text-[#A50064] mt-0.5 flex-shrink-0" fill="none"
                                                stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                            </svg>
                                            <div class="flex-1">
                                                <p class="text-sm font-semibold text-[#A50064] mb-1">
                                                    {{ t('Views.Checkout.payment.momo.securityTitle') }}
                                                </p>
                                                <p class="text-xs text-gray-600">
                                                    {{ t('Views.Checkout.payment.momo.securityDescription') }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Support Info -->
                                    <div class="mt-4 pt-4 border-t border-gray-200">
                                        <div class="flex items-center justify-center gap-2 text-xs text-gray-500">
                                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
                                            </svg>
                                            <span>{{ $t('CheckoutLayout.supportMoMo') }}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- ShopeePay Payment Form -->
                            <div v-if="paymentMethod === 'shopee_pay'"
                                class="mt-6 border border-gray-200 rounded-lg overflow-hidden">
                                <!-- ShopeePay Header -->
                                <div class="bg-gradient-to-r from-[#EE4D2D] to-[#FF6B4A] px-6 py-4">
                                    <div class="flex items-center gap-3">
                                        <div
                                            class="w-10 h-10 bg-white rounded-full flex items-center justify-center overflow-hidden">
                                            <img :src="shopeePayIcon" alt="ShopeePay"
                                                class="w-full h-full object-contain" />
                                        </div>
                                        <div>
                                            <h3 class="text-white font-bold text-lg">{{
                                                t('Views.Checkout.payment.shopeePay.headerTitle') }}</h3>
                                            <p class="text-white/80 text-sm">{{
                                                t('Views.Checkout.payment.shopeePay.headerDescription') }}</p>
                                        </div>
                                    </div>
                                </div>

                                <!-- ShopeePay Content -->
                                <div class="p-6 bg-white">
                                    <!-- Phone Input -->
                                    <div class="mb-6">
                                        <label class="block text-sm font-semibold text-gray-700 mb-2">
                                            {{ t('Views.Checkout.payment.shopeePay.phoneLabel') }}
                                        </label>
                                        <div class="relative">
                                            <div
                                                class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor"
                                                    viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                                </svg>
                                            </div>
                                            <input type="tel" v-model="shopeePayInfo.phoneNumber"
                                                :placeholder="t('Views.Checkout.payment.shopeePay.phonePlaceholder')"
                                                class="w-full pl-12 pr-4 py-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-[#EE4D2D] focus:border-[#EE4D2D] transition-colors"
                                                :maxlength="10" @input="formatShopeePayPhone" />
                                        </div>
                                        <p class="mt-2 text-xs text-gray-500">
                                            {{ t('Views.Checkout.payment.shopeePay.phoneHint') }}
                                        </p>
                                    </div>

                                    <!-- Payment Instructions -->
                                    <div class="mb-6">
                                        <h4 class="text-sm font-semibold text-gray-700 mb-3">
                                            {{ t('Views.Checkout.payment.shopeePay.instructionsTitle') }}
                                        </h4>
                                        <div class="space-y-2">
                                            <div class="flex items-start gap-3"
                                                v-for="step in shopeePayInstructionSteps" :key="`shopee-step-${step}`">
                                                <div
                                                    class="w-6 h-6 bg-[#EE4D2D] text-white rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">
                                                    {{ step }}
                                                </div>
                                                <p class="text-sm text-gray-600">
                                                    {{ t(`Views.Checkout.payment.shopeePay.instructions.step${step}`) }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Security & Info -->
                                    <div
                                        class="bg-gradient-to-r from-[#FFF5F0] to-[#FFE8E0] border border-[#FFD4C4] rounded-lg p-4">
                                        <div class="flex items-start gap-3">
                                            <svg class="w-5 h-5 text-[#EE4D2D] mt-0.5 flex-shrink-0" fill="none"
                                                stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                            </svg>
                                            <div class="flex-1">
                                                <p class="text-sm font-semibold text-[#EE4D2D] mb-1">
                                                    {{ t('Views.Checkout.payment.shopeePay.securityTitle') }}
                                                </p>
                                                <p class="text-xs text-gray-600">
                                                    {{ t('Views.Checkout.payment.shopeePay.securityDescription') }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- ZaloPay Payment Form -->
                            <div v-if="paymentMethod === 'zalopay'"
                                class="mt-6 border border-gray-200 rounded-lg overflow-hidden">
                                <!-- ZaloPay Header -->
                                <div class="bg-gradient-to-r from-[#0068FF] to-[#0084FF] px-6 py-4">
                                    <div class="flex items-center gap-3">
                                        <div
                                            class="w-10 h-10 bg-white rounded-full flex items-center justify-center overflow-hidden">
                                            <img :src="zalopayIcon" alt="ZaloPay"
                                                class="w-full h-full object-contain" />
                                        </div>
                                        <div>
                                            <h3 class="text-white font-bold text-lg">{{
                                                t('Views.Checkout.payment.zaloPay.headerTitle') }}</h3>
                                            <p class="text-white/80 text-sm">{{
                                                t('Views.Checkout.payment.zaloPay.headerDescription') }}</p>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZaloPay Content -->
                                <div class="p-6 bg-white">
                                    <!-- Phone Input -->
                                    <div class="mb-6">
                                        <label class="block text-sm font-semibold text-gray-700 mb-2">
                                            {{ t('Views.Checkout.payment.zaloPay.phoneLabel') }}
                                        </label>
                                        <div class="relative">
                                            <div
                                                class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor"
                                                    viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                                </svg>
                                            </div>
                                            <input type="tel" v-model="zalopayInfo.phoneNumber"
                                                :placeholder="t('Views.Checkout.payment.zaloPay.phonePlaceholder')"
                                                class="w-full pl-12 pr-4 py-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0068FF] focus:border-[#0068FF] transition-colors"
                                                :maxlength="10" @input="formatZaloPayPhone" />
                                        </div>
                                        <p class="mt-2 text-xs text-gray-500">
                                            {{ t('Views.Checkout.payment.zaloPay.phoneHint') }}
                                        </p>
                                    </div>

                                    <!-- Payment Instructions -->
                                    <div class="mb-6">
                                        <h4 class="text-sm font-semibold text-gray-700 mb-3">
                                            {{ t('Views.Checkout.payment.zaloPay.instructionsTitle') }}
                                        </h4>
                                        <div class="space-y-2">
                                            <div class="flex items-start gap-3" v-for="step in zaloPayInstructionSteps"
                                                :key="`zalo-step-${step}`">
                                                <div
                                                    class="w-6 h-6 bg-[#0068FF] text-white rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">
                                                    {{ step }}
                                                </div>
                                                <p class="text-sm text-gray-600">
                                                    {{ t(`Views.Checkout.payment.zaloPay.instructions.step${step}`) }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Security & Info -->
                                    <div
                                        class="bg-gradient-to-r from-[#E6F2FF] to-[#D0E7FF] border border-[#B3D9FF] rounded-lg p-4">
                                        <div class="flex items-start gap-3">
                                            <svg class="w-5 h-5 text-[#0068FF] mt-0.5 flex-shrink-0" fill="none"
                                                stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                            </svg>
                                            <div class="flex-1">
                                                <p class="text-sm font-semibold text-[#0068FF] mb-1">
                                                    {{ t('Views.Checkout.payment.zaloPay.securityTitle') }}
                                                </p>
                                                <p class="text-xs text-gray-600">
                                                    {{ t('Views.Checkout.payment.zaloPay.securityDescription') }}
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Security Notice -->
                            <div class="mt-4 p-4 bg-gray-50 rounded-lg">
                                <div class="flex items-start gap-3">
                                    <svg class="w-5 h-5 text-gray-600 mt-0.5 flex-shrink-0" fill="none"
                                        stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                    </svg>
                                    <p class="text-sm text-gray-600">
                                        {{ t('Views.Checkout.payment.securityNotice') }}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Order Review -->
                    <div v-else-if="currentStep === 3" class="space-y-6">
                        <!-- Shipping Info Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">{{
                                t('Views.Checkout.review.shippingInfoTitle') }}</h2>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                <div>
                                    <p class="text-gray-600">{{ t('Views.Checkout.review.labels.fullName') }}</p>
                                    <p class="font-semibold text-black">{{ shippingForm.fullName }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">{{ t('Views.Checkout.review.labels.phone') }}</p>
                                    <p class="font-semibold text-black">{{ shippingForm.phone }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">{{ t('Views.Checkout.review.labels.email') }}</p>
                                    <p class="font-semibold text-black">{{ shippingForm.email }}</p>
                                </div>
                                <div>
                                    <p class="text-gray-600">{{ t('Views.Checkout.review.labels.address') }}</p>
                                    <p class="font-semibold text-black">
                                        {{ shippingForm.address }}, {{ shippingForm.ward }}, {{ shippingForm.district
                                        }},
                                        {{ shippingForm.city }}
                                    </p>
                                </div>
                                <div v-if="shippingForm.note">
                                    <p class="text-gray-600">{{ t('Views.Checkout.review.labels.note') }}</p>
                                    <p class="font-semibold text-black">{{ shippingForm.note }}</p>
                                </div>
                            </div>
                        </div>

                        <!-- Payment Method Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">{{
                                t('Views.Checkout.review.paymentMethodTitle') }}</h2>
                            <div class="flex items-center justify-between">
                                <div>
                                    <p class="font-semibold text-black">{{ getPaymentMethodLabel(paymentMethod) }}</p>
                                    <p class="text-sm text-gray-600">{{ getPaymentMethodDescription(paymentMethod) }}
                                    </p>
                                </div>
                                <button @click="currentStep = 2"
                                    class="text-black hover:text-gray-700 transition-colors">
                                    {{ t('Views.Checkout.review.editButton') }}
                                </button>
                            </div>
                        </div>

                        <!-- Order Items Review -->
                        <div class="bg-white border border-gray-200 rounded-lg p-6">
                            <h2 class="text-xl font-bold text-black mb-4">{{ t('Views.Checkout.review.productsTitle') }}
                            </h2>
                            <div class="space-y-4">
                                <div v-for="item in cartItems" :key="item.id"
                                    class="flex items-center gap-4 py-3 border-b border-gray-100 last:border-b-0">
                                    <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded-lg" />
                                    <div class="flex-1">
                                        <h3 class="font-semibold text-black">{{ item.name }}</h3>
                                        <p class="text-sm text-gray-600">{{ item.brand }}</p>
                                        <p class="text-sm text-gray-600">
                                            {{ t('Views.Checkout.review.sizeLabel') }} {{ item.size }} |
                                            {{ t('Views.Checkout.review.colorLabel') }} {{ item.color }}
                                        </p>
                                    </div>
                                    <div class="text-right">
                                        <p class="font-semibold text-black">{{ formatPrice(item.price * item.quantity)
                                        }}</p>
                                        <p class="text-sm text-gray-600">{{ t('Views.Checkout.review.quantityLabel') }}
                                            {{ item.quantity }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column - Order Summary -->
                <div class="lg:w-1/3">
                    <div class="bg-white border border-gray-200 rounded-lg p-6 sticky top-4">
                        <h2 class="text-xl font-bold text-black mb-6">{{ t('Views.Checkout.summary.title') }}</h2>

                        <!-- Order Items -->
                        <div class="space-y-3 mb-6">
                            <div v-for="item in cartItems" :key="item.id" class="flex items-center gap-3">
                                <img :src="item.image" :alt="item.name" class="w-12 h-12 object-cover rounded" />
                                <div class="flex-1 min-w-0">
                                    <p class="font-medium text-black text-sm truncate">{{ item.name }}</p>
                                    <p class="text-gray-600 text-xs">
                                        {{ t('Views.Checkout.summary.sizePrefix') }} {{ item.size }} |
                                        {{ t('Views.Checkout.summary.quantityPrefix') }} {{ item.quantity }}
                                    </p>
                                </div>
                                <p class="font-semibold text-black text-sm whitespace-nowrap">
                                    {{ formatPrice(item.price * item.quantity) }}
                                </p>
                            </div>
                        </div>

                        <!-- Pricing -->
                        <div class="space-y-2 border-t border-gray-200 pt-4">
                            <div class="flex justify-between text-sm">
                                <span class="text-gray-600">{{ t('Views.Checkout.summary.subtotal') }}</span>
                                <span class="text-black">{{ formatPrice(subtotal) }}</span>
                            </div>

                            <div class="flex justify-between text-sm">
                                <span class="text-gray-600">{{ t('Views.Checkout.summary.shippingFee') }}</span>
                                <span class="text-black">{{ shippingFee > 0 ? formatPrice(shippingFee) :
                                    t('Views.Checkout.summary.freeShipping') }}</span>
                            </div>

                            <div class="flex justify-between text-lg font-bold border-t border-gray-200 pt-3 mt-2">
                                <span class="text-black">{{ t('Views.Checkout.summary.total') }}</span>
                                <span class="text-black">{{ formatPrice(total) }}</span>
                            </div>
                        </div>

                        <!-- Action Button -->
                        <Button :variant="'primary'" @click="handleAction" class="w-full mt-6">
                            {{ actionButtonText }}
                        </Button>

                        <button v-if="currentStep > 1" @click="goToPreviousStep"
                            class="w-full mt-3 text-sm text-gray-600 hover:text-black transition-colors">
                            {{ t('Views.Checkout.summary.previousStep') }}
                        </button>

                        <!-- Security Badge -->
                        <div class="mt-4 text-center">
                            <div class="flex items-center justify-center gap-2 text-sm text-gray-600">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                </svg>
                                <span>{{ t('Views.Checkout.payment.securityBadge') }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Success Modal -->
        <div v-if="showSuccessModal" class="fixed inset-0 z-50 overflow-y-auto">
            <div class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
                <!-- Background -->
                <div class="fixed inset-0 bg-black bg-opacity-50 transition-opacity" @click="handleSuccessModalClose">
                </div>

                <!-- Modal Panel -->
                <div
                    class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div class="text-center p-8">
                            <div
                                class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                                <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                            </div>

                            <h2 class="text-2xl font-bold text-black mb-4">{{ $t('CheckoutLayout.orderSuccess') }}</h2>
                            <p class="text-gray-600 mb-2">{{ $t('CheckoutLayout.thankYou') }}</p>
                            <p class="text-gray-600 mb-6">{{ $t('CheckoutLayout.orderId') }} <strong
                                    class="text-black">{{ orderResult?.id
                                    }}</strong></p>

                            <div class="bg-gray-50 rounded-lg p-4 mb-6 text-left">
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-gray-600">{{ t('Views.Checkout.successModal.totalLabel') }}</span>
                                    <span class="text-xl font-bold text-black">{{ formatPrice(orderResult?.total || 0)
                                    }}</span>
                                </div>
                                <div class="flex justify-between items-center text-sm">
                                    <span class="text-gray-600">{{
                                        t('Views.Checkout.successModal.deliveryEstimateLabel') }}</span>
                                    <span class="text-black">{{ formatDate(orderResult?.estimatedDelivery) }}</span>
                                </div>
                            </div>

                            <div class="flex gap-4 justify-center">
                                <Button :variant="'outline'" @click="handleSuccessModalClose">
                                    {{ t('Views.Checkout.successModal.continueShopping') }}
                                </Button>
                                <Button :variant="'primary'" @click="viewOrder">
                                    {{ t('Views.Checkout.successModal.viewOrder') }}
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useOrderStore } from '@/stores/order';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import { useToast } from '@/composables/useToast';
import PaymentService from '@/api-services/PaymentService';
import { useI18n } from 'vue-i18n';

// Import các component UI
import InputField from '@/components/FormInput.vue';
import Button from '@/components/Button.vue';

// Import payment icons
import shopeePayIcon from '@/assets/icons/ShopeePay-B.jpg';
import zalopayIcon from '@/assets/icons/zalopay.png';

const router = useRouter();
const orderStore = useOrderStore();
const authStore = useAuthStore();
const toast = useToast();
const { t } = useI18n();

// Step management
const currentStep = ref(1);

// Form data
const shippingForm = ref({
    fullName: '',
    phone: '',
    email: '',
    address: '',
    city: '',
    district: '',
    ward: '',
    note: '',
    shippingMethod: 'standard'
});

const paymentMethod = ref('cod');
const cardInfo = ref({
    number: '',
    name: '',
    expiry: '',
    cvv: ''
});
const momoInfo = ref({
    phoneNumber: ''
});
const shopeePayInfo = ref({
    phoneNumber: ''
});
const zalopayInfo = ref({
    phoneNumber: ''
});

// Cart data - default sample data
const defaultCartItems = [
    {
        id: 1,
        productId: 1,
        name: 'Nike Air Force 1',
        brand: 'Nike',
        price: 2200000,
        image: '/images/shoes/nike-air-max-3.jpg',
        size: 42,
        color: 'Trắng',
        quantity: 1
    },
    {
        id: 2,
        productId: 2,
        name: 'Adidas Ultraboost 22',
        brand: 'Adidas',
        price: 4500000,
        image: '/images/shoes/adidas-ultraboost-1.jpg',
        size: 41,
        color: 'Đen',
        quantity: 2
    }
];

const cartItems = ref([]);

// UI state
const showSuccessModal = ref(false);
const orderResult = ref(null);

// Constants
const steps = computed(() => ([
    { number: 1, label: t('Views.Checkout.steps.shipping') },
    { number: 2, label: t('Views.Checkout.steps.payment') },
    { number: 3, label: t('Views.Checkout.steps.review') }
]));

const shippingOptions = computed(() => ([
    {
        value: 'standard',
        label: t('Views.Checkout.shipping.methods.standard.label'),
        description: t('Views.Checkout.shipping.methods.standard.description'),
        price: t('Views.Checkout.shipping.methods.standard.price')
    },
    {
        value: 'express',
        label: t('Views.Checkout.shipping.methods.express.label'),
        description: t('Views.Checkout.shipping.methods.express.description'),
        price: t('Views.Checkout.shipping.methods.express.price')
    },
    {
        value: 'pickup',
        label: t('Views.Checkout.shipping.methods.pickup.label'),
        description: t('Views.Checkout.shipping.methods.pickup.description'),
        price: t('Views.Checkout.shipping.methods.pickup.price')
    }
]));

const paymentOptions = computed(() => ([
    {
        value: 'cod',
        label: t('Views.Checkout.payment.options.cod.label'),
        description: t('Views.Checkout.payment.options.cod.description')
    },
    {
        value: 'credit_card',
        label: t('Views.Checkout.payment.options.creditCard.label'),
        description: t('Views.Checkout.payment.options.creditCard.description')
    },
    {
        value: 'bank_transfer',
        label: t('Views.Checkout.payment.options.bankTransfer.label'),
        description: t('Views.Checkout.payment.options.bankTransfer.description')
    },
    {
        value: 'momo',
        label: t('Views.Checkout.payment.options.momo.label'),
        description: t('Views.Checkout.payment.options.momo.description')
    },
    {
        value: 'shopee_pay',
        label: t('Views.Checkout.payment.options.shopeePay.label'),
        description: t('Views.Checkout.payment.options.shopeePay.description')
    },
    {
        value: 'zalopay',
        label: t('Views.Checkout.payment.options.zaloPay.label'),
        description: t('Views.Checkout.payment.options.zaloPay.description')
    }
]));

const momoInstructionSteps = [1, 2, 3, 4];
const shopeePayInstructionSteps = [1, 2, 3];
const zaloPayInstructionSteps = [1, 2, 3];

// Computed
const shippingFee = computed(() => {
    let base = 0;
    if (shippingForm.value.shippingMethod === 'standard') base = 30000;
    else if (shippingForm.value.shippingMethod === 'express') base = 50000;
    else if (shippingForm.value.shippingMethod === 'pickup') base = 0;

    // Miễn phí nếu vượt ngưỡng
    if (subtotal.value > 5000000) return 0;
    return base;
});

const subtotal = computed(() => {
    return cartItems.value.reduce((total, item) => total + (item.price * item.quantity), 0);
});

const total = computed(() => {
    return subtotal.value + shippingFee.value;
});

const actionButtonText = computed(() => {
    switch (currentStep.value) {
        case 1:
            return t('Views.Checkout.actions.nextToPayment');
        case 2:
            return t('Views.Checkout.actions.nextToReview');
        case 3:
            return t('Views.Checkout.actions.placeOrder');
        default:
            return t('Views.Checkout.actions.continue');
    }
});

// Methods
const getStepClass = (stepNumber) => {
    if (stepNumber < currentStep.value) {
        return 'bg-black border-black text-white';
    } else if (stepNumber === currentStep.value) {
        return 'border-black bg-white text-black';
    } else {
        return 'border-gray-300 bg-white text-gray-400';
    }
};

const validateShipping = () => {
    const required = ['fullName', 'phone', 'email', 'address', 'city', 'district', 'ward'];
    return required.every(field => shippingForm.value[field].trim() !== '');
};

const goToNextStep = () => {
    if (currentStep.value === 1 && !validateShipping()) {
        toast.warning(t('Views.Checkout.toasts.fillShipping'));
        return;
    }

    // Validate payment phone numbers if e-wallet is selected
    if (currentStep.value === 2) {
        if (paymentMethod.value === 'momo') {
            if (!momoInfo.value.phoneNumber || momoInfo.value.phoneNumber.length !== 10) {
                toast.warning(t('Views.Checkout.toasts.invalidMomoPhone'));
                return;
            }
        } else if (paymentMethod.value === 'shopee_pay') {
            if (!shopeePayInfo.value.phoneNumber || shopeePayInfo.value.phoneNumber.length !== 10) {
                toast.warning(t('Views.Checkout.toasts.invalidShopeePayPhone'));
                return;
            }
        } else if (paymentMethod.value === 'zalopay') {
            if (!zalopayInfo.value.phoneNumber || zalopayInfo.value.phoneNumber.length !== 10) {
                toast.warning(t('Views.Checkout.toasts.invalidZaloPayPhone'));
                return;
            }
        }
    }

    if (currentStep.value < 3) {
        currentStep.value++;
    } else {
        placeOrder();
    }
};

const goToPreviousStep = () => {
    if (currentStep.value > 1) {
        currentStep.value--;
    }
};

const handleAction = () => {
    if (currentStep.value === 3) {
        placeOrder();
    } else {
        goToNextStep();
    }
};

const placeOrder = async () => {
    try {
        // Kiểm tra user đã đăng nhập chưa
        if (!authStore.user) {
            toast.warning(t('Views.Checkout.toasts.loginRequired'));
            router.push('/login');
            return;
        }

        const deliveryDays = 5 + Math.floor(Math.random() * 2); // Random 5 hoặc 6 ngày
        const estimatedDelivery = new Date(Date.now() + deliveryDays * 24 * 60 * 60 * 1000).toISOString();

        const orderData = {
            user_id: authStore.user.id || authStore.user._id,
            status: 'pending',
            items: cartItems.value.map(item => ({
                productId: item.productId,
                productName: item.name,
                brand: item.brand,
                price: item.price,
                image: item.image,
                size: item.size,
                color: item.color,
                quantity: item.quantity
            })),
            fullName: shippingForm.value.fullName,
            phone: shippingForm.value.phone,
            email: shippingForm.value.email,
            address: shippingForm.value.address,
            city: shippingForm.value.city,
            district: shippingForm.value.district,
            ward: shippingForm.value.ward,
            shippingFee: shippingFee.value,
            shippingMethod: shippingForm.value.shippingMethod,
            note: shippingForm.value.note || '',
            total: total.value,
            paymentMethod: paymentMethod.value,
            estimatedDelivery: estimatedDelivery,
            // Add phone number if e-wallet payment is selected
            ...(paymentMethod.value === 'momo' && momoInfo.value.phoneNumber ? {
                momoPhoneNumber: momoInfo.value.phoneNumber
            } : {}),
            ...(paymentMethod.value === 'shopee_pay' && shopeePayInfo.value.phoneNumber ? {
                shopeePayPhoneNumber: shopeePayInfo.value.phoneNumber
            } : {}),
            ...(paymentMethod.value === 'zalopay' && zalopayInfo.value.phoneNumber ? {
                zalopayPhoneNumber: zalopayInfo.value.phoneNumber
            } : {})
        };

        // Gọi API để tạo đơn hàng
        const result = await orderStore.createOrder(orderData);

        if (!result) {
            throw new Error('order_creation_failed');
        }

        const orderId = result.id || result._id || result.data?.id || result.data?._id;

        // Nếu thanh toán bằng MoMo, tạo payment request và redirect
        if (paymentMethod.value === 'momo') {
            try {
                toast.info(t('Views.Checkout.toasts.creatingMomoPayment'));

                // Tạo payment request
                const paymentResponse = await PaymentService.createMomoPayment({
                    order_id: orderId,
                    phone_number: momoInfo.value.phoneNumber || null,
                    return_url: `${window.location.origin}/payment/success?order_id=${orderId}`,
                    cancel_url: `${window.location.origin}/payment/cancel?order_id=${orderId}`
                });

                if (paymentResponse && paymentResponse.pay_url) {
                    // Redirect đến MoMo payment page
                    window.location.href = paymentResponse.pay_url;
                    return; // Không hiển thị success modal vì đang redirect
                } else {
                    throw new Error('missing_pay_url');
                }
            } catch (error) {
                console.error('Error creating MoMo payment:', error);
                const fallbackMessage = t('Views.Checkout.toasts.createPaymentError');
                toast.error(error?.detail || error?.message || fallbackMessage);

                // Vẫn hiển thị success modal nếu có lỗi payment
                orderResult.value = {
                    id: orderId,
                    total: orderData.total,
                    estimatedDelivery: orderData.estimatedDelivery
                };
                await orderStore.loadOrders();
                showSuccessModal.value = true;
                return;
            }
        }

        // Nếu không phải MoMo (COD, bank transfer, etc.), hiển thị success modal bình thường
        orderResult.value = {
            id: orderId,
            total: orderData.total,
            estimatedDelivery: orderData.estimatedDelivery
        };

        await orderStore.loadOrders();
        showSuccessModal.value = true;
    } catch (error) {
        console.error('Error placing order:', error);
        toast.error(t('Views.Checkout.toasts.placeOrderError'));
    }
};

const handleSuccessModalClose = () => {
    showSuccessModal.value = false;
    router.push('/');
};

const viewOrder = () => {
    // Navigate to order detail page
    showSuccessModal.value = false;
    router.push(`/orders/${orderResult.value.id}`);
};

const formatPrice = (price) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price);
};

const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString('vi-VN');
};

const getPaymentMethodLabel = (method) => {
    const methods = {
        cod: t('Views.Checkout.review.paymentMethods.cod'),
        credit_card: t('Views.Checkout.review.paymentMethods.creditCard'),
        bank_transfer: t('Views.Checkout.review.paymentMethods.bankTransfer'),
        momo: t('Views.Checkout.review.paymentMethods.momo'),
        shopee_pay: t('Views.Checkout.review.paymentMethods.shopeePay'),
        zalopay: t('Views.Checkout.review.paymentMethods.zaloPay')
    };
    return methods[method] || method;
};

const getPaymentMethodDescription = (method) => {
    const descriptions = {
        cod: t('Views.Checkout.review.paymentDescriptions.cod'),
        credit_card: t('Views.Checkout.review.paymentDescriptions.creditCard'),
        bank_transfer: t('Views.Checkout.review.paymentDescriptions.bankTransfer'),
        momo: t('Views.Checkout.review.paymentDescriptions.momo'),
        shopee_pay: t('Views.Checkout.review.paymentDescriptions.shopeePay'),
        zalopay: t('Views.Checkout.review.paymentDescriptions.zaloPay')
    };
    return descriptions[method] || '';
};

// Format phone number for MoMo (only numbers, max 10 digits)
const formatPhoneNumber = (event) => {
    let value = event.target.value.replace(/\D/g, ''); // Remove non-digits
    if (value.length > 10) {
        value = value.slice(0, 10);
    }
    momoInfo.value.phoneNumber = value;
    event.target.value = value;
};

// Format phone number for ShopeePay (only numbers, max 10 digits)
const formatShopeePayPhone = (event) => {
    let value = event.target.value.replace(/\D/g, ''); // Remove non-digits
    if (value.length > 10) {
        value = value.slice(0, 10);
    }
    shopeePayInfo.value.phoneNumber = value;
    event.target.value = value;
};

// Format phone number for ZaloPay (only numbers, max 10 digits)
const formatZaloPayPhone = (event) => {
    let value = event.target.value.replace(/\D/g, ''); // Remove non-digits
    if (value.length > 10) {
        value = value.slice(0, 10);
    }
    zalopayInfo.value.phoneNumber = value;
    event.target.value = value;
};

// Lifecycle
onMounted(() => {
    if (orderStore.checkoutItems && orderStore.checkoutItems.length > 0) {
        const mapped = orderStore.checkoutItems.map((item, idx) => ({
            id: idx + 1,
            productId: item.productId,
            name: item.meta?.name,
            brand: item.meta?.brand,
            price: item.meta?.price,
            image: item.meta?.image,
            size: item.size,
            color: item.color,
            quantity: item.quantity || 1
        }));
        cartItems.value = mapped;
    } else {
        const savedCart = localStorage.getItem('cart')
        if (savedCart) {
            try {
                cartItems.value = JSON.parse(savedCart)
            } catch (e) {
                cartItems.value = defaultCartItems
            }
        } else {
            cartItems.value = defaultCartItems
        }
    }

    // Redirect if no items
    if (cartItems.value.length === 0) {
        router.push('/cart');
    }
});
</script>