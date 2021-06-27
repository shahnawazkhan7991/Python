#Local variable:- The variables which are defined inside some particular function.Class or method are called the local variable.

#Global variable:-The variable which are not defined insde any function,class or method.
# They are defined globally and can be used anywhere in the program.

"""#BLL start here
def add(no1,no2):
    res=no1+no2  #Local variable
    return res   #Local Variable
#BLL ends here
#PL start here
n1=int(input("Enetr first number"))   #Global variable
n2=int(input("Enetr second number"))  #Global Variable
sum=add(n1,n2)
print(sum)
#PL ends here"""

# #BLL start here
# def add(no1,no2):
#     res=no1+no2  #Local variable
#     print("This is local n1",n1)
#     print("This is local n2",n2)
#     return res   #Local Variable
# #BLL ends here
# #PL start here
# n1=int(input("Enetr first number"))   #Global variable
# n2=int(input("Enetr second number"))  #Global Variable
# sum=add(n1,n2)
# print(sum)
# print("This is global n1",n1)
# print("This is global n2",n2)
# #PL ends here

#Vaue overwrite
def func1():
    a=5
    print(a)

a=7
func1()
print(a)
#Output-5
      #7
#Value overwrite
def func1():
    global a
    a=5
    print(a)

a=7
func1()
print(a)
#Output-5
       #5
def func1():
    print("This is func1")
def func2():
    print("This is func2")

a=8
b=7.83
c="Hello"
print(type(a))
print(type(b))
print(type(c))
print(type(func1))
print(type(func2))

# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'function'>
# <class 'function'>
