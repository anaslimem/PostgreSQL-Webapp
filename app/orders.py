import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Get all orders
def get_all_orders():
    """Fetch all orders from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM orders;")
            orders = cursor.fetchall()
            print(f"Fetched {len(orders)} orders from the database.")
            return orders
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return []
    finally:
        conn.close()

# Create a new order
def create_order(user_id, status='pending'):
    """Create a new order in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO orders (user_id, status) VALUES (%s, %s);",
                (user_id, status)
            )
        conn.commit()
        print(f"Order for user ID {user_id} created successfully.")
        return True
    except Exception as e:
        print(f"Error creating order: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


# Update an order
def update_order(order_id, user_id=None, status=None):
    """Update an existing order in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            if user_id:
                cursor.execute(
                    "UPDATE orders SET user_id = %s WHERE order_id = %s;",
                    (user_id, order_id)
                )
            if status:
                cursor.execute(
                    "UPDATE orders SET status = %s WHERE order_id = %s;",
                    (status, order_id)
                )
        conn.commit()
        print(f"Order ID {order_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating order: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete an order
def delete_order(order_id):
    """Delete an order from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM orders WHERE order_id = %s;", (order_id,))
        conn.commit()
        print(f"Order ID {order_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting order: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
    