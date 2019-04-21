#coding=utf-8
"""
@Time    : 2019/4/21 11:00
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : apk_path.py
@Desc    :
"""
import os

def apk_path():
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    for root, dirs, files in os.walk(parent_dir+'/apk/'):
        for file in files:
            if os.path.splitext(file)[1] == '.apk':
                apk_path = parent_dir + '/apk/' + file

    return apk_path