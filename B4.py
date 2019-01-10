#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#B4.py 综测成绩数据库操作
#1.计算综测成绩
#    总分=智育x0.7+思想品德得分（10%）+身心素质得分（5%）+创新实践能力得分（10%） +学院特色得分（5%）
#2.排序
#3.导出"综测成绩.xls"
#    格式:序号 学号 姓名 智育x0.7 思想品德得分（10%） 身心素质得分（5%）创新实践能力得分（10%） 学院特色得分（5%） 总分
#
import sqlite3
import os
import xlrd
import xlwt

def B4():
    pass
def order():
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from ZScore order by "综测成绩" desc"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)

    for row in cursor:
        print(row)
    cur.close()
    cn.close()
if __name__=="__main__":
    cn = sqlite3.connect('Score.db')
    cur = cn.execute('select * from ZScore')
    i = 0
    try:
        cn.execute('''alter table ZScore add COLUMN '综测成绩' DOUBLE''')
    except:
        print('Table has Exist')

    while True:
        x=cur.fetchone()
        if not x:break
        k=(x[10]*0.7)+(x[3]*0.1)+(x[5]*0.05)+(x[7]*0.1)+(x[9]*0.05)
        s="""update ZScore set '综测成绩'="""+str(k)+""" where 学号 = '"""+str(x[0])+"""'"""
        print(s)
        cn.execute(s)
        cn.commit()
    order()

    cur.close()
    cn.close()

