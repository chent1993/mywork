# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 21:37 
# @Author : tian
# @File : mysql_util.py
# @desc :
import pymysql

class MySQLUtil:


    # 封装建立连接的对象
    @classmethod
    def get_conn(self):
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="test_db",
            charset="utf8mb4"
        )
        return conn

    # 执行sql语句
    @classmethod
    def execute_sql(self,sql):
        connect = self.get_conn()
        cursor = connect.cursor()
        cursor.execute(sql)  # 执行SQL
        record = cursor.fetchone()  # 查询记录
        return record

if __name__ == '__main__':

    print(MySQLUtil.execute_sql("select * from users limit 1"))
