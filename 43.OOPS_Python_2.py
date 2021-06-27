"""class c1:
    def method1(self, b, c):
        print(self, b, c)

    def method2(self, b, c):
        print(self, b, c)


ob1 = c1()
print(ob1)
ob1.method2(1, 2)

ob2 = c1()
print(ob2)
ob2.method2(5, 7)
#Output--<__main__.c1 object at 0x000001D701CF2FD0
# <__main__.c1 object at 0x000001D701CF2FD0> 1 2
# <__main__.c1 object at 0x000001D701CF2F10
# #<__main__.c1 object at 0x000001D701CF2F10> 5 7"""

#Instance VAriables-
#1.Inside the class:
# self.var_name=vlue
#2.Outside the class
# obj_name.var_name=vlue

#New program
class c1:
    def method1(self):
        self.b=5
ob1=c1()
ob1.a=11

#In this program we are learning how to access the instance variables inside and outside the class;
#so lets get started no
"""class c1:
    def addvariable(self):
        self.b=5
        self.c=9.58
        print(self.a,self.b,self.c)
ob=c1()
ob.a="Hello"
ob.addvariable()
print(ob.a,ob.b,ob.c)"""
#Output-
# Hello 5 9.58
# Hello 5 9.58

"""#now Assigning Two variables
class c1:
    def addvariable(self):
        self.b=5
        self.c=54.789
ob1=c1()
ob1.a=11
ob1.addvariable()

ob2=c1()
ob2.a=1002
ob2.addvariable()

print(ob1.a,ob1.b,ob1.c,ob2.a,ob2.b,ob2.c)
#Output-11 5 54.789 1002 5 54.789"""




