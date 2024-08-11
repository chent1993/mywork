# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:53 
# @Author : tian
# @File : test_contact.py
# @desc :
from app_po.base.wework_app import WeworkApp


class TestContact:

    def setup_method(self):
        '''实例化 app'''
        self.app =WeworkApp()
        #启动app，进入首页
        self.main = self.app.start().goto_main()

    def teardown_method(self):
        self.app.stop()

    def test_add_member(self):
        '''
        添加成员冒烟用例
        1、点击 通讯录 按钮
        2、点击 添加成员 按钮
        3、点击 手动添加成员 按钮
        4、填写 姓名，手机号 保存 按钮
        5、验证出现添加成功的信息
        :return:
        '''
        tips = self.main.goto_address_list_page()\
            .goto_add_member_page()\
            .goto_menual_input_page()\
            .quick_input_member().get_tips()

        assert tips =="添加成功"

