# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 5:30 下午
# @Author  : jinxu
# @File    : conftest.py
import pytest

from utils.preset_cases import PresetCases


@pytest.fixture(scope="session")
def preset_info():
    presetcases = PresetCases()
    # presetcases.get_app_token()
    # data = presetcases.get_family()["data"]
    # data_size = len(data)
    # if data_size >= 1:
    #     for i in data:
    #         if i['homeName'] == '自动化添加家庭':
    #             pass
    #         else:
    #             presetcases.delete_family(i['homeId'])
    # else:
    #     presetcases.creat_family()
    # family_info = presetcases.get_family()["data"]
    # presetcases.bind_batch(family_info[0]['homeId'])
    # yield presetcases
    # presetcases.delete_family(family_info[0]['homeId'])
