#Q.write a program to print number of 10 times.
for i in range(10):
     print(10)

#Q.write a progtam to print table of 7.
num = 7
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Q.Write a program to print table of any number.
num = int(input("Enter a number"))
for i in range(1,11):
    print(num*i)
#Q.Write aprogram to check wether the number is prime or not.
n = int(input("Enter a number"))
for i in range(2,n):
    if n%2 == 0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break
#Q.Write a program to capitalize all characters of an input string.
inp = input("Enter a string")
res_str = " "
for e in inp:
    code = ord(e)
    if code>=97 and code<=122:
        code -= 32
    char = chr(code)
    res_str += char
print(res_str)
