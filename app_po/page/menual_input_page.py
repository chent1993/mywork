# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:49 
# @Author : tian
# @File : menual_input_page.py
# @desc :
'''手动添加成员页面'''
import allure

from appium.webdriver.common.appiumby import AppiumBy

from app_po.base.wework_app import WeworkApp



class MenualInputPage(WeworkApp):
    # 姓名输入框
    __INPUT_NAME =  AppiumBy.XPATH, "//*[@text='必填']"
    # 手机号输入框
    __INPUT_PHONE = AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='选填']"
    # 保存按钮
    __SAVE_BTN = AppiumBy.XPATH, "//*[@text='保存']"

    __ADD_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='添加成员']"
    #todo:补充
    __FAIL_TIPS = AppiumBy.XPATH, ""

    @allure.step("快速输入成员姓名与手机号")
    def quick_input_member(self,name,phone,):
        '''
        快速添加成员
        :return:
        '''
        #解决循环引用问题
        from app_po.page.add_member_page import AddMemberPage
        # 输入姓名
        # self.driver.find_element(
        #     *self.__INPUT_NAME
        # ).send_keys(name)
        self.find_and_sendKeys(*self.__INPUT_NAME,name)
        # 输入手机号
        # self.driver.find_element(
        #     *self.__INPUT_PHONE
        # ).send_keys(phone)
        self.find_and_sendKeys(*self.__INPUT_PHONE,phone)
        # 点击保存
        # self.driver.find_element(
        #     *self.__SAVE_BTN
        # ).click()
        self.find_and_click(*self.__SAVE_BTN)
        return AddMemberPage(self.driver)

    @allure.step("快速输入成员姓名与手机号")
    def quick_input_member_fail(self,name,phone,):

        self.find_and_sendKeys(*self.__INPUT_NAME, name)

        self.find_and_sendKeys(*self.__INPUT_PHONE, phone)

        self.find_and_click(*self.__SAVE_BTN)
        return self

    @allure.step("获取 添加成员失败 toast 提示信息")
    def get_add_member_fail_tips(self):
        '''
        获取toast 文本
        '''
        toast_tips = self.get_ele_text(*self.__FAIL_TIPS)

        return toast_tips

    @allure.step("通过点击 添加成员，返回添加成员页面")
    def goto_add_member(self):
        '''
        返回 添加成员页面
        :return:
        '''
        from app_po.page.add_member_page import AddMemberPage

        self.find_and_click(*self.__ADD_MEMBER_BTN)
        return AddMemberPage(self.driver)
