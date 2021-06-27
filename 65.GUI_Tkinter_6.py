################################################################################################################################
# #New program
# from tkinter import *
# root= Tk()
# root.geometry("500x500")
# #Extra padding and spacing
# btn1=Button(root, text="Hello", font=20)
# btn1.grid(row=0, column=0,padx=10,pady=10)
# #Internal padding
# btn2=Button(root, text="Welcome",font=20)
# btn2.grid(row=0,column=1,padx=20, pady=20, ipadx=20,ipady=30)
# root.mainloop()

###################################columnspan, rowspan,sticky################################################################
# #New program
# from tkinter import*
# root=Tk()
# root.geometry("500x400")
# lbl=Label(root,text="I am GUI Window",font=20)
# lbl.grid(row=0, column=0,columnspan=20)
#
# btn1=Button(root, text="Hello", font=20)
# btn1.grid(row=1, column=0,columnspan=20)
#
# btn2=Button(root, text="Welcome",font=20)
# btn2.grid(row=0,column=1,rowspan=10,sticky='W')
# root.mainloop()
#############Adding Images to root window#######################################################################################
"""gif or png images"""
# from tkinter import*
# root=Tk()
# img=PhotoImage(file=r"C:\Users\Shahnawaz Khan\OneDrive\Desktop\Web project\Responsive blog templates\img\Logo.png")
# btn=Button(root,image=img)
# btn.pack()
# root.mainloop()
###############################"jpg"###############################################################
# #New program
# from tkinter import*
# from PIL import Image
# from PIL import ImageTk
# root=Tk()
# root.geometry("1000x1000")
# image=Image.open(r"C:\Users\Shahnawaz Khan\OneDrive\Desktop\Web project\Responsive blog templates\img\bg.jpg")
# photo=ImageTk.PhotoImage(image)
# lbl=Label(image=photo)
# lbl.pack()
# root.mainloop()

#################################################Color grid##################################################################
# from tkinter import*
# import tkinter.colorchooser
# def btncolor_click():
#     mycolor=tkinter.colorchooser.askcolor()
#     print(mycolor)
# root=Tk()
# root.geometry("500x500")
# root.minsize(300,300)
# root.maxsize(600,600)
# btncolor=Button(root,text="Select Me",command= btncolor_click ,font=20)
# btncolor.pack()
# # root.mainloop()
# from tkinter import*
# import tkinter.colorchooser
# def btncolor_click():
#     mycolor=tkinter.colorchooser.askcolor()
#     btncolor['bg']=mycolor[1]
#     print(mycolor)
#     print(type(mycolor))
#     print(type(mycolor[0]))
#     print(type(mycolor[1]))
# root=Tk()
# root.geometry("500x500")
# root.minsize(300,300)
# root.maxsize(600,600)
# btncolor=Button(root,text="Select Me",command= btncolor_click ,font=20)
# btncolor.pack()
# root.mainloop()

##############################FIle Handling#############################################
# #New program
# from tkinter import*
# from tkinter import filedialog
# def func1():
#     path= filedialog.askopenfile()
#     print(path)
#     f=open("Introduction to Python",'r')
#     data=f.read()
#     print(data)
# root=Tk()
# root.geometry("500x400")
# btn1=Button(master=root, text="open file",command=func1,font=20)
# btn1.pack()
# root.mainloop()


#########################################Menubar##############################################################
#Doubt
# #New program
# from tkinter import*
# def func1():
#     print("I am clicked")
# root =Tk()
# root.geometry("500x400")
# menubar=Menu(root)
# filemenu=Menu(menubar)
# filemenu.add_command(label="Save",command=func1)
#
# filemenu.add_command(Label="Open",command=func1)
#
# filemenu.add_separator()
#
# filemenu.add_command(Label="Exit",command= func1)
#
# menubar.add_cascade(Lebal="File",menu=filemenu)
# root.config(menu=menubar)
# root.mainloop()
##########################################################################################################################
##############################################Frame widget#################################################################
# #New program
# from tkinter import*
# root=Tk()
# root.geometry("500x500")
# f1=Frame(root)
# f1.place(x=100, y=100)
# btn1=Button(f1,text="Submit")
# btn1.pack()
# btn2=Button(root,text="Hello")
# btn2.place(x=0,y=0)
# root.mainloop()