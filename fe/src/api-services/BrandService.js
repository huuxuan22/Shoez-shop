import BaseAxios from "./BaseAxios";

const PREFIX = "brands";

const BrandService = {
  /**
   * Lấy tất cả thương hiệu
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
   * Lấy thương hiệu theo ID
   */
  async getById(id) {
    try {
      const response = await BaseAxios.get(`/${PREFIX}/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Tạo thương hiệu mới
   */
  async create(brandData, logoFile = null) {
    try {
      // Validate name
      const name = (brandData.name || '').trim();

      const formData = new FormData();
      formData.append('name', name);
      if (brandData.description) {
        formData.append('description', (brandData.description || '').trim());
      }
      if (logoFile) {
        formData.append('logo_file', logoFile);
      } else if (brandData.logo && !brandData.logo.startsWith('data:')) {
        // Nếu là URL (không phải base64), gửi như logo_url
        formData.append('logo_url', (brandData.logo || '').trim());
      }
      // is_active: FastAPI sẽ tự động convert string thành boolean
      // Gửi 'true' hoặc 'false' dưới dạng string cho Form field
      if (brandData.is_active !== undefined) {
        formData.append('is_active', String(brandData.is_active));
      }
      debugger;

      const response = await BaseAxios.post(`/${PREFIX}/create`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Cập nhật thương hiệu
   */
  async update(brandId, brandData, logoFile = null) {
    try {
      const formData = new FormData();
      if (brandData.name) {
        formData.append('name', brandData.name);
      }
      if (brandData.description !== undefined) {
        formData.append('description', brandData.description || '');
      }
      if (logoFile) {
        formData.append('logo_file', logoFile);
      } else if (brandData.logo && !brandData.logo.startsWith('data:')) {
        // Nếu là URL (không phải base64), gửi như logo_url
        formData.append('logo_url', brandData.logo);
      }
      if (brandData.is_active !== undefined) {
        formData.append('is_active', brandData.is_active);
      }

      const response = await BaseAxios.put(
        `/${PREFIX}/update/${brandId}`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Xóa thương hiệu
   */
  async delete(brandId) {
    try {
      const response = await BaseAxios.delete(`/${PREFIX}/delete/${brandId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Đồng bộ logos từ MinIO vào database (tự động gọi nội bộ)
   */
  async syncLogos() {
    try {
      const response = await BaseAxios.post(`/${PREFIX}/sync-logos`, {}, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default BrandService;

