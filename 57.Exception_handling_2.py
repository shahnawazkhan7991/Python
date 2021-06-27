#########################################finally and raise keyword###################################################
# finally: it is a block of code which execute everytime in our program
# while True:
#     try:
#         n1 = int(input("Enetr first number"))
#         n2 = int(input("Enetr second number"))
#         op = input("Select any number: +, - . *, /, power, log")
#
#         if op == '+':
#             res = n1 + n2
#             print("The sum is", res)
#
#         elif op == '-':
#             res = n1 - n2
#             print("The difference is", res)
#         elif op == '*':
#             rs = n1 * n2
#             print("TRhe product is", res)
#         elif op == '/':
#             res = n1 / n2
#             print("The division is ", res)
#
#         else:
#             print("Invalid choice")
#
#
#     except ValueError:
#            print("Enter e=whole number only")
#
#     except ZeroDivisionError:
#         print("The second number should be non-zero")
#
#     except Exception as err:
#         print("Error!!",err)
#
#     finally:
#         chyn=input("Do you want to perform another calculation? Y/N")
#         if chyn== "N" or chyn== "n":
#             break

#############################################################raise#############################################
# while True:
#     try:
#         n1 = int(input("Enetr first number"))
#         n2 = int(input("Enetr second number"))
#         op = input("Select any number: +, - . *, /, power, log")
#
#         if op == '+':
#             res = n1 + n2
#             print("The sum is", res)
#
#         elif op == '-':
#             res = n1 - n2
#             print("The difference is", res)
#         elif op == '*':
#             rs = n1 * n2
#             print("TRhe product is", res)
#         elif op == '/':
#             res = n1 / n2
#             print("The division is ", res)
#
#         else:
#             raise NotImplementedError("Incorrect choice")
#
#
#     except ValueError:
#            print("Enter e=whole number only")
#
#     except ZeroDivisionError:
#         print("The second number should be non-zero")
#
#     except Exception as err:
#         print("Error!!",err)
#
#     finally:
#         chyn=input("Do you want to perform another calculation? Y/N")
#         if chyn== "N" or chyn== "n":
#             break

#New program
try:
    ch=int(input("Enter choice 1,2 or 3:"))
    if ch==1:
        raise ValueError("Cetpa")
    elif ch==2:
        raise ValueError("Welcome")
    else:
        raise ValueError("Hello")
except ValueError as err:
    print("Error!!",err)

