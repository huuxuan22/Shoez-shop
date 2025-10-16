<template>
    <button :class="[
        'px-6 py-3 rounded-lg font-semibold transition-all duration-200 flex items-center justify-center',
        variantClasses[variant],
        disabled ? 'opacity-50 cursor-not-allowed' : 'hover:shadow-md'
    ]" :disabled="disabled" @click="$emit('click', $event)">
        <slot />
    </button>
</template>

<script setup>
const props = defineProps({
    variant: {
        type: String,
        default: 'primary',
        validator: (value) => ['primary', 'secondary', 'outline'].includes(value)
    },
    disabled: {
        type: Boolean,
        default: false
    }
});

defineEmits(['click']);

const variantClasses = {
    primary: 'bg-black text-white hover:bg-gray-800',
    secondary: 'bg-gray-200 text-black hover:bg-gray-300',
    outline: 'border-2 border-black text-black bg-transparent hover:bg-black hover:text-white'
};
</script>