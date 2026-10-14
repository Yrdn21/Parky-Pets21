from fastapi import APIRouter

from models.product import ProductBase
from data.product import create_product_csv

router = APIRouter()


#TODO
@router.post("/")
def create_product(new_product:ProductBase):
    if create_product_csv(new_product):
        return {"Product":"Added"}
    return None


#TODO
@router.get("/")
def show_all_products():
    pass


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