// src/api/ProductService.js
import BaseAxios from "./BaseAxios";

const PREFIX_PRODUCT = "products";

const ProductService = {
    async getAll(data) {
        try {
            debugger;
            const response = await BaseAxios.get(`/${PREFIX_PRODUCT}/get-all`, {
                params: data,
                withCredentials: true,
            });
            return response;
        } catch (error) {
            console.error("❌ Fetch products failed:", error);
            throw error;
        }
    },

    // ➕ Thêm mới sản phẩm
    async create(productData) {
        try {
            const response = await BaseAxios.post(`${PREFIX_PRODUCT}/create`, productData);
            return response.data;
        } catch (error) {
            console.error("❌ Create product failed:", error);
            throw error;
        }
    },

    // ✏️ Cập nhật sản phẩm
    async update(productId, productData) {
        try {
            const response = await BaseAxios.put(`${PREFIX_PRODUCT}/update/${productId}`, productData);
            return response.data;
        } catch (error) {
            console.error("❌ Update product failed:", error);
            throw error;
        }
    },

    // 🗑️ Xóa sản phẩm
    async delete(productId) {
        try {
            const response = await BaseAxios.delete(`${PREFIX_PRODUCT}/delete/${productId}`);
            return response.data;
        } catch (error) {
            console.error("❌ Delete product failed:", error);
            throw error;
        }
    },

    // 🔍 Lấy chi tiết sản phẩm theo ID
    async getById(productId) {
        try {
            const response = await BaseAxios.get(`${PREFIX_PRODUCT}/${productId}`);
            return response.data;
        } catch (error) {
            console.error("❌ Get product by ID failed:", error);
            throw error;
        }
    },
};

export default ProductService;
