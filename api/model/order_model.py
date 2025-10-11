from typing import List
from pydantic import Field
from datetime import datetime

from model import Product
from model.mongodb_base_model import BaseMongoModel


class Order(BaseMongoModel):
    user_id: str
    status: str = "pending"
    products: List[Product] = []
