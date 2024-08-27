# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:38 
# @Author : tian
# @File : test_department.py
# @desc :


import allure



from api_auto.api_po.api.contact.member_api import MemberApi



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
        self.depart_id = 1


    def teardown_class(self):
        '''

        :return:
        '''

    @allure.title("获取部门成员ID列表")
    @allure.description("获取部门成员ID列表成功")
    def test_memberlistid(self):

        res = self.member.list_id()
        print(res.text)

        # ids = [ i["id"] for i in res.json().get("department_id")]
        #jsonpath
        # ids = jsonpath.jsonpath(res.json(),"$.department_id..id")
        # assert res.status_code == 200
        # # 断言接口响应体
        # assert res.json().get("errcode") == 0
        # assert self.depart_id in ids





