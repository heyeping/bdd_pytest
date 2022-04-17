# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 3:39 下午
# @Author  : jinxu
# @File    : handle_file.py
import os

from ayla_public.public import get_pathfile

case_dir = os.path.join(get_pathfile(), 'testSteps')


class HandleDirFile:
    def get_file_info(self, case_dir_own):
        '''获取文件信息'''
        filepath_info = {}
        filepath_list = []
        sub_dir_list = []
        for root_dir, sub_dir, files in os.walk(case_dir_own):

            sub_dir_list.append(sub_dir)
            for i in range(0, len(files)):
                if files[i].endswith('py') and not files[i].endswith('__.py'):
                    filepath_list.append(root_dir + "/" + files[i])

        for sub_dir in sub_dir_list[0]:
            filepath_l = []
            for i in range(0, len(filepath_list)):
                title_info = filepath_list[i].split("/")[-3]
                if sub_dir == title_info:
                    filepath_l.append(filepath_list[i])
            filepath_info[sub_dir] = filepath_l

        return filepath_info


handlefile = HandleDirFile().get_file_info(case_dir)

