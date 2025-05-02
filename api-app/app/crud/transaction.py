from sqlalchemy.orm import Session
from app.models.trx_total import Transaction
from app.models.store import Store
from app.schemas.transaction import TransactionDetail

def get_transaction_detail(db: Session, trx_id: int) -> TransactionDetail:

    result = (
        db.query(Transaction, Store)
        .join(Store, Transaction.store_id == Store.store_id)
        .filter(Transaction.trx_id == trx_id)
        .first()
    )
    if result:
        trx, store = result
        return TransactionDetail(
            trx_id=trx.trx_id,
            store_id=trx.store_id,
            customer_id=trx.customer_id,
            trx_amount=trx.trx_amount,
            store_name=store.store_name,
            store_format_name=store.store_format_name,
            store_city=store.store_city,
            store_state=store.store_state
        )
    return None

def get_all_transactions(db: Session) -> list[TransactionDetail]:

    result = (
        db.query(Transaction, Store)
        .join(Store, Transaction.store_id == Store.store_id)
        .all()
    )
    return [
        TransactionDetail(
            trx_id=trx.trx_id,
            store_id=trx.store_id,
            customer_id=trx.customer_id,
            trx_amount=trx.trx_amount,
            store_name=store.store_name,
            store_format_name=store.store_format_name,
            store_city=store.store_city,
            store_state=store.store_state
        )
        for trx, store in result
    ]
