####################################################Function Types##################################################
#There are 5-6 different types of function,
#1.Required arguemenet function
# #New program
# def sub(a,b):
#     return a-b
# u,v=5,3
# diff=sub(u,v)
# print(diff)

# #Keyword arguent functions:-
# #New program
# def sub(a,b):
#     return a-b
# u,v=5,3
# diff=sub(b=u,a=v)
# print(diff)

# #Default arguement functions:-
# def sub(a=10,b=6):
#     return a-b
# u,v=5,3
# diff=sub(v)
# print(diff)

# #New program
# l1=[23,44,56,34,32.22]
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# #Variable length arguement functions:-
# def func1(*t):
#     print(t)
#
# func1(2,3)
# func1()
# func1(2,3,4,5,6,7,8)

# #New program
# def add(*args):
#     res=0
#     for e in args:
#         res+=e
#     return res
# n1,n2,n3,n4,n5,n6=1,2,3,4,5,6
# sum=add(n1,n2)
# print(sum)
# sum2=add(n1,n2,n3)
# print(sum2)
# sum3=add(n1,n2,n3,n4,n5,n5,n6)
# print(sum3)

# #Variable length keyword arguement functions:
# def func1(**kwargs):
#     print(kwargs)
#
# a,b,c,d,e=1,2,3,4,5
# func1(u=a)
# func1(no1=a,no2=b,no3=c,no4=d,no5=e)
# func1(no1="")
# func1(no1=None)
# func1(no1=True)

# #New program
# def kwadd(**kwargs):
#     res=0
#     print(kwargs.values())
#     for e in kwargs.values():
#         res +=e
#     return res
# sum1=kwadd(a=2,b=2)
# sum2=kwadd(a=2,b=3,c=11,d=5)
# print(sum1,sum2)



##############################################Lambda function######################################################
# #New program
# x=lambda a,b:a+b
# s=x(2,3)
# print(s)
#
# #New program
# checkEven=lambda a: a%2==0
# print(checkEven(5))
# print(checkEven(12))


