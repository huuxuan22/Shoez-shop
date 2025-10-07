
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref



class Category():
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=False)


