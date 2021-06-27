#We use the decortor before the method which we have to create as a static method
#That decorator is @staticmethod

#Decoratoer:- A decorator can change and modify the functionality of function.

class c1:
    def insmethod(self):
        print("This is Instance Method")

    @staticmethod
    def staticmethod(self):
        print("This is static Method")