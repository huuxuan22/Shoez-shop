from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship



class ProductVariant():
    __tablename__ = 'product_variants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(100), nullable=False)
    variant_type = Column(String(100), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('colors.id'), nullable=False)
    size_id = Column(Integer, ForeignKey('sizes.id'), nullable=False)
