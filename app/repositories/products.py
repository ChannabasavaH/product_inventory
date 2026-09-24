from sqlalchemy.orm import Session
from app.models.product import Products

def create(db: Session, product: Products):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get(db: Session):
    return db.query(Products).all()

def get_by_id(id: int, db: Session):
    return db.query(Products).filter(Products.id == id).first()

def update(id: int, product_data: Products, db: Session):
    product = db.query(Products).filter(Products.id == id).first()

    if not product:
        return None

    product.title = product_data.title
    product.description = product_data.description
    product.price = product_data.price
    product.quantity = product_data.quantity

    db.commit()
    db.refresh(product)
    return product

def delete(id: int, db: Session):
    product = db.query(Products).filter(Products.id == id).first()

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product

