import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
USE_DOCKER = os.getenv("USE_DOCKER", "false").lower() == "true"


def get_postgres_engine():
    if USE_DOCKER:
        host = os.getenv("POSTGRES_HOST", "postgres")  # Nama service di Docker Compose
        port = int(os.getenv("POSTGRES_PORT", 5432))   # Port dalam container
    else:
        host = os.getenv("POSTGRES_HOST", "localhost")  # Host lokal
        port = int(os.getenv("POSTGRES_PORT_HOST", 1945))  # Port di host yang dipetakan

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=host,
        port=port,
        database=os.getenv("POSTGRES_DB")
    )
    return create_engine(url, pool_pre_ping=True)

# --- CREATE ENGINE & SESSIONMAKER ---
engine = get_postgres_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()