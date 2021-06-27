#A loop inside another loop is called nested loop.
"""for i in range(5):
    for j in range(2):
        print(i,j)"""
#Extra added-
"""print("1.First pattern")
value = int(input("Enter a value"))
for i in range(value):
    print("*"*i)"""
#Pattern printing program-
# 1.First pattern
# *
# * *
# * * *
# * * * *
# * * * * *

#Code-
"""rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i+1):
        print("*", end = " ")
    print()"""

print("2.second pattern**********************************")
#Second pattern-
# * * * * *
# * * * *
# * * *
# * *
# *

#Code-
"""rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(rows-i):
        print("*", end = " ")
    print()"""

print("3.Third pattern**********************")
#3.Third pattern-
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#Code-
"""rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    print()"""

print("4.Forth pattern***************************")
#4.forth pattern-
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
#Code-
"""rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i+1):
        print("*", end = " ")
    for k in range((rows - i - 1)*2):
        print(" ", end=" ")
    for l in range(i + 1):
        print("*", end=" ")
    print()"""

print("5.Fifth pattern********************")
# 5.fifth pattern-
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
"""rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(rows-i-1):
       print(" ", end = " ")
    for k in range(i*2+1):
        print("*", end = " ")
    print()"""
print("***********************************************************************************************")
rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(2*rows-2):
        print("", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    print()





