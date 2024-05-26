from store_dio.models.base import CreateBaseModel
from store_dio.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    pass
