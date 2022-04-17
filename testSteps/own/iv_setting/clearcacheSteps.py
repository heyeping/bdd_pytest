# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 10:46 AM
# @Author  : jinxu
# @File    : clearcacheSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/iv_setting/clear_cache.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("清除缓存-显示当前缓存-点击清除缓存")
@scenario(feature, "清除缓存-显示当前缓存-点击清除缓存")
def test_cache(driver_obj, phone_type):
    pass


@given("当前在设置页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在设置页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.clickSetting(type=phone_type)


@when("查看清除缓存")
def get_cache(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("查看清除缓存")
    setting_obj.click_cache(type=phone_type)


@then("缓存清理完成，重新获取应显示为0.00mb")
def click_cache(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("缓存清理完成，重新获取应显示为0.00mb")
    setting_obj.get_cache_text(type=phone_type)


@then("会有toaSt提示用户清理完成")
def check_cache(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("会有toaSt提示用户清理完成")
