import tkinter as tk
from tkinter import *
import os
win = tk.Tk()
win.title("title")
win.geometry("600x400")
var=tk.StringVar()
var2=tk.StringVar()
def comman():
    folderName=var.get()
    try:
        os.mkdir(folderName)
        var2.set("成功创建文件夹："+folderName)
    except:
        print("文件夹已存在")
        var2.set("文件夹："+folderName+"    已存在")

la=tk.Label(win,text="创建文件夹",font=("Arial",16),bg="greenyellow",width=100,height=2)
la.pack()

la2=tk.Label(win,text="文件夹名称",font=("Arial",12),height=1)
la2.pack()

ent=tk.Entry(win,textvariable=var,font=("Arial",20))
ent.pack()

btn=tk.Button(win,text="创建",font=("Arial",12),height=1,command=comman)
btn.pack()

la3=tk.Label(win,textvariable=var2,font=("Arial",12),height=1)
la3.pack()

win.mainloop()
