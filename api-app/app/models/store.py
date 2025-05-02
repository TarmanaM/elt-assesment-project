from sqlalchemy import Column, Integer, String
from app.db.db_connection import Base

class Store(Base):
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String(100))
    store_format_name = Column(String(100))
    store_city = Column(String(100))
    store_state = Column(String(50))
