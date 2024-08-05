# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 22:28 
# @Author : tian
# @File : base_page.py
# @desc :
import logging
import os
import time

import allure
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.utils.log_utils import logger


class BasePage:

    def __init__(self,driver: WebDriver = None):
        """初始化driver"""
        if driver is None:

            # 初始化driver
            self.driver = webdriver.Chrome()
            # 最大化浏览器
            self.driver.maximize_window()
            # 隐式等待
            self.driver.implicitly_wait(15)
        else:
            self.driver = driver

    def find_ele(self,by,locate):
        """找一个元素"""
        try:
            ele = self.driver.find_element(by,locate)
        except Exception as e:
            ele =None
            self.screen_image()
            logger.info(f"元素{locate}未找到，具体错误信息为{e}")
        return ele

    def find_ele_click(self, by, locate):
        """找到一个元素，并点击"""
        self.find_ele(by,locate).click()
    def find_ele_sendkeys(self, by, locate,text):
        """找到一个元素，并输入文本"""
        self.find_ele(by,locate).send_keys(text)

    def find_eles(self,by,locate):
        """找多个元素"""
        try:
            eles = self.driver.find_elements(by,locate)
        except Exception as e:
            eles =None
            self.screen_image()
            logger.info(f"元素{locate}未找到，具体错误信息为{e}")
        return eles
    def open_url(self,url):
        """打开页面"""
        self.driver.get(url)
    def wait_locate(self,by,locate,timeout=10):
        """显示等待"""
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, locate))
        )
    def wait_click(self,by,locate,timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, locate))
        ).click()

    def login_by_cookie(self):
        """使用cookie登录"""
        # 使用 cookie 登录
        # 从文件中获取 cookie 信息登陆
        # with open("cookie.yaml", "r", encoding="utf-8") as f:
        with open("cookie.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            try:
                # 添加 cookie
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)
        self.driver.refresh()

    def close_brower(self):
        """关闭浏览器"""
        self.driver.quit()

    def get_path(self, path_name):
        '''
        获取绝对路径
        :param path_name: 目录名称
        :return: 目录绝对路径
        '''
        # 获取当前工具文件所在的路径
        root_path = os.path.dirname(os.path.abspath(__file__))
        print(root_path)
        # 拼接当前要输出日志的路径
        dir_path = os.sep.join([root_path, '..', f'{path_name}'])
        return dir_path

    def screen_image(self):
        '''
        截图
        :return: 图片保存路径
        '''
        # 截图命名
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        image_name = f"{now_time}.png"
        # 拼接截图保存路径
        # windows f"{self.get_path('image')}\\{image_name}"
        image_path = f"{self.get_path('image')}/{image_name}"
        logger.info(f"截图保存路径为 {image_path}")
        # 截图
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path,name="image_name", attachment_type=allure.attachment_type.PNG)

        return image_path

    def save_page_source(self):
        '''
        保存页面源码
        :return: 页面源码保存路径
        '''
        # 文件命名
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        pagesource_name = f"{now_time}_pagesource.html"
        # 拼接文件保存路径
        # windows f"{self.get_path('pagesource')}\\{pagesource_name}"
        pagesource_path = f"{self.get_path('pagesource')}/{pagesource_name}"
        logger.info(f"页面源码文件保存路径为 {pagesource_path}")
        # 保存 page source
        with open(pagesource_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        return pagesource_path
