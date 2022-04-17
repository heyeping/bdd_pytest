# coding:utf-8
# @Time   :2022/2/15 16:07
# @Author :Nicholas.liu
# @File   :messagePage.py
# @Software   :bbd_test


class MessagePage():
    # 消息中心
    msg_calendar = ("accessibility id", '''my_notification_calendarselect''')
    msg_calendar_icon = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "全部"`][2]''')
    msg_calendar_ok = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "确定"`]''')
    msg_collect_icon = ("accessibility id", '''iv_collect''')
    msg_no_message = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "已经全部加载完毕"`][1]''')
    all_msg = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "确定"`]''')
    empty_set_title = ("accessibility id", "empty set title")
    tv_read = ("accessibility id", "tv_read")
    # 下个月的24号
    msg_next_month = ("accessibility id", "24")
    msg_collect_tab = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "收藏"`]''')

    # 消息内容
    tv_content = ("accessibility id", "tv_content")
    tv_time = ("accessibility id", "tv_time")
    tab_message = ("accessibility id", "tab_message")
    back_button = ("accessibility id", "navi back")
    rv_message1 = ("-ios class chain", '''**/XCUIElementTypeTable[`name == "rv_message"`][1]/XCUIElementTypeCell[1]''')
    # 收藏
    rv_message = ("-ios class chain", '''**/XCUIElementTypeTable[`name == "rv_message"`][2]/XCUIElementTypeCell''')
    del_button = ("accessibility id", "trailing0")
    # 编辑页
    iv_multi_pick = ("accessibility id", "iv_multi_pick")
    tv_delete = ("accessibility id", "tv_delete")
    is_ok = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "完成"`]''')
    cancel_button = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "取消"`]''')
