#Stream:- Block of data
#Modes in File handling:-
# 1. Character oriented Stream
# 'r':-Read mode:if the file is present then thr[e data will be read from the starting ofthe file but
#     if the file is not present.
#
# 'w':Write mode
# 'a':append mode
# 'r+':Read and Write
# 'w+':Write and read
# 'a+':Read and append
# 2.Byte oriented stream-
# 'rb'
# 'wb'
# 'ab'
# 'rb+'
# 'wb+'
# 'ab+'

# #New program
# import os
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\Introduction to Python","r")
# data = f.read()
# print(data)
# f.close()

# #New program
# import os
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt","r")
# data = f.read()
# print(data)
# f.close()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'w')
# s = "I am willing to to learn Python"
# f.write(s)
# f.close()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'a')
# s = ". I am expert in python"
# f.write(s)
# f.close()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'rb')
# data=f.read()
# print(data)
# f.close()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\File2.txt","w")
# s= "Welcome to cetpa\n"
# f.write(s)
# f.write("We will studying Python as Cetpa")
# f.close()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'r')
# data=f.read(6)
# print(data)
# data=f.read(15)
# print(data)
# f.close()

########################################################################################################
# the tell() method:the tell() method with tell is the position of the cursor at any given point of time.
# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'r')
# print(f.tell())
# data=f.read(6)
# print(data)
# print(f.tell())
# data=f.read(15)
# print(data)
# print(f.tell())
# f.close()

#Seek() method: The seek() ,ethod is used to sendd the cursor ferom one position to another position.
#syntax of seek method():
# obj_name.seek(offset, whence)

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'rb')
# print(f.tell())
# data=f.read(11)
# print(data)
# print(f.tell())
# f.seek(4,0)
# print(f.tell())
# data=f.read(7)
# print(data)
# f.seek(8,1)
# print(f.tell())
# f.tell()

# #New program
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'rb')
# data=f.read(100)
# print(data)
# f.close()

#New program
f1 = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\filehandling.txt",'rb')
f2 = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\file2.txt",'wb')
while True:
    data = f1.read(100)
    if data == b"":
        break
    else:
        f2.write(data)
f1.close()
f2.close()