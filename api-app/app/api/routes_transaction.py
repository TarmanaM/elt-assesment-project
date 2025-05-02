from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionDetail
from app.db.deps import get_db
from app import crud
from typing import List


router = APIRouter()

@router.get("/{trx_id}", response_model=TransactionDetail)
def get_transaction_detail(trx_id: int, db: Session = Depends(get_db)):

    transaction = crud.transaction.get_transaction_detail(db, trx_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/", response_model=List[TransactionDetail])
def get_all_transactions(db: Session = Depends(get_db)):

    transactions = crud.transaction.get_all_transactions(db)
    return transactions