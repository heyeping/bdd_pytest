# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 2:25 下午
# @Author  : jinxu
# @File    : zdeletefamilyStepts.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile, random_str

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/family_management/delete_family.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("删除家庭—家庭被成功删除")
@scenario(feature, "删除家庭—家庭被成功删除")
def test_family2(driver_obj, phone_type):
    pass


@given("已存在成功创建家庭")
def to_family(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已存在成功创建家庭")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.init_family(type=phone_type)

@when("在家庭管理页面，删除家庭")
def click_save(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在家庭管理页面，删除家庭")
    own_obj.delete_family(type=phone_type)


@then("二次确认弹窗点击“确定”")
def check_name(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("二次确认弹窗点击“确定”")
    own_obj.delete_ok(type=phone_type)


@then("家庭被成功删除")
def check_name1(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("家庭被成功删除")
