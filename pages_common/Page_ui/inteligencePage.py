# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 2:52 下午
# @Author  : jinxu
# @File    : inteligencePage.py
class Intelligence:
    inte_control = ("accessibility id", '''智控''')
    empty_info = ("accessibility id", '''空空如也''')
    key_linkage = ("accessibility id", '''一键执行''')
    add_btn = ("accessibility id", '''iv_intelligence_add''')
    tv_title = ("accessibility id", '''tv_title''')
    btn_add_item = ("accessibility id", '''btn add item''')
    iv_action = ("accessibility id", '''iv_action''')
    iv_right = ("accessibility id", '''iv_right''')
    device_status = ('-ios class chain', '''**/XCUIElementTypeTable[`name == "rv_device"`]/XCUIElementTypeCell''')
    sure_button = ('-ios class chain', '''**/XCUIElementTypeButton[`label == "确定"`]''')
    next_button = ("accessibility id", '''下一步''')
    save_button = ("accessibility id", '''保存''')
    canel_button = ("accessibility id", '''取消''')

    # 名称
    input_name = ('-ios class chain', '''**/XCUIElementTypeTextField[`value == "请输入名称"`]''')
    clear_text = ("accessibility id", '''清除文本''')

    # 删除联动
    tv_name = ("accessibility id", '''tv_name''')
    iv_more = ("accessibility id", '''iv_more''')
    del_button = ('-ios class chain', '''**/XCUIElementTypeButton[`label == "删除"`]''')

    is_ok = ("accessibility id", '''确认''')
    is_sure = ("accessibility id", '''确定''')

    # 修改
    right_in_arrow = ("accessibility id", '''right_in_arrow''')
    iv_icon = ("accessibility id", '''iv_icon''')
    btn_save = ("accessibility id", '''btn_save''')

    # 删除动作
    rv_action = ("accessibility id", '''rv_action''')
    trailing0 = ("accessibility id", '''trailing0''')

    # 场景速配
    matching_button = ("accessibility id", '''场景速配''')
    choice_room = ('-ios class chain', '''**/XCUIElementTypeStaticText[`label == "选择房间"`]''')
