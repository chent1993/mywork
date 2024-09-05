# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:38 
# @Author : tian
# @File : test_department.py
# @desc :


import allure
import jsonpath
from faker import Faker

from api_auto.api_po.api.contact.member_api import MemberApi
from api_auto.api_po.utils.jsonschema_util import JSONSchemaUtils


@allure.suite("企业微信接口管理")
@allure.sub_suite("成员管理模块")
class TestDepartment:

    def setup_class(self):
        '''

        :return:
        '''
        #实例化成员
        self.member = MemberApi()
        #数据准备
        self.fake = Faker("zh_CN")
        self.name = self.fake.name()
        self.userid = self.fake.uuid4()
        self.phone =self.fake.phone_number()
        self.create_member = {
            "userid": self.userid,
            "name": self.name,
            "mobile": self.phone
        }
        self.schema ={'$schema': 'http://json-schema.org/schema#', 'type': 'object', 'properties': {'errcode': {'type': 'integer'}, 'errmsg': {'type': 'string'}, 'dept_user': {'type': 'array', 'items': {'type': 'object', 'properties': {'userid': {'type': 'string'}, 'department': {'type': 'integer'}, 'usrid': {'type': 'string'}}, 'required': ['department']}}}, 'required': ['dept_user', 'errcode', 'errmsg']}

    def teardown_class(self):
        '''

        :return:
        '''

    @allure.title("添加成员")
    @allure.description("添加成员成功")
    def test_create_member(self):

        res = self.member.create(self.create_member)
        assert res.status_code == 200
        # 断言接口响应体
        assert res.json().get("errcode") == 0

    @allure.title("获取部门成员ID列表")
    @allure.description("获取部门成员ID列表成功")
    def test_memberlistid(self):

        res = self.member.list_id()

        assert res.status_code == 200
        # 断言接口响应体
        assert res.json().get("errcode") == 0
        # ids = [ i["userid"] for i in res.json().get("dept_user")]
        #jsonpath
        ids = jsonpath.jsonpath(res.json(),"$.dept_user..userid")

        assert self.userid in ids
        assert JSONSchemaUtils().validate_schema(res.json(),self.schema)






