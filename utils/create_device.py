# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 5:04 下午
# @Author  : jinxu
# @File    : create_device.py

import json
import os

import requests
from ayla_public.mylog import Log
from ayla_public.public import get_pathfile


class CreatDevice:
    def __init__(self):
        self.base_url = "https://ads-dev.ayla.com.cn"
        self.log = Log()
        self.cookie = self.get_cookie()
        self.token = self.get_token(self.cookie)
        self.header = {"Content-Type": "application/json", "Authorization": "auth_token " + self.token}
        self.v_device_path = os.path.join(get_pathfile(), "config/device_info.py")

    def get_cookie(self):
        sessions_url = 'https://dashboard-dev.sunseaiot.com/sessions'
        data = 'email=liujun%2Bcndev%40aylaasia.om&password=Test123456'
        self.log.info(sessions_url)
        req = requests.request(method="post", url=sessions_url, data=data, verify=False).headers
        self.log.info(req)
        cookie = req.get("Set-Cookie")
        return cookie

    def get_token(self, cookie):
        token_url = 'https://dashboard-dev.sunseaiot.com/credentials'
        header = {"content-type": "application/json;charset=UTF-8", "cookie": cookie}
        self.log.info(token_url)
        req = requests.request(method="get", url=token_url, headers=header, verify=False).json()
        self.log.info(req)
        auth_token = req.get("auth_token")
        return auth_token

    def creat_devic(self, product_name="", oem_model=""):
        '''创建虚拟设备'''
        creat_device_url = self.base_url + "/deviceservice/v1/virtual_devices.json?env=ssct"
        data = {"oem": "3c75973b", "role": "OEM::Admin", "product_name": product_name, "oem_model": oem_model}
        res = requests.request(method='post', url=creat_device_url, data=json.dumps(data), headers=self.header).json()
        self.log.info(creat_device_url)
        self.log.info(res)
        dsn = res["device"]["dsn"]
        return dsn

    def get_telement_id(self, telement_name):
        '''获取模版id'''
        tement_url = self.base_url + "/apiv1/templates?env=ssct&admin_view=true&full_view=true"
        res = requests.get(url=tement_url, headers=self.header).json()
        self.log.info(tement_url)
        for telement in res:
            if telement["template"]["name"] == telement_name:
                return telement["template"]["id"]

    def get_dsn_id(self, dsn):
        '''获取设备id'''
        device_id_url = self.base_url + f"/apiv1/dsns/{dsn}.json?env=ssct"
        res = requests.request(method='get', url=device_id_url, headers=self.header).json()
        self.log.info(device_id_url)
        self.log.info(res)
        vd_id = res["device"]["id"]
        return vd_id

    def set_telement(self, vd_id, template_id):
        '''设置模版'''
        set_telement_url = self.base_url + f'/apiv1/devices/{vd_id}/template/{template_id}.json?env=ssct'
        data = {"device_id": vd_id, "template_id": template_id}
        res = requests.request(method="put", data=json.dumps(data), headers=self.header, url=set_telement_url)
        self.log.info(set_telement_url)
        self.log.info(res)

    def unregister(self, vd_id):
        '''注销'''
        url = self.base_url + f'/apiv1/devices/{vd_id}/unregister.json?env=ssct'
        res = requests.request(method="put", headers=self.header, url=url).content
        self.log.info(url)
        self.log.info(res)

    def get_properties_version(self, vd_id, oem_model):
        '''获取设备版本'''
        url = self.base_url + f'/apiv1/devices/{vd_id}/properties.json?env=ssct'
        res = requests.request(method='get', url=url, headers=self.header).text
        self.log.info(url)
        self.log.info(res)
        res = json.loads(res)
        for data in res:
            test_data = data["property"]
            if oem_model == "IR0-01-0-001":
                version_name = "version"
            else:
                version_name = '1:0x0000:version'
            if test_data["name"] == version_name:
                version_id = test_data["key"]
                return version_id

    def device_online(self, vd_id):
        '''设备上线'''
        url = self.base_url + f'/apiv1/devices/{vd_id}/connection_history.json'
        data = {"connection": {"event_time": "2021-12-14 3:36:31.671141", "status": "Online"}}
        res = requests.request(method='post', url=url, data=json.dumps(data), headers=self.header).text
        self.log.info(url)
        self.log.info(res)

    def san_lan(self, vd_id):
        '''修改注册属性'''
        url = self.base_url + f'/apiv1/devices/{vd_id}?env=ssct'
        data = {"device": {"id": vd_id, "registration_type": "Same-LAN", "jobStatus": {"status": "None"}}}
        res = requests.request(method='put', url=url, data=json.dumps(data), headers=self.header)
        self.log.info(url)
        self.log.info(res)

    def ayla_device_create(self, product_name, oem_model, template_id):
        '''添加虚拟设备'''
        dsn = self.creat_devic(product_name=product_name, oem_model=oem_model)
        vd_id = self.get_dsn_id(dsn)
        self.set_telement(vd_id, template_id)
        self.device_online(vd_id)
        self.san_lan(vd_id)
        self.log.info("创建成功")
        return dsn

    def get_device_list(self, counter):
        '''艾拉云虚拟设备列表'''
        url = self.base_url + f"/apiv1/devices.json?env=ssct&%5Bfilter%5D%5Bdirection%5D=desc&%5Bfilter%5D%5Border%5D=desc&%5Bfilter%5D%5Border_by%5D=dsn&%5Bfilter%5D%5Bsort_by%5D=dsn&direction=desc&order=desc&order_by=dsn&page=1&paginated=true&per_page={counter}&sort_by=dsn&virtual=true"
        res = requests.get(url=url, headers=self.header).json()
        return res["devices"]

    def write_device_info(self, device_info):
        '''将虚拟设备按格式写入json文件'''
        dsn_info = {}
        for info in device_info:
            product_name = info["device"]["product_name"]
            if product_name.endswith("jx1") and not product_name.startswith("米兰") and info["device"][
                'oem_model'] != "IR0-01-0-001":
                dsn_info[product_name] = info["device"]["dsn"] + ":" + info["device"]['oem_model']
                dsn_info[info["device"]['oem_model']] = {
                    "product_name": '虚拟设备-' + product_name,
                    "code": 0,
                    "msg": "success",
                    "data": [
                        {
                            "deviceId": info["device"]["dsn"],
                            "cuId": 0
                        }
                    ]
                }
        with open(self.v_device_path, 'w', encoding='utf-8') as f:
            json.dump(dsn_info, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    # from bind_device import token, bind_device
    '''ZB-NODE-SW0-004	node_onoff_004_for_qa'''
    # a = CreatDevice()
    # template_id = a.get_telement_id("node_onoff_004_for_qa")
    # b = a.ayla_device_create(oem_model="ZB-NODE-SW0-004", product_name="罗马四路智能面板jx1", template_id=template_id)
    # print(b)
    # a.device_online(16055857)
    # device_info = a.get_device_list(30)
    # a.write_device_info(device_info)
    # print(device_info)
    # error_device = []
    # for info in device_info:
    #     key = info["device"]["key"]
    #     a.unregister(key)
    #     res = bind_device(token,deviceId=info["device"]["dsn"],deviceCategory=info["device"]["oem_model"])
    #     if res["code"] !=0:
    #         error_device.append({'deviceId': info["device"]["dsn"],"msg":res["msg"]})
    # print(error_device)
    # print(len(error_device))
