#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#B3.py 综测成绩导入数据库
#1.链接数据库"Score.db"
#2.创建数据表"ZScore"，设置主键"学号 char(20) PRIMARY KEY"
#    数据表格式:学号 姓名 思想品德得分（10%） 身心素质得分（5%）创新实践能力得分（10%） 学院特色得分（5%）
#3.将"综测成绩汇总.xls"导入数据库"ZScore.db"
#
import sqlite3
import os
import xlrd
import xlwt
if __name__=="__main__":
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()

    path = "./综测成绩汇总.xls"
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    ncols = table.ncols
    nrows = table.nrows
    s1 = "学号 char(20) PRIMARY KEY, 姓名 char(10), "
    flag = 0
    for i in table.row_values(0):
        if flag >= 2:
            if flag % 2 == 0:
                if flag == 10:
                    s1 = s1 + i + ' DOUBLE'
                else:
                    s1 = s1 + i + ' char(1000)'
            if flag % 2 != 0:
                s1 = s1 + i + ' DOUBLE'
            if flag != ncols - 1:
                s1 = s1 + ','
        flag += 1
    try:
        cn.execute('''CREATE TABLE IF NOT EXISTS Score(''' + s1 + ''');''')
    except:
        pass
    s2 = ''
    flag = 0
    for i in table.row_values(0):
        s2 = s2 + i
        if flag != ncols - 1:
            s2 = s2 + ','
        flag += 1

    for i in range(nrows):
        flag = 0
        s3 = ''
        if i != 0:
            for k in table.row_values(i):
                if flag == 0:
                    s3 = s3 + str(int(k))
                elif flag == 1:
                    s3 = s3 + "'" + str(k) + "'"
                elif flag == 2:
                    s3 = s3 + "'" + str(k) + "'"
                elif flag == 4:
                    s3 = s3 + "'" + str(k) + "'"
                elif flag == 6:
                    s3 = s3 + "'" + str(k) + "'"
                elif flag == 8:
                    s3 = s3 + "'" + str(k) + "'"
                else:
                    s3 = s3 + str(k)
                if flag != ncols - 1:
                    s3 += ','
                    flag += 1
            cn.execute('''insert into  Score (''' + s2 + ''') values(''' + s3 + ''')''')
            cn.commit()
    cur.close()
    cn.close()

