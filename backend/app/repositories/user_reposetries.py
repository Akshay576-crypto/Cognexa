from typing import Optional
import mysql.connector
from app.database.db import get_db_connection

class UserReposetory:

    def __init__(self):
        pass

    def create_user(self,full_name:str,email:str,password_hash:str):

        connection = get_db_connection()

        if not connection:
            None

        cursor = connection.cursor(dictionary=True)

        query = """INSERT INTO users(full_name,email,password_hash)
        VALUES(%s,%s,%s)"""

        values = (full_name,email,password_hash)
        cursor.execute(query,values)

        connection.commit()

        user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return user_id
    
    def get_user_by_email(self,email:str):

        connnection = get_db_connection()

        cursor = connnection.cursor(dictionary=True)

        query = """SELECT * FROM users WHERE email = %s"""

        cursor.execute(query,(email,))

        user = cursor.fetchone()

        cursor.close()

        connnection.close()

        return user
    
    def get_user_by_id(self,user_id:int):

        connection = get_db_connection()

        if not connection:
            return None

        cursor = connection.cursor(dictionary=True)

        query = """SELECT * FROM users WHERE user_id = %s"""

        cursor.execute(query,(user_id,))

        user = cursor.fetchone()

        connection.close()
        
        return user
    
    def update_last_login(self,user_id:int):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        if not connection:
            return None
        
        query = """UPDATE users SET last_login = NOW() WHERE user_id = %s"""

        cursor.execute(query,(user_id,))

        connection.commit()

        cursor.close()

        connection.close()






    