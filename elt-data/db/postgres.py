import os
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv

load_dotenv()
API_USE_DOCKER = os.getenv("API_USE_DOCKER", "false").lower() == "true"

def get_postgres_engine():
    if API_USE_DOCKER:
        host = os.getenv("POSTGRES_HOST", "postgres")  
        port = int(os.getenv("POSTGRES_PORT", 5432))   
    else:
        host = os.getenv("POSTGRES_HOST", "localhost") 
        port = int(os.getenv("POSTGRES_PORT_HOST", 5433))  

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=host,
        port=port,
        database=os.getenv("POSTGRES_DB")
    )
    return create_engine(url)
