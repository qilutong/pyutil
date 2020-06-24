# -*- coding: utf-8 -*-
"""
@FileName    : path.py
@Description : None
@Author      : 齐鲁桐
@Email       : qilutong@yahoo.com
@Time        : 2020-06-24 17:44
@Modify      : None
"""
from __future__ import absolute_import, division, print_function

import os
from .check import chk_sep


def sep():
    """

    Returns:返回分隔符

    """
    return os.path.sep


def add_sep(path):
    """
    输入文件路径，若结尾没有分隔符，则加上
    Args:
        path: 文件路径

    Returns:加上分隔符后的新路径

    """
    if chk_sep(path):
        path = path + sep()
    return path
