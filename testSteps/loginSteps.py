# coding:utf-8
import os
import time

from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.mylog import logger
from ayla_public.public import get_pathfile
import allure


feature = os.path.join(get_pathfile(), "features/logePage/login.feature")


@allure.feature("用户输入正确的账户和密码进行APP登录")
@pytest.mark.usefixtures("login_obj")
@scenario(feature, u"用户输入正确的账户和密码进行APP登录")
def test_login(driver_obj, phone_type):
    pass


@given(parsers.parse("使用账户:{username}"))
def send_massage(username, phone_type):
    logger.info(u"开始测试登录")
    logger.info(u"输入账户")
    return username


@when("点击切换为密码登录")
def loginType(login_obj, username, myallure_obj, phone_type):
    myallure_obj.allure_step("点击切换为密码登录")
    login_obj.check_login_out(type=phone_type)
    login_obj.allow_app(type=phone_type)
    login_obj.agreement_login(type=phone_type)
    login_obj.switchLoginType(type=phone_type)
    login_obj.inputName(username, type=phone_type)


@when("用户点击下一步")
def nextStepAction(login_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击切换为密码登录")
    login_obj.nextStepAction(type=phone_type)


@when(parsers.parse("密码:{pwd}"))
def pwd_input(login_obj, pwd, myallure_obj, phone_type):
    myallure_obj.allure_step("输入正确的登录密码")
    login_obj.pwd_input(pwd, type=phone_type)
    login_obj.login_button(type=phone_type)


@then("用户登录成功")
def assert_sucess(login_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("用户登录成功")
    result = login_obj.checkLoginStatus(phone_type)


@then("用户进行登出操作")
def loginOut(login_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("用户进行登出操作")
    login_obj.login_out(type=phone_type)
