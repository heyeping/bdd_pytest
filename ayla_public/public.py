import os
import random
import signal
import string


class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass


def get_pathfile():
    path = "/".join(os.path.realpath(__file__).split("/")[:-2])
    return path


def kill_process():
    try:
        for line in os.popen("ps aux | grep mymiddleware"):
            filds = line.split()
            pid = filds[1]
            os.kill(int(pid), signal.SIGKILL)
    except:
        pass


def creat_massage():
    # dos信息
    massage = [
        '<div claSS="eidt-name" Style="padding: 0px 5px; font-Size: 6.64111px;"><i Style="font-family: &quot;Material IconS&quot;;"></i></div>',
        'T@#@*……%（&*@#Y@&……#……@#@……&#%@#（@（#……@*……#*@#……@*', '#Select * from feedback where 1=1']
    return random.choice(massage)


def random_str(len=6):
    # 获取随机名称
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for x in range(len))


def random_int(len=10):
    # 获取随机电话号码
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return "1" + ''.join(random.choice(letters) for x in range(len))
