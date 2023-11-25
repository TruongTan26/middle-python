import mysql.connector
def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbtest"
    )
    return mydb

def create_cursor(mydb):
    return mydb.cursor()