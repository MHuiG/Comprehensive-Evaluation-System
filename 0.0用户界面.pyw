from tkinter import *
import os
import xlrd
import xlwt
import sqlite3

def f1():
    try:
        fr1.pack_forget()
    except:
        pass
    try:
        fr2.pack_forget()
    except:
        pass
    try:
        fr3.pack_forget()
    except:
        pass
    try:
        fr4.pack_forget()
    except:
        pass
    try:
        L2.pack_forget()
    except:
        pass
    fr1.pack(fill=X)
    L.pack(anchor=NW)
    sc.pack(side=RIGHT,fill=Y)
    text.pack(expand=YES,fill=X)
    bt5.pack(anchor=SE)

def f2():
    try:
        fr1.pack_forget()
    except:
        pass
    try:
        fr2.pack_forget()
    except:
        pass
    try:
        fr3.pack_forget()
    except:
        pass
    try:
        fr4.pack_forget()
    except:
        pass
    fr2.pack(fill=X)
    bt6.pack(anchor=SE)

def f3():
    try:
        fr1.pack_forget()
    except:
        pass
    try:
        fr2.pack_forget()
    except:
        pass
    try:
        fr3.pack_forget()
    except:
        pass
    try:
        fr4.pack_forget()
    except:
        pass
    fr3.pack(fill=X)
    bt7.pack(anchor=SE)


def f4():
    try:
        fr1.pack_forget()
    except:
        pass
    try:
        fr2.pack_forget()
    except:
        pass
    try:
        fr3.pack_forget()
    except:
        pass
    try:
        fr4.pack_forget()
    except:
        pass
    fr4.pack(fill=X)

def f5():
    data=text.get('1.0',END)
    L.pack_forget()
    sc.pack_forget()
    bt5.pack_forget()
    text.pack_forget()
    s=data.split('\n')
    try:
        os.makedirs("./Score")
    except:
        pass

    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,'学号')
    sheet1.write(0,1,'姓名')
    a=2
    for i in range(len(s)):
        sheet1.write(0,a,s[i])
        a=a+1
    workbook.save('./学号_姓名成绩导入模板.xls')
    L2.pack()
def f6():
    bt6.pack_forget()
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
    workbook.save('./成绩汇总.xls')
    L3.pack()

def f7():
    bt7.pack_forget()
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()

    path = "./成绩汇总.xls"
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
        
    try:
        cn.execute('''CREATE TABLE IF NOT EXISTS Score('''+s1+''');''')
    except:
        pass
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
            cn.execute('''insert into  Score ('''+s2+''') values('''+s3+''')''')
            cn.commit()
    cur.close()
    cn.close()
    L4.pack()
    
root=Tk()
root.geometry("400x450")

frame1=LabelFrame(relief=GROOVE,text='工具栏：')
frame1.pack(fill=X)
bt1=Button(frame1,text='生成成绩导入模板')
bt1.grid(row=1,column=1)
bt2=Button(frame1,text='成绩汇总')
bt2.grid(row=1,column=2)
bt3=Button(frame1,text='成绩汇总导入数据库')
bt3.grid(row=1,column=3)
bt4=Button(frame1,text='数据库操作')
bt4.grid(row=1,column=4)


fr1=LabelFrame(relief=GROOVE,text='生成成绩导入模板：')
L = Label(fr1,text='输入考试科目(按回车分割)')
L.pack(anchor=NW)
sc=Scrollbar(fr1)
sc.pack(side=RIGHT,fill=Y)
text=Text(fr1)
text.config(yscrollcommand=sc.set)
text.pack(expand=YES,fill=X)
sc.config(command=text.yview)
bt5=Button(fr1,text='下一步')
bt5.pack(anchor=SE)
text.focus()
L2 = Label(fr1,text='成绩导入模板生成成功')


fr2=LabelFrame(relief=GROOVE,text='成绩汇总：')
bt6=Button(fr2,text='下一步')
bt6.pack(anchor=SE)
L3 = Label(fr2,text='成绩汇总成功')

fr3=LabelFrame(relief=GROOVE,text='成绩汇总导入数据库：')
bt7=Button(fr3,text='下一步')
bt7.pack(anchor=SE)
L4 = Label(fr3,text='成绩汇总导入数据库成功')

fr4=LabelFrame(relief=GROOVE,text='数据库操作：')
w = Label(fr4,text='f4') 
w.pack()

bt1.config(command=f1)
bt2.config(command=f2)
bt3.config(command=f3)
bt4.config(command=f4)
bt5.config(command=f5)
bt6.config(command=f6)
bt7.config(command=f7)

root.mainloop()
