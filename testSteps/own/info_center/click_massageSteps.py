# -*- coding: utf-8 -*-
# @Time    : 2022/2/25 4:00 PM
# @Author  : jinxu
# @File    : click_massageSteps.py
import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/click_massage.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("消息中心-点击消息")
@scenario(feature, "消息中心-点击消息")
def test_message_collect1(driver_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("消息中心-点击消息")


@given("当前在消息中心")
def go_messageCenter(login_obj, own_obj, main_obj, phone_type, myallure_obj):
    myallure_obj.allure_step("当前在消息中心")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_msg(phone_type)


@when("点击消息")
def collect_msg(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("点击消息")
    message_obj.to_msg(phone_type)


@then("点击单控/高级的返回按钮")
def swich_to_collect_tab(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("点击单控/高级的返回按钮")
    message_obj.check_to_content(phone_type)


@then("返回到之前的ui")
def swich_to_collect_tab(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("返回到之前的ui")
    message_obj.click_back_button(phone_type)
    message_obj.check_to_msg(phone_type)
