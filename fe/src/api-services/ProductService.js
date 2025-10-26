// src/api/ProductService.js
import BaseAxios from "./BaseAxios";

const PREFIX_PRODUCT = "products";

const ProductService = {
    async getAll(data) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_PRODUCT}/get-all`, {
                params: data,
                withCredentials: true,
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    async create(productData) {
        try {
            const response = await BaseAxios.post(`${PREFIX_PRODUCT}/create`, productData);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    async update(productId, productData) {
        try {
            const response = await BaseAxios.put(`${PREFIX_PRODUCT}/update/${productId}`, productData);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    async delete(productId) {
        try {
            const response = await BaseAxios.delete(`${PREFIX_PRODUCT}/delete/${productId}`);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    async getById(productId) {
        try {
            const response = await BaseAxios.get(`/${PREFIX_PRODUCT}/detail/${productId}`);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    async uploadImages(productId, formData) {
        try {
            const response = await BaseAxios.post(`${PREFIX_PRODUCT}/${productId}/upload-images`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            return response.data;
        } catch (error) {
            throw error;
        }
    },
    async getTopBrand(brand) {
        try {
            const response = await BaseAxios.get(`${PREFIX_PRODUCT}/top-rated-by-brand`, {
                params: { brand: brand },  // Truyền brand qua query params
                withCredentials: true
            });
            debugger;
            console.log(response);
            return response.data;
        } catch (error) {
            throw error;
        }
    },
    async getTopRate() {
        try {
            const response = await BaseAxios.get(`${PREFIX_PRODUCT}/top-rated`);
            debugger;
            console.log(response);
            return response.data;
        } catch (error) {
            throw error;
        }
    },
};

export default ProductService;
