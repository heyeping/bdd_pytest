# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 4:04 PM
# @Author  : jinxu
# @File    : devicemageSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/ownPage/device_management/device_management.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("设备管理-设备管理入口验证_家庭看板处入口")
@scenario(feature, "设备管理-设备管理入口验证_家庭看板处入口")
def test_cache(driver_obj, phone_type):
    pass


@given("在我的页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)


@when("点击某一个家庭的设备")
def get_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击某一个家庭的设备")
    own_obj.init_family(type=phone_type)
    own_obj.click_device(type=phone_type)


@then("进入设备管理页面，全部下显示设备和对应房间")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("进入设备管理页面，全部下显示设备和对应房间")


@then("点击设备直接跳转高级页面")
def check_cache(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击设备直接跳转高级页面")


@then("有移除权限的成员可移除设备")
def check_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("有移除权限的成员可移除设备")
    own_obj.is_device(type=phone_type)
    own_obj.back_button(type=phone_type)
    own_obj.del_init_family(type=phone_type)