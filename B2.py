#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
from docx import *
import os
import xlwt

def B2():
    pass
if __name__=="__main__":
    path = "./ZScore"
    files = os.listdir(path)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

    style = xlwt.easyxf('align: wrap on,horz center,vert center')
    sheet1.col(0).width = 3300
    sheet1.col(2).width = 6000
    sheet1.col(4).width = 6000
    sheet1.col(6).width = 6000
    sheet1.col(8).width = 6000


    flag=0
    a=1
    for file in files:
        f = os.path.basename(file)
        Path=os.path.join(path,f)
        try:
            document = Document(Path)
            tables = document.tables 
            table = tables[0]

            if flag==0:
                for i in range(len(table.rows)):
                    sheet1.write(0,i,table.cell(i,0).text,style)
                    print(table.cell(i,0).text)
                flag=1
            
            for i in range(len(table.rows)):
                sheet1.write(a,i,table.cell(i,1).text,style)
                print(table.cell(i,1).text)
            a=a+1   
        except:
            pass
        
    workbook.save('./综测成绩汇总.xls')
