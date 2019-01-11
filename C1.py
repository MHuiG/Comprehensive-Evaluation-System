#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#C1.py 数据库操作
#对数据库数据增删改查
#
import sqlite3
import os
import xlrd
import xlwt

def select_all():
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from Score"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for row in cursor:
        print(row)
    cur.close()
    cn.close()
def select_by_xh(xh):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from Score where 学号= '"""+str(xh)+"""'"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for row in cursor:
        print(row)
    cur.close()
    cn.close()

def insert(L):
    s=""
    z=0
    for i in L:
        if z==0:
            s+="'"+str(i)+"'"
        else:
            s+=",'"+str(i)+"'"
        z=z+1
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""insert into Score values("""+s+""")"""
    cursor=cn.execute(s)
    cn.commit()
    select_all()
def delete_by_xh(xh):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""delete from Score where 学号= '"""+str(xh)+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    select_all()
def update(xh,a,b):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""update Score set """+str(a)+""" = '"""+str(b)+"""' where 学号= '"""+str(xh)+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    select_all()
def sql(s):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    cursor=cn.execute(s)
    cn.commit()
    select_all()
if __name__=="__main__":
    print()
    #select_all()
        
    #L=['171214080267344','0', 73.0, 82.8, 87.7, 79.7, 65.8, 63.6, 76.0, 83.7, 86.0, 92.0, 81.5, 86.0]
    #insert(L)
    
    
    #update('171214080267344','1','0')

    #select_by_xh('171214080267344')
    
    
    #delete_by_xh(171214080267344)

    #sql("""delete from Score where 学号= '1712140802673s'""")
