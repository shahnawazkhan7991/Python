#########################################Delegation Starts__OOPS##################################################################

#Delegation- The process of definig a function through a variable is called delegation

# #New program
# def func1():
#     print("This is a func1")
#
# func1()
# print(func1)
# x = func1()
#
# def add(no1,no2):
#     print(no1+no2)
# print(add)
# x=add
# x(8,6)

#Output-
# This is a func1
# <function func1 at 0x000001ADECE0E040>
# This is a func1
# <function add at 0x000001ADECFF2280>
# 14

# #New program
# def add(no1,no2):
#     print(no1+no2)
# x=add  #X is a function pointer and its storing the address of function add()
# x(8,5) #add function will be called because x s having the address of add() in it.

# #New program
# def add(no1,no2):
#     no1,no2= 5,6
#     res = no1+no2
#     return res
# def func1():
#     func1=add
#     return func1(2,3)
# r=func1()
# print(r)

#Double sorting Technique
#New program
def mysort(L, key=None):
    if key==None:
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                if L[i]>L[j]:
                    L[i],L[j]=L[j],L[i]

    else:
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                if key (L[i])>key(L[j]):
                    L[i],L[j]=L[j],L[i]

def reverse(e):
    return e
L1=[22,13,12,12,32,78,45,34]
mysort(L1, key=reverse)
print(L1)

