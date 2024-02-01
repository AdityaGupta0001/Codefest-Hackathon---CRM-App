# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = user,
	passwd = password

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE test_db_crm")

print("All Done!")
