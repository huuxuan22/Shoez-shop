from sqlalchemy import Column, Integer, String, ForeignKey, UUID
from sqlalchemy.orm import relationship, backref


class Comment():
    __tablename__ = "comments"

    id = Column(Integer, autoincrement=True, primary_key=True)
    content = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(UUID, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("comments.id"))

    parent = relationship("Comment", remote_side=[id],backref="comments")



