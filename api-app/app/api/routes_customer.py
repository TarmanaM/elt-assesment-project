from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.customer import CustomerDetail
from app.db.deps import get_db
from app import crud

router = APIRouter()

@router.get("/{customer_id}", response_model=CustomerDetail)
def get_customer_detail(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.customer.get_customer_detail(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=List[CustomerDetail])
def get_all_customers(db: Session = Depends(get_db)):
    customers = crud.customer.get_all_customers(db)
    return customers
