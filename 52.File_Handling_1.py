#File Handling:
# print("*********************************************************************")
# # Escape characters:-
# # \n,\t
# s = r"Wel\come t\o  cet\pa"
# print(s)

# New program
# import os
# #it used to read the file
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\Introduction to Python","r")
# data = f.read()
# print(data)
# f.close()

# #New program
# import os
# #Default mode to accessingfile to read mode
# f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\Introduction to Python")
# data = f.read()
# print(data)
# f.close()

#Q. How to create an object?
# obj_Name = class_Name()
# class c1:
#     pass
# ob = c1()
# print(type(ob))
# #We have another way to create an object
#
# class c1:
#     pass
# def func1():
#     return c1()
# for i in range(10):
#     ob = func1()
#     print(type(ob))
#     print(ob)

# New program
import os
#it used to read the file
f = open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\Introduction to Python","r")
data = f.read()
print(data)
f.close()
print(type(f))#<class '_io.TextIOWrapper'>

