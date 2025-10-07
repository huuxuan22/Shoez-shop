<template>
  <div class="form-group">
    <label
      v-if="label"
      :for="name"
      class="block text-sm font-medium text-gray-700 mb-1"
    >
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>

    <div class="relative">
      <input
        :id="name"
        :name="name"
        :type="type"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        @input="handleInput"
        @blur="handleBlur"
        class="block w-full px-4 py-3 border rounded-lg shadow-sm focus:outline-none transition-all"
        :class="[
          inputClasses,
          {
            'border-gray-300 focus:ring-blue-500 focus:border-blue-500':
              !errorMessage,
            'border-red-300 text-red-900 focus:ring-red-500 focus:border-red-500':
              errorMessage,
            'bg-gray-100 cursor-not-allowed': disabled,
          },
        ]"
      />

      <!-- Icon slot -->
      <div
        v-if="$slots.icon"
        class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none"
      >
        <slot name="icon" />
      </div>
    </div>

    <!-- Validation messages -->
    <div v-if="errorMessage || hint" class="mt-1">
      <p v-if="errorMessage" class="text-sm text-red-600">
        {{ errorMessage }}
      </p>
      <p v-else-if="hint" class="text-sm text-gray-500">
        {{ hint }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  modelValue: {
    type: [String, Number],
    default: "",
  },
  name: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    default: "",
  },
  type: {
    type: String,
    default: "text",
  },
  placeholder: {
    type: String,
    default: "",
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  required: {
    type: Boolean,
    default: false,
  },
  hint: {
    type: String,
    default: "",
  },
  errorMessage: {
    type: String,
    default: "",
  },
  inputClasses: {
    type: String,
    default: "",
  },
});

const emit = defineEmits(["update:modelValue", "input", "blur"]);

const handleInput = (event) => {
  emit("update:modelValue", event.target.value);
  emit("input", event);
};

const handleBlur = (event) => {
  emit("blur", event);
};
</script>
