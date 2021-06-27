#Q,Write a program to make a calculator
n1 = int(input("Enter first number"))
n2 = int(input("Enter Second number"))

print("""
press 1 for Addition
press 2 for Subtration
press 3 for multiplication
press 4 for division
press 5 for modulus
pree 6 for float division
""")
operation = int(input("Enter your choice:"))
if operation == 1:
    c = n1 + n2
    print("The sum is",c)
elif operation == 2:
    c = n1 - n2
    print("The subtraction is",c)
elif operation == 2:
    c = n1 - n2
    print("The subtraction is",c)
elif operation == 3:
    c = n1 * n2
    print("The product is",c)
elif operation == 4:
    c = n1 / n2
    print("The division is",c)
elif operation == 5:
    c = n1 % n2
    print("The remainder is",c)
elif operation == 6:
    c = n1 // n2
    print("The float division is",c)
else:
    print("Incorrect choice")
#Second method

n1 = int(input("Enter first number"))
n2 = int(input("Enter Second number"))

operation = input("""
press + for Addition
press - for Subtration
press * for multiplication
press / for division
Enter your choice
""")
if operation == "+":
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
else:
    print("Incorrect choice")