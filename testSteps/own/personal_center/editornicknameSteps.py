# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 2:39 PM
# @Author  : jinxu
# @File    : editornicknameSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.mylog import logger
from ayla_public.myallure import MyAllure
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/personal_center/editor_nickname.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("我的-个人中心-昵称修改")
@scenario(feature, "我的-个人中心-昵称修改")
def test_personal_center3(login_obj):
    pass


@given("跳转页面text内容包含 头像 昵称")
def step_up(login_obj, main_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转页面text内容包含 头像 昵称")
    login_obj.login(username, password, phone_type)
    main_obj.clickOwn(type=phone_type)


@when("点击元素昵称")
def to_nickname(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素昵称")
    global before_nickname
    own_obj.clickCenter(type=phone_type)
    before_nickname = own_obj.get_before_nickname(type=phone_type)
    own_obj.clickNickname(type=phone_type)


@then("昵称修改")
def changeNickname(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("昵称修改")
    global change_name
    change_name = "修改的昵称"
    own_obj.changeNickname(txt=change_name, type=phone_type)


@then("昵称修改成功")
def check_nickname(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("昵称修改成功")
    assert change_name != before_nickname
    own_obj.clickNickname(type=phone_type)
    own_obj.changeNickname(txt=before_nickname, type=phone_type)
