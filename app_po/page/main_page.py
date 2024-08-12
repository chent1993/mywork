# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:44 
# @Author : tian
# @File : main_page.py
# @desc :
'''
企业微信 首页
'''
import allure

from app_po.base.wework_app import WeworkApp
from app_po.page.address_list_page import AddressListPage


class MainPage(WeworkApp):
    #通讯录按钮
    __CONTACT_BTN = AppiumBy.XPATH, "//*[@text='通讯录']"

    @allure.step("点击通讯录按钮，跳转到通讯录页面")
    def goto_address_list_page(self):
        '''进入 通讯录 页面'''
        # self.driver.find_element(
        #     self.__CONTACT_BTN
        # ).click()
        self.find_and_click(*self.__CONTACT_BTN)
        return AddressListPage(self.driver)
