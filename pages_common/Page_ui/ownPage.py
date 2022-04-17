# coding:utf-8
# own page
class OwnPage():
    own = ("accessibility id", '''tb_mine_n''')
    setting = ("accessibility id", '''iv_setting''')
    add_family = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "加入家庭"`]''')
    # 个人中心
    my_top_arrow = ("accessibility id", '''iv_avatar''')
    my_icon = ("accessibility id", "tv_title")
    photograph = ("accessibility id", "拍照")
    photoCapture = ("accessibility id", "PhotoCapture")
    use_photo = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "使用照片"`]''')
    done = ("accessibility id", "Done")

    nickname = ("accessibility id", "tv_title")
    modifynickname = ("accessibility id", "et_input")
    savebutton = ("accessibility id", """保存""")
    navi_back = ("accessibility id", """navi back""")
    check_nickname = ('accessibility id', """tv_desc""")

    pwd = ("accessibility id", "tv_title")
    i_know = ("accessibility id", "我知道了")
    btn_next = ("accessibility id", "btn_next")
    tv_ok = ("accessibility id", "完成")

    # 房间
    room = ("accessibility id", """iv_room""")
    add_room_btn = ("accessibility id", """添加房间""")
    btn_save = ("accessibility id", '''btn_save''')
    room_name = ("accessibility id", """tv_title""")
    room_back = ("accessibility id", '''navi back''')
    room_del = ("accessibility id", """trailing0""")
    room_test = ('-ios class chain', """**/XCUIElementTypeTable[`name == "rv_room"`]/XCUIElementTypeCell[1]""")
    room_management = ('-ios class chain', """**/XCUIElementTypeStaticText[`label == "房间管理"`]""")
    del_room_ok = ('-ios class chain', '''**/XCUIElementTypeStaticText[`label == "确定"`]''')

    # 成员
    member = ("accessibility id", '''iv_member''')

    # 设备
    device = ("accessibility id", '''iv_device''')
    tv_device = ("-ios class chain", '''**/XCUIElementTypeTable[`name == "rv_device"`]/XCUIElementTypeCell[1]''')
    remove_device = ("-ios class chain", '**/XCUIElementTypeStaticText[`label == "高级功能"`]')
    no_device = ("accessibility id", '''暂无设备请添加''')

    # 消息中心
    msg_Enterance = ("accessibility id", '''item_notice''')

    # 添加家庭
    iv_add = ("accessibility id", '''iv_add''')
    add_family_ok = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "确定"`]''')
    family_name = ("-ios class chain", '''**/XCUIElementTypeImage[`name == "iv_right"`][1]''')
    et_input = ("accessibility id", '''et_input''')
    save_family = ("accessibility id", '''保存''')
    save_family_last = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "保存"`]''')
    iv_right = ("accessibility id", '''iv_right''')

    # 成员
    member_icon = ("accessibility id", "iv_member")

    # 家庭名称
    tv_home_name = ("accessibility id", '''tv_home_name''')
    tv_home_name_ele = ("-ios class chain",
                        """**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]""")

    # 家庭设置
    iv_home_setting = ("accessibility id", "iv_home_setting")
    btn_delete = ("accessibility id", "btn_delete")
    iv_ok = ("accessibility id", "确定")
    iv_cancel = ("accessibility id", "取消")
    province = ("accessibility id", "安徽")
    city = ("accessibility id", "安庆")
    area = ("accessibility id", "大观区")
    tv_desc = ("accessibility id", "tv_desc")

    # 我的界面-点击当前家庭下的setting--进入后点击"成员管理"
    member_management = ("accessibility id", "item_member")

    # android
    iv_setting = ("id", "com.ayla.aylahome:id/iv_setting")
    btn_logout = ("id", "com.ayla.aylahome:id/btn_logout")
