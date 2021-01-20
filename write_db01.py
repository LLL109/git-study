"""
    数据库写操作
    Myisam引擎不支持事务,执行语句立即生效
    Innodb引擎支持事务，执行语句结束后需要db.commit()提交事务执行语句才会生效
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

# 创建游标　使用sql操作数据得到结果的对象
cur = db.cursor()

#　使用sql操作数据 insert delete update
try:

    sql="delete from class where id=1;" #class表InnoDB引擎需结束事务
    cur.execute(sql) #执行语句
    sql="update class set score=%s where id=%s;"
    cur.execute(sql,(100,3))
    db.commit() # 提交事务

except Exception as e:
    print(e)
    db.rollback() # 事务回滚
 # sql="delete from hobby where id=1;" #hobby表MyISAM引擎
    # cur.execute(sql)


# 关闭
cur.close()
db.close()

