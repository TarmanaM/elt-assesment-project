from pydantic import BaseModel

class StoreDetail(BaseModel):
    store_name: str
    store_format_name: str
    store_city: str
    store_state: str
    amount: int

    class Config:
        from_attributes = True
