# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 10:50 AM
# @Author  : jinxu
# @File    : facebackSteps.py
import os

from pytest_bdd import given, when, then, parsers, scenario
import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile, creat_massage, random_int

import allure

feature = os.path.join(get_pathfile(), "features/ownPage/iv_setting/problem_feedback.feature")

username = ReadConfig().get_login_massage("userName")
password = ReadConfig().get_login_massage("passWord")


@allure.feature("问题反馈-点击返回-写了数据")
@scenario(feature, "问题反馈-点击返回-写了数据")
def test_feedback1(driver_obj, phone_type):
    pass


@given("当前在问题反馈页面，输入了数据")
def to_feedback(login_obj, main_obj, own_obj, setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("当前在问题反馈页面，输入了数据")
    login_obj.login(username, password, type=phone_type)
    main_obj.clickOwn(type=phone_type)
    own_obj.clickSetting(type=phone_type)
    setting_obj.click_feedback(type=phone_type)


@when("点击返回按钮")
def back_feedback(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击返回按钮")
    massage = creat_massage()
    setting_obj.send_massage(type=phone_type, txt=massage)
    setting_obj.back(type=phone_type)


@then("弹窗提示用户是否返回")
def check_feedback(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("弹窗提示用户是否返回")
    setting_obj.click_cancel(type=phone_type)


# -------------------------------------------------------------

@allure.feature("问题反馈-正常提交")
@scenario(feature, "问题反馈-正常提交")
@given("当前在问题反馈页面")
def test_feedback2(myallure_obj, phone_type):
    myallure_obj.allure_step("当前在问题反馈页面")


@when("输入文案")
def send_word(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("输入文案")
    massage = creat_massage()
    setting_obj.send_massage(type=phone_type, txt=massage)


@then("选择一张图片")
def send_image(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("选择一张图片")
    setting_obj.load_photo(type=phone_type)


@then("输入联系方式")
def send_phone(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("输入联系方式")
    phone_number = random_int()
    setting_obj.send_phone_number(type=phone_type, phone_number=phone_number)


@then("点击提交按钮，正常提交弹窗提示")
def check_feedback(setting_obj, myallure_obj, phone_type):
    myallure_obj.allure_step("点击提交按钮，正常提交弹窗提示")
    setting_obj.submit(type=phone_type)
