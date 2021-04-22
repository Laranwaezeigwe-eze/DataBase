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

            sql = "insert into human (HumanId, Name, Color, Gender, Bloodgroup) Values (%s, %s,%s, %s, %s)"
            val = []

            for i in range (2):

                HumanId =input('Your Human Id: ')
                Name = input('Give full names: ')
                Color = input('What Skincolor are you? ')
                Gender = input('What Gender are you? ')
                BloodGroup = input('What is your blood Group? ')

                val.append((HumanId, Name, Color, Gender, BloodGroup))

            db_cursor.executemany(sql, val)
            push.commit()
            print (db_cursor.rowcount, "rows inserted")
            db_cursor.close        


except Error as e:
    print('Connection lost due to:', e)

finally: 
    if push is not None and push.is_connected:
        push.close
        print('Disconnection from server')

connect_insert()