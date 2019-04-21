#coding=utf-8
"""
@Time    : 2019/4/21 9:39
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : BasePage.py
@Desc    :
"""

from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_toast(self,message):
        """获取toast"""
        toast = ("xpath", "//*[contains(@text," + message + ")]")
        WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(toast))