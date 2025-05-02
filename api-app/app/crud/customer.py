from sqlalchemy.orm import Session
from sqlalchemy import func
from app.schemas.customer import CustomerDetail
from app.models.trx_total import Transaction
from app.models.store import Store

def get_customer_detail(db: Session, customer_id: int) -> CustomerDetail:
    # Total amount
    total_amount = db.query(
        func.coalesce(func.sum(Transaction.trx_amount), 0)
    ).filter(Transaction.customer_id == customer_id).scalar()

    # List of store names
    store_names = (
        db.query(Store.store_name)
        .join(Transaction, Store.store_id == Transaction.store_id)
        .filter(Transaction.customer_id == customer_id)
        .group_by(Store.store_name)
        .all()
    )
    stores = [store.store_name for store in store_names]

    if total_amount == 0:
        return None  # Optional: handle jika customer belum pernah transaksi

    return CustomerDetail(
        customer_id=customer_id,
        amount=total_amount,
        stores=stores
    )

def get_all_customers(db: Session) -> list[CustomerDetail]:
    # Ambil semua customer_id unik
    customer_ids = db.query(Transaction.customer_id).distinct().all()
    result = []

    for (customer_id,) in customer_ids:
        # Total amount per customer
        total_amount = db.query(
            func.coalesce(func.sum(Transaction.trx_amount), 0)
        ).filter(Transaction.customer_id == customer_id).scalar()

        # List store per customer
        store_names = (
            db.query(Store.store_name)
            .join(Transaction, Store.store_id == Transaction.store_id)
            .filter(Transaction.customer_id == customer_id)
            .group_by(Store.store_name)
            .all()
        )
        stores = [store.store_name for store in store_names]

        result.append(CustomerDetail(
            customer_id=customer_id,
            amount=total_amount,
            stores=stores
        ))
    return result
