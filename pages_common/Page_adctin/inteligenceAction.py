# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 3:21 下午
# @Author  : jinxu
# @File    : inteligenceAction.py
import time

from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.inteligencePage import Intelligence


class IntelligenceAction(BaseAction, Intelligence):

    # 点击智控进入智控界面
    def click_control(self, type):
        self.click(self.inte_control if type == "ios" else self.inte_control)

    # 校验是否为空
    def check_info(self, type):
        self.is_element_present(self.empty_info if type == "ios" else self.empty_info)

    # 点击添加
    def click_add(self, type):
        self.click(self.add_btn if type == "ios" else self.add_btn)

    # 点击选项列表，index表示第几行的
    def click_tv_title(self, type, index):
        ele = self.find_my_elements(self.tv_title if type == "ios" else self.tv_title)[index]
        ele.click()

    # 点击添加动作
    def click_add_item(self, type):
        try:
            ele = self.find_my_elements(self.btn_add_item if type == "ios" else self.btn_add_item)[1]
            ele.click()
        except:
            ele = self.find_my_elements(self.iv_action if type == "ios" else self.iv_action)[1]
            ele.click()

    # 点击选项列表的选择项，index表示第几行的
    def click_iv_right(self, type, index):
        ele = self.find_my_elements(self.iv_right if type == "ios" else self.iv_right)[index]
        ele.click()

    # 点击选择设备状态
    def choice_device_status(self, type, index):
        ele = self.find_my_elements(self.device_status if type == "ios" else self.device_status)[index]
        ele.click()

    # 点击确定
    def click_sure_button(self, type):
        self.click(self.sure_button if type == "ios" else self.sure_button)

    # 点击下一步
    def click_next_button(self, type):
        self.click(self.next_button if type == "ios" else self.next_button)

    # 添加设备动作
    def add_device_action(self, type, index):
        time.sleep(1)
        self.click_add_item(type)
        time.sleep(1)
        self.click_tv_title(type, 0)
        time.sleep(1)
        self.click_tv_title(type, index)
        time.sleep(1)
        if index > 0:
            index = 0
        self.click_tv_title(type, index)
        time.sleep(1)
        self.choice_device_status(type, index)
        time.sleep(1)
        self.click_sure_button(type)
        time.sleep(1)
        self.click_next_button(type)
        time.sleep(1)

    # 添加延时
    def add_time_delay(self, type):
        time.sleep(1)
        self.click_add_item(type)
        time.sleep(1)
        self.click_tv_title(type, 1)
        time.sleep(1)
        self.click_next_button(type)
        time.sleep(1)

    # 点击保存
    def click_save_button(self, type):
        self.click(self.save_button if type == "ios" else self.save_button)

    # 输入联动名称
    def input_intel_name(self, type, name):
        time.sleep(1)
        self.click(self.clear_text if type == "ios" else self.clear_text)
        time.sleep(1)
        self.txt_input(self.input_name if type == "ios" else self.input_name, name)

    # 校验联动名称
    def check_name(self, type, name='自动化添加一键联动'):
        try:
            value = self.get_ele_text(self.tv_name if type == "ios" else self.tv_name)
            if value == name:
                return True
        except:
            ele = self.find_my_elements(self.tv_name if type == "ios" else self.tv_name)
            for i in ele:
                value = i.get_attribute('value')
                if value == name:
                    return True
            else:
                return False

    # 删除全部一键联动
    def del_control(self, type):
        for i in range(5):
            ret = self.is_element_present(self.empty_info if type == "ios" else self.empty_info)
            if ret:
                return ret
            else:
                ele = self.find_my_elements(self.iv_more if type == "ios" else self.iv_more)
                time.sleep(1)
                ele[0].click()
                time.sleep(1)
                self.click(self.del_button if type == "ios" else self.del_button)
                time.sleep(1)
                self.click(self.is_ok if type == "ios" else self.is_ok)
                time.sleep(1)

    # 点击一键联动更多
    def click_more(self, type):
        ele = self.find_my_elements(self.iv_more if type == "ios" else self.iv_more)
        time.sleep(1)
        ele[0].click()
        time.sleep(1)

    # 点击删除按钮
    def click_del_button(self, type):
        self.click(self.del_button if type == "ios" else self.del_button)
        time.sleep(1)
        self.click(self.is_ok if type == "ios" else self.is_ok)
        time.sleep(1)

    # 添加一键执行完整流程
    def add_complete_implementation(self, type):
        self.click_add(type)
        self.click_tv_title(type, index=0)
        self.add_device_action(type, index=0)
        self.click_save_button(type)
        name = '自动化添加一键联动'
        self.input_intel_name(type, name=name)
        self.click_sure_button(type)
        ret = self.check_name(type)
        assert ret

    # 点击修改的选项
    def click_right_in_arrow(self, type, index):
        ele = self.find_my_elements(self.right_in_arrow if type == "ios" else self.right_in_arrow)
        ele[index].click()

    # 点击要修改的icon并保存
    def click_iv_icon(self, type, index):
        ele = self.find_my_elements(self.iv_icon if type == "ios" else self.iv_icon)
        ele[index].click()
        time.sleep(1)
        self.click(self.btn_save if type == "ios" else self.btn_save)

    # 点击取消并退出
    def click_canel_button(self, type):
        self.click(self.canel_button if type == "ios" else self.canel_button)
        time.sleep(1)
        self.click(self.is_sure if type == "ios" else self.is_sure)
        time.sleep(1)

    # 删除动作
    def del_action(self, type):
        time.sleep(1)
        self.swipeleLeft(self.rv_action if type == "ios" else self.rv_action)
        time.sleep(1)
        self.click(self.trailing0 if type == "ios" else self.trailing0)

    # 场景速配
    def click_matching_button(self, type):
        self.click(self.matching_button if type == "ios" else self.matching_button)

    # 校验是否有选择房间元素
    def check_choice_room(self, type):
        ret = self.is_element_present(self.choice_room if type == "ios" else self.choice_room)
        return ret
