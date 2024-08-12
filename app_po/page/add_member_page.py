# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:47 
# @Author : tian
# @File : add_member_page.py
# @desc :
'''
添加成员 页面
'''
import allure

from app_po.base.wework_app import WeworkApp
from app_po.page.menual_input_page import MenualInputPage


class AddMemberPage(WeworkApp):
    #手动输入添加按钮
    __MENUAL_INPUT_BTN = AppiumBy.XPATH, "//*[@text='手动输入添加']"


    @allure.step("点击手动添加按钮，跳转到手动输入添加页面")
    def goto_menual_input_page(self):
        '''
        跳转到手动添加成员 页面
        :return:
        '''
        # 点击 手动添加成员
        # self.driver.find_element(
        #     self.__MENUAL_INPUT_BTN
        # ).click()
        self.find_and_click(*self.__MENUAL_INPUT_BTN)

        return MenualInputPage(self.driver)

    @allure.step("获取 toast 提示信息")
    def get_tips(self):
        '''
        获取toast 文本
        '''
        # toast_tips = self.driver.find_element(self.__ADD_MEMBER_TOAST).text
        toast_tips = self.get_toast_tips()

        return toast_tips