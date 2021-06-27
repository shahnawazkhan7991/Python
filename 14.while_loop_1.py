#Loop:-A llop is a program in any programming language that is used to execute block of code repearly.
#Q.Write a program to print the table of 7.
"""n = int(input("Enter a number"))
i = 7
while i<71:
    print("i = ",i)
    i+=7"""
"""Second method"""
"""n = int(input("Enter a number"))
i = 0
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1"""
#Q.Write a program to print number of 10 times.
"""n = int(input("Enter a number"))
i = 0
while i<10:
    print("i=",i,"n=",n)
    i+=1     #i=i"""
print("*******************************************************************************************************")
#Q.write a program to check wether an input nummber is prime or composite
n = int(input("Enter a number"))
i=2
while i < n:
    if n%i == 0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break
    i+=1
