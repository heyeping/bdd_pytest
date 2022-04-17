# coding:utf-8
# @Time   :2022/2/17 15:33
# @Author :Nicholas.liu
# @File   :deleteMember.py
# @Software   :bbd_test
import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/members_management/deleteMember.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")

@allure.feature("成员管理-删除成员")
@scenario(feature, "成员管理-删除成员")
def test_delete_member():
    pass

@given("处于成员管理页面")
def stay_memberPage(own_obj,phone_type,myallure_obj,login_obj,main_obj):
    myallure_obj.allure_step("处于成员管理页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    time.sleep(1)
    own_obj.init_family(type=phone_type)
    own_obj.click_member(phone_type)

@when("选择成员")
def choose_member(phone_type,member_obj,myallure_obj):
    myallure_obj.allure_step("选择成员")
    member_obj.click_add_member_btn(phone_type)
    member_obj.click_add_account_btn(phone_type)
    member_obj.ipuntIphoneNo(phone_type)
    member_obj.saveBtn(phone_type)

@then("删除成员")
def delete_member(phone_type,member_obj,myallure_obj):
    myallure_obj.allure_step("删除成员")
    member_obj.deleteMember(phone_type)

@then("对应成员在app刷新后不能再选择该家庭，没有查看入口")
def check_result(phone_type,member_obj,myallure_obj,own_obj):
    myallure_obj.allure_step("对应成员在app刷新后不能再选择该家庭，没有查看入口")
    #开始在首页中切换家庭，看看是否有被剔的家庭
    own_obj.back_button(phone_type)
    own_obj.del_init_family(phone_type)








