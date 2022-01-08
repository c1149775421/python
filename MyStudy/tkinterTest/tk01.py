import tkinter as tk
#1.实例化object，建立window窗口
window = tk.Tk()

#2.给窗口可视化起名字
window.title('My Window')

#3.设定窗口的大小(长*宽)
window.geometry('500x300')

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        print(on_hit)
    else:
        on_hit = False
        print(on_hit)

lab = tk.Label(window,text="",height=1)
lab.pack()
#4.在图形界面是设定标签
bq = tk.Label(window,text="你好！this is Tkinter",bg="aqua",font=('宋体',12),width=30,height=4)
#5.放置标签
bq.pack()

# 第4步，在图形界面上设定输入框控件entry并放置控件
lab = tk.Label(window,text="用户名",font=('Arial',12),height=1)
lab.pack()
e1 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()

lab = tk.Label(window,text="密码",font=('Arial',12),height=1)
lab.pack()
e2 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
e2.pack()

lab = tk.Label(window,text="",height=1)
lab.pack()
btn = tk.Button(window,text='this is button',font=('Arial',12),width=10,height=1,command=hit_me)
btn.pack()

#6.主窗口循环显示
window.mainloop()
