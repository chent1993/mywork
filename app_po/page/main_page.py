# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:44 
# @Author : tian
# @File : main_page.py
# @desc :
'''
企业通讯录 首页
'''
from app_po.base.wework_app import WeworkApp
from app_po.page.address_list_page import AddressListPage


class MainPage(WeworkApp):



    def goto_address_list_page(self):

        return AddressListPage(self.driver)
