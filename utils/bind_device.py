# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 5:04 下午
# @Author  : jinxu
# @File    : bind_device.py

import json
from ayla_public.mylog import logger

import requests


def get_app_token():
    user = '13389458789'
    pwd = '123456'
    login_data = {
        "account": user,
        "password": pwd
    }
    login_url = "https://abp-test.ayla.com.cn/api/v1/miya/user/passwordlogin"
    header = {"content-type": "application/json", "loginsource": "5"}
    print(json.dumps(login_data))
    res = requests.request(method="post", url=login_url, data=json.dumps(login_data), headers=header).json()
    token = res["data"]["authToken"]
    return token


def bind_device(token, deviceId, deviceCategory, nickName, url_type="ord"):
    ord_url = "https://abp-test.ayla.com.cn/api/v1/device/bind"
    new_url = "https://abp-test.ayla.com.cn/api/v1/miya/device/bind/batch"
    ord_data = {'scopeId': 1379256462408597535, 'cuId': 0, 'deviceId': deviceId, 'scopeType': 2,
                'nickName': nickName,
                'deviceCategory': deviceCategory, 'deviceName': '"罗马烟雾报警器jx1":', 'pid': 'ZBACP-A000003'}
    new_data = {'deviceInfoMaps': [{'scopeId': 1379256462408597535, 'cuId': 0, 'deviceId': deviceId,
                                    'pid': 'ZBOAC-A000001', 'deviceName': '罗马新风面板', 'scopeType': 2,
                                    'nickName': nickName,
                                    'deviceCategory': deviceCategory}]}
    if url_type == 'ord':
        url = ord_url
        data = ord_data
    else:
        url = new_url
        data = new_data

    header = {"content-type": "application/json", "loginsource": "5", "authorization": token,
              "homeid": "1379256462408597535"}
    logger.info(data)
    logger.info(url)
    res = requests.post(url=url, data=json.dumps(data), headers=header).json()
    logger.info(res)
    return res


token = get_app_token()

if __name__ == '__main__':
    res = bind_device(token, "VD3c75973b0000760", "ZB-NODE-SW0-004", "虚拟设备-罗马四路智能面板jx1", url_type="1")
