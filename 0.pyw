#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#0.pyw 综合测评系统用户界面
#1.汇总所有函数
#2.优化用户界面
from tkinter import *
from docx import *
import os
import xlrd
import xlwt
import sqlite3
import A1	#生成智育成绩导入模板
import A2	#智育成绩汇总
import A3	#智育成绩汇总导入数据库
import A4	#导出"智育成绩.xls"
import B1	#综测成绩导入模板
import B2	#综测成绩汇总
import B3	#综测成绩导入数据库
import B4	#导出"综测成绩.xls"
import C1	#数据库操作
import D1	#数据库导入学分

#########移除控件

def PackForget():
    try:
        fr11.pack_forget()
    except:
        pass
    try:
        fr12.pack_forget()
    except:
        pass
    try:
        fr13.pack_forget()
    except:
        pass
    try:
        fr14.pack_forget()
    except:
        pass
    try:
        fr20.pack_forget()
    except:
        pass
    try:
        fr21.pack_forget()
    except:
        pass
    try:
        fr22.pack_forget()
    except:
        pass
    try:
        fr23.pack_forget()
    except:
        pass
    try:
        fr24.pack_forget()
    except:
        pass
    
##########主工具栏
    
def f01():
    PackForget()
    try:
        frame1.pack_forget()
    except:
        pass
    try:
        frame2.pack_forget()
    except:
        pass

    frame1.pack(fill=X)
    
def f02():
    PackForget()
    try:
        frame1.pack_forget()
    except:
        pass
    try:
        frame2.pack_forget()
    except:
        pass
    frame2.pack(fill=X)
    
##########智育成绩

#####智育成绩工具栏
    
def f11():
    PackForget()
    try:
        L12.pack_forget()
    except:
        pass
    fr11.pack(fill=X)
    L01.pack(anchor=NW)
    sc.pack(side=RIGHT,fill=Y)
    text11.pack(expand=YES,fill=X)
    bt15.pack(anchor=SE)

def f12():
    PackForget()
    fr12.pack(fill=X)
    bt16.pack(anchor=SE)

def f13():
    PackForget()
    fr13.pack(fill=X)
    bt17.pack(anchor=SE)


def f14():
    PackForget()
    fr14.pack(fill=X)
    bt18.pack(anchor=SE)

######生成智育成绩导入模板
    
def f15():
    data=text11.get('1.0',END)
    L01.pack_forget()
    sc.pack_forget()
    bt15.pack_forget()
    text11.pack_forget()
    A1.A1(data)
    L12.pack()

######智育成绩汇总
    
def f16():
    bt16.pack_forget()
    A2.A2()
    L13.pack()

######智育成绩汇总导入数据库

def f17():
    bt17.pack_forget()
    A3.A3()
    L14.pack()

######导出"智育成绩.xls"

def f18():
    bt18.pack_forget()
    A4.A4()
    L15.pack()

##########综测成绩

######综测成绩工具栏
    
def f20():
    PackForget()
    try:
        L20.pack_forget()
    except:
        pass
    fr20.pack(fill=X)
    L201.pack(anchor=NW)
    sc2.pack(side=RIGHT,fill=Y)
    text211.pack(expand=YES,fill=X)
    bt201.pack(anchor=SE)

    
def f21():
    PackForget()
    try:
        L22.pack_forget()
    except:
        pass
    fr21.pack(fill=X)
    bt25.pack(anchor=SE)

def f22():
    PackForget()
    fr22.pack(fill=X)
    bt26.pack(anchor=SE)

def f23():
    PackForget()
    fr23.pack(fill=X)
    bt27.pack(anchor=SE)


def f24():
    PackForget()
    fr24.pack(fill=X)
    bt28.pack(anchor=SE)
    
######导入学分

def f201():
    data=text211.get('1.0',END)
    L201.pack_forget()
    sc2.pack_forget()
    bt201.pack_forget()
    text211.pack_forget()
    D1.D1(data)
    L20.pack()

######生成综测成绩导入模板
    
def f25():
    L20.pack_forget()
    B1.B1()
    bt25.pack_forget()
    L22.pack()
    
######综测成绩汇总
    
def f26():
    bt26.pack_forget()
    B2.B2()
    L23.pack()

######综测成绩汇总导入数据库
    
def f27():
    
    bt27.pack_forget()
    B3.B3()
    L24.pack()
    
######导出"综测成绩.xls"

def f28():
    
    bt28.pack_forget()
    B4.B4()
    L25.pack()
    
    
################################################################################
    
root=Tk()
root.geometry("700x500")

##############################主工具栏###############################

frame0=LabelFrame(relief=GROOVE,text='工具栏：')
frame0.pack(fill=X)
bt01=Button(frame0,text='智育成绩')
bt01.grid(row=1,column=1)
bt02=Button(frame0,text='综测成绩')
bt02.grid(row=1,column=2)

#按钮

bt01.config(command=f01)
bt02.config(command=f02)

################################智育成绩##########################

######智育成绩工具栏

frame1=LabelFrame(relief=GROOVE,text='智育成绩')
bt11=Button(frame1,text='生成智育成绩导入模板')
bt11.grid(row=1,column=1)
bt12=Button(frame1,text='智育成绩汇总')
bt12.grid(row=1,column=2)
bt13=Button(frame1,text='智育成绩汇总导入数据库')
bt13.grid(row=1,column=3)
bt14=Button(frame1,text='导出"智育成绩.xls"')
bt14.grid(row=1,column=4)

#按钮

bt11.config(command=f11)
bt12.config(command=f12)
bt13.config(command=f13)
bt14.config(command=f14)

######生成智育成绩导入模板

fr11=LabelFrame(relief=GROOVE,text='生成智育成绩导入模板：')
L01 = Label(fr11,text='输入考试科目(按回车分割)')
L01.pack(anchor=NW)
sc=Scrollbar(fr11)
sc.pack(side=RIGHT,fill=Y)
text11=Text(fr11)
text11.config(yscrollcommand=sc.set)
text11.pack(expand=YES,fill=X)
sc.config(command=text11.yview)
bt15=Button(fr11,text='下一步')
bt15.pack(anchor=SE)
text11.focus()
L12 = Label(fr11,text='智育成绩导入模板生成成功')

#按钮

bt15.config(command=f15)

######智育成绩汇总

fr12=LabelFrame(relief=GROOVE,text='智育成绩汇总：')
bt16=Button(fr12,text='下一步')
bt16.pack(anchor=SE)
L13 = Label(fr12,text='智育成绩汇总成功')

#按钮

bt16.config(command=f16)

######智育成绩汇总导入数据库

fr13=LabelFrame(relief=GROOVE,text='智育成绩汇总导入数据库：')
bt17=Button(fr13,text='下一步')
bt17.pack(anchor=SE)
L14 = Label(fr13,text='智育成绩汇总导入数据库成功')

#按钮

bt17.config(command=f17)

######导出"智育成绩.xls"f18

fr14=LabelFrame(relief=GROOVE,text='导出"智育成绩.xls"：')
bt18=Button(fr14,text='下一步')
bt18.pack(anchor=SE)
L15 = Label(fr14,text='导出"智育成绩.xls"成功')

#按钮

bt18.config(command=f18)

##############################综测成绩##################################

######综测成绩工具栏

frame2=LabelFrame(relief=GROOVE,text='综测成绩')
bt20=Button(frame2,text='导入学分')
bt20.grid(row=1,column=1)
bt21=Button(frame2,text='生成综测成绩导入模板')
bt21.grid(row=1,column=2)
bt22=Button(frame2,text='综测成绩汇总')
bt22.grid(row=1,column=3)
bt23=Button(frame2,text='综测成绩汇总导入数据库')
bt23.grid(row=1,column=4)
bt24=Button(frame2,text='导出"综测成绩.xls"')
bt24.grid(row=1,column=5)

#按钮

bt20.config(command=f20)
bt21.config(command=f21)
bt22.config(command=f22)
bt23.config(command=f23)
bt24.config(command=f24)

######导入学分

fr20=LabelFrame(relief=GROOVE,text='导入学分：')
L201 = Label(fr20,text='输入考试科目及学分(按空格分割)如"高数 5 大物 4"')
L201.pack(anchor=NW)
sc2=Scrollbar(fr20)
sc2.pack(side=RIGHT,fill=Y)
text211=Text(fr20)
text211.config(yscrollcommand=sc.set)
text211.pack(expand=YES,fill=X)
sc2.config(command=text211.yview)
bt201=Button(fr20,text='下一步')
bt201.pack(anchor=SE)
text211.focus()
L20 = Label(fr20,text='导入学分成功')
#按钮

bt201.config(command=f201)

######生成综测成绩导入模板

fr21=LabelFrame(relief=GROOVE,text='生成综测成绩导入模板：')
bt25=Button(fr21,text='下一步')
bt25.pack(anchor=SE)
L22 = Label(fr21,text='综测成绩导入模板生成成功')

#按钮

bt25.config(command=f25)

######综测成绩汇总

fr22=LabelFrame(relief=GROOVE,text='综测成绩汇总：')
bt26=Button(fr22,text='下一步')
bt26.pack(anchor=SE)
L23 = Label(fr22,text='综测成绩汇总成功')

#按钮

bt26.config(command=f26)

######综测成绩汇总导入数据库

fr23=LabelFrame(relief=GROOVE,text='综测成绩汇总导入数据库：')
bt27=Button(fr23,text='下一步')
bt27.pack(anchor=SE)
L24 = Label(fr23,text='综测成绩汇总导入数据库成功')

#按钮

bt27.config(command=f27)

######导出"综测成绩.xls"

fr24=LabelFrame(relief=GROOVE,text='导出"综测成绩.xls"：')
bt28=Button(fr24,text='下一步')
bt28.pack(anchor=SE)
L25 = Label(fr24,text='导出"综测成绩.xls"成功')


#按钮
bt28.config(command=f28)

root.mainloop()
