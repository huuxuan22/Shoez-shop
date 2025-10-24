import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const getProductUrl = (productId) => `${API_URL}/api/products/${productId}`

export const createProduct = (payload) => {
    return axios.post(`${API_URL}/products/create`, payload)
}

export const uploadProductImages = (productId, formData) => {
    return axios.post(`${getProductUrl(productId)}/upload-images`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    })
}

export default {
    API_URL,
    getProductUrl,
    createProduct,
    uploadProductImages,
}
