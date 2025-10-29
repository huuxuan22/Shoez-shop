import BaseAxios from "./BaseAxios";

const PREFIX = "/favourite";

export const getFavouritesApi = (userId) => {
  return BaseAxios.get(`${PREFIX}/${userId}`);
};

export const addFavouriteApi = (userId, productId) => {
  return BaseAxios.post(`${PREFIX}/add`, {
    user_id: userId,
    product: [productId],
  });
};

export const removeFavouriteApi = (userId, productId) => {
  return BaseAxios.post(`${PREFIX}/remove`, {
    user_id: userId,
    product: [productId],
  });
};

export default {
  getFavouritesApi,
  addFavouriteApi,
  removeFavouriteApi,
};


