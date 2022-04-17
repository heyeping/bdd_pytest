# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 1:55 下午
# @Author  : jinxu
# @File    : batchdeleterSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/batch_delete.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("消息中心-批量删除消息-确认")
@scenario(feature, "消息中心-批量删除消息-确认")
def test_click_read(driver_obj, phone_type):
    pass


@given("当前在消息中心")
def to_setting(login_obj, main_obj, own_obj, message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在消息中心")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_msg(type=phone_type)


@when("长按任意一条消息,进入删除页面")
def get_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("长按任意一条消息,进入删除页面")
    message_obj.Long_press(type=phone_type)


@then("选择普通消息，未读消息，收藏消息进行删除")
def click_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("选择普通消息，未读消息，收藏消息进行删除")
    message_obj.click_multi_pick(type=phone_type)
    message_obj.click_delete(type=phone_type)
    message_obj.click_cancel(type=phone_type)


@then("返回到进去编辑状态前的页面")
def click_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("返回到进去编辑状态前的页面")
    message_obj.click_isok(type=phone_type)


@then("当前用户不会再看见相关消息")
def click_cache(message_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前用户不会再看见相关消息")
