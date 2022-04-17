
class EquipmentBean(object):
    params={
        '雅典智能射灯':{'code':'plugin network-steering start 1\n\r','serialPath':'/dev/cu.usbserial-AR0KJ21N'}
    }
    def getParams(self):
        return self.params