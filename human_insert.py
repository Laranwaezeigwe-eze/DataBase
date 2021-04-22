import mysql.connector
from mysql.connector import Error

def connect_insert():
    push = None

try:
        push = mysql.connector.connect(host = 'localhost', database = 'lara',
        user = 'root', password = 'Firstborn1.')
        print('Connecting to database server')
        if push.is_connected:
            print('Connected to database server')
            db_cursor = push.cursor()

            #create a variable to contain the sql query to be executed
            sql = "insert into human (HumanId, Name, Color, Gender, Bloodgroup) Values (%s, %s,%s, %s, %s)"

            #create a list variable to contain all the values we want to insert into the human table

            val = [
                ('1004', 'Mitchelle June', 'Black', 'Female', 'O+'),
                ('1005 ', 'Adullam Barrack', 'Pink', 'Male', 'B-'),
                ('1006', 'Fredrick Cole', 'Black', 'Male', 'AB'),
                ('1007', 'Chloe Martins', 'Fair', 'Female', 'O-')
            ]
            #execute the query using the executemany function because values to execute is more than one
            db_cursor.executemany(sql, val)

            #commit to the database
            push.commit()

            #print a success message
            print (db_cursor.rowcount, "rows inserted")

            #close the cursor
            db_cursor.close
            

except Error as e:
    print('Loss of connection due to:' , e)

finally:
    if push is not None and push.is_connected:
        push.close()
        print('Database window closed')

connect_insert()        
