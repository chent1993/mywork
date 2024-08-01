# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:53 
# @Author : tian
# @File : test_add_member.py
# @desc :
from web_po.pages.login_page import LoginPage


class TestAddMember:
    def setup_class(self):
        self.login=LoginPage()

    def teardown_class(self):
        # ...
        # 关闭浏览器
        self.login.close_brower()

    def test_add_member_success(self):
        """添加成员成功"""
        res = self.login.login().goto_contact().goto_add_member().add_member_success().get_user_info()

        assert "haha" in res

