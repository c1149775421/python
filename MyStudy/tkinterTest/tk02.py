import tkinter as tk
from tkinter import *
def nine():
    bian2=""
    for i in range(1, 10):
        bianl=""
        for j in range(1, i+1):
            #print(str(j)+"*"+str(i)+"="+str(i*j))
            bianl=bianl+str(j)+"*"+str(i)+"="+str(i*j)+"\t"
        print(bianl)
        bian2=bian2+bianl+"\n"
    print()
    t=tk.Label(win,
               bg="greenyellow",
               width=100,
               height=10,
               text=bian2,
               font=("Arial",8),
               justify=LEFT)
    t.pack()

win=tk.Tk()
win.title("Hello World")
win.geometry("480x640")

t=tk.Label(win,bg="aqua",width=40,height=2,text="你好，世界",font=("楷体",40))
t.pack()


btn = tk.Button(win,text="submit",font=("Arial",12),width=20,height=2,command=nine)
btn.pack()

win.mainloop()
