# coding:utf-8
# @Time   :2022/2/15 15:39
# @Author :Nicholas.liu
# @File   :filter_todaySteps.py
# @Software   :bbd_test

import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/fillter_today.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")

@allure.feature("我的界面-信息中心-筛选当前日期查询告警信息")
@scenario(feature, "消息中心- 筛选日期-筛选当前日期-有报警消息")
def test_message(driver_obj, phone_type):
    pass

@given("当前在我的页面")
def go_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)

@when("点击【消息中心】筛选时间")
def go_msgPage(message_obj,own_obj,phone_type,myallure_obj):
    myallure_obj.allure_step("点击【消息中心】筛选时间")
    own_obj.click_msg(phone_type)
    message_obj.click_calendar(type=phone_type)
    time.sleep(2)

@when("选择日期是当天")
def choose_today(message_obj,phone_type,myallure_obj):
    myallure_obj.allure_step("选择日期是当天")
    message_obj.click_calendar_ok(type=phone_type)
    time.sleep(2)


@then("显示当前的报警消息")
def show_warning_msg(message_obj,phone_type,myallure_obj):
    myallure_obj.allure_step("显示当前的报警消息")
    message_obj.getMessageObj(phone_type)




