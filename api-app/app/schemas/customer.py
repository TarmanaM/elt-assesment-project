from pydantic import BaseModel
from typing import List

class CustomerDetail(BaseModel):
    customer_id: int
    amount: int
    stores: List[str]

    class Config:
        from_attributes = True
