# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:38 
# @Author : tian
# @File : test_department.py
# @desc :
import logging

import allure
import jsonpath
import pytest


from api_auto.api_po.api.contact.department_api import DepartmentApi
from api_auto.api_po.utils.jsonschema_util import JSONSchemaUtils


@allure.suite("企业微信接口管理")
@allure.sub_suite("部门管理模块")
class TestDepartment:

    def setup_class(self):
        '''

        :return:
        '''
        #实例化部门
        self.department = DepartmentApi()
        #数据准备
        self.depart_id = 220
        self.create_data = {
         "name": "广州研发中心",
        "parentid": 1,
        "name_en": "RDGZ",
        "order": 1,
        "id": self.depart_id
        }
        self.update_name = "广州研发中心-update"
        self.update_data={
            "name": self.update_name,
            "id": self.depart_id
        }

        self.schema = {'$schema': 'http://json-schema.org/schema#', 'type': 'object',
                       'properties': {'errcode': {'type': 'integer'}, 'errmsg': {'type': 'string'},
                                      'department_id': {'type': 'array', 'items': {'type': 'object', 'properties': {
                                          'id': {'type': 'integer'}, 'parentid': {'type': 'integer'},
                                          'order': {'type': 'integer'}}, 'required': ['id', 'order', 'parentid']}}},
                       'required': ['department_id', 'errcode', 'errmsg']}

    def teardown_class(self):
        '''

        :return:
        '''
    @allure.title("添加部门")
    @allure.description("添加部门成功")
    def test_create_department(self):
        '''
        :return:
        '''
        res = self.department.create(self.create_data)
        assert res.status_code == 200
        # 断言接口响应体
        assert res.json().get("errcode") == 0

        res = self.department.simplelist(self.depart_id)

        ids = [i["id"] for i in res.json().get("department_id")]
        assert self.depart_id in ids
        res = self.department.delete(self.depart_id)

    @allure.title("获取部门ID列表")
    @allure.description("获取部门ID列表成功")
    def test_simplelist(self):
        #创建部门
        self.department.create(self.create_data)
        res = self.department.simplelist(self.depart_id)

        # ids = [ i["id"] for i in res.json().get("department_id")]
        #jsonpath
        # ids = jsonpath.jsonpath(res.json(),"$.department_id..id")
        # assert res.status_code == 200
        # # 断言接口响应体
        # assert res.json().get("errcode") == 0
        # assert self.depart_id in ids

        #jsonschema
        assert JSONSchemaUtils().validate_schema(res.json(),self.schema)




    @allure.title("更新部门")
    @allure.description("更新部门成功")
    def test_update_department(self):
        # 创建部门
        self.department.create(self.create_data)

        res =self.department.update(self.update_data)
        assert res.status_code == 200
        # 断言接口响应体
        assert res.json().get("errcode") == 0

        #删除部门
        res = self.department.delete(self.depart_id)

        # get_res = self.department.get(self.depart_id)
        #
        # name = get_res.json().get("department").get("name")
        #
        # assert self.update_name == name

    # @pytest.mark.skip
    @allure.title("删除部门")
    @allure.description("删除部门成功")
    def test_delete_department(self):
        # 创建部门
        self.department.create(self.create_data)

        del_res = self.department.delete(self.depart_id)
        assert del_res.status_code == 200
        # 断言接口响应体
        assert del_res.json().get("errcode") == 0

