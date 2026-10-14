from fastapi import FastAPI
from routers import user,product

app = FastAPI()

app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=product.router, prefix="/products", tags=["products"])