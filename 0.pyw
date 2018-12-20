#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#0.pyw 综合测评系统用户界面
#1.汇总所有函数
#2.优化用户界面
from tkinter import *
import os
import xlrd
import xlwt
import sqlite3
import A1
import A2
import A3
import A4
import B1
import B2
import B3
import B4
import C1
import D1

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
    A1.A1(data)
    L2.pack()
def f6():
    bt6.pack_forget()
    A2.A2()
    L3.pack()

def f7():
    bt7.pack_forget()
    A3.A3()
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
