#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#A4.py 智育成绩数据库操作
#1.计算智育成绩
#    智育成绩=(学科成绩*学科学分)之和/(学科学分)之和
#2.排序
#3.导出"智育成绩.xls"
#    格式:序号 学号 姓名 (学科) 智育总分
#
import sqlite3
import os
import xlrd
import xlwt


def order():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

    style = xlwt.easyxf('align: wrap on,horz center,vert center')

    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from Score order by "智育成绩" desc"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    #print (col_name_list)
    for i in range(len(col_name_list)):
        sheet1.write(0,i,col_name_list[i],style)
        #print(col_name_list[i])
    a=1
    for row in cursor:
        #print(row)
        for i in range(len(row)):
            sheet1.write(a,i,row[i],style)
            #print(row[i])
        a=a+1   
    workbook.save('./智育成绩.xls')
    cur.close()
    cn.close()
def A4():
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from Credits limit 1"""
    cursor=cn.execute(s)
    for row in cursor:
        xuefen=row

    print(xuefen)
    try:
        cn.execute('''alter table Score add COLUMN '智育成绩' DOUBLE''')
    except:
        print('Table has Exist')
    cur = cn.execute('select * from Score')
    while True:
        x=cur.fetchone()

        if not x:break
        n=len(x)
        k=0
        sum=0
        for i in range(n-3):
            k=k+x[i+2]*xuefen[i]
            sum=sum+xuefen[i]
        k=k/sum
        print(k)
        s="""update Score set '智育成绩'="""+str(k)+""" where 学号 = '"""+str(x[0])+"""'"""
        cn.execute(s)
        cn.commit()
    order()

    cur.close()
    cn.close()

if __name__=="__main__":
    A4()
