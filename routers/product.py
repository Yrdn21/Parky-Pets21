from fastapi import APIRouter

router = APIRouter()


#TODO
@router.post("/")
def create_product():
    pass


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