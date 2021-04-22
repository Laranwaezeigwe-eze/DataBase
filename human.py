import mysql.connector
from mysql.connector import Error

def connect_fetch():
    push = None

try:
        push = mysql.connector.connect(host = 'localhost', database = 'lara',
        user = 'root', password = 'Firstborn1.')
        print('Connecting to database server')
        if push.is_connected:
            print('Connected to database server')

            sql_select_query = 'select * from human'
            marker = push.cursor()
            marker.execute(sql_select_query)
            records = marker.fetchall()
            print('Total number of rows in human is: ', cursor.rowcount)

            print("\nPrinting each human record")
            for row in records:
                print("HumanId:", row[0])
                print("Name:", row[1])
                print("Color:", row[2])
                print("Gender:", row[3])
                print("Blood group:", row[4], '\n') 

            

except Error as e:
            print('Not connecting due to: ',e)
finally:
                if push is not None and push.is_connected():
                    push.close()
                    print('Database shutdown')



connect_fetch()                        