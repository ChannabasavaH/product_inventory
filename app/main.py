from fastapi import FastAPI
from app.api.product_router import router

app = FastAPI(
    title="Product Inventory",
    description="Backend for managing product invetory",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def greet():
    return "hello world"