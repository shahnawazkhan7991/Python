# Function:-Function in any programming language is a block of code that is used to perform soecific task repeatedly.
#New program
# #BLL start here
# def add(no1,no2):
#     res=no1+no2
#     return res
# #BLL ends here
# #PL start here
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# sum=add(n1,n2)
# print(sum)
# #PL ends here

print("###########################################################################################################")
# #BLL start here
# def add(no1,no2):           #Line1   #Line5
#     res=no1+no2              #Line6
#     return res               #Line7
# #BLL ends here
# #PL start here
# n1=int(input("Enetr first number")) #Line2
# n2=int(input("Enetr second number"))  #Line3
# sum=add(n1,n2)        #Line4   #line8
# print(sum)            #Line9
# #PL ends here


# #BLL start here
# def add(no1,no2):
#     res=no1+no2
#     print(res)
# #BLL ends here
# #PL start here
# n1=int(input("Enter first choice"))
# n2=int(input("Enter second choice"))
# sum= add(n1,n2)
# print(sum)
# print(type(sum))
# #Pl ends here

def add(no1,no2):
    return no1+no2
def add(no1,no2,no3=0,no4=0):
    return no1+no2+no3+no4
n1=int(input())
n2=int(input())

sum=add(n1,n2)
print(sum)

