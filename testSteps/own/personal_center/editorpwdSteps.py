# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 2:06 PM
# @Author  : jinxu
# @File    : editorpwdSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.mylog import logger
from ayla_public.myallure import MyAllure
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/personal_center/editor_password.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("修改密码-入口")
@scenario(feature, "修改密码-入口")
def test_personal_center1(phone_type):
    pass


@given("当前在我的页面")
def uesr_login(login_obj, main_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, phone_type)
    main_obj.clickOwn(type=phone_type)


@when("点击【设置】-【密码】")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【设置】-【密码】")
    own_obj.clickCenter(type=phone_type)
    own_obj.click_pwd(type=phone_type)


@then("点击后跳转到修改密码页面")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击后跳转到修改密码页面")
    own_obj.click_I_know(type=phone_type)


# -----------------------------------------------------

@allure.feature("修改密码-修改密码-密码修改成功")
@scenario(feature, "修改密码-修改密码-密码修改成功")
def test_personal_center2(phone_type):
    pass


@given("当前在设置新密码页面")
def uesr_login(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在设置新密码页面")
    own_obj.send_old_pwd(type=phone_type, txt=password)


@when("输入确认密码和新密码-数据一致")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("输入确认密码和新密码-数据一致")
    own_obj.send_new_pwd(type=phone_type, txt=password)


@then("点击完成")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击完成")
    own_obj.click_ok(type=phone_type)


@then("修改完成弹窗提示用户变更完成")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("修改完成弹窗提示用户变更完成")
