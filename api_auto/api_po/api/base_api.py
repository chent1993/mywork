# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:27 
# @Author : tian
# @File : base_api.py
# @desc :
'''
API 基础类
'''
import requests


class BaseApi:
    def send(self,req):
        '''
        发送requests请求
        :return:
        '''
        r = requests.request(**req)
        return r

