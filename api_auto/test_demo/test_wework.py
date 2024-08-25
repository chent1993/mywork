# _*_ coding: utf-8 _*_
# @Time : 2024/8/24 09:43 
# @Author : tian
# @File : test_wework.py
# @desc :
import pytest
import requests
class TestWework:


    def setup_class(self):
        corpid = 'wwdbab80f3359105f4'
        corpsecret = 'HZ4jjqlrKMQzhfklDsSKL7qQpjihzYbcM8zP6R6k5BY'
        self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin'

        url = f'{self.baseurl}/gettoken'
        params = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }
        res = requests.get(url=url, params=params, verify=False)

        self.access_token = res.json()['access_token']





    def test_get_token(self):

        corpid = 'wwdbab80f3359105f4'
        corpsecret = 'HZ4jjqlrKMQzhfklDsSKL7qQpjihzYbcM8zP6R6k5BY'

        url = f'{self.baseurl}/gettoken'
        params = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }
        res = requests.get(url=url, params=params, verify=False)
        assert res.status_code == 200

    @pytest.mark.parametrize(
        "name, parentid",
        [("test1",2),
         ("test2", 2)
        ]
    )
    def test_create_department(self,name,parentid):
        # print(self.access_token)

        url =f'{self.baseurl}/department/create?access_token={self.access_token}'
        data={
         "name": name,
        "parentid": parentid,
        # "name_en": "RDGZ",
        # "order": 1,
        # "id": 2
        }
        res = requests.post(url,json=data,verify=False)
        print(res.text)
        assert res.status_code == 200
        # 断言接口响应体
        assert res.json().get("errcode") == 0




