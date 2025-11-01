import BaseAxios from "./BaseAxios";

const UserService = {
    // Admin: List users with pagination
    async listUsers({ page = 1, page_size = 10 } = {}) {
        try {
            const response = await BaseAxios.get("/users/get-all", {
                params: { page, page_size }
            });
            return response.data?.user_list || [];
        } catch (error) {
            throw error;
        }
    },

    // Admin: Update user (e.g., role, status, name)
    async adminUpdateUser(payload) {
        try {
            const response = await BaseAxios.put("/users/", payload);
            return response.data?.user_update;
        } catch (error) {
            throw error;
        }
    },

    // Admin: Delete multiple users by ids
    async deleteUsers(ids) {
        try {
            const response = await BaseAxios.delete("/users/", { data: ids });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    // Admin: Lock/Unlock multiple users
    async lockUsers(ids, is_active) {
        try {
            const response = await BaseAxios.patch("/users/admin/lock", { ids, is_active });
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    // Admin: Restore soft-deleted users
    async restoreUsers(ids) {
        try {
            const response = await BaseAxios.patch("/users/admin/restore", { ids });
            return response.data;
        } catch (error) {
            throw error;
        }
    },
    // Update user profile
    async updateProfile(userData) {
        try {
            const response = await BaseAxios.put("/users/", userData);
            return response;
        } catch (error) {
            throw error;
        }
    },

    // Get user profile
    async getProfile(userId) {
        try {
            const response = await BaseAxios.get(`/users/${userId}`);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    // Change password
    async changePassword(passwordData) {
        try {
            const response = await BaseAxios.put("/users/reset-password", passwordData);
            return response.data;
        } catch (error) {
            throw error;
        }
    },

    // Upload avatar
    async uploadAvatar(file, userId) {
        try {
            const formData = new FormData();
            formData.append("user_id", userId);
            formData.append("avatar", file);
            const response = await BaseAxios.post("/users/avatar", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            return response;
        } catch (error) {
            throw error;
        }
    },
};

export default UserService;

