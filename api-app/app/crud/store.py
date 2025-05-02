from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.store import Store
from app.models.trx_total import Transaction
from app.schemas.store import StoreDetail

def get_store_detail(db: Session, store_id: int) -> StoreDetail:
    result = (
        db.query(
            Store.store_name,
            Store.store_format_name,
            Store.store_city,
            Store.store_state,
            func.coalesce(func.sum(Transaction.trx_amount), 0).label("amount")
        )
        .join(Transaction, Store.store_id == Transaction.store_id)
        .filter(Store.store_id == store_id)
        .group_by(
            Store.store_id,
            Store.store_name,
            Store.store_format_name,
            Store.store_city,
            Store.store_state
            )
        .first()
    )
    if result:
        return StoreDetail(
            store_name=result.store_name,
            store_format_name=result.store_format_name,
            store_city=result.store_city,
            store_state=result.store_state,
            amount=result.amount
        )
    return None

def get_all_stores(db: Session) -> list[StoreDetail]:
    results = (
    db.query(
        Store.store_name,
        Store.store_format_name,
        Store.store_city,
        Store.store_state,
        func.coalesce(func.sum(Transaction.trx_amount), 0).label("amount")
    )
    .outerjoin(Transaction, Store.store_id == Transaction.store_id)
    .group_by(
        Store.store_id,
        Store.store_name,
        Store.store_format_name,
        Store.store_city,
        Store.store_state
    )
    .all()
)
    return [
        StoreDetail(
            store_name=row.store_name,
            store_format_name=row.store_format_name,
            store_city=row.store_city,
            store_state=row.store_state,
            amount=row.amount
        )
        for row in results
    ]