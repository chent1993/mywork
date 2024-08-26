# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:29 
# @Author : tian
# @File : wework_api.py
# @desc :
import requests

from api_auto.api_po.api.base_api import BaseApi
from api_auto.api_po.conftest import global_env
from api_auto.api_po.utils.utils import Utils


class WeworkApi(BaseApi):
    def __init__(self):
        # self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin'
        # self.corpid = 'wwdbab80f3359105f4'
        self.data = self.get_config()
        self.baseurl =self.data.get("baseurl")
        self.corpid =self.data.get("corpid").get("test")


    def get_token(self,corpsecret):
        '''
        获取企业微信 access_token
        :return:
        '''



        url = f'{self.baseurl}/gettoken'
        params = {
            'corpid': self.corpid,
            'corpsecret': corpsecret
        }
        req ={
            "method":"GET",
            "url":url,
            "params":params,
            "verify":False
        }
        res = self.send(req)

        access_token = res.json()['access_token']
        return access_token

    def get_config(self):
        '''
        获取配置
        :return:
        '''
        file_path = f"{Utils.get_root_path()}/../config/{global_env.get('env')}.yaml"
        yaml_data = Utils.get_yaml_data(file_path)
        print(yaml_data)
        return yaml_data
