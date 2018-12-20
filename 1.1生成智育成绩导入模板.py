import xlwt
import os

try:
    os.makedirs("./Score")
except:
    pass

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

n=input("excel列数\n")

a=0
for i in range(int(n)):
    b=input()
    sheet1.write(0,a,b)
    a=a+1

workbook.save('./学号_姓名智育成绩导入模板.xls')
