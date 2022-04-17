# coding:utf-8

import pytest

from ayla_public.ReadConfig import ReadConfig
from ayla_public.SerialCom import SerialCom
from ayla_public.initAPP import initApp
from ayla_public.mylog import logger
from ayla_public.myallure import MyAllure
from pages_common.Page_adctin.addDeviceAction import AddDeviceAction
from pages_common.Page_adctin.inteligenceAction import IntelligenceAction
from pages_common.Page_adctin.loginAction import LoginAction
from pages_common.Page_adctin.mainAction import MainAction
from pages_common.Page_adctin.ownAction import OwnAction
from pages_common.Page_adctin.settingAction import SettingAction
from pages_common.Page_adctin.messageAction import MessageAction
from pages_common.Page_adctin.memberAction import MemberAction


def pytest_addoption(parser):
    parser.addoption(
        "--phonetype", action="store", default="ios", help="my phonetype: IOS or Android"
    )


@pytest.fixture(scope="module")
def phone_type(request):
    ret = request.config.getoption("--phonetype")
    return ret


@pytest.fixture(scope="module", autouse=True)
def driver_obj(phone_type):
    driver_obj = LoginAction(phone_type)
    logger.info("开启浏览器")
    yield driver_obj.driver
    driver_obj.restart_app()
    logger.info("关闭浏览器")


@pytest.fixture(scope="module")
def myallure_obj(phone_type):
    driver_obj = LoginAction(phone_type).driver
    myallure_obj = MyAllure(driver_obj)
    yield myallure_obj


@pytest.fixture(scope="module")
def login_obj(phone_type):
    loginaction = LoginAction(phone_type)
    yield loginaction


@pytest.fixture(scope="module")
def own_obj(phone_type):
    ownaction = OwnAction(phone_type)
    yield ownaction


@pytest.fixture(scope="module")
def setting_obj(phone_type):
    settingaction = SettingAction(phone_type)
    yield settingaction


@pytest.fixture(scope="module")
def message_obj(phone_type):
    messageacion = MessageAction(phone_type)
    yield messageacion


@pytest.fixture(scope="module")
def member_obj(phone_type):
    memberacion = MemberAction(phone_type)
    yield memberacion


@pytest.fixture(scope="module")
def main_obj(phone_type):
    mainaction = MainAction(phone_type)
    yield mainaction


@pytest.fixture(scope="module")
def intel_obj(phone_type):
    intelligenceaction = IntelligenceAction(phone_type)
    yield intelligenceaction


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    phone_type = request.config.getoption("--phonetype")
    driver = LoginAction(phone_type).driver
    myallure = MyAllure(driver)
    myallure.save_scree_image()
    myallure.save_image_to_allure()


@pytest.fixture(scope="module")
def addDevice_obj():
    deviceaction = AddDeviceAction(phone_type='android')
    yield deviceaction


@pytest.fixture()
def serialCom_obj():
    serialCom = SerialCom()
    yield serialCom
