import os
from sqlalchemy import create_engine, URL

USE_DOCKER = os.getenv("USE_DOCKER", "false").lower() == "true"

def get_postgres_engine():
    if USE_DOCKER:
        host = os.getenv("POSTGRES_HOST", "postgres")  # Nama service di Docker Compose
        port = int(os.getenv("POSTGRES_PORT", 5432))   # Port dalam container
    else:
        host = os.getenv("POSTGRES_HOST", "localhost")  # Host lokal
        port = int(os.getenv("POSTGRES_PORT_HOST", 5433))  # Port di host yang dipetakan

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=host,
        port=port,
        database=os.getenv("POSTGRES_DB")
    )
    return create_engine(url)
