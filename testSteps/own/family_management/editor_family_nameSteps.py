# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 2:24 下午
# @Author  : jinxu
# @File    : editor_family_nameSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile, random_str

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/family_management/editor_family_name.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("家庭-创建家庭-家庭名称修改")
@scenario(feature, "家庭-创建家庭-家庭名称修改")
def test_editor_family1(driver_obj, phone_type):
    pass


@given("在家庭页面")
def to_family1(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("在家庭页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.init_family(type=phone_type)


@when("修改家庭名称")
def click_save(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("修改家庭名称")
    own_obj.click_family_setting(type=phone_type)
    own_obj.click_iv_right(type=phone_type, index=0)
    own_obj.input_room_name(type=phone_type, txt='自动化修改家庭')
    own_obj.saveModify(type=phone_type)
    own_obj.saveModify(type=phone_type)

@then("家庭名称显示为刚刚修改的")
def check_name1(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("家庭名称显示为刚刚修改的")
    own_obj.check_family_name(type=phone_type, family_name="自动化修改家庭")
    own_obj.del_init_family(type=phone_type)
