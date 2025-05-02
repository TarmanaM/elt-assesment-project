from sqlalchemy import Column, Integer, ForeignKey
from app.db.db_connection import Base

class Transaction(Base):
    __tablename__ = "trx_total"

    trx_id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("store.store_id"))
    customer_id = Column(Integer, index=True)
    trx_amount = Column(Integer)
