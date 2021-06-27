"""a,b,c,d,e = 2,3,4,5,6
print(a,b, sep = '#', end = '%%')
print(c,d, sep = '#', end = 'Hello')
print(e, end = 'HelloHi''\n')
#output-2#3%%4#5Hello6HelloHi
print("Second Method")
print(a, end = '#')
print(b,c, sep = '%%', end = '#')
print(d,e, sep = 'Hello', end = 'HelloHi''\n')
"""

print("######################################################################################################")

"""a,b,c,d,e = 2,3,4,5,6
print(a,b, sep = '^', end = '%%''\n')
print(c,d, sep = '$', end = 'HelloHi''\n')
print(e, end = 'Hello')
#output-#2^3%%
        #4$5HelloHi
        #6Hello"""

"""#Output-#2^3%%

        #4$5

        # HelloHi
        #6Hello
a,b,c,d,e = 2,3,4,5,6
print(a,b, sep = '^', end = '%%''\n\n')
print(c,d, sep = '$', end = '\n\nHelloHi\n')
print(e, end = 'Hello')"""

#Output-
#2%3
#4Hello5HiHello
#6$&
a,b,c,d,e = 2,3,4,5,6
print(a,b, sep = '%')
print(c,d, sep = 'Hello', end = 'HiHello''\n')
print(e, end = '$&')






