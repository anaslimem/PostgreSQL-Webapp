import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Get all payments
def get_all_payments():
    """Fetch all payments from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM payments;")
            payments = cursor.fetchall()
            print(f"Fetched {len(payments)} payments from the database.")
            return payments
    except Exception as e:
        print(f"Error fetching payments: {e}")
        return []
    finally:
        conn.close()

# Create a new payment
def create_payment(order_id, method, status='pending'):
    """Create a new payment in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO payments (order_id, method, status) VALUES (%s, %s, %s);",
                (order_id, method, status)
            )
        conn.commit()
        print(f"Payment for order ID {order_id} created successfully.")
        return True
    except Exception as e:
        print(f"Error creating payment: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Update a payment
def update_payment(payment_id, order_id=None, method=None, status=None):
    """Update an existing payment in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            if order_id:
                cursor.execute(
                    "UPDATE payments SET order_id = %s WHERE payment_id = %s;",
                    (order_id, payment_id)
                )
            if method:
                cursor.execute(
                    "UPDATE payments SET method = %s WHERE payment_id = %s;",
                    (method, payment_id)
                )
            if status:
                cursor.execute(
                    "UPDATE payments SET status = %s WHERE payment_id = %s;",
                    (status, payment_id)
                )
        conn.commit()
        print(f"Payment ID {payment_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating payment: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete a payment
def delete_payment(payment_id):
    """Delete a payment from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM payments WHERE payment_id = %s;", (payment_id,))
        conn.commit()
        print(f"Payment ID {payment_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting payment: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()