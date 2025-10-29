import BaseAxios from "./BaseAxios";

const PREFIX = "favourite";

const FavouriteService = {
    async getFavourite(user_id) {
        const res = await BaseAxios.get(`/${PREFIX}/${user_id}`);
        return res.data;
    },
    async addFavourite(user_id, product_id) {
        const res = await BaseAxios.post(`/${PREFIX}/add`, {
            user_id,
            product: [product_id],
        });
        return res.data;
    },
    async removeFavourite(user_id, product_id) {
        const res = await BaseAxios.post(`/${PREFIX}/remove`, {
            user_id,
            product: [product_id],
        });
        return res.data;
    },
};

export default FavouriteService;
