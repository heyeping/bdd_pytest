# @File  : networkAction.py
# @Author: yeping.he
# @Time  : 2021/11/26 10:09:52

from loguru import  logger
from pages_common.Page_adctin.BaseAction import BaseAction
from selenium.webdriver.common.by import By

from pages_common.Page_ui.addDevicePage import AddDevicePage


class AddDeviceAction(BaseAction,AddDevicePage):



    try:
        #点击事件
        def clickOn(self,button):
            self.click(button)
        #文本输入
        def sendText(self,ele,message):
            self.find_my_element(ele).set_text(message)

                  

    except BaseException as e:
        logger.debug(e)