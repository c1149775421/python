#向指定单元格添加内容
import xlwings as xw
app=xw.App(visible=True,add_book=False)#应用
wb=app.books.add()#工作簿
sht=wb.sheets["sheet1"]#工作表
sht.range("a1,a2").value="吴某某"#范围
wb.save("temp01/demo1.xlsx")#保存
wb.close()#关闭
app.quit()#退出
