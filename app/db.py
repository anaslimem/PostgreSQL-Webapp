import psycopg2 
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=5432
        )
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None