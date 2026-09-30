from fastapi import FastAPI
from app.api.product_router import router
from app.utils.observability import setup_telemetry
from app.db.session import engine
from app.utils.logging_config import setup_logging

app = FastAPI(
    title="Product Inventory",
    description="Backend for managing product invetory",
    version="0.1.0"
)

setup_telemetry(app, engine)
setup_logging()

app.include_router(router)

@app.get("/")
def greet():
    return "hello world"