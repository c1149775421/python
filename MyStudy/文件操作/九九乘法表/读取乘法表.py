import xlrd
workbook = xlrd.open_workbook('九九乘法表.xls')
sheet = workbook.sheet_by_name('九九乘法表')
for row in range(0,9):
    for col in range(0,row+1):
        print(sheet.row(row)[col].value, end=' ')
    print('\r')
input("enter")
