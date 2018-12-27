import tkinter as tk
from tkinter import *

btn=Button()
btn.pack()
btn["text"]="Hello everyone!"

def click():
	print("You just clicked me!")
btn["command"]=click

tk.mainloop()