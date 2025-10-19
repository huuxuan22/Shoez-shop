import BaseAxios from "./BaseAxios";

const UserService = {
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
            console.error("Upload avatar failed", error);
            throw error;
        }
    },
};

export default UserService;

