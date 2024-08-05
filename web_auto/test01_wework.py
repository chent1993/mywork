# _*_ coding: utf-8 _*_
# @Time : 2024/7/22 20:36 
# @Author : tian
# @File : test01_wework.py
# @desc :作业-添加成员
import time

import allure
import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.screen_utils import ScreenUtil


# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

@allure.suite("企业微信web端")
@allure.sub_suite("通讯录模块")
class TestWeWork:

    def setup_class(self):
        # 初始化driver
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(15)

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 使用 cookie 登录
        # 从文件中获取 cookie 信息登陆
        # with open("cookie.yaml", "r", encoding="utf-8") as f:
        with open("web_auto/cookie.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            try:
                # 添加 cookie
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)
        self.driver.refresh()

    def teardown_class(self):
        ...
        # 关闭浏览器
        self.driver.quit()



    @allure.title("添加成员成功")
    def test_add_member_success(self):
        """
        添加通讯录成员
        :return:
        """
        self.fake = Faker("zh_CN")
        with allure.step("点击通讯录按钮"):
            self.driver.find_element(By.ID,"menu_contacts").click()
        with allure.step("点击添加成员按钮"):
            # 等待成员列表加载完毕
            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.ID, "member_list"))
            )
            self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
        with allure.step("准备测试数据"):
            name = self.fake.name()
            self.driver.find_element(By.ID,"username").send_keys(name)
        with allure.step("输入账号"):
            mid = self.fake.uuid4()
            self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(mid)
        with allure.step("输入手机号"):
            phone = self.fake.phone_number()
            self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)

        with allure.step("保存"):
            self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        with allure.step("断言添加结果"):
            # 获取成员列表信息
            # 等待成员列表加载完毕
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "member_list"))
            )
            # 定位
            names = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            name_list = []
            for n in names:
                name_list.append(n.text)
                # ScreenUtil.get_screen()
            ScreenUtil().get_screen(self.driver)
            # 断言新添加成员姓名在列表中
            assert name in name_list

    @allure.title("添加成员失败")
    def test_add_member_fail(self):
        """
        添加通讯录成员
        :return:
        """
        self.fake = Faker("zh_CN")
        with allure.step("点击通讯录按钮"):
            self.driver.find_element(By.ID,"menu_contacts").click()
        with allure.step("点击添加成员按钮"):
            # 等待成员列表加载完毕
            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.ID, "member_list"))
            )
            self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
        with allure.step("准备测试数据"):
            name = self.fake.name()
            self.driver.find_element(By.ID,"username").send_keys(name)
        with allure.step("输入账号"):
            mid = self.fake.uuid4()
            self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(mid)
        with allure.step("输入手机号"):
            phone = self.fake.phone_number()
            self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)

        with allure.step("保存"):
            self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        with allure.step("点击添加成员按钮"):
            # 等待成员列表加载完毕
            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.ID, "member_list"))
            )
            self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
        with allure.step("准备测试数据"):
            mname = self.fake.name()
            self.driver.find_element(By.ID,"username").send_keys(mname)
        with allure.step("输入账号"):
            self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(mid)
        with allure.step("输入手机号"):
            self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)
        with allure.step("保存"):
            self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        with allure.step("断言添加成员失败，账号被占用"):

            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".ww_inputWithTips_WithErr"))
            )
            tip_ele = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]/following-sibling::*[1]')
            tips = tip_ele.text
            expected = f"该账号已被“{name}”占有"
            ScreenUtil().get_screen(self.driver)
            # 断言
            assert tips == expected

        with allure.step("取消"):
            self.driver.find_element(By.CSS_SELECTOR,".js_btn_cancel").click()

        #公司电脑无此步骤，奇怪
        with allure.step("离开此页"):
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@node-type='cancel']"))).click()


        with allure.step("断言列表中不存在重复账号"):
            # 获取成员列表信息
            # 等待成员列表加载完毕
            WebDriverWait(self.driver, 15).until(
                expected_conditions.element_to_be_clickable((By.ID, "member_list"))
            )
            # 定位
            names = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            name_list = []
            for n in names:
                name_list.append(n.text)
            ScreenUtil().get_screen(self.driver)
            # 断言新添加成员姓名在列表中
            assert mname not in name_list



