import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
            cursor.execute("USE test_db")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    email VARCHAR(50) NOT NULL UNIQUE
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

def find_user_by_id(user_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            return result
    except Error as e:
        print(f"⚠️ Error finding user by ID: {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def find_user_by_email(email):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            return result
    except Error as e:
        print(f"⚠️ Error finding user by email: {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def count_users():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            return count
    except Error as e:
        print(f"⚠️ Error counting users: {e}")
        return 0
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def list_all_users():
    users = read_users()
    if users:
        print("Current users in the database:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("⚠️ No users found.")

def check_user_existence(email):
    user = find_user_by_email(email)
    if user:
        print(f"✅ User exists: {user}")
        return True
    else:
        print("⚠️ User does not exist.")
        return False

def batch_insert_users(user_list):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", user_list)
            conn.commit()
            print(f"✅ {len(user_list)} users created successfully.")
    except Error as e:
        print(f"⚠️ Error batch inserting users: {e}")
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

    # List all users
    list_all_users()

    # Count users
    total_users = count_users()
    print(f"Total users in the database: {total_users}")

    # Check user existence
    check_user_existence("john.doe@example.com")
    check_user_existence("nonexistent@example.com")

    # Update a user
    update_user(1, "Johnathan Doe", "johnathan.doe@example.com")

    # List users after update
    list_all_users()

    # Delete a user
    delete_user(2)

    # List users after deletion
    list_all_users()

    # Batch insert users
    new_users = [("Alice Johnson", "alice.johnson@example.com"),
                 ("Bob Brown", "bob.brown@example.com")]
    batch_insert_users(new_users)

    # List users after batch insert
    list_all_users()

if __name__ == "__main__":
    main()
