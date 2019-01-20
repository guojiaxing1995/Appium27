#coding=utf-8
import ConfigParser

#'D:\PycharmProjects\Appium27\config\LocalElement.ini'
import os


class ReadIni():
    def __init__(self,path=None):
        self.read_ini = ConfigParser.ConfigParser()
        if path==None:
            # 获取当前目录
            current_dir = os.path.dirname(__file__)
            # 获取当前目录的父级目录
            parent_dir = os.path.dirname(current_dir)
            path = parent_dir + '\config\LocalElement.ini'
            self.read_ini.read(path)
        else:
            self.read_ini.read(path)

    def get_value(self,section,option):
        try:
            return self.read_ini.get(section, option)
        except:
            return None

