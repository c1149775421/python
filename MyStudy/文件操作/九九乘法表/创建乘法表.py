import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('九九乘法表')
for row in range(0,9):
    for col in range(0,row+1):
        sheet.write(row,col,f'{col+1}*{row+1}={(row+1)*(col+1)}')
workbook.save('九九乘法表.xls')
input("按enter进入下一步")

import xlrd
workbook = xlrd.open_workbook('九九乘法表.xls')
sheet = workbook.sheet_by_name('九九乘法表')
for row in range(0,9):
    for col in range(0,row+1):
        print(sheet.row(row)[col].value, end=' ')
    print('\r')
print("\n执行完成")
input("按enter退出")
