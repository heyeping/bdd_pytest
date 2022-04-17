# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 10:03 上午
# @Author  : jinxu
# @File    : delkeylinkage.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/keylinkage/delkeylinkage.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("删除一键执行-正常联动-成功")
@scenario(feature, "删除一键执行-正常联动-成功")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("已存在正常一键执行联动A")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已存在正常一键执行联动A")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)
    intel_obj.add_complete_implementation(type=phone_type)


@when("点击一键执行联动A")
def click_add(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击一键执行联动A")
    intel_obj.click_more(type=phone_type)


@then('在联动详情页点击"删除"按钮')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('在联动详情页点击"删除"按钮')
    intel_obj.click_del_button(type=phone_type)


@then('移除成功，返回到场景列表页不存在删除的联动A')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('移除成功，返回到场景列表页不存在删除的联动A')
    ret = intel_obj.del_control(type=phone_type)
    assert ret
