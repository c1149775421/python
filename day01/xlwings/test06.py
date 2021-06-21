#单元格的遍历实现自动化，全面化，姓名实现随机轮播，无规律
import random
import xlwings as xw
#visible表示是否显示过程，add_book表示是否每次新建
app=xw.App(visible=True,add_book=False)
#工作簿
wb=app.books.add()
#工作表
sht=wb.sheets["sheet1"]
arr=[]#存放单元格的范围
ii=0#数字变量，i的替代品
for i in range(ord("a"),ord("z")+1):#ord把键名(键盘上的按键名)转换成键值(数字)
    arr.append([])#向arr里面添加一个空数组
    for j in range(2,22):#循环2-21
        arr[ii].append(chr(i)+str(j))#chr把键值(数字)转换为键名(键盘上的按键名)
    print(arr[ii])#打印输出所有的数组
    ii+=1#ii变量自增1

name=["吴涛生","杜绍龙","欧少杰","朱桂全","肖振劲","周彦君"]#存放名单的数组
cla="19计网4"#班级的字符赋值给变量cla
dyg=arr[0]#二维数组，代表Excel的a列
#dygb=arr[1]#二维数组，代表Excel的b列
sht.range("a1").value=["班级","姓名","学号"]#Excel里面第一行输入的内容

# 如果要随机输入名字，就用以下注释的代码，把bianl和bianl+=1还有if bianl>=6:bianl=0注释掉，name[bianl]改成sj[i]
sj=[]
for j in range(len(dyg)+1):
    x = random.randint(0, 5)
    sj.append(name[x])
print(sj)
# bianl=0#这是一个变量
for i in range(len(dyg)):
    if i>=9:
        sht.range(dyg[i]).value = [cla,sj[i],"'"+str(i+1)]
    else:
        sht.range(dyg[i]).value=[cla,sj[i],"'0"+str(i+1)]
    # bianl+=1#变量自增1
    # if bianl>=6:bianl=0#因为只有6个名字，到6以后就重新轮播

wb.save("temp01/demo6.xlsx")#保存
wb.close()#关闭
app.quit()#退出