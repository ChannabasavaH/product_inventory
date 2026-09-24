from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.products import ProductCreate, ProductBase, ProductResponse, ProductCreateResponse
from app.services.products import create_product, get_product, get_product_by_id, update_product, delete_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("",response_model=ProductCreateResponse, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product_data: ProductCreate, db: Session =  Depends(get_db)):
    try:
        response = create_product(db, product_data)

        return {
            "message": "Product created successfully",
            "product": response
        }
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create products")

@router.get("", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
def get_product_endpoint(db: Session = Depends(get_db)):
    try:
        response = get_product(db)
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to fetch products")

@router.get("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product_by_id_endpoint(id: int, db: Session = Depends(get_db)):
    try:
        response = get_product_by_id(id, db)
        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to fetch the product by id")

@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product_endpoint(id: int,product_data: ProductCreate, db: Session = Depends(get_db)):
    try:
        response = update_product(id, product_data, db)

        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        return response
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=500, detail="Product updation error")

@router.delete("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def delete_product_endpoint(id: int, db: Session = Depends(get_db)):
    try:
        response = delete_product(id, db)
        if not response:
            raise HTTPException(status_code=404, detail="Product not found")

        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="product deletion error")