import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.log_utils import logger


class TestDataRecord:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_log_data_record(self):
        '''
        日志
        debug记录步骤信息
        info记录关键信息，比如断言等
        :return:
        '''
        search_content = "霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID,"query").send_keys(search_content)
        logger.debug(f"搜索的内容是：{search_content}")
        self.driver.find_element(By.CSS_SELECTOR,"#stb").click()
        time.sleep(3)
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"搜索结果为{search_res.text}")
        assert search_res.text == search_content

    def test_screen_shot_data_record(self):
        search_content = "霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的内容是：{search_content}")
        self.driver.find_element(By.CSS_SELECTOR, "#stb").click()
        time.sleep(3)
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"搜索结果为{search_res.text}")
        #截图记录，双重保障
        '''
        断言页面
        重要的业务场景页面
        容易出错的页面
        '''
        self.driver.save_screenshot("search_res.png")
        assert search_res.text == search_content

    def test_page_source_data_record(self):
        '''
        使用page_source属性获取页面源码
        在调试过程中，如果有找不到元素的错误可以保存当时的page_source调试代码
        :return:
        '''
        search_content = "霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        self.driver.find_element_by_id()
        #获取page_source
        with    open("record.html","w",encoding="u8") as f:
            f.write(self.driver.page_source)