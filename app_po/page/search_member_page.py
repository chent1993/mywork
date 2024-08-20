# _*_ coding: utf-8 _*_
# @Time : 2024/8/14 22:59 
# @Author : tian
# @File : search_member_page.py
# @desc :
import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp


class SearchMemberPage(WeworkApp):

    __SEARCH_BTN = AppiumBy.XPATH, "//*[@text='搜索']"
    __MEMBERS = AppiumBy.XPATH, "//*[@class='android.view.ViewGroup']//*[@class='android.view.ViewGroup']/*/*"

    @allure.step("搜索成员")
    def search_member(self,search_key):
        #搜索框输入搜索关键词
        self.find_and_sendKeys(*self.__SEARCH_BTN,search_key)
        #获取搜索结果
        eles = self.find_eles(self.__MEMBERS)

        results = [ele.text for ele in eles]
        return results
