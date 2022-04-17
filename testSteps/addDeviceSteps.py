# @File  : addDeviceSteps.py
# @Author: yeping.he
# @Time  : 2021/11/29 15:09:14
import os
import time
from functools import partial

import allure
import pytest_bdd
from pytest_bdd import when, parsers, given, then
from selenium.webdriver.common.by import By

from ayla_public import myallure
from ayla_public.mylog import Log
from ayla_public.myallure import MyAllure
from ayla_public.public import get_pathfile
from pages_common.Page_adctin.addDeviceAction import AddDeviceAction

logger = Log()
feature_file = os.path.join(get_pathfile(), "features/homePage/add_device.feature")

#使用functools.partial，可以不用多次输入feature文件
scenario = partial(pytest_bdd.scenario, feature_file)

@scenario(u"添加网关")
def test_add_oneDevices():
    pass

@given(parsers.parse("点击 {button}"))
@when(parsers.parse("点击 {button}"))
def selectOneDriver(addDevice_obj,button):
    logger.info(u"点击{0}".format(button))
    addDevice_obj.clickOn(addDevice_obj.deviceInfo[button])

@when(parsers.parse("{equipmentNetType}：{equipmentNet} 添加"))
@given(parsers.parse("{equipmentNetType}：{equipmentNet} 添加"))
def NetDevice(addDevice_obj,equipmentNetType,equipmentNet):
    logger.info('选择:{0}'.format(equipmentNetType))
    addDevice_obj.clickOn((By.XPATH, addDevice_obj.deviceInfo['ByText'].format(equipmentNetType)))

    logger.info('选择设备:{0}'.format(equipmentNet))
    addDevice_obj.clickOn((By.XPATH,addDevice_obj.deviceInfo['ByText'].format(equipmentNet)))


@given(parsers.parse("输入 {button} ： {DSN}"))
@when(parsers.parse("输入 {button} ： {DSN}"))
def setTexts(addDevice_obj,button,DSN):
    logger.info(u"{0}".format(button))
    print(button,DSN)
    print(addDevice_obj.deviceInfo[button])
    addDevice_obj.sendText(addDevice_obj.deviceInfo[button],DSN)




@when(parsers.parse("网关设备：{equipmentType} 类型设备 {equipmentName} 入网 {equipmentNet}"))
@given(parsers.parse("网关设备：{equipmentType} 类型设备 {equipmentName} 入网 {equipmentNet}"))
def toAutoNetWork(addDevice_obj,equipmentType,equipmentName,equipmentNet):
    logger.info('选择设备类型:{0}'.format(equipmentType))
    logger.info(addDevice_obj.deviceInfo['ByText'])
    addDevice_obj.clickOn((By.XPATH,addDevice_obj.deviceInfo['ByText'].format(equipmentType)))

    logger.info('选择设备:{0}'.format(equipmentName))
    addDevice_obj.clickOn((By.XPATH,addDevice_obj.deviceInfo['ByText'].format(equipmentName)))

    logger.info('选择网关:{0}'.format(equipmentNet))
    addDevice_obj.clickOn((By.XPATH,addDevice_obj.deviceInfo['ByText'].format(equipmentNet)))

@when(parsers.parse("开始 {equipmentName} 配网"))
def SendNet(addDevice_obj,serialCom_obj,equipmentName):
    ser=serialCom_obj.getSer(equipmentName)
    logger.info('第一次下发退网命令')
    serialCom_obj.leaveNet(ser)
    time.sleep(2)
    logger.info('第一次下发配网命令')
    serialCom_obj.startNet_command(ser,equipmentName)
    flage=False
    seconds = 0
    times = 1
    while True:
        time.sleep(1)
        ob=True
        try:
            addDevice_obj.driver.find_element_by_xpath('''//*[@text="已找到1个设备"]''')
        except:
            ob= False
        logger.info(ob)
        if  ob:
            logger.info('配网成功')
            flage=True
            break
        else:
            if times==3:
                logger.info('3次配网均失败')
                break
            seconds+=1
            logger.info('配网等待{0}秒'.format(seconds))
            if seconds==10:
                times+=1
                seconds=0
                logger.info('第{0}次下发退网命令'.format(times))
                serialCom_obj.leaveNet(ser)
                time.sleep(2)
                logger.info('第{0}次下发配网命令'.format(times))
                serialCom_obj.startNet_command(ser,equipmentName)
    if flage:
        addDevice_obj.driver.find_element_by_xpath('''//*[@text="下一步"]''').click()
        time.sleep(10)
        addDevice_obj.driver.find_element_by_xpath('''//*[@text="完成"]''').click()
    else:
        pass


@then(parsers.parse('检查设备：{equipmentName}'))
def cherkdevice(addDevice_obj,equipmentName):
    time.sleep(5)
    assert addDevice_obj.driver.page_source.find(equipmentName)!=-1

@then(parsers.parse('检查网关：{equipmentNet}'))
def cherkdevice(addDevice_obj,equipmentNet):
    time.sleep(5)
    assert addDevice_obj.driver.page_source.find(equipmentNet)!=-1
