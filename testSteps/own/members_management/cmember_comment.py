# coding:utf-8
# @Time   :2022/2/17 10:52
# @Author :Nicholas.liu
# @File   :cmember_comment.py
# @Software   :bbd_test

import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/members_management/member_comment.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("成员管理-添加成员_设置备注")
@scenario(feature, "成员管理-添加成员_设置备注")
def test_member_comment():
    pass


@given("处于成员管理页面")
def stay_member_page(own_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    time.sleep(2)
    # 进入管理页面
    own_obj.init_family(phone_type)
    own_obj.click_member(phone_type)
    time.sleep(2)


@when("点击成员")
def click_member(phone_type, member_obj, myallure_obj):
    myallure_obj.allure_step("点击成员")
    member_obj.query_member_info(phone_type)


@then("设置备注")
def set_member_name(phone_type, own_obj, member_obj, myallure_obj):
    myallure_obj.allure_step("设置备注")
    member_obj.set_memeber_name(phone_type)
    member_obj.send_memeber_new_name(phone_type, '自动化修改的备注')
    member_obj.saveBtn(phone_type)

@then("备注设置成功")
def set_member_name(phone_type, own_obj, member_obj, myallure_obj):
    myallure_obj.allure_step("备注设置成功")
    ret = member_obj.check_new_name(phone_type)
    assert ret == '自动化修改的备注(我)'
    own_obj.back_button(phone_type)
    own_obj.del_init_family(phone_type)