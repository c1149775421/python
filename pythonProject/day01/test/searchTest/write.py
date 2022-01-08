import xlwings as xw
from xlwings import *
f=open("a.txt", mode="w", encoding="utf-8")
f.write("")
f.flush()
f.close()

for i in range(10):
    f=open("a.txt", mode="a", encoding="utf-8")
    f.write(str(i+1))
    f.write("-")
    f.write(chr(i+65))
    f.write("^")
    f.flush()
f.close()