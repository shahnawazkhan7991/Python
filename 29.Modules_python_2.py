#3.How to access selected code of program.
# import Module as M
# a = 5
# b = 7
# sum = M.add(a,b)
# print(sum)
# print("File:",__name__)

#Pre defined value __name__
# from Module import *
# if __name__ == '__main__':
#     a= 7
#     b = 9
#     sum= add(a,b)
#     print("The sum is",sum)
#     print("Module:",__name__)

#4.How to access module which is not in current directory.
# import sys
# print(sys.path)
# sys.path.append(r'C:\\Users\\Shahnawaz Khan\\PycharmProjects\\pythonProject')
# print(sys.path)
# import Module as M
# a = 5
# b = 7
# sum = M.add(a,b)
# print(sum)

##5.How to create .pyc (Python compiled file)
# import py_compile
# py_compile.compile("Module.py")


#6.How to access compile file
# import ModuleC as MCom
# n1 = 5
# n2 = 8
# sum = MCom.add(n1,n2)
# print(sum)


## How to create package-
# import Python.M3
# import Python.M4
# n1 = 5
# n2 = 7
# mul =  Python.M3.mul(n1,n2)
# print(mul)

#New program
# import Python
# import Python
# n1 = 5
# n2 = 7
# mul = Python.M4.div(n1,n2)
# print(mul)


#New program
from Python import *
import Python
n1 = 5
n2 = 7
mul = Python.M1.add(n1,n2)
print(mul)
