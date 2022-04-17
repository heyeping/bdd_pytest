import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.mylog import logger
from ayla_public.myallure import MyAllure
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/personal_center/editor_myicon.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("我的-个人中心")
@scenario(feature, "我的-个人中心")
def test_personal_center1(phone_type):
    pass


@given("用户已登录")
def uesr_login(login_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("用户已登录")
    login_obj.login(username, password, phone_type)


@when("点击元素我的")
def to_own(main_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素我的")
    main_obj.clickOwn(type=phone_type)


@when("点击元素个人中心")
def to_own(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素个人中心")
    own_obj.clickCenter(type=phone_type)


@then("跳转页面text内容包含 头像 昵称")
def checkCenter(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转页面text内容包含 头像 昵称")
    my_icon, nickname = own_obj.get_check_massage(type=phone_type)
    assert my_icon == "头像", nickname == "昵称"


# ----------------------------------

@allure.feature("我的-个人中心-头像")
@scenario(feature, "我的-个人中心-头像")
def test_personal_center2(login_obj):
    pass


@given("跳转页面text内容包含 头像 昵称")
def step_up(myallure_obj):
    myallure_obj.allure_step("跳转页面text内容包含 头像 昵称")


@when("点击元素头像")
def to_my_icon(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击元素头像")
    own_obj.clickavatar(type=phone_type)


@when("更换头像")
def changeavatar(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("更换头像")
    own_obj.changeAvatar(type=phone_type)


@then("更换头像成功")
def check_avatar(myallure_obj):
    myallure_obj.allure_step("更换头像成功")

