# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 10:47 上午
# @Author  : jinxu
# @File    : noDevice.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/scenematching/房间下没有设备.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("创建场景速配-房间下没有设备")
@scenario(feature, "创建场景速配-房间下没有设备")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("当前在创建速配页面，选择的房间下没有在线的动作设备")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在创建速配页面，选择的房间下没有在线的动作设备")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)
    intel_obj.click_add(type=phone_type)
    intel_obj.click_matching_button(type=phone_type)


@when('点击房间')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击房间')
    intel_obj.click_tv_title(type=phone_type, index=1)
    time.sleep(1)


@then('toast 提示用户「无可配置设备，请添加设备后重试」')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('toast 提示用户「无可配置设备，请添加设备后重试」')
    time.sleep(1)
    ret = intel_obj.check_choice_room(type=phone_type)
    assert ret
