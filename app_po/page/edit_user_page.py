# _*_ coding: utf-8 _*_
# @Time : 2024/8/13 22:07 
# @Author : tian
# @File : edit_user_page.py
# @desc :
import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp



class EditUserPage(WeworkApp):
    __DELETE_BTN =AppiumBy.XPATH, "//*[@text='删除']"

    @allure.step("删除成员，返回编辑页面")
    def delete_member(self):
        from app_po.page.address_list_page import AddressListPage
        self.swipe_find("删除成员").click()

        self.find_and_click(*self.__DELETE_BTN)
        return AddressListPage(self.driver)
