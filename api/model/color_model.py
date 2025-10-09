from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Color():
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)


