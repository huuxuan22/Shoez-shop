from sqlalchemy import Column, Integer, String, Float, ForeignKey, ARRAY
from sqlalchemy.orm import relationship, backref



class Product():
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tym = Column(Integer, nullable=False) # số lượng yêu thích
    dislike = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(ARRAY(String), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    #relation ship
    product_variant  = relationship("ProductVariant", backref=backref("products"), cascade="all, delete-orphan")
    order_item = relationship("OrderItem", backref="products")
    comment = relationship("Comment", backref="products")
    cart_item = relationship("CartItem", backref="products")
    favourite_product = relationship("FavouriteProduct", backref="products")
    product_images = relationship("ProductImages", backref="products")
