"""import pymysql
mycon = pymysql.connect(host = 'localhost', user = 'root',password = 'root123')
mycur = mycon.cursor()
mycur.execute("use employees")
qry = "insert into employees values(2010,'Rohan',20,'rohan123@gmail.com')"
mycur.execute(qry)
mycon.commit()
mycon.close()"""

import pymysql
mycon = pymysql.connect(host = 'localhost', user = 'root',password = 'root123')
mycur = mycon.cursor()
mycur.execute("use employees")
Id = int(input("Enter employees Id:"))
name = input("Enter employees name:")
age = int(input("Enter employees age:"))
email = input("Enter employees email:")
qry = f"insert into employees values({'Id'},{'name'},{'age'},{'email'})"
mycur.execute(qry)
mycon.commit()
mycon.close()