# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 22:11 
# @Author : tian
# @File : test_mysql.py
# @desc :
import allure

from api_auto.api_po.utils.mysql_util import MySQLUtil


@allure.suite("企业微信接口管理")
@allure.sub_suite("mysql测试")
class TestMysql:
    @allure.title("查询mysql")
    @allure.description("查询mysql")
    def test_mysql_conn(self):
        sql = MySQLUtil.execute_sql("select * from users limit 1");
        assert sql