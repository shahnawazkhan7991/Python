# #New program
# import re
# s = "sdslmmkwef 144565578322 4785227991475 3654454 79911785601155 8562314765 5554634665525"
# p = r"\d{10}"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = "sdslmmkwef 144565578322 4785227991475 3654454 79911785601155 8562314765 9570622643 5554634665525"
# p = r"\b\d{10}\b"
# res = re.findall(p,s)
# print(res)


#Flags:-
# #New program
# import re
# s = "pytho PYTHon PYTHON PYThon PytHon PYTHon PYTHON"
# p = r"python"
# res = re.findall(p,s, flags= re.IGNORECASE)
# print(res)
# res1= re.findall(p,s flags = re.I)
# print(res1)

# #New program
# import re
# s = "Wel*come t#o cet#pa inf&tech pv%t ltd."
# p = r"[*#&%.]"
# res = re.findall(p,s)
# print(res)
#
# #New program
# import re
# s = "Wel*****come t*o cet********pa infot*********ech pv****t l*td."
# p = r"[*]+"
# sub = " "
# res = re.sub(p,sub,s)
# print(res)
#
# #New program
# import re
# s = "Wel*****come t*o cet********pa infot*********ech pv****t l*td."
# p = r"[*]+"
# res = re.search(p,s)
# print(res)

