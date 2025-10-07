from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, UUID
from sqlalchemy.orm import relationship



class Order():
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total  = Column(Integer, default=0)
    status = Column(Boolean, default=False)
    payment_method = Column(String)
    shipping = Column(String)
    notes = Column(String)

    user_id = Column(UUID, ForeignKey('users.id'))
    order_item = relationship('OrderItem', backref="orders")

