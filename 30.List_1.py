#List-It is a datatype in python which can store multiple hetrogeneous datatypes.
# a = 5
# b = 7
# c = "Hello"
# d =["I am learning pyhon and i will be expert in python",5,5,8,"Hello"(5,6,8)]

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# print(type(L))

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res1 = L
# print("original res1:",res1)
# res = L.copy()
# print("original res:",res)
#
# res1 = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# print(L)
# print(res1)
# print(res)

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res = L.pop() #Remove the last element
# print(L)
# res1 = L.pop(2)
# print(L)

##New program
# list = [10,20,30,40,50,60]
# print(list.pop())

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res = L.append(2) #add 2 in last
# print(res)
# print(L)

# #New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res = L.insert(2,"Welcome")
# print(res)
# print(L)

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res = L.extend("Welcome")
# print(L)

#New program
# L = [3,5.33,"Hello",[1,2,3],("abc","def","ghi")]
# res = L.clear()
# print(L)

#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.sort()#Ascending order
# print(L)


#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.sort(reverse = True)# reverse Ascending order
# print(L)

#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.index(5,0,3)
# # print(L)
# print(res)



#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.remove(10)
# print(L)


#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.count(5) #Counts the characters
# print(res)


#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = L.reverse()
# print(L)
# # print(res)

#New program
# L = [5,6,4,8,9,10,20,4,5]
# res = len(L)
# # print(L)
# print(res)

#How to create User defined list
# list = []
# no_of_element = int(input())
# for i in range(no_of_element):
#     value = input("Enter an element")
#     list.append(value)
# print(list)