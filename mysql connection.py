
import mysql.connector
connection = mysql.connector.connect(user="root",password="",database="piyush")
cursor=connection.cursor()

try:
    # agar primary key likha to table me duplicate value nhi a sakti
    # query = "create table students(roll int primary key auto_increment,name text,class int)"
    # cursor.execute(query)
    #changes saved successfully
    # print("Table Created Successfully✅")
    # Storing data in MYSQL TABLE USING PYTHON
    # name  = input("Enter Name : ")
    # cls   = input("Enter Class : ")
    # data  = (name,cls)
    # query = "insert into students (name,class) values (%s,%s)"
    # cursor.execute(query,data)
    # connection.commit()
    # HOW TO INSERT
    query = "select * from students"
    cursor.execute(query)
    for data in cursor.fetchall():
        print(data)
    #HOW TO DELETE
    # query = "delete from students where id=1"
    # cursor.execute(query)
    # connection.commit()

except BaseException as be:
    print(be)
finally:
    connection.close()
