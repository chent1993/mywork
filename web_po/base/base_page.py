# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 22:28 
# @Author : tian
# @File : base_page.py
# @desc :
import yaml
from selenium import webdriver


class BasePage:

    def __init__(self,driver =None):
        if driver is None:

            # 初始化driver
            self.driver = webdriver.Chrome()
            # 最大化浏览器
            self.driver.maximize_window()
            # 隐式等待
            self.driver.implicitly_wait(15)
        else:
            self.driver = driver
    def quit(self):
        self.driver.quit()
