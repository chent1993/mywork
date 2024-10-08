# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:38 
# @Author : tian
# @File : add_member_page.py
# @desc :
import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.base.base_page import BasePage
from web_po.pages.contact_page import ContactPage
from web_po.utils.log_utils import logger


class AddMemberPage(BasePage):
    """添加成员页面"""
    _NAME =By.ID,"username"
    _ACCID = By.ID,"memberAdd_acctid"
    _PHONE = By.ID,"memberAdd_phone"
    _BTN_SAVE = By.CSS_SELECTOR,".js_btn_save"
    _TIPS_ERR = By.CSS_SELECTOR, ".ww_inputWithTips_WithErr"
    _TIPS_TEXT = By.XPATH, '//*[@id="memberAdd_acctid"]/following-sibling::*[1]'
    _BTN_CANCEL = By.CSS_SELECTOR,".js_btn_cancel"

    # _LEAVE_PAGE = By.XPATH, "//*[@node-type='cancel']"
    @allure.step("添加成员成功")
    def add_member_success(self,name,accid,phone):
        """添加成员成功"""
        self.wait_locate(*self._NAME, 15)

        self.find_ele_sendkeys(*self._NAME,name)

        self.find_ele_sendkeys(*self._ACCID,accid)

        self.find_ele_sendkeys(*self._PHONE,phone)


        self.find_ele_click(*self._BTN_SAVE)
        logger.info(f"添加成员{name}")
        self.screen_image()
        return ContactPage(self.driver)

    @allure.step("输出成员信息（重复），添加成员失败")
    def add_member_fail(self,name,accid,phone):
        """输出成员信息（重复）添加成员失败 返回当前页面"""
        self.wait_locate(*self._NAME, 15)

        self.find_ele_sendkeys(*self._NAME,name)

        self.find_ele_sendkeys(*self._ACCID,accid)

        self.find_ele_sendkeys(*self._PHONE,phone)


        self.find_ele_click(*self._BTN_SAVE)
        logger.info(f"添加成员{name}")
        return self

    @allure.step("获取错误提示信息")
    def get_fail_tips(self):
        """获取错误提示信息"""
        self.wait_locate(*self._TIPS_ERR)
        tip_ele = self.find_ele(*self._TIPS_TEXT)
        self.screen_image()
        tips = tip_ele.text

        return tips

    @allure.step("通过点击取消按钮，返回通讯录页面")
    def goto_contact_by_cancel(self):
        """通过点击取消按钮返回通讯录页面"""
        self.find_eles(*self._BTN_CANCEL)[0].click()
        # self.wait_click(*self._LEAVE_PAGE, 15)
        return ContactPage(self.driver)