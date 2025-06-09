import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Get all users
def get_all_users():
    """Fetch all users from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            users = cursor.fetchall()
            print(f"Fetched {len(users)} users from the database.")
            return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        conn.close()

# Create a new user
def create_user(name, email):
    """Create a new user in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s);",
                (name, email)
            )
        conn.commit()
        print(f"User '{name}' created successfully.")
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Update a user
def update_user(user_id, name=None, email=None):
    """Update an existing user in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            if name:
                cursor.execute(
                    "UPDATE users SET name = %s WHERE user_id = %s;",
                    (name, user_id)
                )
            if email:
                cursor.execute(
                    "UPDATE users SET email = %s WHERE user_id = %s;",
                    (email, user_id)
                )
        conn.commit()
        print(f"User ID {user_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete a user
def delete_user(user_id):
    """Delete a user from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s;", (user_id,))
        conn.commit()
        print(f"User ID {user_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()