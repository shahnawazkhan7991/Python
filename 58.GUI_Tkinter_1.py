#################################GUI PROGRAMMING ###############################################
# Tkinter: A desktop GUI application development framework.
#tkinter framework is created on top of the tcl/tk
#TCL:Tool command language
#TK: Tool kit
###############################let's start progarmming##########################################
# import tkinter as tk #library
# root = tk.Tk()   #Tk () class
# root.geometry("500x500") #Dimension
#
# root.mainloop() #infinite loop, which is used to hold the window on the screen.

# #New program
# import tkinter as tk #library
# root = tk.Tk()   #Tk () class
# root.geometry("500x500") #Dumension ,double quotes(" ")
#
# root.mainloop() #infinite loop, which is used to hold the window on the screen.
# print("Welcome to CETPA") # it will print after closing the window.


########################################### Widges in Tkinter#######################################################
#We have different widgets in tkinter framework:
# like : Button, label, Entry, Text, Menubar,Radiobutton.........
# these widgets are called the slaves widgets and roots are calles master widget.
#Syntax to call widget:
# widget_object = widget_class(properties)
############################################################################################################
# # New program
# import tkinter as tk #library
# root = tk.Tk()   #Tk () class
# root.geometry("500x500") #
# btn = tk.Button(root, text = "Submit")
# #Incomplete priogram

# root.mainloop() #infinite loop, which is used to hold the window on the screen.

##################################################USE TITLE################################################################33
# #New program
# import tkinter as tk
# master = tk.Tk()
# master.geometry("600x700")
# master.title("My first GUI")
# master.mainloop()

###############################################Geometry layout visible############################################################
# 1.pack geometry (side="")
#2.place geometry(x = "pixels", y = pixels)
#3.grid geometrty(row="", column="")

# #New program
# import tkinter as tk
# root = tk.Tk()
# root.geometry("1000x900")
# btn = tk.Button(root, text = "Submit")
# btn.pack(side = "left")
# root.mainloop()
# print("Welcome to python class")

# #New program
# import tkinter as tk
# root = tk.Tk()
# root.geometry("1000x900")
# btn = tk.Button(root, text = "Submit")
# btn.place(x=300, y=100)
# root.mainloop()
# print("Welcome to python class")

# #New program
# import tkinter as tk
# root = tk.Tk()
# root.geometry("1000x900")
# btn = tk.Button(root, text = "Submit")
# btn.grid(row=0, column=0)
# root.mainloop()
# print("Welcome to python class")
################################################################################################################
# #New program
# import tkinter as tk
# root = tk.Tk()
# root.geometry("1000x900")
# btn = tk.Button(root, text = "Submit")
# btn.grid(row=0, column=0)
# btn1 = tk.Button(root, text = "Submit")
# btn1.grid(row=1, column=1)
# btn2 = tk.Button(root, text = "Submit")
# btn2.grid(row=2, column=0)
# btn3 = tk.Button(root, text = "Submit")
# btn3.grid(row=3, column=1)
# root.mainloop()
####################################################################################################################################
#################################################Events#############################################################################
# def func1():
#     print("Welcome to GUI")
# from tkinter import *
# root = Tk()
# root.geometry("500x300")
# btn = Button(root,text = "Click", command= func1)
# btn.pack()
# root.mainloop()

# #New program
# from tkinter import *
# root = Tk()
# root.geometry("500x300")
# btn = Button(root,text = "Click", bg = "Red", fg= "Black", font=30, borderwidth= 10)
# btn.grid(row=0, column=0)
# root.mainloop()


# #New program
# from tkinter import *
# root = Tk()
# root.geometry("500x300")
# btn = Button(root,text = "Click", bg = "Red", fg= "Black", font=30, borderwidth= 10)
# btn.grid(row=0, column=0)
# btn1 = Button(root,text = "Click", bg = "#000000", fg= "#ffffff", font=30, borderwidth= 10)
# btn1.grid(row=1, column=0)
# root.mainloop()

# Label:it is like print function to display data on root window
# #New program
# from tkinter import *
# root = Tk()
# root.geometry("500x300")
# lbl1 = Label(root, text="Welcome to CETPA", font=20, bg="Red", fg= "Black")
# lbl1.grid(row=5, column=6)
# btn = Button(root,text = "Click", bg = "Red", fg= "Black", font=30, borderwidth= 10)
# btn.grid(row=0, column=0)
# btn1 = Button(root,text = "Click", bg = "#000000", fg= "#ffffff", font=30, borderwidth= 10)
# btn1.grid(row=1, column=0)
# root.mainloop()

# #New program
# from tkinter import *
# def handler():
#     print("It is clicked")
# root = Tk()
# root.geometry("500x300")
# lbl1 = Label(root, text="Welcome to CETPA", font=20, bg="Red", fg= "Black")
# lbl1.grid(row=5, column=6)
#
# btn = Button(root,text = "Click", bg = "Red", fg= "Black", font=30, borderwidth= 10, command=handler)
# btn.grid(row=0, column=0)
# btn1 = Button(root,text = "Click", bg = "#000000", fg= "#ffffff", font=30, borderwidth= 10)
# btn1.grid(row=1, column=0)
# root.mainloop()

# #New program
# from tkinter import *
# def handler():
#     lbl1=Label(root, text="welcome to python class", font = 20, bg="white")
#     lbl1.grid(row=8,column=9)
#
#     lbl2=Label(root, text="I am clicked", font = 20, bg="red")
#     lbl2.grid(row=10, column=11)
# root = Tk()
# root.geometry("1000x900")
# lbl1 = Label(root, text="Welcome to CETPA", font=20, bg="Red", fg= "Black")
# lbl1.grid(row=5, column=6)
#
# btn = Button(root,text = "Click", bg = "Red", fg= "Black", font=30, borderwidth= 10, command=handler)
# btn.grid(row=0, column=0)
# btn1 = Button(root,text = "Click", bg = "#000000", fg= "#ffffff", font=30, borderwidth= 10, command=handler)
# btn1.grid(row=1, column=0)
# root.mainloop()



