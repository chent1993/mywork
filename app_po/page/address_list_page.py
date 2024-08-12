# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:46 
# @Author : tian
# @File : address_list_page.py
# @desc :
'''
通讯录 页面
'''
import allure

from app_po.base.wework_app import WeworkApp
from app_po.page.add_member_page import AddMemberPage


class AddressListPage(WeworkApp):
    __ADD_MEMBER_TEXT = "添加成员"

    @allure.step("点击添加成员按钮，跳转到添加成员页面")
    def goto_add_member_page(self):
        '''进入 添加成员 页面'''
        # 滑动点击添加成员按钮
        self.swipe_find(self.__ADD_MEMBER_TEXT).click()

        return AddMemberPage(self.driver)
