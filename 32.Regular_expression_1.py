#RE-RE is a tiny programming language in itself which is used to find out pattern from given strings.
#RE is the collection of special characters which is used to find out these hidden pattern.
#RE is compitable with python using some libraries(re library)

#New program-
# import re
# s = "akjdah sdasndjs shahnawazkhan116@gmail.com anhhq 525655 qwhi jai154@gmail.com jqlwdjn nhinW prabhash54566@gmail.com"
# p = "\w+@\w+[.]\w+"#RE pattern it is used to extract the email id from strings.
# res = re.findall(p,s)
# print(res)

#New program-
# import concurrent.futures
# import re
# s = "Welcome to python class at cetpa infotech.I am your trainer. I will teach you python."
# p = "python"
# res = re.findall(p,s)
# print(res)


##Metacharacters-
#They are some special symbols of the library which have different meanings.
"""
^: cap\caret\hat
$ :
.:
*:
+:
?:
[]: character class
{}: quantity class
(): group measure
\:
|:
"""
#RE pattern made with the help of their metacharacters.

#RE pattern can be 3 types
# 1.character matching pattern
# 2.quantity matching pattern
# 3.location matching pattern

# 1.character matching pattern-
#character matcher class[]:
# #New program
# import re
# s = "Welcome to python class . i will teach you python"
# p = "[abpmszca]"
# res = re.findall(p,s)
# print(res)

#New program
# import re
# s = "Welcom to 123 to 85  .\ class"
# p = "[a-z]"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Welcom to 123 to 85  .\ class"
# p = "[A-Z]"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Welcom to 123 to 85  .\ class"
# p = "[0-9]"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Welcom to 123 to 85  .\ class"
# p = "[a-z A-Z]"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Welcom to 123 to 85  .\ class"
# p = "[a-z A-Z 0-9]"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Welc\som to 123 to 85 pyt\nhon .\ class"
# p = "[^a-z A-Z 0-9]"#It will search everything except alphanumeric
# res = re.findall(p,s)
# print(res)


# #New program
# import re
# s = "Wel\scom to 123 to 85 pyt\nhon .\ class"
# p = r"."#It will serch everything except \n
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "Wel\scom to 123 to 85 pyt\nhon .\ class"
# p = r"\s"#It will search for all white spaces
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = "Wel\ncom to 123 to 85 pyt\nhon .\ class"
# p = r"\S" #It will search everything except white spaces
# res = re.findall(p,s)
# print(res)

