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


def check_sep(path):
    """
    判断路径字符串末尾是否有分隔符，没有则添加
    :param path: 要检查的路径
    :return: 新路径
    """
    if path[-1] != os.path.sep:
        path = path + os.path.sep
    return path


def check_dir(directory):
    """
    判断目录是否存在，不存在则创建
    :param directory: 目录名
    :return:
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
