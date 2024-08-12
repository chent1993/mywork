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
    _MENUAL_INPUT = AppiumBy.XPATH, "//*[@text='手动输入添加']"
    _ADD_MEMBER_TOAST = AppiumBy.XPATH,"//*[@class='android.widget.Toast']"

    def goto_menual_input_page(self):
        '''
        进入手动添加成员 页面
        :return:
        '''
        # 点击 手动添加成员
        self.driver.find_element(
            self._MENUAL_INPUT
        ).click()


        return MenualInputPage(self.driver)

    def get_tips(self):
        '''
        获取toast 文本
        '''
        toast_tips = self.driver.find_element(self._ADD_MEMBER_TOAST).text

        return toast_tips