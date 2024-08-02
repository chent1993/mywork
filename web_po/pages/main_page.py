# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:37 
# @Author : tian
# @File : main_page.py
# @desc :
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.base.base_page import BasePage
from web_po.pages.add_member_page import AddMemberPage
from web_po.pages.contact_page import ContactPage


class MainPage(BasePage):
    """首页"""

    def goto_contact(self):
        """进入通讯录页面"""

        self.find_ele_click(By.ID, "menu_contacts")

        return ContactPage(self.driver)

    def goto_add_member(self):
        """进入添加成员页面"""

        return AddMemberPage()