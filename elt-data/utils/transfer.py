import pandas as pd

def transfer_table(table_name, source_engine, target_engine, chunksize=10000):
    offset = 0
    total_rows = 0

    while True:
        query = f"SELECT * FROM {table_name} LIMIT {chunksize} OFFSET {offset}"
        chunk_df = pd.read_sql(query, source_engine)

        if chunk_df.empty:
            break

        chunk_df.to_sql(
            name=table_name,
            con=target_engine,
            if_exists='replace' if offset == 0 else 'append',
            index=False
        )

        total_rows += len(chunk_df)
        offset += chunksize
        print(f" Transferred {len(chunk_df)} rows (total so far: {total_rows})")

    print(f" Finished transferring table '{table_name}' with {total_rows} rows.")
