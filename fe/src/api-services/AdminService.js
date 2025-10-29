import BaseAxios from "./BaseAxios";

const AdminService = {
    /**
     * Đánh dấu admin đã respond to low rating review
     */
    async respondToLowRatingReview(reviewId) {
        try {
            const response = await BaseAxios.post(
                `/admin/low-rating-reviews/respond/${reviewId}`,
                {},
                {
                    withCredentials: true
                }
            );
            return response.data;
        } catch (error) {
            throw error;
        }
    }
};

export default AdminService;
