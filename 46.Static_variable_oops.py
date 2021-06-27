# #New program
# class c1:
#     a,b = 5,6
#     def __init__(self):
#         self.c = 11
#         self.d = 12
#
#
# ob = c1()
# print(ob.c,ob.d)
# print(c1.a,c1.b)
# print(ob.a,ob.b)
#
# ob2 = c1()
# print(ob2.c,ob.d)
# print(c1.a,c1.b)
# print(ob2.a,ob2.b)

# #New program
# class c1:
#     a,b = 1,2
#     def __init__(self):
#         self.c = 8
#         self.d = 9
#
#
# ob = c1()
# ob2 = c1()
# ob2.c = 11
# ob2.d = 36
# print(ob.c,ob.d)
# print(ob2.c,ob2.d)
# print(c1.a,c1.b)

# #New program
# class c1:
#     def __init__(self):
#         self.c = 8
#         self.d = 9
# ob1 = c1()
# ob2 = c1()
# print("Fist time")
# print(ob1.c,ob1.d)
# print(ob2.c,ob2.d)
#
# c1.a = 5
# c1.b = 7
# ob1.c = 16
# ob1.d = 17
# print("Second time")
# print(ob1.c,ob1.d)
# print(ob2.c,ob2.d)

# #New program
# class c1:
#     a = 0
#     def __init__(self):
#         self.x = 0
#     def inc_show(self):
#         c1.a+=1
#         self.x +=1
#         print(c1.a,ob.x)
# ob = c1()
# ob.inc_show()
# ob.inc_show()
# ob.inc_show()

#New program
class c1:
    a = 0
    def __init__(self):
        self.x = 0

    def inc_show(self):
        c1.a += 1
        self.x += 1
        print(c1.a,self.x)

ob1 = c1()
c1.a = 0
ob1.x = 0
ob1.inc_show()
c1.a = 1
ob1.x = 1

ob2 = c1()
c1.a = 1
ob2.x = 0
ob2.inc_show()
c1.a = 2
ob2.x = 1

ob3 = c1()
c1.a = 2
ob3.x = 0
ob3.inc_show()
c1.a = 3
ob3.x = 1
