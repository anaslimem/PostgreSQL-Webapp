import streamlit as st
import sys
import os

# Ensure project root is in path for imports
ing_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ing_dir)

# Import CRUD functions
from queries import create_tables, drop_tables
from users import get_all_users, create_user, update_user, delete_user
from orders import get_all_orders, create_order, update_order, delete_order
from products import get_all_products, create_product,update_product, delete_product
from categories import get_all_categories, create_category,update_category, delete_category
from order_items import get_all_order_items, create_order_item, update_order_item, delete_order_item
from payments import get_all_payments, create_payment,update_payment, delete_payment

st.title("E-Commerce Database Management")

# Sidebar actions
st.sidebar.header("Actions")
if st.sidebar.button("Create Tables"):
    if create_tables(): st.success("Tables created successfully.")
    else: st.error("Failed to create tables.")
    st.rerun()

if st.sidebar.button("Drop Tables"):
    if drop_tables(): st.success("Tables dropped successfully.")
    else: st.error("Failed to drop tables.")
    st.rerun()

# Table and Operation Selection
table = st.sidebar.selectbox(
    "Select Table", ["Users", "Orders", "Products", "Categories", "Order Items", "Payments"]
)
operation = st.sidebar.radio("CRUD Operation", ("Read", "Create", "Update", "Delete"))
st.subheader(f"{operation} Operation on {table} Table")

# Mapping table to CRUD functions and columns
crud_map = {
    "Users": {
        "columns": ["user_id", "name", "email", "created_at"],
        "Read": get_all_users
    },
    "Orders": {"columns": ["order_id", "user_id", "order_date", "status"], "Read": get_all_orders},
    "Products": {"columns": ["product_id", "name", "price", "stock_qty", "category_id"], "Read": get_all_products},
    "Categories": {"columns": ["category_id", "name"], "Read": get_all_categories},
    "Order Items": {"columns": ["item_id", "order_id", "product_id", "quantity", "unit_price"], "Read": get_all_order_items},
    "Payments": {"columns": ["payment_id", "order_id", "payment_date", "method", "status"], "Read": get_all_payments},
}

# Display table data
def display_table(data, columns):
    if data:
        st.table([dict(zip(columns, row)) for row in data])
    else:
        st.warning("No data available or failed to fetch data.")

# Dynamic form for Create, Update, Delete with auto-refresh
def dynamic_form(table_name, operation):
    # Helper to process action and refresh
    def process_action(func, *args):
        success = func(*args)
        if success is None or success:
            st.success("Operation successful.")
        else:
            st.error("Operation failed.")
        st.rerun()

    if table_name == "Users":
        if operation == "Create":
            with st.form("create_user_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                submitted = st.form_submit_button("Create User")
                if submitted:
                    process_action(create_user, name, email)
        elif operation == "Update":
            users = get_all_users()
            with st.form("update_user_form"):
                user_id = st.selectbox("Select User ID", [u[0] for u in users])
                name = st.text_input("New Name")
                email = st.text_input("New Email")
                submitted = st.form_submit_button("Update User")
                if submitted:
                    process_action(update_user, user_id, name, email)
        elif operation == "Delete":
            users = get_all_users()
            with st.form("delete_user_form"):
                user_id = st.selectbox("Select User ID to Delete", [u[0] for u in users])
                submitted = st.form_submit_button("Delete User")
                if submitted:
                    process_action(delete_user, user_id)
    # Orders
    if table_name == "Orders":
        if operation == "Create":
            with st.form("create_order_form"):
                user_id = st.number_input("User ID", value=1, step=1)
                status = st.text_input("Status")
                submitted = st.form_submit_button("Create Order")
                if submitted:
                    process_action(create_order, user_id, status)
        elif operation == "Update":
            orders = get_all_orders()
            with st.form("update_order_form"):
                order_id = st.selectbox("Select Order ID", [o[0] for o in orders])
                user_id = st.number_input("New User ID", value=1, step=1)
                status = st.text_input("New Status")
                submitted = st.form_submit_button("Update Order")
                if submitted:
                    process_action(update_order, order_id, user_id, status)
        elif operation == "Delete":
            orders = get_all_orders()
            with st.form("delete_order_form"):
                order_id = st.selectbox("Select Order ID to Delete", [o[0] for o in orders])
                submitted = st.form_submit_button("Delete Order")
                if submitted:
                    process_action(delete_order, order_id)

    # Products
    if table_name == "Products":
        if operation == "Create":
            with st.form("create_product_form"):
                name = st.text_input("Product Name")
                price = st.number_input("Price", value=0.0)
                stock_qty = st.number_input("Stock Quantity", value=0, step=1)
                category_id = st.number_input("Category ID", value=1, step=1)
                submitted = st.form_submit_button("Create Product")
                if submitted:
                    process_action(create_product, name, price, stock_qty, category_id)
        elif operation == "Update":
            products = get_all_products()
            with st.form("update_product_form"):
                product_id = st.selectbox("Select Product ID", [p[0] for p in products])
                name = st.text_input("New Name")
                price = st.number_input("New Price", value=0.0)
                stock_qty = st.number_input("New Stock Quantity", value=0, step=1)
                category_id = st.number_input("New Category ID", value=1, step=1)
                submitted = st.form_submit_button("Update Product")
                if submitted:
                    process_action(update_product, product_id, name, price, stock_qty, category_id)
        elif operation == "Delete":
            products = get_all_products()
            with st.form("delete_product_form"):
                product_id = st.selectbox("Select Product ID to Delete", [p[0] for p in products])
                submitted = st.form_submit_button("Delete Product")
                if submitted:
                    process_action(delete_product, product_id)

    # Categories
    if table_name == "Categories":
        if operation == "Create":
            with st.form("create_category_form"):
                name = st.text_input("Category Name")
                submitted = st.form_submit_button("Create Category")
                if submitted:
                    process_action(create_category, name)
        elif operation == "Update":
            cats = get_all_categories()
            with st.form("update_category_form"):
                category_id = st.selectbox("Select Category ID", [c[0] for c in cats])
                name = st.text_input("New Name")
                submitted = st.form_submit_button("Update Category")
                if submitted:
                    process_action(update_category, category_id, name)
        elif operation == "Delete":
            cats = get_all_categories()
            with st.form("delete_category_form"):
                category_id = st.selectbox("Select Category ID to Delete", [c[0] for c in cats])
                submitted = st.form_submit_button("Delete Category")
                if submitted:
                    process_action(delete_category, category_id)

    # Order Items
    if table_name == "Order Items":
        if operation == "Create":
            with st.form("create_order_item_form"):
                order_id = st.number_input("Order ID", value=1, step=1)
                product_id = st.number_input("Product ID", value=1, step=1)
                quantity = st.number_input("Quantity", value=1, step=1)
                unit_price = st.number_input("Unit Price", value=0.0)
                submitted = st.form_submit_button("Create Order Item")
                if submitted:
                    process_action(create_order_item, order_id, product_id, quantity, unit_price)
        elif operation == "Update":
            items = get_all_order_items()
            with st.form("update_order_item_form"):
                item_id = st.selectbox("Select Order Item ID", [i[0] for i in items])
                order_id = st.number_input("New Order ID", value=1, step=1)
                product_id = st.number_input("New Product ID", value=1, step=1)
                quantity = st.number_input("New Quantity", value=1, step=1)
                unit_price = st.number_input("New Unit Price", value=0.0)
                submitted = st.form_submit_button("Update Order Item")
                if submitted:
                    process_action(update_order_item, item_id, order_id, product_id, quantity, unit_price)
        elif operation == "Delete":
            items = get_all_order_items()
            with st.form("delete_order_item_form"):
                item_id = st.selectbox("Select Order Item ID to Delete", [i[0] for i in items])
                submitted = st.form_submit_button("Delete Order Item")
                if submitted:
                    process_action(delete_order_item, item_id)

            # Payments
    if table_name == "Payments":
        methods = ['card', 'paypal', 'bank']
        statuses = ['completed', 'pending', 'failed']
        if operation == "Create":
            with st.form("create_payment_form"):
                order_id = st.number_input("Order ID", value=1, step=1)
                method = st.selectbox("Method", methods)
                status = st.selectbox("Status", statuses)
                submitted = st.form_submit_button("Create Payment")
                if submitted:
                    process_action(create_payment, order_id, method, status)
        elif operation == "Update":
            pays = get_all_payments()
            with st.form("update_payment_form"):
                payment_id = st.selectbox("Select Payment ID", [p[0] for p in pays])
                order_id = st.number_input("New Order ID", value=1, step=1)
                method = st.selectbox("New Method", methods)
                status = st.selectbox("New Status", statuses)
                submitted = st.form_submit_button("Update Payment")
                if submitted:
                    process_action(update_payment, payment_id, order_id, method, status)
        elif operation == "Delete":
            pays = get_all_payments()
            with st.form("delete_payment_form"):
                payment_id = st.selectbox("Select Payment ID to Delete", [p[0] for p in pays])
                submitted = st.form_submit_button("Delete Payment")
                if submitted:
                    process_action(delete_payment, payment_id)

# Main execution
def main():
    if operation == "Read":
        data = crud_map[table]["Read"]()
        display_table(data, crud_map[table]["columns"])
    else:
        dynamic_form(table, operation)

if __name__ == "__main__":
    main()
