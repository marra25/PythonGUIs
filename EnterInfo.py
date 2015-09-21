# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:32:11 2015

@author: Bryce Marra
"""
from tkinter import *
import tkinter.messagebox

root = Tk()

title1 = root.title("Enter Information")
label1 = Label(root, text="First Name")
E1 = Entry(root, bd=5)

label2 = Label(root, text="Last Name")
E2 = Entry(root, bd=5)

label3 = Label(root, text="Age")
E3 = Entry(root, bd=5)

def getName():
    fName = (E1.get())
    lName = (E2.get())
    age = (E3.get())
    message = 'You entered'
    output = (message), (fName), (lName), (age)

# Produce the output

    tkinter.messagebox._show("Results", output)

submit = Button(root, text="Submit", command = getName)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
submit.pack(side =BOTTOM) 
root.mainloop()
