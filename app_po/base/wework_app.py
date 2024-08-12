# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 20:39 
# @Author : tian
# @File : wework_app.py
# @desc :
from appium import webdriver
from appium.options.common import AppiumOptions

from app_po.base.base_page import BasePage


"""
企业微信 app 启动入口
"""
class WeworkApp(BasePage):

    def start(self):
        '''启动 app'''
        # Capability 设置定义为字典
        caps = {}
        # 设置 app 安装的平台（Android、iOS）
        caps["platformName"] = "Android"
        # 设置 appium 驱动
        caps["appium:automationName"] = "uiautomator2"
        # 设置被测设备的名字
        caps["appium:deviceName"] = "emulator-5554"
        # 设置 app 的包名
        caps["appium:appPackage"] = "com.tencent.wework"
        # 设置 app 启动页Activity
        caps["appium:appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存
        caps["appium:noReset"] = True
        # 每次初始化driver 强制app重启
        caps["appium:forceAppLaunch"] = True
        # 定义 appium 配置项
        options = AppiumOptions().load_capabilities(caps)
        # options = UiAutomator2Options().load_capabilities(caps)
        # 初始化 driver
        self.driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )
        # 设置全局的隐式等待
        self.driver.implicitly_wait(15)

        return self

    def stop(self):
        '''关闭app'''
        self.driver.quit()

    def goto_main(self):
        '''
        进入 app 首页
        返回首页实例
        '''
        from app_po.page.main_page import MainPage

        return MainPage(self.driver)