import allure

from api_auto.api_po.api.wework_api import WeworkApi
from api_auto.api_po.utils.log_util import logger


class MemberApi(WeworkApi):
    def __init__(self):
        super().__init__()
        #每个模块有自己独立对secret
        # self.corpsecret = 'HZ4jjqlrKMQzhfklDsSKL7qQpjihzYbcM8zP6R6k5BY'
        self.corpsecret = self.data.get("corpsecret").get("contacts")
        self.token = self.get_token(self.corpsecret)
    def list_id(self):
        '''
        获取成员ID列表
        :return:
        '''
        listid_url = f'{self.baseurl}/user/list_id?access_token={self.token}'
        # data={
        #     "cursor": "xxxxxxx",
	    #     "limit": 10000}
        req = {
            "method": "POST",
            "url": listid_url,
            # "json":data,
            "verify": False
        }
        res = self.send(req)
        # res = requests.get(simplelist_url, verify=False)
        logger.info(f"查询结果：{res.text}")
        return res

    @allure.step("创建成员")
    def create(self,data):
        '''
        创建部门
        :return:
        '''
        create_url = f'{self.baseurl}/user/create?access_token={self.token}'
        logger.info(f"创建成员：{data}")
        req ={
            "method":"POST",
            "url":create_url,
            "json":data,
            "verify":False
        }
        res = self.send(req)
        # res = requests.post(create_url, json=data, verify=False)
        return res