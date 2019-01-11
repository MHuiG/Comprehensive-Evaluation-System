#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#D1.py 数据库导入学分
#1.输入科目对应的学分
#2.创建数据表"XScore" 学分表导入数据库
#
import sqlite3
import os
import xlrd
import xlwt

def D1(data):
    s=data.split(' ')
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    a=0
    for i in range(len(s)):
        if(i%2==0):
            sheet1.write(0,a,s[i])
        else:
            sheet1.write(1,a,s[i])
            a=a+1
    workbook.save('./学分导入.xls')

    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()

    path = "./学分导入.xls"
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    ncols = table.ncols
    nrows = table.nrows
    s1=""
    flag=0
    for i in table.row_values(0):
        if flag>=0:
            s1=s1+i+' DOUBLE'
            if flag!=ncols-1:
                s1=s1+','
        flag+=1
    print(s1)
    try:
        # print('''CREATE TABLE IF NOT EXISTS Credits('''+s1+''');''')
        cn.execute('''CREATE TABLE IF NOT EXISTS Credits('''+s1+''');''')
    except:
        pass
    s2=''
    flag=0
    for i in table.row_values(0):
        s2=s2+i
        if flag!=ncols-1:
            s2=s2+','
        flag+=1


    flag = 0
    s3 = ''
    for k in table.row_values(1):
        s3 = s3 + str(k)
        if flag != ncols - 1:
            s3+=','
            flag += 1
    # print('''insert into  Credits ('''+s2+''') values('''+s3+''')''')
    cn.execute('''insert into  Credits ('''+s2+''') values('''+s3+''')''')
    cn.commit()
    cur.close()
    cn.close()
if __name__=="__main__":
    # data=input()
    # s=data.split(' ')
    # workbook = xlwt.Workbook()
    # sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    # a=0
    # for i in range(len(s)):
    #     if(i%2==0):
    #         sheet1.write(0,a,s[i])
    #     else:
    #         sheet1.write(1,a,s[i])
    #         a=a+1
    # workbook.save('./学分导入.xls')

    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()

    path = "./学分导入.xls"
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    ncols = table.ncols
    nrows = table.nrows
    s1=""
    flag=0
    for i in table.row_values(0):
        if flag>=0:
            s1=s1+i+' DOUBLE'
            if flag!=ncols-1:
                s1=s1+','
        flag+=1
    print(s1)
    try:
        # print('''CREATE TABLE IF NOT EXISTS Credits('''+s1+''');''')
        cn.execute('''CREATE TABLE IF NOT EXISTS Credits('''+s1+''');''')
    except:
        pass
    s2=''
    flag=0
    for i in table.row_values(0):
        s2=s2+i
        if flag!=ncols-1:
            s2=s2+','
        flag+=1


    flag = 0
    s3 = ''
    for k in table.row_values(1):
        s3 = s3 + str(k)
        if flag != ncols - 1:
            s3+=','
            flag += 1
    # print('''insert into  Credits ('''+s2+''') values('''+s3+''')''')
    cn.execute('''insert into  Credits ('''+s2+''') values('''+s3+''')''')
    cn.commit()
    cur.close()
    cn.close()
