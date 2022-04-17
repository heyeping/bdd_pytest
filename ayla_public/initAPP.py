# coding:utf-8
# @Time   :2022/2/9 10:41
# @Author :Nicholas.liu
# @File   :initAPP.py
# @Software   :bbd_test

# install APP and uninstall APP

import os
import time

import requests

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import get_pathfile

readconfig = ReadConfig()


class initApp():
    def appPath_ios(self):
        return os.path.join(get_pathfile(), readconfig.get_app_path("ayla_ios_app_path"))

    def uninstallApp_ios(self):
        os.system("ideviceinstaller -U {}".format(readconfig.get_desired_caps_ios("bundleId")))

    def installAPP_ios(self):
        os.system("ideviceinstaller -i {}".format(self.appPath_ios()))

    def isappPresent_ios(self):
        os.system("ios-deploy --id {} --exists --bundle_id {}".format(readconfig.get_desired_caps_ios("udid"),
                                                                      readconfig.get_desired_caps_ios("bundleId")))

    def appPath_android(self):
        return os.path.join(get_pathfile(), readconfig.get_app_path("ayla_android_app_path"))

    def installApp_android(self):
        os.system("/Users/ayla/Library/Android/sdk/platform-tools/adb install -r {}".format(self.appPath_android()))

    def init_app_ios(self):
        self.uninstallApp_ios()
        time.sleep(5)
        self.installAPP_ios()
        time.sleep(5)
        self.isappPresent_ios()

    def init_app_android(self):
        self.installApp_android()
        time.sleep(5)


if __name__ == "__main__":
    app = initApp()
    print(app.installApp_android())
