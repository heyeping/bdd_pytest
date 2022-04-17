# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 2:32 PM
# @Author  : jinxu
# @File    : delete_roomSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/room_management/delete_room.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("房间管理-删除房间_确认删除")
@scenario(feature, "房间管理-删除房间_确认删除")
def test_cache1(driver_obj, phone_type):
    pass


@given("已进入房间管理页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("已进入房间管理页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_room(type=phone_type)
    room_name = own_obj.get_one_room_name(type=phone_type)
    if room_name != '自动化添加房间':
        own_obj.click_add_room_button(type=phone_type)
        room_name = '自动化添加房间'
        own_obj.input_room_name(type=phone_type, txt=room_name)
        own_obj.click_save(type=phone_type)


@when("任选一个房间列向左滑动")
def get_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("任选一个房间列向左滑动")
    own_obj.move_new_room(type=phone_type)


@then("点击【删除】按钮")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【删除】按钮")
    own_obj.confirm_the_deletion(type=phone_type)


@then("弹窗消失，提示：删除成功。")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("弹窗消失，提示：删除成功。")
    room_name = own_obj.get_one_room_name(type=phone_type)
    assert room_name != '自动化添加房间'
    own_obj.back_button(type=phone_type)
    own_obj.del_init_family(type=phone_type)