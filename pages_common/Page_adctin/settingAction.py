# coding:utf-8
import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.ownPage import OwnPage
from pages_common.Page_ui.settingPage import SettingPage


class SettingAction(BaseAction, OwnPage, SettingPage):

    # 跳转setting页面是否包含 用户协议 隐私协议
    def to_setting(self, type):
        userAgreement = self.get_ele_text(self.userAgreement if type == "ios" else self.userAgreement)
        privacy_agreement = self.get_ele_text(self.privacy if type == "ios" else self.privacy)
        assert userAgreement == "用户协议", privacy_agreement == "隐私协议"

    # 进入用户协议 并包含"软件许可及服务协议"
    def user_agreement(self, type):
        self.click(self.userAgreement if type == "ios" else self.userAgreement)
        txt = self.get_ele_text(self.userAgreementTittle if type == "ios" else self.userAgreementTittle)
        assert txt == "软件许可及服务协议"
        time.sleep(1)
        self.back(type)

    # 进入隐私协议 并包含"隐私政策"
    def privacy_agreement(self, type):
        self.click(self.privacy if type == "ios" else self.privacy)
        txt = self.get_ele_text(self.privacyTitle if type == "ios" else self.privacyTitle)
        assert txt == "隐私政策"
        time.sleep(1)
        self.back(type)

    # 返回
    def back(self, type):
        self.click(self.navi_back if type == "ios" else self.navi_back)

    # 点击清除缓存
    def click_cache(self, type):
        self.click(self.cache if type == "ios" else self.cache)

    # 获取缓存数量
    def get_cache_text(self, type):
        txt = self.get_ele_text(self.desc_1 if type == "ios" else self.desc_1)
        assert txt == "0.00MB"

    # 进入问题反馈
    def click_feedback(self, type):
        self.click(self.feedback if type == "ios" else self.feedback)

    # 输入问题和意见
    def send_massage(self, type, txt):
        self.txt_input(self.input_issue if type == "ios" else self.input_issue, txt)

    # 取消
    def click_cancel(self,type):
        self.click(self.cancel if type == "ios" else self.input_issue)

    # 获取字数
    def get_massage_txt(self, type):
        self.get_ele_text(self.words_count if type == "ios" else self.words_count)

    # 上传图片
    def load_photo(self, type):
        time.sleep(1)
        self.click(self.rv_photo if type == "ios" else self.rv_photo)
        time.sleep(1)
        self.click(self.pictures if type == "ios" else self.pictures)
        time.sleep(1)
        self.click(self.PhotoCapture if type == "ios" else self.PhotoCapture)
        time.sleep(1)
        self.click(self.use_pictures if type == "ios" else self.use_pictures)

    # 输入电话
    def send_phone_number(self, type, phone_number):
        self.txt_input(self.et_input if type == "ios" else self.et_input, phone_number)

    # 提交
    def submit(self, type):
        self.click(self.btn_submit if type == "ios" else self.btn_submit)
