"""
    编写一个程序，将dict.txt单词本中的单词存储到数据库中的一个数据表里
    库：dict
    表：word id word mean
"""

import pymysql
import re
file=open("dict.txt")
data=[]
for line in file:
    data+=re.findall("(\w+)\s+(.*)",line)



file.close()

kwargs = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}
db = pymysql.connect(**kwargs)
cur = db.cursor()
try:


    sql="insert into word (word,mean) values (%s,%s)"
    cur.executemany(sql,data)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()





