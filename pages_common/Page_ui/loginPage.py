# coding:utf-8
# loginPage

class LoginPage():
    # ios
    usernameEle = ("-ios class chain", '''**/XCUIElementTypeTextField''')
    clearbutton = ("-ios class chain", '''**/XCUIElementTypeButton[`label == "right clear btn normal"`]''')
    loginTypeEle = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "密码登录"`]''')
    nextButtonEle = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "下一步"`]''')
    pwdEle = ("-ios class chain", '''**/XCUIElementTypeSecureTextField[`value == "请输入您的密码"`]''')
    loginButtonEle = ("-ios class chain", '''**/XCUIElementTypeStaticText[`label == "登录"`]''')
    logininput = ("-ios class chain", '''**/XCUIElementTypeImage[`name == "login_input_bg"`]''')

    welcomeHome = ("accessibility id", '''房间''')

    ok = ("accessibility id", '好')
    allow = ("accessibility id", "允许")
    agree = ("accessibility id", "同意")

    # android
    username_input = ("id", 'com.ayla.aylahome:id/edit_account')
    login_tv_toggle = ("id", 'com.ayla.aylahome:id/login_tv_toggle')
    mLoginBtn = ("id", 'com.ayla.aylahome:id/mLoginBtn')
    login_cb_agreement = ("id", 'com.ayla.aylahome:id/login_cb_agreement')
    pi_et_password = ("id", 'com.ayla.aylahome:id/pi_et_password')
