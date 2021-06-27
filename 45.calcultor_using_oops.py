#BLL start here
class calculator:
    def __init__(self):
        self.no1 = 0
        self.no2 =0
        self.res = 0

    def add(self):
        self.res = self.no1 + self.no2
    def sub(self):
        self.res = self.no1 - self.no2
    def mul(self):
        self.res = self.no1 * self.no2
    def div(self):
        self.res = self.no1 / self.no2
    def remainder(self):
        self.res = self.no1 % self.no2
    def exp(self):
        self.res = self.no1 ** self.no2
    def floordiv(self):
        self.res = self.no1 // self.no2








#BLL ends here
#Pl start here
while True:
    operation = input("""
                   press + for addition 
                   press - for subtraction
                   press * for multiplication
                   press / for division
                   press % for remainder
                   press ** for exponent
                   press // for float division
                   press 0 to exit 
                   Enter your choice:""")

    if operation==0:
        break

    ob = calculator()
    ob.no1 = int(input("Enter first number"))
    ob.no2 = int(input("Enter second number"))
    if operation=='+':
        ob.add()
        print(ob.res)
    elif operation=='-':
        ob.sub()
        print(ob.res)
    elif operation=='*':
        ob.mul()
        print(ob.res)
    elif operation=='/':
        ob.div()
        print(ob.res)
    elif operation=='%':
        ob.remainder()
        print(ob.res)
    elif operation=='**':
        ob.exp()
        print(ob.res)
    elif operation=='//':
        ob.floordiv()
        print(ob.res)
    else:
        print("Invalid choice")