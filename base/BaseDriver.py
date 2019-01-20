#coding=utf-8
import os
import time
from appium import webdriver
from util.OperateYaml import OperateYaml
class BaseDriver:
    def __init__(self):
        self.operateYaml = OperateYaml()

    def get_android_driver(self,i):
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        app_path = parent_dir + '/apk/wdfp.apk'
        device_info = self.operateYaml.get_devices('device_info_' + str(i))
        capabilities = {
            "platformName": "Android",
            "deviceName": device_info['deviceName'],
            "automationName": "uiautomator2",
            "app": app_path,
            "unicodeKeyboard":True,
            "resetKeyboard":True
            # "noReset":"True"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+device_info['port']+"/wd/hub", capabilities)
        return driver

    def get_ios_driver(self):
        pass

    def get_driver(self,system):
        if system == 'android':
            self.get_android_driver()
        elif system == 'ios':
            self.get_ios_driver()