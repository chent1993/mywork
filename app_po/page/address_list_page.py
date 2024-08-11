# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:46 
# @Author : tian
# @File : address_list_page.py
# @desc :
'''
添加通讯录 页面
'''
from app_po.base.wework_app import WeworkApp
from app_po.page.add_member_page import AddMemberPage


class AddressListPage(WeworkApp):

    def goto_add_member_page(self):


        return AddMemberPage(self.driver)
