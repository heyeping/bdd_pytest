# coding:utf-8
# @Time   :2022/2/16 15:58
# @Author :Nicholas.liu
# @File   :memberAction.py
# @Software   :bbd_test

import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.memberPage import MemberPage
import requests
import json


class MemberAction(BaseAction, MemberPage):

    def click_add_member_btn(self, type):
        self.click(self.add_member_btn if type == "ios" else self.add_member_btn)

    def click_add_account_btn(self, type):
        self.click(self.account_btn if type == "ios" else self.account_btn)

    def ipuntIphoneNo(self, type):
        self.txt_input(self.phoneNo if type == "ios" else self.phoneNo, "15885537820")
        self.click(self.next_btn if type == "ios" else self.next_btn)

    def saveBtn(self, type):
        self.click(self.save_member if type == "ios" else self.save_member)

    # 校验添加成员信息
    def check_member(self, type):
        phoneObj = self.find_my_elements(self.check_phoneNo if type == "ios" else self.check_phoneNo)
        value = phoneObj[1].get_attribute("value")
        assert value == '15885537820'

    # 点击指定的成员信息-进行成员详情界面
    def query_member_info(self, type):
        time.sleep(1)
        phoneObj = self.find_my_elements(self.check_phoneNo if type == "ios" else self.check_phoneNo)[0]
        time.sleep(1)
        phoneObj.click()
        time.sleep(1)

    # 点击成员备注名
    def set_memeber_name(self, type):
        self.click(self.memeber_name if type == "ios" else self.memeber_name)

    # 输入成员备注名并确定
    def send_memeber_new_name(self, type, txt):
        self.txt_input(self.input_button if type == "ios" else self.input_button, txt)
        self.click(self.is_ok if type == "ios" else self.is_ok)

    # 校验备注修改
    def check_new_name(self, type):
        ele = self.find_my_elements(self.tv_title if type == "ios" else self.tv_title)[0]
        return ele.get_attribute('value')

    def queryInfo(self, type):
        phoneObj = self.find_my_elements(self.check_phoneNo if type == "ios" else self.check_phoneNo)
        value = phoneObj[0].get_attribute("value")
        assert value == '15802824470'

    def deleteMember(self, type):
        # tableObj = self.find_my_elements(self.memeber_table if type == "ios" else self.memeber_table)
        self.drag(0.5, 100, 0, 1, 0, self.find_my_element(self.memeber_table if type == "ios" else self.memeber_table))
        time.sleep(2)
        self.click(self.delete_member if type == "ios" else self.delete_member)

    # 核查删除后
    def check_delete_member_result(self, type):
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.Session()
        session.keep_alive = False
        url = "https://abp-test.ayla.com.cn/api/v1/miya/user/passwordlogin"

        payload = "{\n\"password\": \"123abc\",\n\"account\": \"15802824470\"\n}"
        headers = {
            'loginSource': '5',
            'Content-Type': 'application/json'
        }
        response = session.request("POST", url, headers=headers, data=payload)
        newDic = json.loads(response.text)
        for i in newDic["data"]["homeList"]:
            if i["homeName"] == "自动化添加家庭":
                assert 1 == 1
            else:
                assert 1 == 0

