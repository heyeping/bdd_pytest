# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 1:45 下午
# @Author  : jinxu
# @File    : allreadSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/all_read.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("消息中心-点击全部已读")
@scenario(feature, "消息中心-点击全部已读")
def test_click_read(driver_obj, phone_type):
    pass


@given("当前在消息中心有未读消息")
def to_setting(login_obj, main_obj, own_obj, message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在消息中心有未读消息")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_msg(type=phone_type)


@when("点击全部已读")
def get_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击全部已读")
    message_obj.click_all_read(type=phone_type)


@then("点击后未读消息全部已读，小红点消失")
def click_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击后未读消息全部已读，小红点消失")
    message_obj.click_back_button(type=phone_type)
