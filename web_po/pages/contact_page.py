# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:37 
# @Author : tian
# @File : contact_page.py
# @desc :
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.base.base_page import BasePage
from web_po.utils.log_utils import logger


class ContactPage(BasePage):
    """通讯录页面"""
    _ADD_MEMBER_BTN = By.CSS_SELECTOR, ".ww_operationBar .js_add_member"
    _MEMBER_LIST_NAME = By.CSS_SELECTOR,"#member_list>tr>td:nth-child(2)"

    @allure.step("进入添加成员页面")
    def goto_add_member(self):
        """进入添加成员页面"""
        # 等待成员列表加载完毕
        from web_po.pages.add_member_page import AddMemberPage
        self.wait_locate(*self._MEMBER_LIST_NAME)
        self.find_ele_click(*self._ADD_MEMBER_BTN)

        logger.info("进入添加成员页面")
        return AddMemberPage(self.driver)

    def get_user_info(self):
        """获取成员信息"""
        self.wait_locate(*self._MEMBER_LIST_NAME)
        # 定位
        names = self.find_eles(*self._MEMBER_LIST_NAME)
        # names = self.find_eles(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for n in names:
            name_list.append(n.text)
        return name_list