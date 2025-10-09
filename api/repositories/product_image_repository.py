
from model import ProductImages
from repositories.base_repository import BaseRepository


class ProductImagesRepository(BaseRepository[ProductImages]):
    model = ProductImages
