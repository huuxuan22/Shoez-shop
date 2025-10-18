import BaseAxios from "./BaseAxios";

const UserService = {
    // Update user profile
    async updateProfile(userData) {
        try {
            const response = await BaseAxios.put("/users/", userData);
            return response;
        } catch (error) {
            console.error("❌ Update profile failed:", error);
            throw error;
        }
    },

    // Get user profile
    async getProfile(userId) {
        try {
            const response = await BaseAxios.get(`/users/${userId}`);
            return response.data;
        } catch (error) {
            console.error("❌ Get profile failed:", error);
            throw error;
        }
    },

    // Change password
    async changePassword(passwordData) {
        try {
            const response = await BaseAxios.put("/users/password", passwordData);
            return response.data;
        } catch (error) {
            console.error("❌ Change password failed:", error);
            throw error;
        }
    },

    // Upload avatar
    async uploadAvatar(file) {
        try {
            const formData = new FormData();
            formData.append("avatar", file);

            const response = await BaseAxios.post("/users/avatar", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            return response.data;
        } catch (error) {
            console.error("❌ Upload avatar failed:", error);
            throw error;
        }
    },
};

export default UserService;

