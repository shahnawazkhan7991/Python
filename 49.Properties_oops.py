#Types of inheritance
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchial Inheritance
# 5. Hybrid Inheritance

#1.Single Inheritance:-
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2(c1):
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c2")
#
#     def showdata(self):
#         print("This is class c2(1)")
# ob = c2()
# print(ob.a,ob.b,ob.c,ob.d)
# ob.showdata()
#Multilevel Inheritance:-
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2(c1):
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c2")
# class c3(c2):
#     def __init__(self):
#         self.e = 10
#         self.f = 11
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c3")
#
# ob = c3()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f)
# ob.showdata()

#Hierarchial Inheritance:-
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2(c1):
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c2")
# class c3(c1):
#     def __init__(self):
#         self.e = 10
#         self.f = 11
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c3")
# class c4(c1):
#     def __init__(self):
#         self.g = 12
#         self.h = 13
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c4")
# ob = c3()
# print(ob.a,ob.b,ob.e,ob.f, )
# ob.showdata()

#Multiple Inherritance
#New program
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2():
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#
#     def showdata(self):
#         print("This is class c2")
# class c3():
#     def __init__(self):
#         self.e = 10
#         self.f = 11
#
#
#     def showdata(self):
#         print("This is class c3")
# class c4(c1,c2,c3):
#     def __init__(self):
#         self.g = 12
#         self.h = 13
#         super().__init__()
#         c2.__init__(self)
#         c3.__init__(self)
#
#     def showdata(self):
#         print("This is class c4")
# ob = c4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.h)
# ob.showdata()
# print(c4.__mro__)
# #Hybrid Inheritance-1
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2(c1):
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c2")
# class c3(c1):
#     def __init__(self):
#         self.e = 10
#         self.f = 11
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c3")
# class c4(c2,c3):
#     def __init__(self):
#         self.g = 12
#         self.h = 13
#         super().__init__()
#         c3.__init__(self)
#
#     def showdata(self):
#         print("This is class c4")
# ob = c4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h )
# ob.showdata()
# print(c4.__mro__)

# #Hybrid Inheritance-2
# #New program
# class c1:
#     def __init__(self):
#         self.a = 4
#         self.b = 5
#
#     def showdata(self):
#         print("This is classs c1")
#
# class c2(c1):
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c2")
# class c3:
#     def __init__(self):
#         self.e = 10
#         self.f = 11
#         super().__init__()
#
#     def showdata(self):
#         print("This is class c3")
# class c4(c2,c3):
#     def __init__(self):
#         self.g = 12
#         self.h = 13
#         super().__init__()
#         c3.__init__(self)
#
#     def showdata(self):
#         print("This is class c4")
# ob = c4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h )
# ob.showdata()
# print(c4.__mro__)