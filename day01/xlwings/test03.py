#循环生成名单，姓名单一，单元格范围的遍历全靠手打，不完全
import xlwings as xw
app=xw.App(visible=True,add_book=False)
#工作簿
wb=app.books.add()
#工作表
sht=wb.sheets["sheet1"]
#范围
num=[[],[]]
for i in range(2,12):
    num[0].append("a"+str(i))
    num[1].append("b"+str(i))
print(num)

cla="19计网4"
dyg=num[0]#从a1开始，对应cla
dygb=num[1]
sht.range("a1").value=["班级","姓名","学号"]
for i in range(len(dyg)):
    if i==9:
        sht.range(dyg[i]).value = [cla, "杜绍龙","'"+str(i + 1)]
    else:
        sht.range(dyg[i]).value=[cla,"杜绍龙","'0"+str(i+1)]
#保存
wb.save("temp01/demo3.xlsx")
#关闭
wb.close()
#退出
app.quit()