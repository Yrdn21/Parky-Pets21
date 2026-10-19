from fastapi import APIRouter, HTTPException

from models.product import ProductBase, ProductID
from data.product import create_product_csv, read_all_products_csv, read_one_product_csv

router = APIRouter()



@router.post("/")
def create_product(new_product:ProductBase):
    if create_product_csv(new_product):
        return {"Product":"Added"}
    return None



@router.get("/", response_model=list[ProductID])
def show_all_products():
    return read_all_products_csv()


#TODO
@router.get("/{product_id}", response_model=ProductBase)
def show_one_product(product_id:int):
    one_product = read_one_product_csv(product_id)
    if one_product:
        return read_one_product_csv(product_id)
    else:
        raise HTTPException(status_code=404, detail="Product not found")


#TODO
def update_product():
    pass


#TODO
def delete_product():
    pass