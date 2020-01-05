# -*- coding: utf-8 -*-
"""
@FileName    : __init__.py.py
@Description : None
@Author      : 齐鲁桐
@Email       : qilutong@yahoo.com
@Time        : 2019-12-23 下午6:10
@Modify      : None
"""
from __future__ import absolute_import, division, print_function
import sys

# 判断版本
if sys.version_info[0] != 3:
    print("本工具包只支持Python3及以上版本，目前版本为：{}.{}.{}".format(sys.version_info[0],
                                                      sys.version_info[1],
                                                      sys.version_info[2]))
