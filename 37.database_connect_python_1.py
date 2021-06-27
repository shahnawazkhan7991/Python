"""import pymysql
con = pymysql.connect(host='Localhost', user='root',password='root123', database='employees')
print(type(con))
cur = con.cursor()
print(type(cur))
con.close()

#output-
#<class 'pymysql.connections.Connection'>
#<class 'pymysql.cursors.Cursor'>"""
"""import pymysql
con = pymysql.connect(host='Localhost', user='root',password='root123', database='employees')
cur = con.cursor()
qry = "select * from employees"
cur.execute(qry)
data = cur.fetchall()
print(data)
con.close()"""

"""import pymysql
con = pymysql.connect(host='Localhost', user='root',password='root123', database='employees')
cur = con.cursor()
qry = "select * from employees"
cur.execute(qry)
data = cur.fetchall()
for Id,name,age,email in data:
    print(Id,name,age,email)
con.close()"""
