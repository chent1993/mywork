# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:37 
# @Author : tian
# @File : contact_page.py
# @desc :
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_po.base.base_page import BasePage


class ContactPage(BasePage):
    """通讯录页面"""

    def goto_add_member(self):
        """进入添加成员页面"""
        # 等待成员列表加载完毕
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located((By.ID, "member_list"))
        )
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()

        from web_po.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_user_info(self):
        """获取成员信息"""
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "member_list"))
        )
        # 定位
        names = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for n in names:
            name_list.append(n.text)
        return name_list