import random
import xlwings as xw
import tkinter as tk
from tkinter import *

window= tk.Tk()
window.title("My Window")
window.geometry("480x640")

app=xw.App(visible=True,add_book=False)
wb=app.books.open("temp/班级名单.xlsx")
sht=wb.sheets["Sheet1"]
x=sht.range("a2:i7").value
arr=[]
for i in range(len(x)):
    y=x[i]
    for j in range(len(y)):
        arr.append(y[j])
# print(arr)
wb.close()
app.quit()

name=random.choice(arr)
print(name)

var = tk.StringVar()
on_hit = False
def hit_me():
    name=random.choice(arr)
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set(name)
        pass
    else:
        on_hit = False
        var.set('')
l= tk.Label(window, textvariable=var, bg='aqua', font=('Arial', 15), width=30, height=3)
l.pack()
b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()