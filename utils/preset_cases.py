# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 11:28 上午
# @Author  : jinxu
# @File    : preset_cases.py
import json
import os

import requests

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from ayla_public.mylog import logger


class PresetCases:

    def __init__(self):
        self.username = ReadConfig().get_login_massage("userName")
        self.password = ReadConfig().get_login_massage("passWord")
        self.base_url = ReadConfig().get_ayal_url("base_url")

    def get_app_token(self):
        login_data = {
            "account": self.username,
            "password": self.password
        }
        login_url = self.base_url + "/api/v1/miya/user/passwordlogin"
        header = {"content-type": "application/json", "loginsource": "5"}
        print(json.dumps(login_data))
        res = requests.request(method="post", url=login_url, data=json.dumps(login_data), headers=header).json()
        self.token = res["data"]["authToken"]
        return self.token

    def creat_family(self):
        url = self.base_url + '/api/v1/miya/home'
        header = {"content-type": "application/json", "loginsource": "5", "authorization": self.token}
        data = {
            "roomNameList": ["客厅", "主卧", "次卧", "厨房", "餐厅"],
            "homeName": "自动化添加家庭",
            "homeLocation": ""
        }
        ret = requests.post(url=url, data=json.dumps(data), headers=header).json()
        return ret

    def get_family(self):
        url = self.base_url + '/api/v1/miya/home'
        header = {"content-type": "application/json", "loginsource": "5", "authorization": self.token}
        ret = requests.get(url=url, headers=header).json()
        return ret

    def delete_family(self, homeId):
        url = self.base_url + '/api/v1/miya/home/{}'.format(homeId)
        header = {"content-type": "application/json", "loginsource": "5", "authorization": self.token, "homeid": homeId}
        ret = requests.delete(url=url, headers=header).json()
        return ret

    def bind_batch(self, homeId):
        device_info_path = os.path.join(get_pathfile(), "config/preset_device_info.json")
        url = self.base_url + '/api/v1/miya/device/bind/batch'
        header = {"content-type": "application/json", "loginsource": "5", "authorization": self.token,
                  "homeid": homeId}
        with open(device_info_path) as f:
            data = dict(json.loads(f.read()))
            for k, v in data.items():
                deviceId, deviceCategory, pid = v.split(':')
                bind_data = {'deviceInfoMaps': [
                    {'scopeId': homeId, 'cuId': 0, 'deviceId': deviceId, 'pid': pid, 'deviceName': k, 'scopeType': 2,
                     'nickName': k, 'deviceCategory': deviceCategory}]}
                logger.info(bind_data)
                logger.info(url)
                ret = requests.post(url=url, data=json.dumps(bind_data), headers=header).json()
                logger.info(ret)

if __name__ == '__main__':
    a = PresetCases()
    b = a.get_app_token()
    c= a.get_family()
    a.bind_batch("1498486897992069212")
    print(c)