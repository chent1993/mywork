# _*_ coding: utf-8 _*_
# @Time : 2024/8/1 21:53 
# @Author : tian
# @File : test_add_member.py
# @desc :
import allure
from faker import Faker

from web_po.pages.login_page import LoginPage

@allure.suite("企业微信后台管理")
@allure.sub_suite("添加成员管理模块")
class TestAddMember:
    def setup_class(self):
        self.login=LoginPage()

    def teardown_class(self):
        ...
        # 关闭浏览器
        # self.login.close_brower()

    @allure.title("添加成员成功")
    @allure.description("输入正确的成员信息，添加成功")
    def test_add_member_success(self):
        """添加成员成功"""
        self.fake = Faker("zh_CN")
        name = self.fake.name()
        # name = "haha"
        mid = self.fake.uuid4()
        phone = self.fake.phone_number()
        res = self.login.login().goto_contact().goto_add_member().add_member_success(name=name,accid=mid,phone=phone).get_user_info()

        assert name in res

    @allure.title("添加成员失败")
    @allure.description("输入重复的成员信息，添加失败")
    def test_add_member_fail(self):
        """添加成员失败"""
        self.fake = Faker("zh_CN")
        name = self.fake.name()

        mid = self.fake.uuid4()
        phone = self.fake.phone_number()
        self.login.login().goto_contact().goto_add_member().add_member_success(name=name, accid=mid,
                                                                                     phone=phone).get_user_info()
        mname = self.fake.name()
        tips = self.login.login().goto_contact().goto_add_member().add_member_fail(name=mname, accid=mid,
                                                                               phone=phone)

        expected = f"该账号已被“{name}”占有"

        assert tips == expected
        res = self.login.login().goto_contact().get_user_info()
        assert mname not in res


