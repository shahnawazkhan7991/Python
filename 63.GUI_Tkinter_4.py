################################################Events######################################################
###########################################Event Handler####################################################
# #New program
# from tkinter import *
# #Event handler
# def func1():
#     print("Submit botton pressed")
# def func2():
#     print("Hello button pressed")
# root = Tk()
# root.geometry("500x400")
# btn=Button(root, text="Submit", font=20, command=func1)
# btn.grid(row=0, column=0)
# btn1=Button(root, text="Hello", font=20, command=func2)
# btn1.grid(row=0, column=1)
# root.mainloop()

# #How do we apply multiple event handlers on the same widget?
# #We do this with the help of bind method
# #syntax to use bind method
# #widget.bind("event",handler)
#
# #New program
# from tkinter import*
#
# def leftClick(e):
#     btn["bg"] = "yellow"
# def rightClick(e):
#     btn["bg"] = "Blue"
#
# root = Tk()
# root.geometry("500x400")
# btn= Button(root, text = "submit", font= 'Arial 20 bold', bg= 'red', fg='Black', borderwidth=10 )
# btn.grid(row=0, column=0)
# btn.bind("<Button-1>", leftClick)
# btn.bind("<Button 3>", rightClick)
# root.mainloop()

#######################################################################################################################################
######################################################################################################################################
# #New program
# from tkinter import *
# def func1(e):
#     btn["bg"] = "Orange"
# def func2(e):
#     btn["bg"] = "Violet"
# def func3(e):
#     btn["bg"] = "Yellow"
# def func4(e):
#     btn["bg"] = "Pink"
# root = Tk()
# root.geometry("500x400")
# btn = Button(root,text="Submit", font="arial 20 bold", bg = "BlUE", fg="Red", borderwidth=10)
# btn.grid(row=0, column=0)
# btn.bind("<Enter>", func1)
# btn.bind("<Leave>", func2)
# btn.bind("<Button-1>", func3)
# btn.bind("<Button-3>", func4)
# root.mainloop()


# #New program
# from tkinter import*
# def func1():
#     print("Button is pressed")
# root=Tk()
# root.geometry("500x400")
# btn=Button(root,text="Clear",font='arial 10 bold',bg="Green",fg="Black",borderwidth=10, command=func1)
# btn.grid(row=0, column=0)
# root.mainloop()

# #New program
# from tkinter import*
# def func1(e):
#     print(e)
#     print(e.x,e.y)
#     print(e.x_root, e.y_root)
#     print(e.widget)
#     widgt=e.widget
#     print(widgt["bg"])
#     print(widgt["fg"])
#     print(widgt["text"])
# root=Tk()
# root.geometry("500x400")
# btn=Button(root,text="1",font='arial 10 bold',bg="Green",fg="Black",borderwidth=10)
# btn.grid(row=0, column=0)
# btn.bind("<Button-1>", func1)
# btn1=Button(root,text="2",font='arial 10 bold',bg="Yellow",fg="Black",borderwidth=10)
# btn1.grid(row=1, column=0)
# btn1.bind("<Button-1>", func1)
# btn=Button(root,text="3",font='arial 10 bold',bg="Violet",fg="Black",borderwidth=10)
# btn.grid(row=2, column=0)
# btn.bind("<Button-1>", func1)
# root.mainloop()

# #New program
# from tkinter import*
# def func1(e):
#     w= e.widget
#     if w["text"]=='1':
#         print("Burron 1 is pressed")
#     elif w["text"] == '2':
#         print("Burron 2 is pressed")
#     elif w["text"]=='3':
#         print("Burron 1 is pressed")
# root=Tk()
# root.geometry("500x400")
# btn=Button(root,text="1",font='arial 10 bold',bg="Green",fg="Black",borderwidth=10)
# btn.grid(row=0, column=0)
# btn.bind("<Button-1>", func1)
# btn1=Button(root,text="2",font='arial 10 bold',bg="Yellow",fg="Black",borderwidth=10)
# btn1.grid(row=1, column=0)
# btn1.bind("<Button-1>", func1)
# btn=Button(root,text="3",font='arial 10 bold',bg="Violet",fg="Black",borderwidth=10)
# btn.grid(row=2, column=0)
# btn.bind("<Button-1>", func1)
# root.mainloop()

# #New program
# from tkinter import*
# def func1(e):
#     w= e.widget
#     if w["text"]=='1':
#         print("Burron 1 is pressed")
#     elif w["text"] == '2':
#         print("Burron 2 is pressed")
#     elif w["text"]=='3':
#         print("Burron 1 is pressed")
# root=Tk()
# root.geometry("500x400")
# for i in range(3):
#
#     btn=Button(root,text = f"{i+1}",font='arial 10 bold',borderwidth=10)
#     btn.grid(row=i, column=0)
#     btn.bind("<Button-1>", func1)
#
# root.mainloop()

# #New program
# from tkinter import*
# def motionhandler(e):
#     btn.place(x=e.x+5, y=e.y+5)
# x,y=200,200
# root = Tk()
# root.geometry("500x400")
# btn=Button(root,text = "Catch me",font='arial 10 bold',borderwidth=10, bg="yellow")
# btn.grid(row=0, column=0)
# btn.bind("<Motion>", motionhandler)
# root.mainloop()

# #New program
# from tkinter import*
# root=Tk()
# root.geometry("500x400+300+150")
# root.mainloop()