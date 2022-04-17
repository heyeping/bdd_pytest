# @File  : addDevicePage.py
# @Author: yeping.he
# @Time  : 2021/12/13 13:55:35
from selenium.webdriver.common.by import By
class AddDevicePage():

    deviceInfo = {
        '照明':(By.XPATH, '''//*[@text="照明"]'''),
        '添加设备+':(By.ID, '''iv_add_devices'''),
        '雅典智能射灯':(By.XPATH, '''//*[@text="雅典智能射灯"]'''),
        '雅典智能网关':(By.XPATH, '''//*[@text="雅典智能网关"]'''),
        '已确认上述操作': (By.XPATH, '''//*[@text="已确认上述操作"]'''),
        '我已确认上述操作': (By.XPATH, '''//*[@text="我已确认上述操作"]'''),
        '手动输入': (By.XPATH, '''//*[@text="手动输入"]'''),
        '请输入设备ID': (By.XPATH, '''//*[@text="请输入设备ID"]'''),
        '设备ID': (By.ID, '''ddi_et_dsn'''),
        '客厅': (By.XPATH, '''//*[@text="客厅"]'''),
        '完成': (By.XPATH, '''//*[@text="完成"]'''),



        '下一步':(By.XPATH, '''//*[@text="下一步"]'''),
        'ByText':'''//*[@text="{0}"]'''
             }


