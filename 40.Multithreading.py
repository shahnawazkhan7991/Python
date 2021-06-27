"""def func1():
    for i in range(10):
        print("This is func1:",i)

def func2():
    for i in range(10):
        print("This is func2",i)
func1()
func2()"""
print("*****************************************************************************************************************************")
"""import threading
def func1():
    for i in range(10):
        print("This is func1:",i)

def func2():
    for i in range(10):
        print("This is func2",i)

th1=threading.Thread(target=func1)
th2=threading.Thread(target=func2)

th1.start()
th2.start()"""
print("**************************************************************************************************************************")
#Thread-A thread is process.
"""import threading
def func1():
    for i in range(10):
        print("This is func1:",i)

def func2():
    for i in range(10):
        print("This is func2",i)

th1=threading.Thread(target=func1)
th2=threading.Thread(target=func2)

th1.start()
th2.start()
for i in range(10):
    print("This is main:",i)"""
print("*************************************************************************************************************")
"""import threading
def func1():
    for i in range(10):
        print("This is func1:",i)

th1=threading.Thread(target=func1)
th2=threading.Thread(target=func1)

th1.start()
th2.start()
# for i in range(10):
#     print("This is main:",i)
"""
"""import threading
def func1():
    for i in range(10):
        print("This is func1:",i)

th1=threading.Thread(target=func1)
th2=threading.Thread(target=func1)

th1.setName("Thread1")
th1.setName("Thread2")

th1.start()
th2.start()
for i in range(10):
     print("This is main:",i)"""


