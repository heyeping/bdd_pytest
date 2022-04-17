# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 11:27 AM
# @Author  : jinxu
# @File    : add_roomSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/room_management/add_room.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("房间管理-房间管理入口验证_家庭看板处入口")
@scenario(feature, "房间管理-房间管理入口验证_家庭看板处入口")
def test_cache1(driver_obj, phone_type):
    pass


@given("当前在【我的】页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在【我的】页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)


@when("点击【xxx的家】下的【房间】")
def get_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【xxx的家】下的【房间】")
    own_obj.click_room(type=phone_type)


@then("跳转到【房间管理】")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("跳转到【房间管理】")
    own_obj.check_room_management(type=phone_type)


# --------------------------------------------------
@allure.feature("房间管理-添加房间_成功添加房间")
@scenario(feature, "房间管理-添加房间_成功添加房间")
def test_cache2(driver_obj, phone_type):
    pass


@given("已进入房间管理页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已进入房间管理页面")
    own_obj.check_room_management(type=phone_type)
    room_name = own_obj.get_one_room_name(type=phone_type)
    if room_name == '自动化添加房间':
        own_obj.move_new_room(type=phone_type)
        own_obj.confirm_the_deletion(type=phone_type)
        room_name = own_obj.get_one_room_name(type=phone_type)
        assert room_name != '自动化添加房间'


@when("点击【添加房间】")
def get_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【添加房间】")
    own_obj.click_add_room_button(type=phone_type)


@then("输入房间名称（不存在的房间名称）")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("输入房间名称（不存在的房间名称）")
    room_name = '自动化添加房间'
    own_obj.input_room_name(type=phone_type, txt=room_name)


@then("点击【确定】")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【确定】")
    own_obj.click_save(type=phone_type)


@then("返回房间管理页面，提示：房间创建成功，新建房间显示在房间管理页面")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("返回房间管理页面，提示：房间创建成功，新建房间显示在房间管理页面")
    room_name = own_obj.get_one_room_name(type=phone_type)
    assert room_name == '自动化添加房间'
    own_obj.back_button(type=phone_type)
    own_obj.del_init_family(type=phone_type)
