# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 21:18 
# @Author : tian
# @File : base_page.py
# @desc :
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver