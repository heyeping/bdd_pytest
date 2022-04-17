# coding:utf-8
# @Time   :2022/2/16 10:50
# @Author :Nicholas.liu
# @File   :collect_msgSteps.py
# @Software   :bbd_test
# 消息中心-收藏信息
import os

from pytest_bdd import given, when, then, scenario
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/info_center/collect_msg.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("消息中心-收藏消息-一条")
@scenario(feature, "消息中心-收藏消息-一条")
def test_message_collect3(driver_obj, phone_type):
    pass


@given("当前在消息中心")
def go_messageCenter(login_obj, main_obj, own_obj, phone_type, myallure_obj):
    myallure_obj.allure_step("当前在消息中心")


@when("点击收藏")
def collect_msg(myallure_obj, login_obj, main_obj, own_obj, message_obj, phone_type):
    myallure_obj.allure_step("点击收藏")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_msg(phone_type)
    message_obj.fist_collect_msg(phone_type)


@then("切换到收藏table")
def swich_to_collect_tab(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("切换到收藏table")
    message_obj.send_collect_msg(phone_type)
    message_obj.switch_to_collectTab(phone_type)

@then("展现刚收藏的消息")
def swich_to_collect_tab(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("展现刚收藏的消息")


# -------------------------------------------------------

@allure.feature("消息中心-取消收藏")
@scenario(feature, "消息中心-取消收藏")
def test_message_collect4(driver_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("消息中心-取消收藏")


@given("当前在消息中心")
def go_messageCenter(login_obj, main_obj, own_obj, phone_type, myallure_obj):
    myallure_obj.allure_step("当前在消息中心")


@when("取消收藏的消息")
def collect_msg(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("取消收藏的消息")



@then("之前收藏的消息图标变为非收藏的")
def swich_to_collect_tab(myallure_obj, message_obj, phone_type):
    myallure_obj.allure_step("之前收藏的消息图标变为非收藏的")
    ret = message_obj.check_msg_is(phone_type)
    assert ret == '空空如也'
