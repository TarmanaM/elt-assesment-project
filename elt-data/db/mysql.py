import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL

load_dotenv()
USE_DOCKER = os.getenv("USE_DOCKER", "false").lower() == "true"

def get_mysql_engine():
    
    if USE_DOCKER:
        host = os.getenv("MYSQL_HOST", "mysql")  # Nama service container di Docker
        port = int(os.getenv("MYSQL_PORT", 3306))  # Port di dalam Docker container
    else:
        host = os.getenv("MYSQL_HOST", "localhost")  # Host lokal
        port = int(os.getenv("MYSQL_PORT_HOST", 3307))  # Port yang dipetakan dari Docker container


    url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
        host= host,
        port= port, 
        database=os.getenv("MYSQL_DB")
    )
    return create_engine(url)
