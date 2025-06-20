# PostgreSQL CRUD Web App

This is a small web application that allows users to perform basic **CRUD** (Create, Read, Update, Delete) operations on a PostgreSQL database.

## Features

- Perform essential CRUD operations on PostgreSQL database tables.
- Backend logic implemented in **Python**.
- Interactive frontend built with **Streamlit**.
- Runs inside a **Docker container** for easy deployment and consistent environment.

## Technologies Used

- Python
- Streamlit
- PostgreSQL
- Docker

## Getting Started

### Prerequisites

- Docker installed on your machine.
- A running PostgreSQL database (can be local or remote).

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd PostgreSQL-Webapp
   ```

2. Create a .env file in the root directory with your PostgreSQL credentials:
    ```bash
    DB_HOST=postgres # or your DB host IP
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    ```

3. Build and run the Docker container:  
    ```bash
    docker-compose up --build
    ```


