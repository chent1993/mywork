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
    def login_by_cookie(self):
        """
        通过cookie登录
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 使用 cookie 登录
        # 从文件中获取 cookie 信息登陆
        # with open("cookie.yaml", "r", encoding="utf-8") as f:
        with open("cookie.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            try:
                # 添加 cookie
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)
        self.driver.refresh()
        return MainPage(self.driver)
    def login_by_account(self):
        ...