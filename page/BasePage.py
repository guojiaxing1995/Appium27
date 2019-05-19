#coding=utf-8
"""
@Time    : 2019/4/21 9:39
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : BasePage.py
@Desc    :
"""
from selenium.webdriver.common.by import By

from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_toast(self,section,key):
        """获取toast"""
        message = self.getByLocal.get_element(section,key)
        toast = (By.XPATH, "//*[contains(@text," + message + ")]")
        WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(toast))


    def switch_to_native(self):
        """切换NATIVE_APP"""
        self.driver.switch_to.context('NATIVE_APP')

    def switch_to_web_view(self,WEBVIEW=None):
        """切换内嵌h5"""
        view = self.driver.contexts
        if WEBVIEW:
            self.driver.switch_to.context(WEBVIEW)
        else:
            for v in view:
                if 'WEBVIEW' in v:
                    self.driver.switch_to.context(v)
                    break