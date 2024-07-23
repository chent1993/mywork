# _*_ coding: utf-8 _*_
# @Time : 2024/7/22 21:11 
# @Author : tian
# @File : test_cookie.py
import time
# @desc :







# driver.get("")
# sleep(2)
import yaml
from selenium import webdriver

url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
def test_get_cookie():
    driver = webdriver.Chrome()
    # 保存 cookie
    # 1. 访问企业微信主页/登录页面
    driver.get(url)
    # 2. 等待20s，人工扫码操作
    time.sleep(20)
    # 3. 等成功登陆之后，再去获取cookie信息
    cookie = driver.get_cookies()
    print(cookie)
    # 将 cookie 写入文件
    with open("cookie.yaml", "w") as f:
        yaml.safe_dump(cookie, f)

def test_set_cookie():
    driver = webdriver.Chrome()
    # 使用 cookie 登录
    # 从文件中获取 cookie 信息登陆
    with open("cookie.yaml", "r", encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
    print(f"读取出来的cookie:{cookies}")
    for cookie in cookies:
        try:
            # 添加 cookie
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)
    time.sleep(3)



