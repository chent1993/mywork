# _*_ coding: utf-8 _*_
# @Time : 2024/8/3 20:56 
# @Author : tian
# @File : test_demo.py
# @desc :
from web_po.base.base_page import BasePage


def test_path():
    bp =BasePage()
    print(bp.get_path("aa"))
    bp.screen_image()
    # with open(bp.get_path("image")+"/image_1721961820.PNG", "r", encoding="utf-8") as f:

        # print(f)