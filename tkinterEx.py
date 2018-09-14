# -*- coding: utf-8 -*-
from tkinter import *

OPTIONS = [
"+",
"-",
"*",
"÷"
] #etc

root = Tk()
root.title('La calco Jess :) ')
#You can set the geometry attribute to change the root windows size
root.geometry("200x350") #You want the size of the app to be 100x100
root.resizable(0, 0) #Don't allow resizing in the x or y direction

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value
var = StringVar()
var.set('')

def calculatrice():
    if(e1.get()== "") or (e5.get() == ""):
        print("error,  a field is empty")
        var.set("empty field")
    elif (e1.get()).isdigit() and (e5.get()).isdigit():
        if variable.get() == "+":
           print(int(e1.get())+ int(e5.get()))
           e9.delete(0,END)
           e9.insert(10,int(e1.get()) + int(e5.get()))
           var.set("")
        if variable.get() == "*":
           print(int(e1.get())* int(e5.get()))
           e9.delete(0,END)
           e9.insert(10,int(e1.get()) * int(e5.get()))
           var.set("")
        if variable.get() == "-":
           print(int(e1.get())- int(e5.get()))
           e9.delete(0,END)
           e9.insert(10,int(e1.get()) - int(e5.get()))
           var.set("")
        if variable.get() == "÷":
           print(int(e1.get())/ int(e5.get()))
           e9.delete(0,END)
           e9.insert(10,int(e1.get())/int(e5.get()))
           var.set("")
        else:
           print(e3.get())    
    else:
        print("error, please control the inputs")
        var.set("error")

Label(root, text="Number 1:").grid(row=0)
Label(root, text="").grid(row=1)
OptionMenu(root, variable, *OPTIONS).grid(row=2, column=1)
Label(root, text="").grid(row=3)
Label(root, text="Number 2:").grid(row=4)
Label(root, text="").grid(row=5)
Button(root, text ="=", command = calculatrice, width="10").grid(row=6, column=1)
Label(root, text="").grid(row=7)
Label(root, text="Result:").grid(row=8)
Label(root, textvariable= var  ,fg="red").grid(row=9)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9 = Entry(root)
e10 = Entry(root)

e1.grid(row=0, column=1)
e5.grid(row=4, column=1)
e9.grid(row=8, column=1)

