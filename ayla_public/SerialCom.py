# @File  : SerialCom.py
# @Author: yeping.he
# @Time  : 2021/12/03 16:03:09

import serial
from loguru import logger

from ayla_public.EquipmentBean import EquipmentBean


class SerialCom():

    def __init__(self):
        #这里有三个参数，第一个是连接的端口，第二个是波特率，第三个是超时时间
        self.jsonO=EquipmentBean().getParams()

    def getSer(self,equipment_name):
        return serial.Serial(self.jsonO[equipment_name]['serialPath'], 115200, timeout=3)
    # 配网指令
    def startNet_command(self,ser,equipment_name):
        logger.info(u'下发配网指令')
        ser.write(self.jsonO[equipment_name]['code'].encode('utf-8'))

    #离网指令
    def leaveNet(self,ser,):
        logger.info(u'下发退网指令')
        leave_com = "network leave\n\r"
        ser.write(leave_com.encode('utf-8'))

    #开启debug的log模式
    def debug_log(self,ser):
        logger.info(u'下发开启debug模式')
        debug_com = "log debug2\n\r"
        ser.write(debug_com.encode('utf-8'))



if __name__== '__main__':
    s = SerialCom('雅典智能射灯')
    s.startNet_command()


