from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.store import StoreDetail
from app.db.deps import get_db
from app import crud

router = APIRouter()

@router.get("/{store_id}", response_model=StoreDetail)
def get_store_detail(store_id: int, db: Session = Depends(get_db)):
    store = crud.store.get_store_detail(db, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.get("/", response_model=List[StoreDetail])
def get_all_stores(db: Session = Depends(get_db)):
    stores = crud.store.get_all_stores(db)
    return stores
