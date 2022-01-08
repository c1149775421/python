import turtle as t
t.setup(650,650,0,0)#前两个是窗口大小，后两个是窗口位置。
t.penup()#提笔
t.fd(-150)#起始位置
t.pendown()#落笔
t.pensize(5)#笔尖大小
t.pencolor("purple")#画笔颜色
for i in range(4):#循环次数
    t.circle(50)#半径大小
    t.fd(80)#前进距离
    

