import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

# Get all categories
def get_all_categories():
    """Fetch all categories from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM categories;")
            categories = cursor.fetchall()
            print(f"Fetched {len(categories)} categories from the database.")
            return categories
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return []
    finally:
        conn.close()


# Create a new category
def create_category(name):
    """Create a new category in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO categories (name) VALUES (%s);",
                (name,)
            )
        conn.commit()
        print(f"Category '{name}' created successfully.")
        return True
    except Exception as e:
        print(f"Error creating category: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Update a category
def update_category(category_id, name):
    """Update an existing category in the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE categories SET name = %s WHERE category_id = %s;",
                (name, category_id)
            )
        conn.commit()
        print(f"Category ID {category_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating category: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Delete a category
def delete_category(category_id):
    """Delete a category from the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM categories WHERE category_id = %s;",
                (category_id,)
            )
        conn.commit()
        print(f"Category ID {category_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting category: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
        