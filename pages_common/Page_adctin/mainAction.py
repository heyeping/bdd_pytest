# coding:utf-8
import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.inteligencePage import Intelligence
from pages_common.Page_ui.ownPage import OwnPage
from pages_common.Page_ui.settingPage import SettingPage


# 底部导航栏
class MainAction(BaseAction, OwnPage, Intelligence):

    # 点击元素 我的
    def clickOwn(self, type):
        self.click(self.own if type == "ios" else self.own)

    def clickRoom(self, type):
        '''
        点击房间
        :return:
        '''
        pass

    def clickSmartContrl(self, type):
        '''
        点击智控
        :return:
        '''
        self.click(self.inte_control if type == "ios" else self.inte_control)
