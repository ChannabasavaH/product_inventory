from sqlalchemy.orm import Session
from app.schemas.products import ProductCreate
from app.models.product import Products
from app.repositories.products import create, get, get_by_id, update, delete

def create_product(db: Session, product:ProductCreate):
    db_product = Products(**product.model_dump())

    return create(db, db_product)

def get_product(db: Session):
    return get(db)

def get_product_by_id(id: int, db: Session):
    return get_by_id(id, db)

def update_product(id: int,product_data: ProductCreate, db: Session):
    db_product = Products(**product_data.model_dump())
    return update(id, db_product, db)

def delete_product(id: int, db: Session):
    return delete(id, db)