# 综合测评系统
# Comprehensive Evaluation System

[![Open Source Love](https://cdn.jsdelivr.net/gh/MHuiG/imgbed/github/open-source.svg)](https://github.com/ellerbrock/open-source-badges/)[![MIT Licence](https://cdn.jsdelivr.net/gh/MHuiG/imgbed/github/mit.svg)](https://opensource.org/licenses/mit-license.php)


运行该项目首先需要pip安装 docx xlwt xlrd

<b>0.pyw 综合测评系统用户界面</b>

1.汇总所有函数

2.优化用户界面

<b>A1.py 生成智育成绩导入模板</b>

1.创建"Score"文件夹

2.输入科目

3.生成"学号_姓名智育成绩导入模板.xls"

<b>A2.py 智育成绩汇总</b>

1.遍历"Score"文件夹中的"xxx学号_xxx姓名智育成绩导入模板.xls"

2.生成"智育成绩汇总.xls"

3."智育成绩汇总.xls"格式 : 固定(学号 姓名)  用户指定(科目)

<b>A3.py 智育成绩汇总导入数据库</b>	

1.创建数据库"Score.db"

2.创建数据表"Score"，设置主键"学号 char(20) PRIMARY KEY" 

数据表格式:学号 姓名 (科目)

3.将"智育成绩汇总.xls"导入数据库"Score.db"

<b>A4.py 导出"智育成绩.xls"</b>

1.计算智育成绩 

(学科成绩*学科学分)之和/(学科学分)之和

2.排序

3.导出"智育成绩.xls" 

格式:序号 学号 姓名 (学科) 智育总分

<b>B1.py 综测成绩导入模板</b>

1.创建"ZScore"文件夹

2.生成"学号_姓名综测成绩导入模板.docx"

格式:学号 姓名 思想品德素质得分明细 思想品德得分（10%） 身心素质得分明细 身心素质得分（5%） 创新实践能力得分明细 创新实践能力得分（10%） 学院特色得分明细 学院特色得分（5%）

<b>B2.py 综测成绩汇总</b>

1.遍历ZScore文件夹中的"xxxx学号_xxxx姓名综测成绩导入模板.docx"

2.生成"综测成绩汇总.xls"

格式:学号 姓名 思想品德素质得分明细 思想品德得分（10%） 身心素质得分明细 身心素质得分（5%） 创新实践能力得分明细 创新实践能力得分（10%） 学院特色得分明细 学院特色得分（5%）

<b>B3.py 综测成绩导入数据库</b>

1.链接数据库"Score.db"

2.创建数据表"ZScore"，设置主键"学号 char(20) PRIMARY KEY" 

数据表格式:学号 姓名 思想品德得分（10%） 身心素质得分（5%）创新实践能力得分（10%） 学院特色得分（5%）

3.将"综测成绩汇总.xls"导入数据库"ZScore.db"

<b>B4.py 导出"综测成绩.xls"</b>

1.计算综测成绩 

总分=智育x0.7+思想品德得分（10%）+身心素质得分（5%）+创新实践能力得分（10%） +学院特色得分（5%） 

2.排序

3.导出"综测成绩.xls" 

格式:序号 学号 姓名 智育x0.7 思想品德得分（10%） 身心素质得分（5%）创新实践能力得分（10%） 学院特色得分（5%） 总分

<b>C1.py 数据库操作</b>

对数据库数据增删改查


<b>D1.py 数据库导入学分</b>

1.设置科目对应的学分 

2.创建数据表"XScore"  学分表导入数据库


