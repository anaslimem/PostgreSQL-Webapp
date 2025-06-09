import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

#Get all products
def get_all_products():
    """Fetch all products from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products;")
            products = cursor.fetchall()
            print(f"Fetched {len(products)} products from the database.")
            return products
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []
    finally:
        conn.close()

# Create a new product
def create_product(name, description, price, category_id):
    """Create a new product in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO products (name, description, price, category_id) VALUES (%s, %s, %s, %s);",
                (name, description, price, category_id)
            )
        conn.commit()
        print(f"Product '{name}' created successfully.")
        return True
    except Exception as e:
        print(f"Error creating product: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Update a product
def update_product(product_id, name, description, price, category_id):
    """Update an existing product in the database."""
    conn = get_db_connection()
    if not conn:
        return False
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE products SET name = %s, description = %s, price = %s, category_id = %s WHERE id = %s;",
                (name, description, price, category_id, product_id)
            )
        conn.commit()
        print(f"Product with ID '{product_id}' updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating product: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete a product
def delete_product(product_id):
    """Delete a product from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s;", (product_id,))
        conn.commit()
        print(f"Product with ID '{product_id}' deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting product: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()