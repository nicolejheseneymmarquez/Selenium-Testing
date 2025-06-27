import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Default XAMPP username
            password=""   # Default XAMPP password
        )
        if conn.is_connected():
            cursor = conn.cursor()
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
            cursor.execute("USE test_db")

            # Create table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    email VARCHAR(50) NOT NULL
                )
            """)

            conn.commit()
            print("✅ Database and table created successfully.")
    except Error as e:
        print(f"⚠️ Error creating database/table: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def create_user(name, email):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print(f"✅ User '{name}' created successfully.")
    except Error as e:
        print(f"⚠️ Error creating user: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_users():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            return result
    except Error as e:
        print(f"⚠️ Error reading users: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_user(user_id, new_name, new_email):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (new_name, new_email, user_id))
            conn.commit()
            print(f"✅ User with ID '{user_id}' updated successfully.")
    except Error as e:
        print(f"⚠️ Error updating user: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_user(user_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print(f"✅ User with ID '{user_id}' deleted successfully.")
    except Error as e:
        print(f"⚠️ Error deleting user: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def main():
    # Create database and table
    create_database_and_table()

    # Create users
    create_user("John Doe", "john.doe@example.com")
    create_user("Jane Smith", "jane.smith@example.com")

    # Read users
    users = read_users()
    print("Current users in the database:")
    for user in users:
        print(user)

    # Update a user
    update_user(1, "Johnathan Doe", "johnathan.doe@example.com")

    # Read users again
    users = read_users()
    print("Users after update:")
    for user in users:
        print(user)

    # Delete a user
    delete_user(2)

    # Read users again
    users = read_users()
    print("Users after deletion:")
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
