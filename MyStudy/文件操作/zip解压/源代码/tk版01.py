import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
import zipfile,time,os
window = tk.Tk()
window.title("批量解压")
window.geometry("600x600")

def unzip(fileName,outName):
    start_time_all = time.time()#开始时间
    try:
        file=os.listdir(fileName+"/")#os.listdir遍历所有文件
    except:
        print("文件夹为空")
        return
    print("<-------------------------------------->")
    print("\n\t压缩包总共有：",len(file),"个","\n")
    print("<-------------------------------------->")
    ok=0#计算解压成功数的变量
    for i in range(len(file)):
        try:
            zfile = zipfile.ZipFile(fileName+"/"+file[i],'r')#读取压缩包
            print(file[i])
        except:
            print(file[i],"\n输入有误")
            pass
        
        try:
            start_time = time.time()#开始时间           
            zfile.extractall(path=outName+"/"+file[i],pwd="".encode('utf-8'))#解压命令
            end_time = time.time()#结束时间
            print("解压成功")
            print ('当前压缩包花了%s秒'%(end_time-start_time))
            print("--------------------")
            ok+=1
        except Exception as e:
            print("解压失败")
            print("--------------------")
            ok-=1
            pass
    print("\n解压成功",ok,"个")
    end_time_all = time.time()#结束时间
    print ('全部压缩包总共花了%s秒'%(end_time_all-start_time_all))
    var3.set("解压成功")

var = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
def hit_me():
    folder_path = askdirectory()
    var.set(folder_path)

def hit_me2():
    folder_path2 = askdirectory()
    var2.set(folder_path2)

def zip_file():
    if var.get()=="" and var2.get()=="":
        try:
            os.mkdir("1")
            os.mkdir("output")
        except:
            print("文件夹已存在")
        unzip("1","output")
        
    elif var.get()=="":
        try:
            os.mkdir("1")
        except:
            print("文件夹已存在")
        unzip("1",var2.get())
        
    elif var2.get()=="":
        try:
            os.mkdir("output")
        except:
            print("文件夹已存在")
        unzip(var.get(),"output")
        
    else:
        unzip(var.get(),var2.get())
        try:
            os.mkdir(var.get())
            os.mkdir(var2.get())
        except:
            print("文件夹已存在")

#选择存放压缩包的文件夹
la = tk.Label(window,text="选择存放压缩包的文件夹",font=('Arial',16),height=1)
la.pack()

enter = tk.Entry(window,textvariable=var,show=None,font=('Arial',22))
enter.pack()
var.set(var.get())

btn = tk.Button(window,text='选择文件夹',font=('Arial',12),width=10,height=1,command=hit_me)
btn.pack()

la2 = tk.Label(window,text="",font=('Arial',16),height=1)
la2.pack()

#选择压缩包输出的文件夹
la3 = tk.Label(window,text="选择压缩包输出的文件夹",font=('Arial',16),height=1)
la3.pack()

enter2 = tk.Entry(window,textvariable=var2,show=None,font=('Arial',22))
enter2.pack()
var2.set(var2.get())

btn2 = tk.Button(window,text='选择文件夹',font=('Arial',12),width=10,height=1,command=hit_me2)
btn2.pack()

#开始解压
la4 = tk.Label(window,text="",font=('Arial',22),height=1)
la4.pack()
la5 = tk.Label(window,textvariable=var3,font=('Arial',12),height=1)
la5.pack()
btn3 = tk.Button(window,text='开始解压',font=('Arial',12),width=10,height=1,command=zip_file)
btn3.pack()






window.mainloop()
