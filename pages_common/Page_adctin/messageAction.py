# coding:utf-8
# @Time   :2022/2/15 16:16
# @Author :Nicholas.liu
# @File   :messageAction.py
# @Software   :bbd_test
import time

from loguru import logger
from pages_common.Page_adctin.BaseAction import BaseAction
from pages_common.Page_ui.messagePage import MessagePage


class MessageAction(BaseAction, MessagePage):

    # 我的--信息中心-点击日历icon
    def click_calendar(self, type):
        self.click(self.msg_calendar_icon if type == "ios" else self.msg_calendar_icon)

    # 我的 - -信息中心 - 点击日历 OK
    def click_calendar_ok(self, type):
        self.click(self.msg_calendar_ok if type == "ios" else self.msg_calendar_icon)

    # 选择下个月的24号
    def click_next_month(self, type):
        self.swipLeft()
        time.sleep(2)
        # 点击下个月24号
        self.click(self.msg_next_month if type == "ios" else self.msg_calendar_icon)

    # 点击收藏信息
    def fist_collect_msg(self, type):
        time.sleep(1)
        ele = self.find_my_elements(self.msg_collect_icon if type == "ios" else self.msg_calendar_icon)[0]
        time.sleep(1)
        ele.click()

    # 取消收藏
    def send_collect_msg(self, type):
        time.sleep(1)
        ele = self.find_my_elements(self.msg_collect_icon if type == "ios" else self.msg_calendar_icon)[0]
        time.sleep(1)
        ele.click()

    # 切换到收藏  TAB
    def switch_to_collectTab(self, type):
        self.click(self.msg_collect_tab if type == "ios" else self.msg_calendar_icon)

    # 获取收藏消息的时间
    def get_msg_time(self, type):
        ele = self.find_my_elements(self.tv_time if type == "ios" else self.tv_time)[1]
        txt = ele.get_attribute('value')
        return txt

    # 校验消息是否存在
    def check_msg_is(self, type):
        txt = self.get_ele_text(self.empty_set_title if type == "ios" else self.empty_set_title)
        return txt

    # 得到信息对象体
    def getMessageObj(self, type):
        try:
            collectobj = self.find_my_element(self.msg_collect_icon if type == "ios" else self.msg_collect_icon)
            assert collectobj != None
        except:

            no_message_obj = self.find_my_element(self.msg_no_message if type == "ios" else self.msg_no_message)
            assert no_message_obj != None
        else:
            assert 1 == 0

    # 点击消息
    def to_msg(self, type):
        ele = self.find_my_elements(self.tv_content if type == "ios" else self.tv_content)[0]
        ele.click()

    # 校验是否进入消息详情
    def check_to_content(self, type):
        self.is_element_present(self.tab_message if type == "ios" else self.tab_message)

    # 点击返回按钮
    def click_back_button(self, type):
        self.click(self.back_button if type == "ios" else self.back_button)

    # 校验是否进入消息中心
    def check_to_msg(self, type):
        time.sleep(1)
        ret = self.is_element_present(self.tv_read if type == "ios" else self.tv_read)
        assert ret

    # 删除收藏的消息
    def delete_collect(self, type):
        self.swipeleLeft(self.rv_message if type == "ios" else self.rv_message)

    # 点击删除按钮
    def click_del_button(self, type):
        self.click(self.del_button if type == "ios" else self.del_button)

    # 点击全部已读
    def click_all_read(self, type):
        self.click(self.tv_read if type == "ios" else self.tv_read)

    # 长按进入编辑页
    def Long_press(self, type):
        self.Long_press_ele(self.rv_message1 if type == "ios" else self.rv_message1)

    # 点击复选框
    def click_multi_pick(self, type):
        self.click(self.iv_multi_pick if type == "ios" else self.iv_multi_pick)

    # 编辑页的删除按钮
    def click_delete(self, type):
        self.click(self.tv_delete if type == "ios" else self.tv_delete)

    # 点击取消按钮
    def click_cancel(self, type):
        self.click(self.cancel_button if type == "ios" else self.tv_delete)

    # 点击完成退出编辑页
    def click_isok(self, type):
        self.click(self.is_ok if type == "ios" else self.is_ok)
