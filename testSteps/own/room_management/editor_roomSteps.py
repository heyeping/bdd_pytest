# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 2:45 PM
# @Author  : jinxu
# @File    : editor_roomSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/room_management/editor_room.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("房间管理-默认房间验证_修改数据")
@scenario(feature, "房间管理-默认房间验证_修改数据")
def test_cache1(driver_obj, phone_type):
    pass


@given("当前刚新建了一个家庭在其房间管理页面")
def to_setting(login_obj, main_obj, own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前刚新建了一个家庭在其房间管理页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.click_room(type=phone_type)
    room_name = own_obj.get_one_room_name(type=phone_type)
    if room_name != '自动化添加房间':
        own_obj.click_add_room_button(type=phone_type)
        room_name = '自动化添加房间'
        own_obj.input_room_name(type=phone_type, txt=room_name)
        own_obj.click_save(type=phone_type)


@when("修改房间名称保存")
def get_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("修改房间名称保存")
    new_name = '自动化修改的房间名称'
    own_obj.editor_room_name(type=phone_type, txt=new_name)


@then("返回房间管理页面时房间刷新与修改一致")
def click_cache(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("返回房间管理页面时房间刷新与修改一致")
    room_name = own_obj.get_one_room_name(type=phone_type)
    assert room_name != '自动化添加房间'
    own_obj.move_new_room(type=phone_type)
    own_obj.confirm_the_deletion(type=phone_type)
    room_name = own_obj.get_one_room_name(type=phone_type)
    assert room_name != '自动化添加房间'
    own_obj.back_button(type=phone_type)
    own_obj.del_init_family(type=phone_type)
