# coding:utf-8
import logging
import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_adctin.mainAction import MainAction
from pages_common.Page_ui.loginPage import LoginPage
from pages_common.Page_ui.settingPage import SettingPage
from pages_common.Page_ui.ownPage import OwnPage


class LoginAction(BaseAction, LoginPage, SettingPage, OwnPage):

    def restart_app(self):
        self.driver.close_app()
        time.sleep(1)
        self.driver.launch_app()

    def allow_app(self, type):
        '''同意首次登陆app的选项'''
        if type == 'ios':
            count = 0
            while count < 5:
                try:
                    self.click(self.ok if type == "ios" else self.ok)
                    self.click(self.allow if type == "ios" else self.allow)
                    self.click(self.agree if type == "ios" else self.agree)
                except Exception as e:
                    logging.info("初始化登陆app失败：{},尝试初始化次数{}".format(e, count))
                    count += 1

    def switchLoginType(self, type):
        '''
        点击切换为密码登录
        :return:
        '''
        self.click(self.loginTypeEle if type == "ios" else self.login_tv_toggle)

    def nextStepAction(self, type):
        '''
        用户点击下一步
        :return:
        '''
        self.click(self.nextButtonEle if type == "ios" else self.mLoginBtn)

    def inputName(self, username, type):
        '''
        输入用户名
        :param username: 用户名
        :return:
        '''
        self.clear(self.usernameEle if type == "ios" else self.username_input)
        self.txt_input(self.usernameEle if type == "ios" else self.username_input, username)

    def pwd_input(self, pwd, type):
        '''
        输入密码
        :param pwd: 密码
        :return:
        '''
        self.txt_input(self.pwdEle if type == "ios" else self.pi_et_password, pwd)

    def agreement_login(self, type):
        if type != 'ios':
            self.click(self.login_cb_agreement)

    def login_button(self, type):
        '''
        登陆按钮
        :return:
        '''
        self.click(self.loginButtonEle if type == "ios" else self.mLoginBtn)

    def get_username(self, type):
        '''
        获取当前登陆账号
        :return:
        '''
        return self.get_ele_text(self.usernameEle if type == "ios" else self.usernameEle)

    def checkLoginStatus(self, type):
        '''
        判断是否登陆成功
        :return:
        '''
        element = self.find_my_element(self.welcomeHome if type == "ios" else self.welcomeHome)
        return element.text

    def login_out(self, type):
        '''
        登出
        :return:
        '''
        time.sleep(1)
        self.click(self.own if type == "ios" else self.own)
        time.sleep(1)
        self.click(self.setting if type == "ios" else self.iv_setting)
        time.sleep(1)
        self.click(self.loginOutEle if type == "ios" else self.btn_logout)
        time.sleep(1)

    def login(self, username, pwd, type):
        '''
        登陆
        :param username: 用户名
        :param pwd: 密码
        :return:
        '''
        try:
            self.checkLoginStatus(type)
        except:
            self.switchLoginType(type)
            self.inputName(username, type)
            self.nextStepAction(type)
            self.pwd_input(pwd, type)
            self.login_button(type)

    def check_login_out(self, type):
        '''登出'''
        try:
            self.checkLoginStatus(type)
            self.login_out(type)
        except:
            pass
