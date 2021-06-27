"""#Write a program to convert all character of a string into upper case.
inp_str = input("Enter a string")
res_str = " "
i = 0
while i<len(inp_str):
    code = ord(inp_str[i])
    if code >= 97 and code <= 122:
        code -= 32
    char = chr(code)
    res_str += char  #res_str = res_str+char
    i+=1             #i = i + 1
print(res_str)
print("************************************************************************************************")

#Write a program to convert all character of a string into lower case.
inp_str = input("Enter a string")
res_str = " "
i = 0
while i<len(inp_str):
    code = ord(inp_str[i])
    if code >= 65 and code <= 90:
        code += 32
    char = chr(code)
    res_str += char  #res_str = res_str+char
    i+=1             #i = i + 1
print(res_str)"""
print("##################################################################################################")
#Write aprogram to capitalize all the character present at even indexes in an input string.
inp = input("Enter a string")
res = " "
i = 0
while i<len(inp):
    code = ord(inp[i])
    if i % 2 == 0:
        if code >= 97 and code <= 122:
            code -= 32
    char = chr(code)
    res += char
    i+=1
print(res)

#Q.write a program to capitalize all characters at odd indexes of an input string and convert all characters at even indexes into lower case.
inp = input("Enter a string")
res = " "
i = 0
while i<len(inp):
    code = ord(inp[i])
    if i % 2 == 0:
        if code >= 65 and code <= 90:
            code += 32
    else:
        if code >= 97 and code <=122:
            code -= 32

    char = chr(code)
    res += char
    i+=1
print(res)



