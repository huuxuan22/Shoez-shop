<template>
  <div class="max-w-2xl mx-auto p-6 bg-white rounded-2xl shadow-md mt-8">
    <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">{{$t('Admin.AddProduct.title')}}</h2>
    
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.nameLabel')}}</label>
        <input v-model.trim="form.name" class="input" :placeholder="$t('Admin.AddProduct.form.namePlaceholder')" required />
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.brandLabel')}}</label>
        <input v-model.trim="form.brand" class="input" :placeholder="$t('Admin.AddProduct.form.brandPlaceholder')" />
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.categoryLabel')}}</label>
        <input v-model.trim="form.category" class="input" :placeholder="$t('Admin.AddProduct.form.categoryPlaceholder')" />
      </div>
      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.sizesLabel')}}</label>
        <input v-model="form.sizes" class="input mb-3" :placeholder="$t('Admin.AddProduct.form.sizesPlaceholder')" />
      </div>
      <div>
        <textarea v-model.trim="form.description" class="input" :placeholder="$t('Admin.AddProduct.form.descriptionPlaceholder')"></textarea>
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.priceLabel')}}</label>
        <input v-model.number="form.price" type="number" class="input" required min="0" />
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.stockLabel')}}</label>
        <input v-model.number="form.stock" type="number" class="input" min="0" />
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.imagesLabel')}}</label>
        <input type="file" multiple accept="image/*" @change="handleImageChange" class="input" />
        <div class="flex flex-wrap gap-2 mt-2">
          <img v-for="(img, idx) in imagePreviews" :key="idx" :src="img" class="w-20 h-20 object-cover rounded border" />
        </div>
      </div>

      <div>
        <label class="block font-semibold mb-1">{{$t('Admin.AddProduct.form.colorsLabel')}}</label>
        <input v-model="form.colors" class="input" :placeholder="$t('Admin.AddProduct.form.colorsPlaceholder')" />
      </div>

      <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition">
        {{$t('Admin.AddProduct.form.submitButton')}}
      </button>
    </form>

    <div v-if="message" :class="{'text-green-600': success, 'text-red-600': !success}" class="mt-4 font-semibold text-center">
      {{ message }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import axios from 'axios'
import { getProductUrl } from '../../api/api.js'
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const { t: $t } = useI18n()

const form = ref({
  name: '',
  brand: '',
  category: '',
  description: '',
  price: 0,
  stock: 0,
  colors: '',
  sizes: ''
})
const imageFiles = ref([])
const imagePreviews = ref([])
const message = ref('')
const success = ref(false)

const handleImageChange = (e) => {
  imageFiles.value = Array.from(e.target.files)
  imagePreviews.value = []
  imageFiles.value.forEach(file => {
    const reader = new FileReader()
    reader.onload = ev => imagePreviews.value.push(ev.target.result)
    reader.readAsDataURL(file)
  })
}

const handleSubmit = async () => {
  try {
    // Bước 1: Tạo sản phẩm (chưa có ảnh)
    const payload = {
      ...form.value,
      images: [],
      colors: form.value.colors.split(',').map(s => s.trim()).filter(Boolean),
      sizes: form.value.sizes.split(',').map(s => ({ size: parseInt(s.trim()), stock: form.value.stock }))
    }
    const res = await axios.post(`${API_URL}/api/products/create`, payload)
    const productId = res.data.id || res.data._id

    // Bước 2: Upload ảnh nếu có
    if (imageFiles.value.length > 0 && productId) {
      const formData = new FormData()
      imageFiles.value.forEach(f => formData.append('files', f))
      await axios.post(`${getProductUrl(productId)}/upload-images`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
    }

    message.value = $t('Admin.AddProduct.messages.success')
    success.value = true
    Object.assign(form.value, {
      name: '', brand: '', category: '', description: '', price: 0, stock: 0, colors: '', sizes: ''
    })
    imageFiles.value = []
    imagePreviews.value = []
  } catch (err) {
    message.value = $t('Admin.AddProduct.messages.error')
    success.value = false
  }
}
</script>

<style scoped>
.input {
  width: 100%;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  padding: 0.5rem 0.75rem;
  transition: box-shadow 0.2s;
  outline: none;
  background: #fff;
}
.input:focus {
  box-shadow: 0 0 0 2px #60a5fa;
  border-color: #60a5fa;
}
</style>

