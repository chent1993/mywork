# _*_ coding: utf-8 _*_
# @Time : 2024/8/8 22:00 
# @Author : tian
# @File : test_wework_contact.py
# @desc :
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
# from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker
from selenium.common import NoSuchElementException


class TestWeWorkContact:
    def setup_class(self):
        """准备测试数据"""
        fake = Faker("zh_CN")
        self.name =fake.name()
        self.phone = fake.phone_number()

    def setup_method(self):
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
        print(caps)
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




    def teardown_method(self):
        """关闭driver"""
        self.driver.quit()

    def test_search_contact(self):
        """搜索存在的联系人"""
        search_key = "白辉"
        #点击 通讯录
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='通讯录']"
        ).click()
        #点击搜索框
        self.driver.find_element(
            AppiumBy.XPATH, "//*[@text='测试6部']/../../../following-sibling::*/*[1]"
        ).click()
        #搜索框输入搜索关键词
        self.driver.find_element(
            AppiumBy.XPATH, "//*[@text='搜索']"
        ).send_keys(search_key)
        #获取搜索结果
        eles = self.driver.find_elements(
            AppiumBy.XPATH,"//*[@class='androidx.recyclerview.widget.RecyclerView']//*[@class='android.view.ViewGroup']/*/*"
        )

        results = [ele.text for ele in eles]
        print(f"搜索结果{results}")

        #断言
        assert search_key in results

    def test_add_contact(self):
        """
        添加成员冒烟用例
        1、点击 通讯录 按钮
        2、点击 添加成员 按钮
        3、点击 手动添加成员 按钮
        4、填写 姓名，手机号 保存 按钮
        5、验证出现添加成功的信息
        """

        #点击 通讯录
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='通讯录']"
        ).click()
        #点击 添加成员
        # self.driver.find_element(
        #     AppiumBy.XPATH,"//*[@text='添加成员']"
        # ).click()
        # 滑动点击添加成员按钮
        self.swipe_find("添加成员").click()
        #点击 手动添加成员
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='手动输入添加']"
        ).click()
        #输入姓名
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='必填']"
        ).send_keys(self.name)
        #输入手机号
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='手机']/..//*[@text='选填']"
        ).send_keys(self.phone)
        #点击保存
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='保存']"
        ).click()
        tips = self.driver.find_element(
            AppiumBy.XPATH,
            "//*[@class='android.widget.Toast']").text
        assert "添加成功" == tips

    def swipe_window(self):
        '''
        滑动界面
        '''
        # 滑动操作
        # 获取设备的尺寸
        size = self.driver.get_window_size()
        # {"width": xx, "height": xx}
        print(f"设备尺寸为 {size}")
        width = size.get("width")
        height = size.get('height')
        # # 获取滑动操作的坐标值
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.2
        # swipe(起始x坐标，起始y坐标，结束x坐标，结束y坐标，滑动时间（单位毫秒）)
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

    def swipe_find(self, text, max_num=5):
        '''
        滑动查找
        通过文本来查找元素，如果没有找到元素，就滑动，
        如果找到了，就返回元素
        '''
        # 为了滑动操作更快速，不用等待隐式等待设置的时间
        self.driver.implicitly_wait(1)
        for num in range(max_num):
            try:
                # 正常通过文本查找元素
                ele = self.driver.find_element(
                    AppiumBy.XPATH,
                    f"//*[@text='{text}']"
                )
                print("找到元素")
                # 能找到则把隐式等待恢复原来的时间
                self.driver.implicitly_wait(15)
                # 返回找到的元素对象
                return ele
            except Exception:
                # 当查找元素发生异常时
                print(f"没有找到元素，开始滑动")
                print(f"滑动第{num + 1}次")
                # 滑动操作
                self.swipe_window()
        # 把隐式等待恢复原来的时间
        self.driver.implicitly_wait(15)
        # 抛出找不到元素的异常
        raise NoSuchElementException(f"滑动之后，未找到 {text} 元素")

