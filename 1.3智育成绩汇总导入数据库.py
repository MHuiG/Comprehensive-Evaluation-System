import sqlite3
import os
import xlrd
import xlwt

cn = sqlite3.connect('Score.db')
cur = cn.cursor()

path = "./智育成绩汇总.xls"
data = xlrd.open_workbook(path) 
table = data.sheets()[0]
ncols = table.ncols
nrows = table.nrows
s1="学号 char(20) PRIMARY KEY, 姓名 char(10), "
flag=0
for i in table.row_values(0):
    if flag>=2:
        s1=s1+i+' DOUBLE'
        if flag!=ncols-1:
            s1=s1+','
    flag+=1
    

cn.execute('''CREATE TABLE IF NOT EXISTS Score('''+s1+''');''')
#print('''CREATE TABLE IF NOT EXISTS Score('''+s1+''');''')
s2=''
flag=0
for i in table.row_values(0):
    s2=s2+i
    if flag!=ncols-1:
        s2=s2+','
    flag+=1

for i in range(nrows):
    flag = 0
    s3 = ''
    if i!=0:
        for k in table.row_values(i):
            if flag==0:
                s3 = s3 + str(int(k))
            elif flag==1:
                s3 = s3 + "'"+str(k)+ "'"
            else:
                s3 = s3 + str(k)
            if flag != ncols - 1:
                s3+=','
                flag += 1
        #print('''insert into  Score ('''+s2+''') values('''+s3+''')''')
        cn.execute('''insert into  Score ('''+s2+''') values('''+s3+''')''')
        cn.commit()
cur.close()
cn.close()
