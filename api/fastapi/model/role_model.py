from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



class Role():
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
