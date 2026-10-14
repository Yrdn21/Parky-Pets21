from pydantic import BaseModel
from enums.product_category import ProductCategory


class ProductBase(BaseModel):
    id:int
    name:str
    price:float
    category:ProductCategory
    expiration_date:str