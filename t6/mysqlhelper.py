import pymysql
import hashlib
class MysqlHelper:
    def __init__(self, host='118.25.217.90', port=3306, db='test', user='root', passwd='djyiL%;j.3:4_', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

    def insert(self, sql, params):
        return self.__cud(sql, params)

    def update(self, sql, params):
        return self.__cud(sql, params)

    def delete(self, sql, params):
        return self.__cud(sql, params)

    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()

    def __cud(self, sql, params=[]):
        try:
            # 用来获得python执行Mysql命令的方法
            cs1 = self.conn.cursor()
            # 真正执行MySQL语句
            rows = cs1.execute(sql, params)
            self.conn.commit()
            cs1.close()
            self.conn.close()
            return rows  # 影响到了哪行
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchone(self, sql, params=[]):
        # 一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            row = cs1.fetchone()
            # 把查询的结果集中的下一行保存为序列
            # print(row)
            # row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self, sql, params):
        # 接收全部的返回结果行
        # 返回查询到的全部结果值
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            rows = cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None", e)
