import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Get all order items
def get_all_order_items():
    """Fetch all order items from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM order_items;")
            order_items = cursor.fetchall()
            print(f"Fetched {len(order_items)} order items from the database.")
            return order_items
    except Exception as e:
        print(f"Error fetching order items: {e}")
        return []
    finally:
        conn.close()


# Create a new order item
def create_order_item(order_id, product_id, quantity, price):
    """Create a new order item in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s);",
                (order_id, product_id, quantity, price)
            )
        conn.commit()
        print(f"Order item for order ID {order_id} created successfully.")
        return True
    except Exception as e:
        print(f"Error creating order item: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Update an order item
def update_order_item(order_item_id, order_id=None, product_id=None, quantity=None, price=None):
    """Update an existing order item in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            if order_id:
                cursor.execute(
                    "UPDATE order_items SET order_id = %s WHERE order_item_id = %s;",
                    (order_id, order_item_id)
                )
            if product_id:
                cursor.execute(
                    "UPDATE order_items SET product_id = %s WHERE order_item_id = %s;",
                    (product_id, order_item_id)
                )
            if quantity is not None:
                cursor.execute(
                    "UPDATE order_items SET quantity = %s WHERE order_item_id = %s;",
                    (quantity, order_item_id)
                )
            if price is not None:
                cursor.execute(
                    "UPDATE order_items SET price = %s WHERE order_item_id = %s;",
                    (price, order_item_id)
                )
        conn.commit()
        print(f"Order item ID {order_item_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating order item: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete an order item
def delete_order_item(order_item_id):
    """Delete an order item from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM order_items WHERE order_item_id = %s;",
                (order_item_id,)
            )
        conn.commit()
        print(f"Order item ID {order_item_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting order item: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
    