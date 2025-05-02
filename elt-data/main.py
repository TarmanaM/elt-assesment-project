from db.mysql import get_mysql_engine
from db.postgres import get_postgres_engine
from utils.transfer import transfer_table
import logging 


def run_elt():
    try:
        mysql_engine = get_mysql_engine()
        pg_engine = get_postgres_engine()

        for table in ["store", "trx_total"]:
            transfer_table(table, mysql_engine, pg_engine, chunksize=10000)

        print(" ETL success!")
    except Exception as e:
        logging.error("ETL Failed", exc_info=True)

if __name__ == "__main__":
    run_elt()