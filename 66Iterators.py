#######################################################################################################################
# #New program
# l1=[2,3,4,5,6]
# ob=l1.__iter__()
# print(type(ob))
# ob.__next__()

# #New program
# class student:
#     def __init__(self,Math,English,Hindi,Science):
#         self.Math=Math
#         self.English=English
#         self.Hindi=Hindi
#         self.Science=Science
#
# st1=student(21,30,27,15)
# st2=student(85,97,98,92)
# print(st1)
# print(st2)

# #New program
# l1=[2,3,4,5]
# ob=l1.__iter__()
# print(type(ob))
# e=ob.__next__()
# print(e)
# e=ob.__next__()
# print(e)
# e=ob.__next__()
# print(e)
# e=ob.__next__()
# print(e)
# print("Hello")

# #New program
# for i in range(2,3,0.1):
#     print(i)
#     output-TypeError: 'float' object cannot be interpreted as an integer


# #New program
# for i in range(2,3,5):
#     print(i)

# #New program
# class MyfloatRange:
#     def __init__(self,start,stop,step):
#         self.start=start
#         self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start>=self.stop:
#             raise StopIteration
#         temp=self.start
#         self.start+=self.step
#         return temp
# for i in MyfloatRange(2,3,0.1):
#     print(i)

# # New program  Return Even values in given ranges
# class MyEvenRange:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __next__(self):
#         if self.start % 2 == 1:
#             self.start += 1
#         if self.start >= self.stop:
#             raise StopIteration
#         temp = self.start
#         self.start += 2
#         return temp
#
#
# for i in MyEvenRange(0, 53):
#     print(i)

#New program
#####################################################Generators####################################################
# def add(a,b):
#     return a+b
# x=add(5,7)
# print(x)
# y=add
# print(type(y))
# print(type(add))


# #New progtram
# def add(a,b):
#     yield a+b #Generator
# x=add(5,7)
# print(x)
# print(type(x))

# #New program
# def func1():
#     yield 5
#     yield 6
#     yield 7
# for i in func1():
#     print(i)

# #New program to generator or return even numbers
# def myEvenGenerator(start,stop):
#     if start % 2 ==1:
#         start += 1
#     for j in range(start,stop,2):
#         yield j
# for i in myEvenGenerator(3,9):
#     print(i)
