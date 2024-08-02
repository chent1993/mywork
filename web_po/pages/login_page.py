# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:37 
# @Author : tian
# @File : login_page.py
# @desc :
import yaml

from web_po.base.base_page import BasePage
from web_po.pages.main_page import MainPage


class LoginPage(BasePage):
    """登录页面"""
    def login(self):
        """
        通过cookie登录
        :return:
        """
        self.open_url("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.login_by_cookie()
        return MainPage(self.driver)
    def login_by_account(self):
        ...