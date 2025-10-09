from sqlalchemy import Column, Integer, ForeignKey,UUID
from sqlalchemy.orm import relationship, backref



class Cart():
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    cart_item = relationship("CartItem", backref=backref("carts"), cascade="all, delete-orphan")
