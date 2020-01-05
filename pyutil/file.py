# -*- coding: utf-8 -*-
"""
@FileName    : file.py
@Description : None
@Author      : 齐鲁桐
@Email       : qilutong@yahoo.com
@Time        : 2019-12-23 下午11:35
@Modify      : None
"""
from __future__ import absolute_import, division, print_function

import glob
import os
import shutil

from .check import check_sep


def create_file(file_name):
    """
    创建文件
    :param file_name: 文件名，路径形式
    :return:
    """
    file_dir = os.path.dirname(file_name)
    if os.path.exists(file_name) and os.path.isfile(file_name):
        print("文件已经存在")
        return
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(file_name, 'w') as f:
        f.close()


def remove(file_path):
    """
    删除文件
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        os.removedirs(file_path)


def rename(old, new):
    """
    重命名文件或目录
    :param old: 旧的路径
    :param new: 新的路径
    :return:
    """
    os.rename(old, new)


def file_list(path, suffix="*"):
    """
    从给定路径中读取符合后缀的文件名，并将路径存入列表,默认是全匹配
    :param path:
    :param suffix:要匹配的文件后缀，可传入字符串、列表或元组
    :return: 存有文件名的列表
    """
    # 判断要读取的文件后缀
    suffixes = []
    if isinstance(suffix, str):
        suffixes.append(suffix)
    elif isinstance(suffix, list) or isinstance(suffix, tuple):
        suffixes = list(suffix)
    else:
        raise ValueError("suffix should be string, list or tuple")

    # 判断末尾文件是否有分隔符，没有则添加
    path = check_sep(path)

    f_list = []
    for suffix in suffixes:
        # 将目录下符合条件的文件名存入列表中
        f_list.extend(glob.glob("{}*.{}".format(path, suffix)))
    return f_list


def clear(path):
    """
    清空文件夹
    :param path: 路径
    :return:
    """
    shutil.rmtree(path)
    os.mkdir(path)
