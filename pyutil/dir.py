# -*- coding: utf-8 -*-
"""
@FileName    : dir.py
@Description : None
@Author      : 齐鲁桐
@Email       : qilutong@yahoo.com
@Time        : 2020-06-24 17:33
@Modify      : None
"""
from __future__ import absolute_import, division, print_function

import os

from .check import chk_dir


def create(directory):
    """
    创建目录
    :param directory: 目录名，路径形式
    :return:
    """
    if chk_dir():
        return True
    else:
        try:
            os.makedirs(directory)
            return True
        except Exception as e:
            print(e)
            return False
