from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship



class OrderItem():
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True,autoincrement=True)
    quantity = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.id"))
    size_id = Column(Integer, ForeignKey("sizes.id"))
    color_id = Column(Integer, ForeignKey("colors.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

