# ELT Data

## Proses pada Transfer data
<p> Proses transfer data tabel dari database sumber (MySQL) ke database target (PostgreSQL) menggunakan pendekatan ELT (Extract, Load, Transform). Fungsi transfer_table membaca data per chunk (default 10.000 baris) dari tabel sumber, lalu menyimpannya ke database target. Proses ini efisien untuk menangani data dalam jumlah besar.

- Extract: Mengambil data dari MySQL per chunk dengan query LIMIT dan OFFSET.

- Load: Menyimpan data ke PostgreSQL menggunakan to_sql, dengan opsi replace untuk chunk pertama dan append untuk selanjutnya.

- Transform: Transformasi dilakukan pada API 

ELT berhasil saat sudah memberikan output "ELT success!"
</p>

## Running Program
<p>ELT Datapipeline akan berjalan otomatis saat docker pertamakali dibuild. Namun juga dapat dijalankan dengan mandiri dengan</p>

```bash
 docker exec -it quiz_elt bash 
 python main.py
    

```markdown
> 💡 Note: `quiz_elt` adalah nama service container untuk ETL di `docker-compose.yml`. Jika kamu pakai nama berbeda, ganti sesuai nama servicemu.

## Penjelasan Folder :
- db/ → digunakan untuk koneksi DBMS Postgres dan Mysql
- utils/ → digunakan untuk menyimpan function program
- main.py → digunakan untuk menjalankan seluruh program