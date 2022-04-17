# coding:utf-8
# @Time   :2022/2/16 15:57
# @Author :Nicholas.liu
# @File   :memberPage.py
# @Software   :bbd_test
class MemberPage():
    add_member_btn = ("accessibility id", "btn_add")
    account_btn = ("accessibility id", "账号添加")
    phoneNo = ("accessibility id", "et_input")
    next_btn = ("accessibility id", "btn_next")
    save_member = ("accessibility id", "btn_save")
    check_phoneNo = ("accessibility id", "tv_content")
    # 成员备注名
    memeber_name = ("accessibility id", "tv_desc")
    delete_member = ("accessibility id", "trailing0")
    memeber_table = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "15885537820"`]''')
    input_button = ("-ios class chain", '''**/XCUIElementTypeTextField[`value == "请输入备注不多于20个字符"`]''')
    is_ok = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "确定"`]''')
    tv_title = ("accessibility id", "tv_title")
