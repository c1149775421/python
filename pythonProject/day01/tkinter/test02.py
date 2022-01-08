import tkinter as tk
from tkinter import *
win=tk.Tk()
win.title("显示文本")
win.geometry("600x400")

var=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
on_hit = False
def disable():
    global on_hit
    if on_hit == False:
        on_hit = True
        var3.set("隐藏")
        var2.set(var.get())
        # var.set("")
    else:
        on_hit = False
        var3.set('显示')
        var2.set("")
ent=tk.Entry(win,textvariable=var)
ent.pack()

btn=tk.Button(win,textvariable=var3,height=2,font=("Arial",12),width=12,command=disable)
btn.pack()
var3.set("显示")

la=tk.Label(win,textvariable=var2,height=2,font=("Arial",12),width=12)
la.pack()
win.mainloop()