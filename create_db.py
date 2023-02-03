# Description: Create a database in MySQL
# USE ONLY IF YOU HAVE NOT CREATED A DATABASE IN MYSQL

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Supermancsgo!00",
)

my_cursor = mydb.cursor()


my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
