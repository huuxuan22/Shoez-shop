<template>
  <div>
    <button :type="type" @click="onClick"
      class="w-full px-4 py-3 rounded-lg font-medium transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 flex items-center justify-center gap-2"
      :class="[variantClass, isDisabled ? 'opacity-60 cursor-not-allowed' : '']" :disabled="isDisabled">
      <span v-if="loading"
        class="inline-block w-4 h-4 border-2 border-white/80 border-t-transparent rounded-full animate-spin"></span>
      <span v-else>{{ label }}</span>
    </button>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    default: "button",
  },
  variant: {
    // Sửa lỗi chính tả từ "varriant" -> "variant"
    type: String,
    default: "primary",
  },
  loading: {
    type: Boolean,
    default: false,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["click"]);

const onClick = () => {
  emit("click");
};

// Style button theo variant
const variantClass = computed(() => {
  switch (props.variant) {
    case "primary":
      return "bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500 shadow hover:shadow-md";
    case "secondary":
      return "bg-gray-200 text-gray-700 hover:bg-gray-300 focus:ring-gray-500";
    case "danger":
      return "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500";
    case "black":
      return "bg-black text-white hover:bg-gray-900 focus:ring-gray-800";
    case "dark":
      return "bg-gray-800 text-white hover:bg-gray-900 focus:ring-gray-700";
    case "slate":
      return "bg-slate-800 text-white hover:bg-slate-900 focus:ring-slate-700";
    case "zinc":
      return "bg-zinc-800 text-white hover:bg-zinc-900 focus:ring-zinc-700";
    case "neutral":
      return "bg-neutral-800 text-white hover:bg-neutral-900 focus:ring-neutral-700";
    default:
      return "bg-blue-600 text-white hover:bg-blue-700";
  }
});

const isDisabled = computed(() => props.disabled || props.loading);
</script>
