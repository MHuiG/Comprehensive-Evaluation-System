# 综合测评系统
# Comprehensive Evaluation System
#

#0.0用户界面.pyw
优化用户界面

#1.1生成智育成绩导入模板.py	
1.创建"Score"文件夹
2.输入科目
3.生成"学号_姓名智育成绩导入模板.xls"

#1.2智育成绩汇总.py	
1.遍历Score文件夹中的"xxx学号_xxx姓名智育成绩导入模板.xls"
2.生成"智育成绩汇总.xls"

#1.3智育成绩汇总导入数据库.py	
1.创建数据库"Score.db"
2.创建数据表"Score"，设置主键"学号 char(20) PRIMARY KEY"
3.将"智育成绩汇总.xls"导入数据库"Score.db"

#2.1综测成绩导入模板.py	
1.创建"ZScore"文件夹
2.生成"学号_姓名综测成绩导入模板.docx"

#2.2综测成绩汇总.py
1.遍历ZScore文件夹中的"xxxx学号_xxxx姓名综测成绩导入模板.docx"
2.生成"综测成绩汇总.xls"
