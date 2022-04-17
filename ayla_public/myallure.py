import os
import time

import allure
from ayla_public.public import get_pathfile
from ayla_public.mylog import logger


class MyAllure:
    def __init__(self, driver):
        self.driver = driver
        self.error_img = get_pathfile()

    def allure_step(self, title):
        '''操作步骤'''
        with allure.step(title):
            logger.info(title)

    def save_scree_image(self):
        """
        对当前页面进行截图
        :return:
        """
        start_time = time.time()
        filename = 'image/{}.png'.format(start_time)
        file_path = os.path.join(self.error_img, filename)
        self.driver.save_screenshot(file_path)
        logger.info("错误页面截图成功，图表保存的路径 :{}".format(file_path))
        return file_path

    def save_image_to_allure(self):
        """
        保存失败的截图到allure报告中
        :return:
        """
        file_path = self.save_scree_image()
        with open(file_path, "rb") as f:
            file = f.read()
            allure.attach(file, "失败截图", allure.attachment_type.PNG)
