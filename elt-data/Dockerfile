# Gunakan base image Python resmi
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements ke container dan install dependensi
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode ke dalam container
COPY . .

# Jalankan script ETL saat container dijalankan
CMD ["python", "main.py"]
