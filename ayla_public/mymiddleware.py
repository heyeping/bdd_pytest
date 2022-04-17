# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 5:04 下午
# @Author  : jinxu
# @File    : mymiddleware.py

import json
import os.path, sys
import re

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

from mitmproxy import http

from ReadConfig import ReadConfig
from public import get_pathfile
from mylog import logger


class MyMiddleware:
    def __init__(self):
        readconfig = ReadConfig()
        self.base_url = readconfig.get_ayal_url("base_url")
        self.bind_batch_url = readconfig.get_ayal_url("bind_batch_url")
        self.deviceCategory = ""
        self.deviceId = ""
        self.nickName = ""
        self.device_path = os.path.join(get_pathfile(), "config/device_info.json")
        self.headers = {"Content-Type": "application/json"}

    def response(self, flow: http.HTTPFlow):
        url = re.search("/api/v1/miya/device/.*?/candidates/", flow.request.pretty_url)
        logger.info(flow.request.pretty_url)
        if url:
            if flow.request.pretty_url.startswith(self.base_url + url.group()):
                self.deviceCategory = flow.request.pretty_url.split("/")[-1]
                with open(self.device_path) as f:
                    data = dict(json.loads(f.read()))
                    request_info = data.get(self.deviceCategory)
                    if request_info:
                        self.deviceId = request_info["data"][0]["deviceId"]
                        self.nickName = request_info["product_name"]
                        logger.info(request_info)
                        flow.response = http.Response.make(200, json.dumps(request_info).encode(), self.headers)
                    else:
                        logger.info(f'没有该oem: {self.deviceCategory} 虚拟设备')

        if flow.request.pretty_url.startswith(self.base_url + self.bind_batch_url):
            data = {
                "code": 0,
                "msg": "success",
                "data": {
                    "failed": [],
                    "success": [self.deviceId]
                }
            }
            logger.info(flow.request.pretty_url)
            logger.info(data)
            flow.response = http.Response.make(200, json.dumps(data).encode(), self.headers)

    def request(self, flow: http.HTTPFlow):
        if flow.request.pretty_url.startswith(self.base_url + self.bind_batch_url):
            data = json.loads(flow.request.content)
            data["deviceInfoMaps"][0]["deviceId"] = self.deviceId
            data["deviceInfoMaps"][0]["nickName"] = self.nickName
            flow.request.content = json.dumps(data).encode()
            logger.info(flow.request.pretty_url)
            logger.info(data)


addons = [
    MyMiddleware()
]
