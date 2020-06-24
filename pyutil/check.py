# -*- coding: utf-8 -*-
"""
@FileName    : check.py
@Description : 检查各种条件
@Author      : 齐鲁桐
@Email       : qilutong@yahoo.com
@Time        : 2019-12-23 下午11:32
@Modify      : None
"""
from __future__ import absolute_import, division, print_function

import os


def chk_sep(path):
    """
    判断路径字符串末尾是否有分隔符
    :param path: 要检查的路径
    :return: 布尔值
    """
    if path[-1] != os.path.sep:
        return False
    else:
        return True


def chk_dir(directory):
    """
    判断目录是否存在
    :param directory: 目录路径
    :return:
    """
    if os.path.exists(directory):
        if os.path.isdir(directory):
            print("目录{}已经存在".format(directory))
            return True
        else:
            print("路径{}存在，但并不是目录".format(directory))
            return False
    else:
        print("目录{}不存在".format(directory))
        return False


def chk_file(file_name):
    """
    判断文件是否存在
    :param file_name: 文件路径
    :return:
    """
    if os.path.exists(file_name):
        if os.path.isfile(file_name):
            print("文件{}已经存在".format(file_name))
            return True
        else:
            print("路径{}存在，但并不是文件".format(file_name))
            return False
    else:
        print("文件{}不存在".format(file_name))
        return False


if __name__ == '__main__':
    a = ['aaa', 'bbb', 'ccc']
    path1 = os.path.sep.join(a)
    path2 = os.path.sep.join(a) + os.path.sep
    print(chk_sep(path1))
    print(chk_sep(path2))
