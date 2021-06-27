"""import threading
def func1():
    global x
    for i in range(100):
        x+=1
def func2():
    global y
    for i in range(100):
        y+=1
th1=threading.Thread(target=func1)
th2=threading.Thread(target=func2)

x,y=0,0
th1.start()
th2.start()
print(x,y)"""

 # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(10):
#         x+=1
#
# def func2():
#     global y
#     for i in range(10):
#         y+=1
#
# x,y = 0,0
#
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()
# print(x,y)

# # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x,y = 0,0
#
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()
# print(x,y)



# # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x,y = 0,0
#
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()
#
# while th1.is_alive() or th2.is_alive():
#     pass
#
#
# print(x,y)


# # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x,y = 0,0
#
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(th1.is_alive(), th2.is_alive())
#
# print(x,y)




"""
The join method will join any thread on which it has been called with the MainThread and will put
the MainThread o hold till that thread is completely executed
"""

# # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(10):
#         x+=1
#
# x = 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func1)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(x)

# # New Program
# import threading
#
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# x = 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func1)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(x)


"""
Yaha pe jadoo nahi ho raha hai, balki is condition ko race condition kehte hai

Race Condition:
This condition occurs when two or more threads access the same shared variable at the same time.


The solution to race condition is that we have to create an object of the lock class
"""

# # New Program
# import threading
# lockobj = threading.Lock()
# def func1():
#     global x
#     for i in range(100000):
#         lockobj.acquire()
#         x+=1
#         lockobj.release()
#
# x = 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func1)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(x)

"""
The requirement that we have now is that if the main thread stops working, then all the other
threads also stop working. How do we achieve this?

We achieve this requirement by seting the Daemon 
"""

# New Program
import threading
def func1():
    for i in range(100):
        print("1:",i)

def func2():
    for i in range(100):
        print("2:",i)
th1 = threading.Thread(target=func1)
th2 = threading.Thread(target=func2)

th1.setDaemon(True)
th2.setDaemon(True)

th1.start()
th2.start()

print("Main Thread Terminated")


