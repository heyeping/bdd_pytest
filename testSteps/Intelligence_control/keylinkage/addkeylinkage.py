# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 2:01 下午
# @Author  : jinxu
# @File    : addkeylinkage.py

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.loginAction import LoginAction
import allure

feature = os.path.join(get_pathfile(), "features/controlPage/keylinkage/addkeylinkage.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("验证正常添加一键执行联动")
@scenario(feature, "验证正常添加一键执行联动")
def test_cache(driver_obj, phone_type, preset_info):
    pass


@given("当前在创建一键执行联动ui且绑定有多个正常设备")
def to_setting(login_obj, main_obj, intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在创建一键执行联动ui且绑定有多个正常设备")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickSmartContrl(type=phone_type)
    intel_obj.del_control(type=phone_type)

@when("点击“+”按钮")
def click_add(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击“+”按钮")
    intel_obj.click_add(type=phone_type)


@then("在添加任务选择弹窗内选择“控制设备”")
def click_cache1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在添加任务选择弹窗内选择“控制设备”")
    intel_obj.click_tv_title(type=phone_type, index=0)
    time.sleep(1)
    intel_obj.click_add_item(type=phone_type)
    time.sleep(1)
    intel_obj.click_tv_title(type=phone_type, index=0)
    time.sleep(1)
    intel_obj.click_tv_title(type=phone_type, index=0)
    time.sleep(1)

@then("选择设备A的属性1，点击完成")
def choice_attribute1(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("选择设备A的属性1，点击完成")
    intel_obj.click_tv_title(type=phone_type, index=0)
    time.sleep(1)
    intel_obj.choice_device_status(type=phone_type, index=0)
    time.sleep(1)
    intel_obj.click_sure_button(type=phone_type)
    time.sleep(1)
    intel_obj.click_next_button(type=phone_type)


@then("在动作选择弹窗内选择“延时”")
def choice_attribute2(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在动作选择弹窗内选择“延时”")
    intel_obj.add_time_delay(type=phone_type)


@then("在延时设置弹窗内设置延时时间")
def check_complete(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在延时设置弹窗内设置延时时间")


@then("点击完成")
def check_add(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击完成")


@then('点击“+”按钮')
def choice_time(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击“+”按钮')


@then("选择设备A的属性2，点击完成")
def set_time(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("选择设备A的属性2，点击完成")
    intel_obj.add_device_action(type=phone_type, index=1)


@then('点击"保存"按钮')
def check_save(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step('点击"保存"按钮')
    intel_obj.click_save_button(type=phone_type)


@then("弹窗内输入执行名称")
def set_name(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("弹窗内输入执行名称")
    name = '自动化添加一键联动'
    intel_obj.input_intel_name(type=phone_type, name=name)


@then("点击确定")
def check_ok2(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击确定")
    intel_obj.click_sure_button(type=phone_type)


@then("联动保存成功，返回到联动列表页显示刚刚添加成功的联动")
def check_linkage(intel_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("联动保存成功，返回到联动列表页显示刚刚添加成功的联动")
    ret = intel_obj.check_name(type=phone_type)
    assert ret
    intel_obj.del_control(type=phone_type)
