# coding:utf-8
# 元素操作封装
import time

import selenium
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from ayla_public.DriverCreat import DriverCreat
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class BaseAction(object):

    def __init__(self, phone_type):
        self.driver = DriverCreat().get_drive(phone_type)
        self.wait = WebDriverWait(self.driver, 10)

    def find_my_element(self, ele):
        if ele[0].startswith("-ios") or ele[0].startswith("accessibility"):
            return self.driver.find_element(*ele)
        else:
            return self.wait.until(EC.presence_of_element_located(ele))

    def find_my_elements(self, ele):
        if ele[0].startswith("-ios") or ele[0].startswith("accessibility"):
            return self.driver.find_elements(*ele)
        else:
            return self.wait.until(EC.presence_of_all_elements_located(ele))

    def move_element(self, x1, y1, x2, y2):
        '''拖动位置'''
        TouchAction(self.driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).wait(500).release().perform()

    def click(self, ele):
        '''
        点击操作
        :param ele: 操作元素
        :return:
        '''
        time.sleep(1)
        element = self.find_my_element(ele)
        time.sleep(1)
        element.click()
        time.sleep(1)

    def txt_input(self, ele, txt):
        '''
        输入操作
        :param txt: 输入文本
        :param ele: 操作元素
        :return:
        '''
        element = self.find_my_element(ele)
        time.sleep(2)
        element.send_keys(txt)

    def is_element_present(self, ele):
        '''
        判断元素是否存在
        :param ele: 操作元素
        :return:
        '''
        try:
            element = self.find_my_element(ele)
        except:
            return False
        return True

    def get_ele_text(self, ele):
        '''
        获取元素文本
        :param ele:
        :return:
        '''
        element = self.find_my_element(ele)
        return element.text

    def clear(self, ele):
        '''
        清除元素数据
        :param ele:操作元素
        :return:
        '''
        element = self.find_my_element(ele)
        element.clear()

    def close(self):
        '''
        退出driver
        :return:
        '''
        self.driver.close_app()

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self, t=500):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t=500):
        l = self.getSize()
        print(l)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t=500, y=0.5):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * y)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t=500, y=0.5):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * y)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 元素向下滑动
    def swipeleDown(self, ele, t=1):
        ele = self.find_my_element(ele)
        w = ele.size['width']
        h = ele.size['height']
        x = ele.location["x"]
        y = ele.location["y"]
        x1 = int(w / 2 + x)
        y1 = int(h / 5 * 4 + y)
        y2 = int(h / 5 * 3 + y)
        for i in range(t):
            self.driver.swipe(x1, y1, x1, y2, 1000)

    # 元素向左滑动
    def swipeleLeft(self, ele, t=1):
        ele = self.find_my_element(ele)
        w = ele.size["width"]
        h = ele.size['height']
        x = ele.location["x"]
        y = ele.location["y"]
        y1 = int(h / 2 + y)
        x1 = int(w / 5 * 4 + x)
        x2 = int(w / 5 * 2 + x)
        for i in range(t):
            self.driver.swipe(x1, y1, x2, y1, 1000)

    # 长按某元素
    def Long_press_ele(self, ele):
        ele = self.find_my_element(ele)
        w = ele.size["width"]
        h = ele.size['height']
        x = ele.location["x"]
        y = ele.location["y"]
        x1 = int(x + w / 2)
        y1 = int(y + h / 2)
        TouchAction(self.driver).long_press(ele, x1, y1, duration=1000).wait(1000).release().perform()

    # 指定元素滑动
    def drag(self, duration, fromX, fromY, toX, toY, ele=None):
        self.driver.execute_script(
            "mobile:dragFromToForDuration",
            {"duration": duration, "element": ele, "fromX": fromX, "fromY": fromY, "toX": toX, "toY": toY}
        )
