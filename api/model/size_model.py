
from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship



class Size():
    __tablename__ = "sizes"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    product_varaint = relationship("ProductVariant", backref="sizes")
    order_item = relationship("OrderItem", backref="sizes")
    cart_item = relationship("CartItem", backref="sizes")

