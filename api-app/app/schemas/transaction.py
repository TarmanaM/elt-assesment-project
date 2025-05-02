from pydantic import BaseModel

class TransactionDetail(BaseModel):
    trx_id: int
    store_id: int
    customer_id: int
    trx_amount: int
    store_name: str
    store_format_name: str
    store_city: str
    store_state: str

    class Config:
        from_attributes = True
