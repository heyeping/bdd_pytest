# coding:utf-8
import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.ownPage import OwnPage
from pages_common.Page_ui.settingPage import SettingPage


class OwnAction(BaseAction, OwnPage):

    # 跳转页面text内容包含 头像 昵称
    def get_check_massage(self, type):
        time.sleep(1)
        my_icon = self.find_my_elements(self.my_icon if type == "ios" else self.my_icon)[0]
        my_icon_txt = my_icon.get_attribute('value')
        time.sleep(1)
        nickname = self.find_my_elements(self.nickname if type == "ios" else self.nickname)[1]
        nickname_txt = nickname.get_attribute('value')
        return my_icon_txt, nickname_txt

    # 点击元素设置按钮
    def clickSetting(self, type):
        self.click(ele=self.setting if type == "ios" else self.setting)

    # 点击个人中心
    def clickCenter(self, type):
        self.click(ele=self.my_top_arrow if type == "ios" else self.my_top_arrow)

    # 点击头像
    def clickavatar(self, type):
        my_icon = self.find_my_elements(self.my_icon if type == "ios" else self.my_icon)[0]
        my_icon.click()

    # 更换头像
    def changeAvatar(self, type):
        time.sleep(1)
        self.click(ele=self.photograph if type == "ios" else self.photograph)
        self.click(ele=self.photoCapture if type == "ios" else self.photoCapture)
        self.click(ele=self.use_photo if type == "ios" else self.use_photo)
        time.sleep(1)

    # 点击昵称
    def clickNickname(self, type):
        time.sleep(1)
        nickname = self.find_my_elements(self.nickname if type == "ios" else self.nickname)[1]
        time.sleep(1)
        nickname.click()

    # 更换昵称
    def changeNickname(self, txt, type):
        time.sleep(1)
        element = self.find_my_element(ele=self.modifynickname if type == "ios" else self.modifynickname)
        element.clear()
        time.sleep(1)
        element.send_keys(txt)
        self.click(ele=self.savebutton if type == "ios" else self.savebutton)

    # 保存修改
    def saveModify(self, type):
        self.click(ele=self.savebutton if type == "ios" else self.savebutton)

    # 获取修改前的昵称
    def get_before_nickname(self, type):
        check_nickname = self.find_my_elements(self.check_nickname if type == "ios" else self.check_nickname)[0]
        time.sleep(1)
        text = check_nickname.get_attribute("value")
        return text

    # 点击密码
    def click_pwd(self, type):
        my_pwd = self.find_my_elements(self.pwd if type == "ios" else self.pwd)[3]
        time.sleep(1)
        my_pwd.click()

    # 确认第三方服务
    def click_I_know(self, type):
        self.click(self.i_know if type == "ios" else self.i_know)

    # 输入密码,点击下一步
    def send_old_pwd(self, type, txt):
        self.txt_input(self.et_input if type == "ios" else self.et_input, txt=txt)
        self.click(self.btn_next if type == "ios" else self.btn_next)

    # 输入新密码点击完成
    def send_new_pwd(self, type, txt):
        elements = self.find_my_elements(self.et_input if type == "ios" else self.et_input)
        elements[0].send_keys(txt)
        elements[1].send_keys(txt)

    # 点击完成
    def click_ok(self, type):
        self.click(self.tv_ok if type == "ios" else self.tv_ok)

    # 校验是否有家庭
    def check_family(self, type):
        result = self.is_element_present(self.add_family if type == "ios" else self.add_family)
        return result

    # 点击房间
    def click_room(self, type):
        self.init_family(type)
        self.click(self.room if type == "ios" else self.room)

    # 房间管理
    def check_room_management(self, type):
        result = self.is_element_present(self.room_management if type == "ios" else self.room_management)
        assert result

    # 点击添加房间
    def click_add_room_button(self, type):
        self.click(self.add_room_btn if type == "ios" else self.add_room_btn)

    # 输入房间名称，点击确定
    def input_room_name(self, type, txt):
        self.clear(self.et_input if type == "ios" else self.et_input)
        self.txt_input(self.et_input if type == "ios" else self.et_input, txt=txt)

    # 点击保存
    def click_save(self, type):
        self.click(self.btn_save if type == "ios" else self.btn_save)

    # 获取房间管理页面第一个房间名称
    def get_one_room_name(self, type):
        room_name_ele = self.find_my_elements(self.room_name if type == "ios" else self.room_name)[0]
        return room_name_ele.get_attribute("value")

    # 拖动新增房间删除房间
    def move_new_room(self, type):
        self.swipLeft(y=0.14)
        time.sleep(2)

    # 确认删除房间
    def confirm_the_deletion(self, type):
        self.click(self.del_room_ok if type == "ios" else self.del_room_ok)

    # 修改房间名称
    def editor_room_name(self, type, txt):
        room_name_ele = self.find_my_elements(self.room_name if type == "ios" else self.room_name)[0]
        room_name_ele.click()
        time.sleep(1)
        et_input = self.find_my_element(self.et_input if type == "ios" else self.et_input)
        et_input.clear()
        time.sleep(1)
        et_input.send_keys(txt)
        time.sleep(1)
        self.click_save(type)

    # 删除新增房间
    def del_new_room(self, type):
        self.click(self.room_del if type == "ios" else self.room_del)

    # 点击设备
    def click_device(self, type):
        time.sleep(1)
        self.click(self.device if type == "ios" else self.device)

    # 判断是否有设备，有设备进入高级页
    def is_device(self, type):
        try:
            time.sleep(1)
            self.click(self.tv_device if type == "ios" else self.tv_device)
            time.sleep(1)
            result = self.is_element_present(self.remove_device if type == "ios" else self.remove_device)
            assert result
        except:
            result = self.is_element_present(self.no_device if type == "ios" else self.device)
            assert result

    # 我的--信息中心
    def click_msg(self, type):
        self.click(self.msg_Enterance if type == "ios" else self.msg_Enterance)

    # 初始化家庭
    def init_family(self, type):
        if self.check_family(type):
            self.click(self.add_family if type == "ios" else self.add_family)
            self.addFamily(type, '自动化添加家庭')
        elif self.check_family_name(type, '自动化添加家庭'):
            pass
        else:
            self.clickadd(type)
            self.addFamily(type, '自动化添加家庭')

    # 点击+号
    def clickadd(self, type):
        if self.check_family(type):
            self.click(self.add_family if type == "ios" else self.add_family)
        else:
            self.click(self.iv_add if type == "ios" else self.iv_add)

    # 点击>进入下一级
    def click_iv_right(self, type, index):
        time.sleep(1)
        ele = self.find_my_elements(self.iv_right if type == "ios" else self.iv_right)[index]
        time.sleep(1)
        ele.click()
        time.sleep(1)

    # 创建家庭
    def addFamily(self, type, family_name):
        time.sleep(1)
        self.click(self.add_family_ok if type == "ios" else self.add_family_ok)
        time.sleep(1)
        self.click(self.family_name if type == "ios" else self.family_name)
        time.sleep(1)
        self.txt_input(self.et_input if type == "ios" else self.et_input, family_name)
        time.sleep(1)
        self.click(self.save_family if type == "ios" else self.save_family)
        time.sleep(1)
        self.click(self.save_family_last if type == "ios" else self.save_family_last)
        time.sleep(2)

    # 点击我的--成员按钮
    def click_member(self, type):
        self.click(self.member_icon if type == "ios" else self.member_icon)

    # 校验家庭是否创建成功
    def check_family_name(self, type, family_name):
        count = 0
        while count < 5:
            text = self.find_my_element(self.tv_home_name if type == "ios" else self.tv_home_name).get_attribute(
                "value")

            if text == family_name:
                return True
            count += 1
            self.swipLeft(y=0.28)
        else:
            return False

    # 删除家庭
    def delete_family(self, type):
        time.sleep(1)
        self.click(self.iv_home_setting if type == "ios" else self.iv_home_setting)
        time.sleep(1)
        self.click(self.btn_delete if type == "ios" else self.btn_delete)

    # 确认删除
    def delete_ok(self, type):
        time.sleep(1)
        self.click(self.iv_ok if type == "ios" else self.iv_ok)
        time.sleep(1)

    # 点击我的--当前家庭下的setting按钮
    def click_family_setting(self, type):
        self.click(self.iv_home_setting if type == "ios" else self.iv_home_setting)

    # 我的界面-点击当前家庭下的setting--进入后点击"成员管理"
    def click_memberMange(self, type):
        self.click(self.member_management if type == "ios" else self.member_management)

    # 返回按钮
    def back_button(self, type):
        self.click(self.navi_back if type == "ios" else self.navi_back)

    # 删除初始化的房间
    def del_init_family(self, type):
        self.delete_family(type)
        self.delete_ok(type)

    # 选择家庭位置
    def select_location(self, type):
        self.click(self.province if type == "ios" else self.province)
        self.click(self.city if type == "ios" else self.city)
        self.click(self.area if type == "ios" else self.area)

    # 校验信息
    def check_tv_desc_msg(self, type, index):
        ele = self.find_my_elements(self.tv_desc if type == "ios" else self.tv_desc)[index]
        msg = ele.get_attribute('value')
        assert msg != None
