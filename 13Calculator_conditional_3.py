#Scientific Calculator-
import math
import operator
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))

operation = input("""
press + for addition
press - for subtraction
press * for multiplication
press / for division
press % for modulus
press // for float division
press pow for float power
press log for float logorithm
press sin for sine 
press cos for cosine
Enter your choice:
""")
if operation == "+" :
    c = n1 + n2
    print("The sum is",c)
elif operation == "-":
    c = n1 - n2
    print("The difference is",c)
elif operation == "*":
    c = n1 * n2
    print("The product is",c)
elif operation == "/":
    c = n1 / n2
    print("The division is",c)
elif operation == "%":
    c = n1 % n2
    print("The remainder is",c)
elif operation == "//":
    c = n1 // n2                  
    print("The float division is",c)
elif operation == "pow":
    c = operator.pow(n1,n2)
    print("The power is",c)
elif operation == "log":
    c = math.log(n1,n2)
    print("The logorithm is",c)
elif operation == "sin":
    c = math.sin(n1)
    print("The sine is",c)
elif operation == "cos":
    c = math.cos(n2)
    print("The cosine is",c)
else:
 print("Incorrect choice")