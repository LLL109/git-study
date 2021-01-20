
import re
import pymysql
# with open("dict.txt") as f:
#
#     list_word=[line.split(" ")[0] for line in f]
#     print(list_word)
#     f.seek(0,0)
#     list_mean=[]
#     for line in f:
#         data=re.split('  ',line)[-1]
#         list_mean.append(re.findall(".+", data))
#     print(list_mean)
# list_data=list(zip(list_word,list_mean))
with open("dict.txt") as f:
    for line in f:
        mean=line.split(" ",2)
        print(mean)
# kwargs={
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "123456",
#     "database": "dict",
#     "charset": "utf8"
# }
# db=pymysql.connect(**kwargs)
# cur=db.cursor()
# try:
#     sql="insert into word (word,mean) values (%s,%s)"
#     cur.executemany(sql,list_data)
#
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()



