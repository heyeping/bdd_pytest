import time

from ayla_public.ReadConfig import ReadConfig
from ayla_public.public import Single
from appium import webdriver


class DriverCreat(Single):
    def get_drive(self, phone_type):
        if not hasattr(self, '_driver'):
            readconfig = ReadConfig()
            if phone_type != "ios":
                desired_cpas = {
                    "platformName": readconfig.get_desired_caps_android("platformName"),
                    "platformVersion": readconfig.get_desired_caps_android("platformVersion"),
                    "deviceName": readconfig.get_desired_caps_android("deviceName"),
                    "appPackage": readconfig.get_desired_caps_android("appPackage"),
                    "appActivity": readconfig.get_desired_caps_android("appActivity"),
                    "noReset": readconfig.get_desired_caps_android("noReset")
                }
                self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cpas)
                # self._driver.implicitly_wait(10)
            else:
                desired_cpas = {
                    "platformName": readconfig.get_desired_caps_ios("platformName"),
                    "platformVersion": readconfig.get_desired_caps_ios("platformVersion"),
                    "deviceName": readconfig.get_desired_caps_ios("deviceName"),
                    "bundleId": readconfig.get_desired_caps_ios("bundleId"),
                    "udid": readconfig.get_desired_caps_ios("udid"),
                    "automationName": readconfig.get_desired_caps_ios("automationName"),
                    "noreset": readconfig.get_desired_caps_ios("noreset"),
                    'resetKeyboard': readconfig.get_desired_caps_ios("resetKeyboard"),
                }
                self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cpas)
                self._driver.implicitly_wait(10)
                self._driver.set_page_load_timeout(60)
                self._driver.set_script_timeout(60)
            self.driver = self._driver
        return self.driver
