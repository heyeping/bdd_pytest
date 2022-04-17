import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.mylog import logger
from ayla_public.myallure import MyAllure
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/iv_setting/sets_protocol.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("设置-操作路由")
@scenario(feature, u"设置-操作路由")
def test_protocol1(login_obj):
    pass


@given("用户已登录")
def userlogin(login_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("用户已登录")
    login_obj.login(username, password, type=phone_type)


@when("点击元素我的")
def own(main_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素我的")
    main_obj.clickOwn(type=phone_type)


@when("点击元素设置按钮")
def setting(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素设置按钮")
    own_obj.clickSetting(type=phone_type)


@then("跳转页面text内容包含 用户协议 隐私协议")
def checkTitle(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转页面text内容包含 用户协议 隐私协议")
    setting_obj.to_setting(type=phone_type)


# -------------------------------------------------------------

@allure.feature("设置-隐私协议")
@scenario(feature, u"设置-隐私协议")
def test_protocol2(login_obj):
    pass


@given('''当前页面text内容包含 用户协议 隐私协议''')
def settingPage(setting_obj, myallure_obj):
    myallure_obj.allure_step("当前页面text内容包含 用户协议 隐私协议")


@when("点击元素 隐私协议")
def click_privacy(myallure_obj):
    myallure_obj.allure_step("点击元素 隐私协议")


@when("跳转进入title为 隐私政策 页面")
@then("swip_down无误")
def check_privacy(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转进入title为 隐私政策 页面")
    setting_obj.privacy_agreement(type=phone_type)


# -------------------------------------------------------------

@allure.feature("设置-用户协议")
@scenario(feature, "设置-用户协议")
@given("当前页面text内容包含 用户协议 隐私协议")
def test_protocol3(myallure_obj, phone_type):
    myallure_obj.allure_step("当前页面text内容包含 用户协议 隐私协议")


@when("点击元素 用户协议")
def click_userAgreement(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素 用户协议")


@when("跳转进入title为 用户政策 页面")
@then("swip_down无误")
def check_userAgreement(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转进入title为 用户协议 页面")
    setting_obj.user_agreement(type=phone_type)



