
import traceback

import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.utils.log_util import logger

# 弹窗黑名单
black_list = [
    (AppiumBy.XPATH, "//*[@text='确定']"),
    (AppiumBy.XPATH, "//*[@text='取消']"),
    (AppiumBy.XPATH, "//*[@text='马上升级']")
]


# 传入的 fun 相当于 find_ele(self, by, value): 方法
def black_wrapper(fun):
    def run(*args, **kwargs):
        # basepage 相当于传入的第一个参数 self
        basepage = args[0]
        try:
            logger.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:
            logger.warning("未找到元素，处理异常")
            # 遇到异常截图
            # 获取当前工具文件所在的路径
            image_path = basepage.screenshot()
            allure.attach.file(
                image_path,
                name="查找元素异常截图",
                attachment_type=allure.attachment_type.PNG
            )
            # 保存页面源码
            pagesource_path = basepage.save_page_source()
            allure.attach.file(
                pagesource_path,
                name="page_source",
                attachment_type=allure.attachment_type.TEXT
            )

            for b in black_list:
                # 设置隐式等待时间为 1 s
                basepage.set_implicitly_wait()
                #  查找黑名单中的每一个元素
                eles = basepage.driver.find_elements(*b)
                if len(eles) > 0:
                    # 点击弹框
                    basepage.driver.find_elements(*b)[0].click()
                    # 恢复隐式等待设置
                    basepage.set_implicitly_wait(15)
                    # 继续查找元素
                    return fun(*args, **kwargs)
            logger.error(f"遍历黑名单，仍未找到元素，异常信息为 ====> {e}")
            logger.error(f"traceback.format_exc() 信息为 ====> {traceback.format_exc()}")
            raise e
    return run
