import xlwings as xw
from xlwings import *
import random

app = xw.App(visible=True,add_book=False)
wb = app.books.open("Excel2.xlsx")
sht = wb.sheets("sheet1")
sht.range("a1").value=['工号','姓名','性别','年龄','部门',
                       '工作岗位','职工级别','事假天数','病假天数',
                       '旷工天数','基本工资','级别工资','奖金','岗位补贴']
def id():
    arr=[]
    for i in range(1,21):
        if i > 9:
            arr.append("'0"+str(i))
        else:
            arr.append("'00"+str(i))
    print("工号：",arr,"\n")
    sht.range("a2:a21").options(transpose=True).value=arr

def name():
    name=[]
    for i in range(1,21):
        name.append('天'+str(i))
    print("姓名：",name,"\n")
    sht.range("b2:b21").options(transpose=True).value=name

def sex():
    sex=[]
    for i in range(1,21):
        x=random.randint(0,1)
        if x==0:
            sex.append("女")
        else:
            sex.append("男")
    print("性别：",sex,"\n")
    sht.range("c2:c21").options(transpose=True).value=sex

def age():
    age=[]
    for i in range(1,21):
        x=random.randint(20,50)
        age.append(x)
    print("年龄：",age,"\n")
    sht.range("d2:d21").options(transpose=True).value=age

def job():
    bm=["经理办公室","秘书部","财务部","会计部","设计部","法务部","采购部"]
    gw=["总经理","秘书","财务主管","会计","设计师","律师","采购经理"]
    jb=["总裁","员工","主管","员工","员工","主管","经理"]
    print("部门：",bm,"\n")
    print("岗位：",gw,"\n")
    print("级别：",jb,"\n")
    bl = 0
    for i in range(2,22):
        sht.range("e"+str(i)).options(transpose=True).value=bm[bl]
        sht.range("f"+str(i)).options(transpose=True).value=gw[bl]
        sht.range("g"+str(i)).options(transpose=True).value=jb[bl]
        #print(bl)
        bl+=1
        if bl>=len(bm):
            bl=0

def day():
    for i in range(2,22):
        sht.range("h"+str(i)).options(transpose=True).value=random.randint(0,2)
        sht.range("i"+str(i)).options(transpose=True).value=random.randint(0,2)
        sht.range("j"+str(i)).options(transpose=True).value=random.randint(0,2)
  
if __name__=="__main__":
    id()
    name()
    sex()
    age()
    job()
    day()
    wb.save()
    wb.close()
    app.quit()
    input("按enter退出")








