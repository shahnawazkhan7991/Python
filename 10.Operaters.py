# The operators are symbols that we use to perform an operation on two operands.
"""print("1.Arithmetic operator"'\n')
a, b = 5,6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)"""

"""print("2.Conditional operator"'\n')
a, b = 5,6
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
"""
#print("3.Logical operator")
"""and - Logical and
or - Logical or
not - Logical not"""

print("4.Bitwise operator")
a = 5
b = 7
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c =  ~b
print(c)
c = a << b
print(c)
c = a >> b
print(c)

print("5.Assignment operator")
"""
= :Assigment operator
+= : a+=b: a = a+b
-= : a-=b: a = a-b
*= : a*=b: a = a*b
/= : a/=b: a = a/b
%= : a%=b: a = a%b
**= : a**b: a = a**b
//= : a//=b: a = a//b
Apart from this, All the bitwise opeartors can also be used as assignment operators.
"""
print("6.Identity operator")
# is
# is not
a = 5
b = 7
c = a
d = 7
e = [1,2,3,4]
f = [1,8,5,4]
print(a is b)
print(a is not b)
print(a is c)
print(b is d)

print("****************************************************************************************")
print("7.Membership operator")
#in
# not in
a = "Shahnawaz khan"
print('ah' in a)
print('ah' not in a)


