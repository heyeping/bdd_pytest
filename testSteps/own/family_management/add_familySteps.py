# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 2:23 下午
# @Author  : jinxu
# @File    : add_familySteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile, random_str

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/family_management/add_family.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("家庭-创建家庭")
@scenario(feature, "家庭-创建家庭")
def test_family(driver_obj, phone_type):
    pass


@given("在创建家庭页面")
def to_family1(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在创建家庭页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.init_family(type=phone_type)


@when("编辑家庭名称")
def click_save(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("编辑家庭名称")


@then("点击保存")
def check_name(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击保存")


@then("成功创建家庭")
def check_name1(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("成功创建家庭")
    own_obj.check_family_name(type=phone_type, family_name="自动化添加家庭")
    own_obj.del_init_family(type=phone_type)
