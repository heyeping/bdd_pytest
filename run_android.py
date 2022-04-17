# -*- coding: utf-8 -*-
# @Time    : 2022/3/4 11:12 上午
# @Author  : jinxu
# @File    : run_android.py
import posix

import pytest
import os
import sys

from ayla_public.handle_file import handlefile
from ayla_public.mylog import logger
from ayla_public.initAPP import initApp
from ayla_public.public import get_pathfile
from mainRun.buildBeforeRun import get_Main_command
from ayla_public.public import get_pathfile, kill_process

if __name__ == "__main__":
    results_path = os.path.join(get_pathfile(), "report/allure-results")
    report_path = os.path.join(get_pathfile(), "report/allure-report")
    app = initApp()
    app.init_app_android()
    # 暂时注释
    # mymiddleware_path = os.path.join(get_pathfile(), "ayla_public/mymiddleware")
    # s=get_Main_command("zhijia")
    # commandlist=["-sq", "--phonetype=ios","--alluredir", results_path]+s

    # os.system("mitmdump -p 8999 -s {} &".format(mymiddleware_path))
    # pytest.main(commandlist)
    # pytest.main(["-sq", 'testSteps/loginSteps.py', "--alluredir", results_path, "--phonetype=ios"])
    pytest.main(["-sq", 'testSteps/loginSteps.py', "--phonetype=Android"])
    # pytest.main(["-sq", "--alluredir", results_path, "--phonetype=Android"])
    # os.system("allure generate {} -o {} --clean".format(results_path, report_path))
    # kill_process()
