"""
    使用pymysql操作数据库模板
"""
import pymysql

kwargs = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**kwargs)
cur=db.cursor()

#　数据库数据的获取　select
sql="select * from class where score>90;"
cur.execute(sql)

# all=cur.fetchall()
# print(all)
# one =cur.fetchone()
# print(one)
#
# many=cur.fetchmany(2)
# print(many)
print(type(cur))
for item in cur:
    print(item)



# 关闭
cur.close()
db.close()

