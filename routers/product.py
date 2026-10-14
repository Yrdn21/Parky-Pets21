from fastapi import APIRouter

from models.product import ProductBase
from data.product import create_product_csv, read_all_products_csv

router = APIRouter()



@router.post("/")
def create_product(new_product:ProductBase):
    if create_product_csv(new_product):
        return {"Product":"Added"}
    return None


#TODO
@router.get("/", response_model=list[ProductBase])
def show_all_products():
    return read_all_products_csv()


#TODO
@router.get("/{id}")
def show_one_product():
    pass


#TODO
def update_product():
    pass


#TODO
def delete_product():
    pass