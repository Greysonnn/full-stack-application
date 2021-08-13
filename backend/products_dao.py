import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='Ru7angc1an666$',
                               port='3306',
                               database='3-tier-db'
                               )

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM users')
