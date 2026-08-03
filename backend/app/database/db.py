import mysql.connector
from mysql.connector import Error
from app.config.settings import Settings

def get_db_connection():

    try:
        connection = mysql.connector.connect(
            host = Settings.MYSQL_HOST,
            port = Settings.MYSQL_PORT,
            user = Settings.MYSQL_USER,
            password = Settings.MYSQL_PASSWORD,
            database = Settings.MYSQL_DATABASE
        )

        if connection.is_connected():
            print("Database Connected ")

        return connection
    
    except Error as e:
        print(f"Database Connection Error {e}")
        return None
    

