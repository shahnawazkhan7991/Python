# # 3.Location matching pattern
# # ^ : It searches at the beginning of the pattern
# #$: It searches at the end of the string
#
# #New program
# import re
# s = """Welcome to python class.Welcome to hello world. i will teach you python"""
# p = "^Welcome"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = """welcome to python class.I am your trainer. i will teach you python.
#         I will be expert you to learn python."""
# p = "^[a-z]"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = """Welcome to python class.Welcome to hello world. i will teach you python"""
# p = "python$"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = """Shahnawaz, Rehan, jai, prabhash,Shahnawaz """
# p = "^Shahnawaz"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = "Shahnawaz,Shahnawaz "
# p = "^Shahnawaz$"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# email = input("Enter your email ID")
# p = "\w+@\w+[.]\w+$"
# res = re.findall(p,email)
# print(res)
# print(len(res))
# if len(res)== 1:
#     print("Valid email ID")
# else:
#     print("Invalid email ID")

#
# #New program
# import re
# s = """ adhnasj abcd@gmail.com 4645WDBB shahnawaz555@gmail.com rehan@gmail.com aduhaihujwdjj evolution.academy@acem.edu.in"""
# p = r"\w+[.]?\w*@\w+[.]\w+[.]?\w*"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "jefojhj 9570652344 7991785621 5657665555 758216654 7559662115 22335445455"
# p = r"\d{10}"
# res = re.findall(p,s)
# print(res)

#New program
import re
s = """ adhnasj  kon *$abcd@gmail.com 4645WDBB shahnawaz555@gmail.com rehan@gmail.com aduhaihujwdjj evolution.academy@acem.edu.in"""
p = r"\w+[.]?\w*@\w+[.]\w+[.]?\w*"
res = re.findall(p,s)
print(res)


