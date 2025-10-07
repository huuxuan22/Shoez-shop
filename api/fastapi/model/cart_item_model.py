from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship



class CartItem():
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    total_price = Column(Integer)

    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    size_id = Column(Integer, ForeignKey('sizes.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('colors.id'), nullable=False)

    product = relationship("Product")
    size = relationship("Size")
    color = relationship("Color")
    cart = relationship("Cart")

