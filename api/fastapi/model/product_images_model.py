from sqlalchemy import Integer, Column, String, ForeignKey



class ProductImages():
    __tablename__ = 'products_images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ile_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    object_key = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))