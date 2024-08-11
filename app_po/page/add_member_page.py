# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:47 
# @Author : tian
# @File : add_member_page.py
# @desc :
'''
添加成员 页面
'''
from app_po.base.wework_app import WeworkApp
from app_po.page.menual_input_page import MenualInputPage


class AddMemberPage(WeworkApp):

    def goto_menual_input_page(self):


        return MenualInputPage(self.driver)

    def get_tips(self):
        '''
        获取toast 文本
        '''
        toast_tips = "添加成功"
        return toast_tips