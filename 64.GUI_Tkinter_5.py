######################################################################################################################
# #New program
# from tkinter import *
# root = Tk()
# root.geometry("400x400")
# Button(root, text = "Submit", font = 20).pack()
# root.mainloop()

# #New program with font size
# from tkinter import *
# root = Tk()
# root.geometry("500x400")
# btn = Button(root, text = "Submit", font=20)
# btn.pack()
# btn2 = Button(root, text = "CETPA", font=10)
# btn2.pack()
# btn3 = Button(root, text = "Hello", font=30)
# btn3.pack()
# root.mainloop()

# #New program without font size
# from tkinter import *
# root = Tk()
# root.geometry("500x400")
# btn = Button(root, text = "CETPA", font="Cetpa") #Big font size
# btn.pack()
# btn2=Button(root,text="Submit") #Small fnt size
# btn2.pack()
# root.mainloop()

# #New program
# from tkinter import*
# root=Tk()
# root.geometry("500x500")
# btn=Button(root,text="Submit", font=("Times New Roman",30,"bold","italic"))
# btn.pack()
# root.mainloop()
###################################Keyboards Events#################################################################

#
# #New program
# from tkinter import*
# def windowup(e):
#     pass
# root=Tk()
# root.geometry("500x500")
# btn=Button(root,text="Mera font to dekho", font=("Monotype Corsiva",30,"bold","italic","underline"))
# btn.pack()
# btn.bind("<Up>",windowup)
# root.mainloop()


#New program

# #New program
# from tkinter import*
# def windowup(e):
#     global Y
#     Y -= 10
#     btn.place(x=X, y=Y)
#
# def windowdown(e):
#     global Y
#     Y += 10
#     btn.place(x=X, y=Y)
# def windowLeft(e):
#     global X
#     X -= 10
#     btn.place(x=X, y=Y)
# def windowRight(e):
#     global X
#     X += 10
#     btn.place(x=X, y=Y)
# X,Y= 100,100
# root=Tk()
# root.geometry("500x500")
# btn=Button(root,text="Mera font to dekho", font=("Monotype Corsiva",30,"bold","italic","underline"))
# btn.place(x=100,y=100)
# btn.bind("<Up>",windowup)
# btn.bind("<Down>",windowdown)
# btn.bind("<Left>",windowLeft)
# btn.bind("<Right>",windowRight)
#
# root.mainloop()


# #New program
# from tkinter import*
# def func1(e):
#     print("key 'a' is presed")
# def func2(e):
#     print("key '5' is presed")
# def func3(e):
#     print("key 'Hello' is presed")
# root=Tk()
# root.geometry("500x500")
# root.bind("a",func1)
# root.bind("5",func2)
# root.bind("Hello",func3)
#
# root.mainloop()

# ##New program
# import time
# from tkinter import*
# def mooveroot():
#     for i in range(1001):
#         root.geometry(f"500x500+{i}+100")
# root=Tk()
# mooveroot()
# root.mainloop()
#################################################time library##########################################################
# #New program
# import time
# from tkinter import*
# root=Tk()
# root.geometry("500x500")
# time.sleep(5)
# root.mainloop()

# #New program
# import time
# from tkinter import*
# def moveroot():
#     global i
#     if i == 1000:
#         i= 0
#     i+=10
#     root.geometry(f"500x500+{i}+100")
#     root.after(100,moveroot)
# root=Tk()
# i=0
# moveroot()
# root.mainloop()

# #New program
# import time
# from tkinter import*
# def moveroot():
#     global i
#     if i == 1000:
#         i= 0
#     i+=10
#     root.geometry(f"{i}x{i}+{i}+{i}")
#     root.after(100,moveroot)
# root=Tk()
# i=0
# moveroot()
# root.mainloop()
