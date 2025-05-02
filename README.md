# 🚀 DDV ELT API Project

Ini adalah API service untuk kebutuhan data ELT (Extract, Load, Transform) berbasis **FastAPI** + **SQLAlchemy** + **PostgreSQL**, dengan setup dockerized.

---



## Running Program
⚠️ Harus menginstal Docker 27.4.0++

```bash
git clone https://github.com/TarmanaM/elt-assesment-project.git
cd elt-assesment-project
cp .env.template .env
docker-compose up --build
```


## Testing enpoint
GET
1. localhost:8000/store/
2. localhost:8000/store/{store_id}
3. localhost:8000/transaction/
4. localhost:8000/transaction/{trx_id}
5. localhost:8000/customer/
6. localhost:8000/customer/{customer_id} 

## Struktur folder

- api-app/ → folder projek api menggunaakn FastAPI
- elt-data/ → folder Data Pipeline
- database/ → folder menyimpan inisasi data
- .env.template → file env template yang harus dibuat
- docker-compose.yml → file untuk membuat container docker

# TASK 
1. Create ELT data pipeline from MySQL to PostgreSQL ✅
2. Create API for consuming the processed data 
    - get transaction detail ✅
        payload: trx_id, store_id, customer_id, trx_amount, store_name, store_format_name, store_city, store_state
    - get store detail ✅
        payload: store_name, store_format_name, store_city, store_state, amount
    - get customer detail ✅
        payload: customer_id, amount, stores