"""
[a-z A-Z 0-9]: \w
[^a-z A-Z 0-9]: \W
[0-9]: \d
[^0-9]: \D
"""

# 2.Quantity matching pattern-
# Quantity mearsure class {}
# A,Category first
# #New program
# import re
# s ="Wel_come 123c_$aa bcd pqrs123"
# p = r"[a-z]{3}"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s ="WEL_come 123c_$aa bcd pqrs123"
# p = r"[A-Z]{3}"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s ="Wel_come 123c_$aa bcd pqrs123_95706234654_7954661245 45789521 542135 8560322546"
# p = r"[0-9]{10}"
# res = re.findall(p,s)
# print(res)



# #New program
# import re
# s ="Wel_come 123c_$aa bcd pqrs123_95706234654_7954661245 45789521 542135 8560322546"
# p = r"[0-9]{,}"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s ="Wel_come 123c_$aa bcd pqrs123_95706234654_7954661245 45789521 542135 8560322546"
# p = r"[0-9]{1,}"
# res = re.findall(p,s)
# print(res)

#New program
# import re
# s ="Wel_come 123c_$aa bcd pqrs123_95706234654_7954661245 4578952102122112 542135 8560322546"
# p = r"[0-9]{10,15}"
# res = re.findall(p,s)
# print(res)

# B.second category
# #New program
# import re
# s = "(123-[234-789-12"
# p = "[ab * 12]{3}"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "(123-[234-789-"
# p = r"[([] ? \d {3}-"
# res = re.findall(p,s)
# print(res)

# #New program
# import re
# s = "pwrd shahnawazkhan7991@gmail.com sdnfbiwh jai2655655@gmail.com fthtrh6644rt harry456@gmail.com"
# p = "\w+@\w+[.]\w+"
# res = re.findall(p,s)
# print(res)

