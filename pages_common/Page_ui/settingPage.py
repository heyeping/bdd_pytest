# coding:utf-8
# iv_setting page
class SettingPage():
    # 用户协议
    userAgreement = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "用户协议"`]''')
    userAgreementTittle = ("accessibility id", '''软件许可及服务协议''')
    navi_back = ("accessibility id", '''navi back''')

    # 隐私政策
    privacy = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "隐私协议"`]''')
    privacyTitle = ('-ios class chain', '''**/XCUIElementTypeStaticText[`label == "隐私政策"`]''')

    # 退出登陆
    loginOutEle = ("accessibility id", '''btn_logout''')

    # 清除缓存
    cache = ("-ios class chain", """**/XCUIElementTypeTable[`name == "rv_setting"`]/XCUIElementTypeCell[3]""")
    desc_1 = ("accessibility id", "tv_desc")

    # 问题反馈
    feedback = ('-ios class chain', '**/XCUIElementTypeTable[`name == "rv_setting"`]/XCUIElementTypeCell[7]')
    cancel = ("accessibility id", "取消")
    words_count = ("accessibility id", "tv_words_count")
    input_issue = ("accessibility id", "input_issue")
    rv_photo = ("accessibility id", "rv_photo")
    pictures = ("accessibility id", "拍照")
    PhotoCapture = ("accessibility id", "PhotoCapture")
    use_pictures = ('-ios class chain', '**/XCUIElementTypeButton[`label == "使用照片"`]')
    et_input = ("accessibility id", "et_input")
    btn_submit = ("accessibility id", "btn_submit")
