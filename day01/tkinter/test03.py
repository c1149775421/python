import tkinter as tk
from tkinter import *
win=tk.Tk()
win.title("test")
win.geometry('300x400')

var= tk.StringVar()
var.set("删除")
on_hit = False
def dels():
    global on_hit
    if on_hit == False:
        on_hit = True
        label.place_forget()
        var.set('添加')
    else:
        on_hit = False
        label.place(x=60, y=20)
        var.set('删除')

label=tk.Label(win,text='text',bg='aqua',font=('Arial',12),width=20,height=2)
label.place(x=60,y=20)

btn=tk.Button(win,textvariable=var,font=('Arial',12),width=12,height=2,command=dels)
btn.place(x=90,y=80)
win.mainloop()