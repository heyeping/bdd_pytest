# coding:utf-8
# @Time   :2022/2/17 14:21
# @Author :Nicholas.liu
# @File   :familyToMemberPage.py
# @Software   :bbd_test

import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/members_management/familyToMemberPage.feature")
username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("成员管理-成员管理入口验证_家庭管理中入口")
@scenario(feature, "成员管理-成员管理入口验证_家庭管理中入口")
def test_family_to_memberPage():
    pass


@given("当前在我的页面")
def stay_ownPage(own_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.init_family(type=phone_type)
    time.sleep(2)


@when("点击【xxx的家】右边的【设置】图标")
def click_family_setting(own_obj, phone_type, myallure_obj):
    myallure_obj.allure_step("点击【xxx的家】右边的【设置】图标")
    own_obj.click_family_setting(phone_type)


@when("点击【成员管理】")
def click_member_menue(own_obj, phone_type, myallure_obj):
    myallure_obj.allure_step("点击【成员管理】")
    own_obj.click_memberMange(phone_type)


@then('''跳转到【成员管理】页面，展示：添加成员按钮、成员列表，成员列表包含：成员头像、成员名称、成员账号、成员角色''')
def show_memberInfo(phone_type, member_obj, own_obj, myallure_obj):
    myallure_obj.allure_step('''跳转到【成员管理】页面，展示：添加成员按钮、成员列表，成员列表包含：成员头像、成员名称、成员账号、成员角色''')
    member_obj.queryInfo(phone_type)
    own_obj.back_button(phone_type)
    own_obj.back_button(phone_type)
    own_obj.del_init_family(phone_type)
