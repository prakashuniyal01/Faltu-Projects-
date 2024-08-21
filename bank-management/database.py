#Database Management Banking
import mysql.connector as sql

mydb = sql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="banks"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) NOT NULL unique,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL DEFAULT 0,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL)
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()