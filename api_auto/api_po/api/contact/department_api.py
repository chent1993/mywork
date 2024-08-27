# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 18:33 
# @Author : tian
# @File : department_api.py
# @desc :
import allure
import requests

from api_auto.api_po.api.wework_api import WeworkApi
from api_auto.api_po.utils.log_util import logger


class DepartmentApi(WeworkApi):
    def __init__(self):
        super().__init__()
        #每个模块有自己独立对secret
        # self.corpsecret = 'HZ4jjqlrKMQzhfklDsSKL7qQpjihzYbcM8zP6R6k5BY'
        self.corpsecret = self.data.get("corpsecret").get("contacts")
        self.token = self.get_token(self.corpsecret)

    @allure.step("创建部门")
    def create(self,data):
        '''
        创建部门
        :return:
        '''
        create_url = f'{self.baseurl}/department/create?access_token={self.token}'
        logger.info(f"创建部门：{data}")
        req ={
            "method":"POST",
            "url":create_url,
            "json":data,
            "verify":False
        }
        res = self.send(req)
        # res = requests.post(create_url, json=data, verify=False)
        return res

    @allure.step("更新部门")
    def update(self,data):
        '''
        修改部门
        :return:
        '''

        update_url = f'{self.baseurl}/department/update?access_token={self.token}'
        logger.info(f"修改部门信息：{data}")
        req ={
            "method":"POST",
            "url":update_url,
            "json":data,
            "verify":False
        }
        res = self.send(req)
        # res = requests.post(update_url, json=data, verify=False)
        return res

    @allure.step(f"删除部门{id}")
    def delete(self,id):
        '''
        删除部门
        :return:
        '''
        delete_url = f'{self.baseurl}/department/delete?access_token={self.token}&id={id}'
        logger.info(f"删除部门：{id}")
        req ={
            "method":"GET",
            "url":delete_url,
            # "params":params,
            "verify":False
        }
        res = self.send(req)
        # res = requests.get(delete_url, verify=False)
        return res

    @allure.step(f"获取部门ID{id}")
    def simplelist(self,id):
        '''
        查询子部门ID列表
        :return:
        '''
        simplelist_url = f'{self.baseurl}/department/simplelist?access_token={self.token}&id={id}'
        req ={
            "method":"GET",
            "url":simplelist_url,
            # "params":params,
            "verify":False
        }
        res = self.send(req)
        # res = requests.get(simplelist_url, verify=False)
        logger.info(f"查询结果：{res.text}")
        return res
    def get(self,id):
        '''
        查询具体部门，无权限
        :param id:
        :return:
        '''
        get_url = f'{self.baseurl}/department/get?access_token={self.token}&id={id}'

        res = requests.get(get_url, verify=False)
        logger.info(f"查询结果：{res.text}")
        return res
