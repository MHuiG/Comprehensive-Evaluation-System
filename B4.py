#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#B4.py 导出"综测成绩.xls"
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


def order():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

    style = xlwt.easyxf('align: wrap on,horz center,vert center')
    sheet1.col(0).width = 3300
    sheet1.col(2).width = 6000
    sheet1.col(4).width = 6000
    sheet1.col(6).width = 6000
    sheet1.col(8).width = 6000

    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from ZScore order by "综测成绩" desc"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for i in range(len(col_name_list)):
        sheet1.write(0,i,col_name_list[i],style)
        print(col_name_list[i])
    a=1
    for row in cursor:
        print(row)
        for i in range(len(row)):
            sheet1.write(a,i,row[i],style)
            print(row[i])
        a=a+1   
    workbook.save('./综测成绩.xls')
    cur.close()
    cn.close()
def B4():
    cn = sqlite3.connect('Score.db')
    cur = cn.execute('select * from ZScore')
    i = 0
    try:
        cn.execute('''alter table ZScore add COLUMN '综测成绩' DOUBLE''')
    except:
        print('Table has Exist')
    #导入智育成绩开始
    while True:
        x = cur.fetchone()
        if not x: break
        t=x[0]
        print(t)
        cu=cn.cursor()
        cu.execute("""select 智育成绩 from Score where 学号='"""+t+"""'""")
        values = cu.fetchall()
        print(values[0][0],'***********')
        s = """update ZScore set '智育成绩'=""" + str(values[0][0]) + """ where 学号 = '""" + str(x[0]) + """'"""
        cn.execute(s)
        cn.commit()
    #导入完毕

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


if __name__=="__main__":
    B4()
