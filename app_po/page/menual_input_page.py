# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:49 
# @Author : tian
# @File : menual_input_page.py
# @desc :
'''手动添加成员页面'''
from app_po.base.wework_app import WeworkApp


class MenualInputPage(WeworkApp):

    def quick_input_member(self):
        '''
        快速添加成员
        :return:
        '''
        #解决循环引用问题
        from app_po.page.add_member_page import AddMemberPage
        # 输入姓名
        self.driver.find_element(
            AppiumBy.XPATH, "//*[@text='必填']"
        ).send_keys(self.name)
        # 输入手机号
        self.driver.find_element(
            AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='选填']"
        ).send_keys(self.phone)
        # 点击保存
        self.driver.find_element(
            AppiumBy.XPATH, "//*[@text='保存']"
        ).click()
        return AddMemberPage(self.driver)
