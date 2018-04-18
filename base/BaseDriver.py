#coding=utf-8
import time
from appium import webdriver
from util.OperateYaml import OperateYaml
class BaseDriver:
    def __init__(self):
        self.operateYaml = OperateYaml()

    def get_android_driver(self,i):
        device_info = self.operateYaml.get_devices('device_info_' + str(i))
        capabilities = {
            "platformName": "Android",
            "deviceName": device_info['deviceName'],
            "automationName": "uiautomator2",
            "app": "../apk/wdfp.apk",
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