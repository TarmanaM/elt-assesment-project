# API market using FastAPI

`api-app` adalah service utama yang berisi kode **API FastAPI**. Fungsinya sebagai backend yang menyediakan endpoint untuk data **Store**, **Transaction**, dan **Customer** dari database PostgreSQL.

## Running Program
<p>API akan berjalan otomatis saat docker pertamakali dibuild. Namun juga dapat dijalankan dengan mandiri dengan</p>

```bash
 docker exec -it quiz_api bash 
 python run.py
```

<p></p>

```markdown
> 💡 Note: `quiz_api` adalah nama service container untuk ETL di `docker-compose.yml`. Jika kamu pakai nama berbeda, ganti sesuai nama servicemu.
```

## Struktur utamanya:

- **app/**: 
    - `models/`: Definisi struktur tabel database (pakai SQLAlchemy ORM).
    - `schemas/`: Struktur data untuk request & response (pakai Pydantic).
    - `crud/`: Query database dan logika bisnis.
    - `routers/`: Routing untuk masing-masing endpoint API.
    - `db/`: Setup koneksi database (engine dan session).
    - `main.py`: Entry point untuk inisialisasi FastAPI dan mendaftarkan router.

- **run.py**: Script untuk menjalankan API dengan `uvicorn`.

- **requirements.txt**: Daftar dependency Python.

---
