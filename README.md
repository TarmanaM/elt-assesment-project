# 🚀 DDV ELT API Project

Ini adalah API service untuk kebutuhan data ELT (Extract, Load, Transform) berbasis **FastAPI** + **SQLAlchemy** + **PostgreSQL**, dengan setup dockerized.

---

## 📥 1️⃣ Cara Clone & Jalankan Docker

### 💻 Clone repo:

```bash
git clone https://github.com/TarmanaM/elt-assesment-project.git
cd elt-assesment-project
```
## Duplicate .env.template dan hapus .template pada file

## Jalankan docker
```bash
docker-compose up --build
```

## Testing enpoint

1. localhost:8000/store/
2. localhost:8000/transaksi/
3. loaclhost:8000/customer/

## Manual Development

models/ → Definisi ORM (SQLAlchemy) untuk semua tabel.

schemas/ → Struktur data yang di-return atau divalidasi (pakai Pydantic).

crud/ → Logika query/operasi DB.

routers/ → Routing API / endpoint.

db/ → Setup database (engine, sessionmaker).

main.py → Bootstrap FastAPI & daftar semua router.

