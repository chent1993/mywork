# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 22:28 
# @Author : tian
# @File : base_page.py
# @desc :
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait





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
        ele = self.driver.find_element(by,locate)
        return ele

    def find_ele_click(self, by, locate):
        """找到一个元素，并点击"""
        self.find_ele(by,locate).click()
    def find_ele_sendkeys(self, by, locate,text):
        """找到一个元素，并输入文本"""
        self.find_ele(by,locate).send_keys(text)
    def find_eles(self,by,locate):
        """找多个元素"""
        eles = self.driver.find_elements(by,locate)
        return eles
    def open_url(self,url):
        """打开页面"""
        self.driver.get(url)
    def wait_locate(self,by,locate,timeout=10):
        """显示等待"""
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, locate))
        )
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
