from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    title: str = Field(max_length=30)
    description: str = Field(max_length=255)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    quantity: int = Field(gt=0, le=100)

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    quantity: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProductCreateResponse(BaseModel):
    message: str
    product: ProductResponse