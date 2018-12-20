#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
import xlwt
import os

def A1(data):
    try:
        os.makedirs("./Score")
    except:
        pass
    s=data.split('\n')
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,'学号')
    sheet1.write(0,1,'姓名')
    a=2
    for i in range(len(s)):
        sheet1.write(0,a,s[i])
        a=a+1
    workbook.save('./学号_姓名成绩导入模板.xls')

if __name__=="__main__":
    try:
        os.makedirs("./Score")
    except:
        pass

    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,'学号')
    sheet1.write(0,1,'姓名')
    n=input("excel列数\n")
    a=2
    for i in range(int(n)):
        b=input()
        sheet1.write(0,a,b)
        a=a+1

    workbook.save('./学号_姓名智育成绩导入模板.xls')
