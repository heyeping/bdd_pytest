import configparser
import os
from ayla_public.public import get_pathfile

config = configparser.ConfigParser()


class ReadConfig():
    def __init__(self):
        path = get_pathfile()
        config_path = os.path.join(path, 'config', 'ayla_param.ini')
        config.read(config_path, encoding='utf-8')

    def get_desired_caps_ios(self, name):
        value = config.get('desired_caps_ios', name)
        return value

    def get_desired_caps_android(self, name):
        value = config.get('desired_caps_android', name)
        return value

    def get_login_massage(self, login_massage):
        value = config.get("login_massage", login_massage)
        return value

    def get_ayal_url(self, ayla_url):
        return config.get("ayla_url", ayla_url)

    def get_app_path(self, app_path):
        return config.get("app_path", app_path)


if __name__ == '__main__':
    a = ReadConfig().get_login_massage("userName")
    print(a)
