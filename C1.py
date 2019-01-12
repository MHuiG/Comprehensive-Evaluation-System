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

def Score_select_all():
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
def Score_select_by_xh(xh):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from Score where 学号= '"""+str(xh.split("\n")[0])+"""'"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for row in cursor:
        print(row)
    cur.close()
    cn.close()

def Score_insert(L):
    L=L.split()
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
    Score_select_all()
def Score_delete_by_xh(xh):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""delete from Score where 学号= '"""+str(xh.split("\n")[0])+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    Score_select_all()
def Score_update(data):
    data=data.split()
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""update Score set """+str(data[1])+""" = '"""+str(data[2])+"""' where 学号= '"""+str(data[0])+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    Score_select_all()
def Score_sql(s):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    cursor=cn.execute(s.split("\n")[0])
    cn.commit()
    Score_select_all()




def ZScore_select_all():
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from ZScore"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for row in cursor:
        print(row)
    cur.close()
    cn.close()
def ZScore_select_by_xh(xh):
    #print(xh.split("\n")[0])
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""select * from ZScore where 学号= '"""+str(xh.split("\n")[0])+"""'"""
    cursor=cn.execute(s)
    col_name_list = [tuple[0] for tuple in cursor.description]
    print (col_name_list)
    for row in cursor:
        print(row)
    cur.close()
    cn.close()

def ZScore_insert(L):
    L=L.split()
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
    s="""insert into ZScore values("""+s+""")"""
    cursor=cn.execute(s)
    cn.commit()
    ZScore_select_all()
def ZScore_delete_by_xh(xh):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""delete from ZScore where 学号= '"""+str(xh.split("\n")[0])+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    ZScore_select_all()
def ZScore_update(data):
    data=data.split()
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    s="""update ZScore set """+str(data[1])+""" = '"""+str(data[2])+"""' where 学号= '"""+str(data[0])+"""'"""
    cursor=cn.execute(s)
    cn.commit()
    ZScore_select_all()
def ZScore_sql(s):
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()
    cursor=cn.execute(s.split("\n")[0])
    cn.commit()
    ZScore_select_all()

if __name__=="__main__":
    pass
    
