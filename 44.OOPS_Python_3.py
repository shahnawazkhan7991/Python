"""class c1:
    def addvariables(self):
        self.b=5
        self.c=6

ob1=c1()
ob1.a="Hello"
ob1.b="Welcome"
ob1.addvariables()
print(ob1.a,ob1.b)

ob2=c1()
ob2.a="Hello"
ob2.b="Welcome"
ob2.addvariables()
print(ob2.a,ob2.b)"""

#New program
# class c1:
#     def addvariable(self):
#         self.b=5
#         self.c=6
# ob=c1()
# print(ob.b,ob.c)
"""Above program
We got an error because the addvariable() is not called thats why for creating  the object of the class we use Constructor here.

Constructor:-
syntax-
__init__(self):
"""
# class c1:
#     def __init__(self):
#         self.b=5
#         self.c=6
#
# ob=c1()
# print(ob.b,ob.c)
#
# ob1=c1()
# print(ob1.b,ob1.c)

# output-5 6
#        5 6
"""
When program is terminated the object is deleted and for deleting the object the destructor is called automatically.
Destructor-
syntax-
__del__(self):
"""
# class c1:
#     def __init__(self):
#         print("Constructor is callled")
#         self.a=5
#         self.b=6
#
#     def __del__(self):
#         print("Destructor  is called")
# ob=c1()
# print(ob.a,ob.b)
# #output-Constructor is callled
#           5 6
#         Destructor  is called


#   #Parameteriezed constructor
# class c1:
#     def __init__(self,m,n):
#         self.a=m
#         self.b=n
# x= int(input("Enter a number"))
# y= int(input("Enter second number"))
# ob=c1(x,y)
# print(ob.a,ob.b)

#New program
# class c1:
#     def __init__(self,m=1,n=2):
#         self.a=m
#         self.b=n
#
# ob=c1(11,20)
# print(ob.a,ob.b)
# #Output-11 20


