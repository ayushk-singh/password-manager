import mysql.connector
import os
from dotenv import load_dotenv

def connect_to_database():
    try:
        load_dotenv()
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )

        if connection.is_connected():
             print("Connected to MySQL database")
             return connection

    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
        return None

def insert_record(password, user_email, username, url, app_name):
    connection = connect_to_database()
    try:
        if connection is None:
            print("Database connection is not established. Exiting.")
            return

        cursor = connection.cursor()

        # Define the INSERT query
        mysql_insert_query = """
        INSERT INTO pswd (password, email, username, url, app_name)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Data to insert
        record_to_insert = (password, user_email, username, url, app_name)

        # Execute the INSERT query
        cursor.execute(mysql_insert_query, record_to_insert)

        # Commit the changes to the database
        connection.commit()
        print("Record inserted successfully into accounts table")

    except mysql.connector.Error as error:
        print(f"Error inserting record: {error}")

    finally:
        if 'cursor' in locals():
            cursor.close()

def search_pass(app_name):
    connection = connect_to_database()
    try:
        if connection is None:
            print("Database connection is not established. Exiting.")
            return

        cursor = connection.cursor()

        # Define the SELECT query to retrieve a password by app name
        select_query = "SELECT password FROM pswd WHERE app_name = %s"

        # Execute the SELECT query with the app_name as a tuple
        cursor.execute(select_query, (app_name,))

        # Fetch and print the stored passwords
        passwords = cursor.fetchall()
        if passwords:
            for password in passwords:
                print(f"Password for {app_name}: {password[0]}")
        else:
            print(f"No password found for {app_name}.")

    except mysql.connector.Error as error:
        print(f"Error retrieving password: {error}")

    finally:
        if 'cursor' in locals():
            cursor.close()


def find_user_name(username):
    connection = connect_to_database()
    try:
        if connection is None:
            print("Database connection is not established. Exiting.")
            return
        cursor = connection.cursor()

        # Define the SELECT query to retrieve a password by app name
        select_query = "SELECT password FROM pswd WHERE username = %s"

        # Execute the SELECT query with the app_name as a tuple
        cursor.execute(select_query, (username,))

        # Fetch and print the stored passwords
        passwords = cursor.fetchall()
        if passwords:
            for password in passwords:
                print(f"Password for {username}: {password[0]}")
        else:
            print(f"No password found for {username}.")

    except mysql.connector.Error as error:
        print(f"Error retrieving password: {error}")

    finally:
        if 'cursor' in locals():
            cursor.close()

