# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 10:27 上午
# @Author  : jinxu
# @File    : editerkeylinkage.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/keylinkage/editerkeylinkage.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("一键执行-修改")
@scenario(feature, "一键执行-修改")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("app已登录在一键执行联动列表页面")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("app已登录在一键执行联动列表页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)
    intel_obj.add_complete_implementation(type=phone_type)


@when('点击"更多"按钮')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"更多"按钮')
    intel_obj.click_more(type=phone_type)


@then('输入新的联动名称')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('输入新的联动名称')
    intel_obj.click_right_in_arrow(type=phone_type, index=0)
    intel_obj.input_intel_name(type=phone_type, name='自动化修改的名称')
    intel_obj.click_sure_button(type=phone_type)


@then('切换新的icon')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('切换新的icon')
    intel_obj.click_right_in_arrow(type=phone_type, index=2)
    intel_obj.click_iv_icon(type=phone_type, index=4)


@then('点击"保存"按钮')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"保存"按钮')
    intel_obj.click_save_button(type=phone_type)


@then('联动名称更新成功，一键联动列表页显示新的名称icon')
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('联动名称更新成功，一键联动列表页显示新的名称icon')
    ret = intel_obj.check_name(type=phone_type, name='自动化修改的名称')
    assert ret
    ret = intel_obj.del_control(type=phone_type)
    assert ret
