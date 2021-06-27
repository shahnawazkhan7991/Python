# #New program
# from tkinter import *
# root = Tk()
# root.geometry("500x600")
# btn = Button(root, text="Submit",bg="Red",fg="Black",font=30)
# btn.place(x = 200, y=100)
# lbl1=Label(root,text="Welcome to GUI",bg="Red",fg="Orange")
# lbl1.place(x=300, y=200)
# root.mainloop()

##########################################Entry widget #####################################################################
#It works like input function in GUI

# #New program
# from tkinter import *
# def func1():
#     x = var.get()
#     print(x)
#     var.set(" ")
# root = Tk()
# root.geometry("500x600")
# lbl1=Label(root,text="Enter email address",bg="Red",fg="Orange", font=20)
# lbl1.grid(row=0, column=0)
# var= StringVar()
# entr= Entry(root,font=20, textvariable= var)
# entr.grid(row=0, column=1)
# btn = Button(root, text="Submit",bg="Red",fg="Black",font=30,command=func1)
# btn.grid(row = 1, column=1)
#
# root.mainloop()


# #Lets make login password in GUI:-
# #New program
# from tkinter import *
# def handler():
#     id= user_var.get()
#     pwd=user_pass.get()
#     if id == "shahnawazkhan" and pwd == "shahnawazkhan7991":
#         print("Login Successfully")
#     else:
#         print("Access  denied")
#         user_var.set(" ")
#         user_pass.set(" ")
#
#
# root = Tk()
# root.geometry("500x400")
# label1=Label(root,text="Enter Your Login Id", font=20)
# label1.grid(row=0,column=0)
# user_var=StringVar()
# entr1=Entry(root,textvariable= user_var,font=20)
# entr1.grid(row=0, column=1)
# label2=Label(root,text="Enter Your password", font=20)
# label2.grid(row=1,column=0)
# user_pass=StringVar()
# entr2=Entry(root,textvariable= user_pass,font=20,show="*")
# entr2.grid(row=1, column=1)
# btn=Button(root,text= "Submit",font=10, command=handler)
# btn.grid(row=3, column=1)
# root,mainloop()

#############################################Access the properties of widget in 3 ways#########################################
#We can pass the properties of widget in 3 ways:
# 1.At the time of creation of widget.
# Accessing the properties as keys of a dictionary and passing the values in them widget["property"] = value
#3.using config method:
# widget.config(property = value)

# #New program
# from tkinter import *
# root =Tk()
# root.geometry("600x400")
# btn=Button(root,text="Submit")
# btn["font"]=20
# btn["height"]=3
# btn.config(bg= "Black", fg="Red")
# btn.config(bd=7)
# btn.pack()
# root.mainloop()

###################################################################################################################
# #New program
# from tkinter import *
# def func1():
#     x = var.get()
#     print(x)
#     lbl2["text"]=""
#     lbl2["text"]= x
#
# root = Tk()
# root.geometry("500x600")
# root.title("First GUI")
# lbl1=Label(root,text="Enter email address",bg="Red",fg="Orange", font=20)
# lbl1.grid(row=0, column=0)
# var= StringVar()
# entr= Entry(root,font=20, textvariable= var)
# entr.grid(row=0, column=1)
# btn = Button(root, text="Submit",bg="Red",fg="Black",font=30,command=func1)
# btn.grid(row = 1, column=1)
# lbl2=Label(root,text="",bg="Red",fg="Orange", font=20)
# lbl2.grid(row=2, column=0)
#
# root.mainloop()




