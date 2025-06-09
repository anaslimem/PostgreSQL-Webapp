import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Create tables if they do not exist
def create_tables():
    schema_sql = """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS categories (
        category_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock_qty INT DEFAULT 0,
        category_id INT REFERENCES categories(category_id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS orders (
        order_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'pending'
    );

    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
        product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
        quantity INT NOT NULL DEFAULT 1,
        price DECIMAL(10, 2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS payments (
        payment_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        method TEXT CHECK (method IN ('card', 'paypal', 'bank')),
        status TEXT CHECK (status IN ('completed', 'pending', 'failed')) DEFAULT 'pending'
    );

    CREATE INDEX IF NOT EXISTS idx_user_email ON users(email);
    CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
    CREATE INDEX IF NOT EXISTS idx_order_date ON orders(order_date);
    """
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to DB, cannot create tables.")
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(schema_sql)
        conn.commit()
        print("Tables created or already exist.")
        return True
    except Exception as e:
        print(f"Error creating tables: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Drop all tables
def drop_tables():
    """Drop all tables in the database."""
    schema_sql = """
    DROP TABLE IF EXISTS order_items CASCADE;
    DROP TABLE IF EXISTS payments CASCADE;
    DROP TABLE IF EXISTS orders CASCADE;
    DROP TABLE IF EXISTS products CASCADE;
    DROP TABLE IF EXISTS categories CASCADE;
    DROP TABLE IF EXISTS users CASCADE;
    """
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to DB, cannot drop tables.")
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(schema_sql)
        conn.commit()
        print("All tables dropped successfully.")
        return True
    except Exception as e:
        print(f"Error dropping tables: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()