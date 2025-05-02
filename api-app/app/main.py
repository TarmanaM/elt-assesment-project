from fastapi import FastAPI
from app.api import routes_transaction, routes_store, routes_customer

# Inisialisasi FastAPI dengan metadata 
app = FastAPI(
    title="Retail Transaction API",
    description="API untuk tugas DDV rekrutment",
    version="1.0.0",
    contact={
        "name": "Isa Tarmana M",
        "email": "isatarmanamustopa54@gmail.com",
    }
)

app = FastAPI()
# Include router per domain
app.include_router(routes_transaction.router, prefix="/transaction", tags=["Transaction"])
app.include_router(routes_store.router, prefix="/store", tags=["Store"])
app.include_router(routes_customer.router, prefix="/customer", tags=["Customer"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Retail Transaction API!"}
