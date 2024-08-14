# _*_ coding: utf-8 _*_
# @Time : 2024/8/13 21:54 
# @Author : tian
# @File : user_info_page.py
# @desc :
'''
个人信息 页面
'''
import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp
from app_po.page.personal_detail_page import PersonalDetailPage


class UserInfoPage(WeworkApp):
    #...详情
    __DETAIL_BTN = AppiumBy.XPATH,"//*[@text='个人信息']/../../../../following-sibling::*/*[1]"

    @allure.step("点击详情，跳转到成员详情页面")
    def goto_personal_detail_page(self):
        self.find_and_click(*self.__DETAIL_BTN)
        return PersonalDetailPage(self.driver)