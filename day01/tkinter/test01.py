import tkinter as tk
from tkinter import *
window= tk.Tk()
window.title("My Window")
window.geometry("480x640")

var= tk.StringVar()
l= tk.Label(window, textvariable=var, bg='aqua', font=('Arial', 15), width=30, height=3)
l.pack()

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')

b= tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
