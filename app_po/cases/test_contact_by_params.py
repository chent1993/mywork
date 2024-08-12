# _*_ coding: utf-8 _*_
# @Time : 2024/8/12 21:44 
# @Author : tian
# @File : test_contact_by_params.py
# @desc :
import allure
import pytest

from app_po.base.wework_app import WeworkApp
from app_po.utils.log_util import logger
from app_po.utils.utils import Utils


def get_member_info():
    '''
    读取添加成员测试数据
    :return:
    '''
    # mac 用 /，win \\
    yaml_path = Utils.get_file_path("datas/members_info.yaml")
    yaml_data = Utils.get_yaml_data(yaml_path)
    # 获取成员信息数据
    datas = yaml_data.get("member_info")
    logger.info(f"获取到的成员数据为 {datas}")
    return datas


@allure.feature("企业微信联系人操作")
class TestContactByParams:


    def setup_method(self):
        '''实例化 app'''
        self.app =WeworkApp()
        #启动app，进入首页
        self.main = self.app.start().goto_main()

    def teardown_method(self):
        self.app.stop()

    @allure.story("添加成员")
    @allure.title("参数化添加成员：姓名 {name}, 手机号 {phone}")
    @pytest.mark.parametrize(
        "name, phone",
        get_member_info()
    )
    def test_add_member(self,name,phone):
        '''
        添加成员冒烟用例
        1、点击 通讯录 按钮
        2、点击 添加成员 按钮
        3、点击 手动添加成员 按钮
        4、填写 姓名，手机号 保存 按钮
        5、验证出现添加成功的信息
        :return:
        '''
        tips = self.main.goto_address_list_page()\
            .goto_add_member_page()\
            .goto_menual_input_page()\
            .quick_input_member(name,phone).get_tips()

        assert "添加成功" ==tips
