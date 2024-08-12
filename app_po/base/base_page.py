# _*_ coding: utf-8 _*_
# @Time : 2024/8/11 21:18 
# @Author : tian
# @File : base_page.py
# @desc :
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_po.utils.log_util import logger
from app_po.utils.utils import Utils


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find_ele(self,by,locate):
        """
        查找单个元素，并返回元素
        :param by:定位方式
        :param locate:元素定位表达式
        :return:定位到的元素对象
        """
        step_text = f"查找单个元素的定位：{by},{locate}"
        logger.info(step_text)
        ele = self.driver.find_element(
            by,locate
        )
        return ele
    def find_eles(self,by,locate):
        """
        查找多个元素
        :param by:定位方式
        :param locate:元素定位表达式
        :return:定位到的元素对象
        """
        step_text = f"查找多个元素的定位：{by},{locate}"
        logger.info(step_text)
        eles = self.driver.find_elements(
            by,locate
        )
        return eles

    def find_and_click(self,by,locate):
        """
        查找并点击元素
        :param by:定位方式
        :param locate:元素定位表达式
        """
        step_text = f"查找并点击元素：{by},{locate}"
        logger.info(step_text)
        self.find_ele(by,locate).click()

    def find_and_sendKeys(self,by,locate,text):
        """
        查找元素并输入
        :param by:定位方式
        :param locate:元素定位表达式
        :param text:输入的内容
        :return:
        """
        step_text = f"查找元素：{by},{locate},并输入{text}"
        logger.info(step_text)
        self.find_ele(by, locate).send_keys(text)

    def set_implicitly_wait(self, time=1):
        """
        设置隐式等待
        :param time: 隐式等待时间
        """
        logger.info(f"设置隐式等待时间为 {time}")
        self.driver.implicitly_wait(time)

    def wait_ele_located(self, by, value, timeout=10):
        """
        显式等待元素可以被定位
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :param timetout: 等待时间
        :return: 定位到的元素对象
        """
        logger.info(f"显式等待 {by} {value} 出现，等待时间为 {timeout}")
        ele = WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located((by, value))
        )
        return ele

    def wait_ele_click(self, by, value, timeout=10):
        """
        显式等待元素可以被点击
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :param timeout: 等待时间
        """
        logger.info(f"显式等待 {by} {value} 出现，等待时间为 {timeout}")
        ele = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, value))
        )
        return ele

    def wait_for_text(self, text, timeout=5):
        """
        等待某一个文本出现
        """
        logger.info(f"显式等待 {text} 出现，等待时间为 {timeout}")
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda x: x.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
            )
            logger.info(f"{text}元素出现")
            return True
        except:
            logger.info(f"{text}元素未出现")
            return False

    def swipe_window(self):
        """
        滑动界面
        """
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
        """
        滑动查找
        通过文本来查找元素，如果没有找到元素，就滑动，
        如果找到了，就返回元素
        """
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
    def get_toast_tips(self):
        """
         获取 toast 文本
        :return:
        """
        toast_text = self.find_ele(
            AppiumBy.XPATH,
            "//*[@class='android.widget.Toast']"
        ).text
        logger.info(f"获取到的 toast 文本为 {toast_text}")
        return toast_text

    def go_back(self, num=5):
        '''
        执行返回操作
        :param num: 返回的次数
        '''
        logger.info(f"点击返回按钮 {num + 1} 次")
        for i in range(num):
            self.driver.back()

    def screenshot(self):
        '''
        截图
        :param path: 截图保存路径
        '''
        file_path = Utils.save_source_datas("images")
        # 截图
        self.driver.save_screenshot(file_path)
        logger.info(f"截图保存的路径为{file_path}")
        # 返回保存图片的路径
        return file_path

    def save_page_source(self):
        '''
        保存页面源码
        :return: 返回源码文件路径
        '''
        file_path = Utils.save_source_datas("pagesource")
        # 写 page source 文件
        with open(file_path, "w", encoding="u8") as f:
            f.write(self.driver.page_source)
        logger.info(f"源码保存的路径为{file_path}")
        # 返回 page source 保存路径
        return file_path
