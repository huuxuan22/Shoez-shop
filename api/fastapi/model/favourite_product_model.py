from sqlalchemy import Column, Integer, ForeignKey,UUID
from sqlalchemy.orm import relationship



class FavouriteProduct():
    __tablename__ = "favourite_products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)