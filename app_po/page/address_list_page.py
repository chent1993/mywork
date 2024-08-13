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

from app_po.page.user_info_page import UserInfoPage


class AddressListPage(WeworkApp):
    __ADD_MEMBER_TEXT = "添加成员"
    __SEARCH_BTN =  AppiumBy.XPATH, "//*[@text='搜索']"
    __MEMBERS =AppiumBy.XPATH,"//*[@class='androidx.recyclerview.widget.RecyclerView']//*[@class='android.view.ViewGroup']/*/*"


    @allure.step("点击添加成员按钮，跳转到添加成员页面")
    def goto_add_member_page(self):
        '''进入 添加成员 页面'''
        # 滑动点击添加成员按钮
        from app_po.page.add_member_page import AddMemberPage
        self.swipe_find(self.__ADD_MEMBER_TEXT).click()

        return AddMemberPage(self.driver)

    @allure.step("搜索成员")
    def search_member(self,search_key):
        #搜索框输入搜索关键词
        self.find_and_sendKeys(*self.__SEARCH_BTN,search_key)
        #获取搜索结果
        eles = self.find_eles(self.__MEMBERS)

        return eles

    @allure.step("点击成员，进入成员个人信息页面")
    def goto_user_info_page(self,name):
        self.swipe_find(name).click()
        return UserInfoPage(self.driver)

