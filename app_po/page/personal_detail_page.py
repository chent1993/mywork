# _*_ coding: utf-8 _*_
# @Time : 2024/8/13 22:04 
# @Author : tian
# @File : personal_detail_page.py
# @desc :
import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp
from app_po.page.edit_user_page import EditUserPage


class PersonalDetailPage(WeworkApp):
    #编辑成员
    __EDIT_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='编辑成员']"

    @allure.step("点击 编辑成员，跳转到编辑页面")
    def goto_edit_user_page(self):
        self.find_and_click(*self.__EDIT_MEMBER_BTN)
        return EditUserPage(self.driver)