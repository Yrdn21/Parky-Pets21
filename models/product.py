from pydantic import BaseModel
from enums.product_category import ProductCategory


class ProductBase(BaseModel):
    name:str
    price:float
    category:ProductCategory
    expiration_date:str


class ProductID(ProductBase):
    id:int
