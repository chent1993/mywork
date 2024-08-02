# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:38 
# @Author : tian
# @File : add_member_page.py
# @desc :
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.base.base_page import BasePage
from web_po.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    """添加成员页面"""
    def add_member_success(self):
        """添加成员成功"""

        # self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
        self.fake = Faker("zh_CN")
        # name = self.fake.name()
        name = "haha"
        self.find_ele_sendkeys(By.ID,"username",name)

        mid = self.fake.uuid4()
        self.find_ele_sendkeys(By.ID,"memberAdd_acctid",mid)

        phone = self.fake.phone_number()
        self.find_ele_sendkeys(By.ID,"memberAdd_phone",phone)


        self.find_ele_click(By.CSS_SELECTOR,".js_btn_save")

        return ContactPage(self.driver)
    def add_member_fail(self):
        """添加成员失败"""
        ...