import os
import xlrd
import xlwt

path = "./Score"
files = os.listdir(path)
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
flag=0
x=0
y=0
for file in files:
    f = os.path.basename(file)
    data = xlrd.open_workbook(os.path.join(path,f)) 
    table = data.sheets()[0]
    if flag==0:
        for i in table.row_values(0):
            sheet1.write(x,y,i)
            y+=1
        flag=1
        x+=1
        y=0
    for i in table.row_values(1):
        sheet1.write(x,y,i)
        y+=1
    x+=1
    y=0
workbook.save('./智育成绩汇总.xls')
