"""
Q.What are modules?
A. Any pre defines=d or user defined .py file or .pyc file that contains some code.
.pyc file-----python compiled file(machine understable file)
module-----libraries
"""
# 1.How to accesss modules
#There are five ways to access modules:
# a.import module_name
# b.import module_name as alias
# c. from module_name import features
# d. from module_name import features as alias
# e. from module_name import *


# a.import module_name
# import operator
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
#
# sum=operator.add(n1,n2)
# print(sum)
#
# sub=operator.sub(n1,n2)
# print(sub)
#
# product=operator.mul(n1,n2)
# print(product)
#
# division=operator.div(n1,n2)
# print(division)

# b.import module_name as alias

# import operator as op
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
#
# sum=op.add(n1,n2)
# print(sum)

#c.import module_name import feature

# from operator import add
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# sum=add(n1,n2)
# print(sum)

# #New import module
# import Module
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# sum= Module.add(n1,n2)
# print(sum)

# #import module_name as alias
# import Module as M
# a=5
# b=8
# sum=M.add(a,b)
# print("This is the sum of program",sum)

#from module_name as  import feature
# from Module import add,sub
# n1=5
# n2=10
# sum=add(n1,n2)
# print(sum)
# diff=sub(n1,n2)

#d.from module_name import feature as alias

#New program
from Module import add as a
n1=8
n2=10
sum=a(n1,n2)
print("This is the sum",sum)

#e.from module import *
# from Module import *
# n1=8
# n2=10
# sum=add(n1,n2)
# print("This is the sum",sum)
#
# diff=sub(n1,n2)
# print("This is the diff",sub)
#
# product=mul(n1,n2)
# print("This is the product",mul)
print("***********************************************************************************************************************")
# from Module import *
# # from math import *
# # from operator import *
#
# n1=5
# n2=10
# sum=add(n1,n2)
# print(type(sum))








