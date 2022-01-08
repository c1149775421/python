import random
import xlwings as xw
import tkinter as tk
from tkinter import *
print("正在点名：")
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
print(name,'\n')
input("enter")