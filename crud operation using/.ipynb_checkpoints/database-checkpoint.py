import mysql.connector as sql

def create_database():
    try:
        # Connect to the MySQL server
        db_connection = sql.connect(
            host="localhost",
            user="root",
            password="root"
        )

        # Create a cursor to execute SQL queries
        cursor = db_connection.cursor()

        # Check if database already exists
        cursor.execute("SHOW DATABASES LIKE 'main'")
        result = cursor.fetchone()

        if result:
            print("Database 'main' already exists.")
        else:
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE main")
            print("Database 'main' created successfully.")
        
        # Commit any changes
        db_connection.commit()

    except sql.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

if __name__ == "__main__":
    create_database()
