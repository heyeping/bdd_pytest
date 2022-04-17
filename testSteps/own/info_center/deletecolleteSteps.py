# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 10:08 AM
# @Author  : jinxu
# @File    : deletecolleteSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/delete_collect.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("消息中心-当前用户删除收藏的消息")
@scenario(feature, "消息中心-当前用户删除收藏的消息")
def test_dele_msg1(driver_obj, phone_type):
    pass


@given("当前收藏了一条消息")
def to_setting(login_obj, main_obj, own_obj,message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前收藏了一条消息")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_msg(type=phone_type)
    message_obj.fist_collect_msg(type=phone_type)


@when("删除收藏的消息")
def get_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("删除收藏的消息")
    message_obj.switch_to_collectTab(type=phone_type)
    message_obj.delete_collect(type=phone_type)
    message_obj.click_del_button(type=phone_type)

@then("当前用户不会再看见此条消息")
def click_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前用户不会再看见此条消息")
    message_obj.check_msg_is(type=phone_type)