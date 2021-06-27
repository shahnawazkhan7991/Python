import pymysql
con = pymysql.connect(host='Localhost', user='root',password='root123', database='employees')
cur = con.cursor()
qry = "select * from employees"
cur.execute(qry)
data = cur.fetchall()
f = open(r"C:\Users\Shahnawaz Khan\Desktop\mybd.xls",'w')
s = "Id\tName\tAge\tEmail\n"
f.write(s)
for Id,name,age,email in data:
    s = str(Id)+"\t"+str(name)+"\t"+str(age)+"\t"+str(email)+"\n"
    f.write(s)
con.close()