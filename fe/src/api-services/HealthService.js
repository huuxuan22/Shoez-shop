import BaseAxios from "./BaseAxios";

const HealthService = {
    async check() {
        const res = await BaseAxios.get("/health");
        return res.data;
    }
};

export default HealthService;


