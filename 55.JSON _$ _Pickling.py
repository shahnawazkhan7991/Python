#################################################################################################################################
#Pickling - This is python internal standard and data is managed in binary format.
# #New program
# #dump
# import pickle
# data = [22,33,44,"Python","Cetp",11.53]
# f=open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\pickling.txt",'wb')
# pickle.dump(data,f)
# f.close()

# #New program
# #load
# import pickle
# data = [22,33,44,"Python","Cetp",11.53]
# f=open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\pickling.txt",'rb')
# data=pickle.load(f)
# print(data)
# f.close()

#JSON-Java script Object Notation
#The data in Json is managed in key value pair
# #New program
# #dump
# import json
# data = [22,33,44,"Python","Cetp",11.53]
# f=open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\json.txt",'w')
# json.dump(data,f)
# f.close()

#New program
#dump
import json
data = [22,33,44,"Python","Cetp",11.53]
f=open(r"C:\Users\Shahnawaz Khan\PycharmProjects\pythonProject\json.txt",'r')
data=json.load(f)
print(data)
f.close()

