import BaseAxios from './BaseAxios';

const PREFIX_PAYMENT = 'payments';

const PaymentService = {
    /**
     * Tạo MoMo payment request
     * @param {Object} paymentData - Thông tin payment
     * @param {string} paymentData.order_id - ID đơn hàng
     * @param {string} [paymentData.phone_number] - Số điện thoại MoMo
     * @param {string} [paymentData.return_url] - URL redirect sau khi thanh toán thành công
     * @param {string} [paymentData.cancel_url] - URL redirect khi hủy thanh toán
     * @returns {Promise<Object>} Payment response với pay_url
     */
    async createMomoPayment(paymentData) {
        try {
            const response = await BaseAxios.post(
                `/${PREFIX_PAYMENT}/momo/create`,
                paymentData
            );
            return response.data;
        } catch (error) {
            console.error('Error creating MoMo payment:', error);
            throw error.response?.data || error.message || 'Failed to create payment';
        }
    },

    /**
     * Lấy trạng thái thanh toán của đơn hàng
     * @param {string} orderId - ID đơn hàng
     * @returns {Promise<Object>} Payment status
     */
    async getPaymentStatus(orderId) {
        try {
            const response = await BaseAxios.get(
                `/${PREFIX_PAYMENT}/momo/status/${orderId}`
            );
            return response.data;
        } catch (error) {
            console.error('Error getting payment status:', error);
            throw error.response?.data || error.message || 'Failed to get payment status';
        }
    }
};

export default PaymentService;

