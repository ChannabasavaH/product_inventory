from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    createdAt: datetime

    class Config:
        from_attribute: True