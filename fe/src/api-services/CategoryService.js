import BaseAxios from "./BaseAxios";

const PREFIX = "categories";

const CategoryService = {
  /**
   * Lấy tất cả danh mục
   */
  async getAll() {
    try {
      const response = await BaseAxios.get(`/${PREFIX}`, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Lấy danh mục theo ID
   */
  async getById(id) {
    try {
      const response = await BaseAxios.get(`/${PREFIX}/${id}`, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Tạo danh mục mới
   */
  async create(data) {
    try {
      const response = await BaseAxios.post(`/${PREFIX}`, data, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Cập nhật danh mục
   */
  async update(id, data) {
    try {
      const response = await BaseAxios.put(`/${PREFIX}/${id}`, data, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Xóa danh mục
   */
  async delete(id) {
    try {
      const response = await BaseAxios.delete(`/${PREFIX}/${id}`, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default CategoryService;

