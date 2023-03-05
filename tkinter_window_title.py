#How to create a label in Tkinter
import os
import tkinter as tk

from tkinter import *

#First create a screen
new_window = Tk()
new_window.title("My Python Project")
new_window.geometry("300x250")

x=Label(new_window, text = "Hello World")
x.pack()
#Label : Tells Python that a label is being created
#new_window : whatever screen you want the label to be shown on ; name the screen whatever you like
#text : this tells that there is text being typed in the label
#.pack() : shows the label on the screen
new_window.mainloop()
