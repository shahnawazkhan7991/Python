#Calculator using while True loop.
while True:
    n1 = int(input("Enter first number"))
    n2 = int(input("Enter second number"))
    print("""
    press 1 for Addition
    press 2 for subtraction
    press 3 for multiplication
    press 4 for division
    """)
    operation = int(input("Enter your choice"))
    if operation == 1:
        C = n1 + n2
        print("The sum is", C)

    elif operation == 2:
        C = n1 - n2
        print("The difference is", C)
    elif operation == 3:
        C = n1 * n2
        print("The multiplication is", C)
    elif operation == 4:
        C = n1 / n2
        print("The division is", C)
    else:
        print("Incorrect choice")


