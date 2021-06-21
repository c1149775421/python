#单元格的遍历实现自动化，全面化，姓名单一
import xlwings as xw
app=xw.App(visible=True,add_book=False)
#工作簿
wb=app.books.add()
#工作表
sht=wb.sheets["sheet1"]
#范围
arr=[]
ii=0
for i in range(ord("a"),ord("z")+1):
    arr.append([])
    for j in range(2,22):
        arr[ii].append(chr(i)+str(j))
    print(arr[ii])
    ii+=1

cla="19计网4"
dyg=arr[0]
dygb=arr[1]
sht.range("a1").value=["班级","姓名","学号"]
for i in range(len(dyg)):
    if i>=9:
        sht.range(dyg[i]).value = [cla, "杜绍龙","'"+str(i+1)]
    else:
        sht.range(dyg[i]).value=[cla,"杜绍龙","'0"+str(i+1)]
#保存
wb.save("temp01/demo4.xlsx")
#关闭
wb.close()
#退出
app.quit()