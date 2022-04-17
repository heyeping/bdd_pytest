# coding:utf-8
# @Time   :2022/2/17 11:47
# @Author :Nicholas.liu
# @File   :ownPageToMember.py
# @Software   :bbd_test

import os
import time
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/members_management/ownPageToMember.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("成成员管理-成员管理入口验证_家庭看板处入口")
@scenario(feature, "成员管理-成员管理入口验证_家庭看板处入口")
def test_go_to_memberPage():
    pass


@given("当前在我的页面")
def stay_myOwnPage(own_obj, phone_type, myallure_obj, login_obj, main_obj):
    myallure_obj.allure_step("当前在我的页面")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    time.sleep(2)
    own_obj.init_family(type=phone_type)

@when("点击【xxx的家】下的【成员】")
def stay_memberPage(own_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击【xxx的家】下的【成员】")
    # 进入管理页面
    own_obj.init_family(phone_type)
    own_obj.click_member(phone_type)
    time.sleep(2)


@then('''跳转到【成员管理】，展示：添加成员按钮、成员列表，成员列表包含：成员头像、成员名称、成员账号、成员角色''')
def show_memberInfo(phone_type,own_obj, member_obj, myallure_obj):
    myallure_obj.allure_step('''跳转到【成员管理】，展示：添加成员按钮、成员列表，成员列表包含：成员头像、成员名称、成员账号、成员角色''')
    member_obj.queryInfo(phone_type)
    own_obj.back_button(phone_type)
    own_obj.del_init_family(phone_type)