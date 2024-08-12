# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 21:18 
# @Author : tian
# @File : base_page.py
# @desc :
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver



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
