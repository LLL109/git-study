"""
    练习：在stu数据库下创建一个表　user
    user -->id user password


写一个类，类中需要有一个注册方法和一个登录方法
通过这两个方法可以完成注册登录功能

注册的用户名　不能重复
"""
import pymysql


class User:
    def __init__(self):
        self.kwargs = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "stu",
            "charset": "utf8"
        }
        self.connect()

    # 完成数据库连接
    def connect(self):
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()

    # 注册
    def register(self,user_input,password_input):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        while True:
            try:


                sql="insert into users (user,password) values " \
                    "(%s,%s);"
                self.cur.execute(sql,(user_input,password_input))
                self.db.commit()
                return True


            except Exception as e:
                print(e)
                self.db.rollback()
                return False








    # 登录
    def login(self,user_input,password_input):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        sql="select user from users where user=%s and password=%s;"
        self.cur.execute(sql,[user_input,password_input])
        if self.cur.fetchone():
            return True
        else:
            return False











if __name__ == '__main__':
    # user = User()
    # print(user.register("张", "abc123"))
    # user.close()

    user = User()
    print(user.login("张三", "abc123"))
    user.close()