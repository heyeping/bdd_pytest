# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 2:50 下午
# @Author  : jinxu
# @File    : addstatusconclue.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/keylinkage/新增设备和延时.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("一键执行-新增设备和延时")
@scenario(feature, "一键执行-新增设备和延时")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("已存在一键执行联动A")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已存在一键执行联动A")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)
    intel_obj.add_complete_implementation(type=phone_type)


@when('点击一键执行联动A')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击一键执行联动A')
    intel_obj.click_more(type=phone_type)


@then('点击动作中的延时')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击动作中的延时')
    intel_obj.add_time_delay(type=phone_type)


@then('编辑延时时间')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('编辑延时时间')


@then('在设备属性选择页中重新选择设备属性')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('在设备属性选择页中重新选择设备属性')
    intel_obj.add_device_action(type=phone_type, index=1)


@then('点击"完成"按钮')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"完成"按钮')
    intel_obj.click_save_button(type=phone_type)


@then('点击"保存"按钮，联动动作更新成功')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"保存"按钮，联动动作更新成功')
    ret = intel_obj.del_control(type=phone_type)
    assert ret
