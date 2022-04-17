# coding:utf-8
# @Time   :2022/2/16 16:31
# @Author :Nicholas.liu
# @File   :add_membereSteps.py
# @Software   :bbd_test

import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/members_management/add_member.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("成员管理-添加成员_账号添加_成功添加成员")
@scenario(feature, "成员管理-添加成员_账号添加_成功添加成员")
def test_add_member():
    pass


@given("处于成员管理页面")
def stay_memberPage(own_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    time.sleep(2)
    own_obj.init_family(type=phone_type)


@when("点击【添加成员】")
def add_btn(phone_type, own_obj, member_obj, myallure_obj):
    myallure_obj.allure_step("点击成员icon")
    own_obj.click_member(phone_type)
    time.sleep(2)
    myallure_obj.allure_step("增添加成员")
    member_obj.click_add_member_btn(phone_type)


@when("点击【账号添加】")
def add_account(phone_type, member_obj, myallure_obj):
    myallure_obj.allure_step("点击【账号添加】")
    member_obj.click_add_account_btn(phone_type)


@when("输入账号")
def input_account(phone_type, member_obj, myallure_obj):
    myallure_obj.allure_step("输入账号")
    member_obj.ipuntIphoneNo(phone_type)


@when("点击【确认】")
def saveMember(phone_type, member_obj, myallure_obj):
    myallure_obj.allure_step("点击【确认】")
    member_obj.saveBtn(phone_type)


@then("页面关闭，提示添加成功，跳转到成员信息设置页面，展示：显示该用户头像、名称、账号，可设置备注、角色")
def saveCheck(phone_type, own_obj, member_obj, myallure_obj):
    myallure_obj.allure_step("开始校验成员新增结果")
    member_obj.check_member(phone_type)
    own_obj.back_button(phone_type)
    own_obj.del_init_family(phone_type)
