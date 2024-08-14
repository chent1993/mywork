# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:53 
# @Author : tian
# @File : test_contact.py
# @desc :
from time import sleep

import allure
from faker import Faker

from app_po.base.wework_app import WeworkApp

@allure.feature("企业微信联系人操作")
class TestContact:
    def setup_class(self):
        """准备测试数据"""
        fake = Faker("zh_CN")
        self.name =fake.name()
        self.phone = fake.phone_number()
    def setup_method(self):
        '''实例化 app'''
        self.app =WeworkApp()
        #启动app，进入首页
        # self.main = self.app.start().goto_main()
        self.address_list =self.app.start().goto_main().goto_address_list_page()
        # self.menual_input = self.app.start().goto_main()\
        #     .goto_address_list_page()\
        #     .goto_add_member_page()\
        #     .goto_menual_input_page()
    def teardown_method(self):
        self.app.stop()

    @allure.story("添加成员")
    @allure.title("快捷添加成员冒烟用例")
    def test_add_member_success(self):
        '''
        添加成员冒烟用例
        1、点击 通讯录 按钮
        2、点击 添加成员 按钮
        3、点击 手动添加成员 按钮
        4、填写 姓名，手机号 保存 按钮
        5、验证出现添加成功的信息
        :return:
        '''
        search_key = self.name
        tips = self.address_list.goto_add_member_page().goto_menual_input_page().quick_input_member(search_key,self.phone).get_tips()

        assert "添加成功" ==tips
        eles = self.address_list.search_member(search_key)
        results = [ele.text for ele in eles]
        #断言
        assert search_key in results

    @allure.story("添加成员")
    @allure.title("快捷添加成员失败，手机号重复")
    def test_add_member_fail(self):

        tips = self.address_list.goto_add_member_page().goto_menual_input_page().quick_input_member(self.name, self.phone).get_tips()

        assert "添加成功" == tips

        fail_tips = self.address_list.goto_add_member_page().goto_menual_input_page().quick_input_member_fail(self.name,self.phone).get_add_member_fail_tips()

        assert "手机已存在于通讯录，无法添加" == fail_tips


    @allure.story("搜索成员")
    @allure.title("搜索成员")
    def test_search_member(self):
        search_key = self.name
        quick_input_member = self.address_list.goto_add_member_page().goto_menual_input_page().quick_input_member(search_key, self.phone)

        assert "添加成功" == quick_input_member.get_tips()

        eles = quick_input_member.goto_address_list_by_return().goto_search_member_page().search_member(search_key)

        results = [ele.text for ele in eles]
        # 断言
        assert search_key in results


    @allure.story("删除成员")
    @allure.title("删除成员")
    def test_delete_member(self):
        search_key = self.name
        quick_input_member = self.address_list.goto_add_member_page().goto_menual_input_page().quick_input_member(search_key, self.phone)

        assert "添加成功" == quick_input_member.get_tips()

        quick_input_member.goto_address_list_by_return().goto_user_info_page(search_key)\
            .goto_personal_detail_page()\
            .goto_edit_user_page()\
            .delete_member()

        search_key = '王军'
        # self.address_list.goto_user_info_page(search_key).goto_personal_detail_page().goto_edit_user_page().delete_member()
        eles = self.address_list.goto_search_member_page().search_member(search_key)
        #
        # results = [ele.text for ele in eles]
        # # 断言
        # assert search_key not in results









