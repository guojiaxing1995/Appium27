#coding:utf-8
"""
@Time    : 2019/3/10 15:19
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : test.py
@Desc    :
"""
from appium import webdriver

devicesName = '2116ca98'
app_path = r'D:\pythonProgram\Appium27\apk\wdfp.apk'
capabilities = {
    "platformName": "Android",
    "deviceName": devicesName,
    "automationName": "uiautomator2",
    "app": app_path,
    # "appPackage": "com.elephant.myinvoice",
    # "appActivity": "com.elephant.myinvoice.MainActivity",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)