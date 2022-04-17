# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 4:36 下午
# @Author  : jinxu
# @File    : delallaction.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/keylinkage/删除所有动作.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("一键执行-删除所有动作")
@scenario(feature, "一键执行-删除所有动作")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("已存在一键执行联动A，联动内存在多个动作")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已存在一键执行联动A，联动内存在多个动作")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)
    intel_obj.add_complete_implementation(type=phone_type)


@when('点击一键执行联动A')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击一键执行联动A')
    intel_obj.click_more(type=phone_type)


@then('删除全部动作')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('删除全部动作')
    intel_obj.del_action(type=phone_type)


@then('点击"完成"按钮')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"完成"按钮')
    intel_obj.click_save_button(type=phone_type)


@then('toast提示"没有可执行任务"')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('toast提示"没有可执行任务"')
    intel_obj.click_canel_button(type=phone_type)
    ret = intel_obj.del_control(type=phone_type)
    assert ret