###########################################Exception Handling############################################################
#Handling runtime error in the program
# try:
#   n1=int(input("Enter a  number"))
#   n2=int(input("Enter second number"))
#   res=n1/n2
#   print(res)
# except:
#   print("Error in the program")
#
# while 1:
#     try:
#         n1 = int(input("Enter a  number"))
#         n2 = int(input("Enter second number"))
#         res = n1 / n2
#         print(res)
#         break
#     except:
#         print("Error in the program")

# #New program
# while True:
#     try:
#         n1 = int(input("Enter a  number"))
#         n2 = int(input("Enter second number"))
#         res = n1 / n2
#         print(res)
#         break
#     except Exception as err:
#         print("Error!!",err)

#New program
while True:
    try:
        n1 = int(input("Enter a  number"))
        n2 = int(input("Enter second number"))
        res = n1 / n2
        print(res)
        break
    except ValueError:
        print("please enter whole number only")
    except ZeroDivisionError:
        print("The second number should be non-zero")
    except Exception as err:
        print("Error!!",err)