# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:46 
# @Author : tian
# @File : address_list_page.py
# @desc :
'''
通讯录 页面
'''
import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp
from app_po.page.search_member_page import SearchMemberPage

from app_po.page.user_info_page import UserInfoPage


class AddressListPage(WeworkApp):
    __ADD_MEMBER_TEXT = "添加成员"
    __SEARCH_INPUT = AppiumBy.XPATH, "//*[@text='测试6部']/../../../following-sibling::*/*[1]"

    @allure.step("点击添加成员按钮，跳转到添加成员页面")
    def goto_add_member_page(self):
        '''进入 添加成员 页面'''
        # 滑动点击添加成员按钮
        from app_po.page.add_member_page import AddMemberPage
        self.swipe_find(self.__ADD_MEMBER_TEXT).click()

        return AddMemberPage(self.driver)

    def goto_search_member_page(self):
        self.find_and_click(*self.__SEARCH_INPUT)
        return SearchMemberPage(self.driver)

    @allure.step("点击成员，进入成员个人信息页面")
    def goto_user_info_page(self,name):
        # self.wait_ele_click()
        self.scroll_to_top()
        self.swipe_find(name).click()
        return UserInfoPage(self.driver)

