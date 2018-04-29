#coding=utf-8

from handle.HomeHandle import HomeHandle
from handle.BbsHandle import BbsHandle
import time

class BbsBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.home_handle = HomeHandle(driver)
        self.bbs_handle = BbsHandle(driver)

    def switch_bbs(self):
        self.home_handle.click_discover()
        time.sleep(10)
        webview = self.bbs_handle.get_bbs_webview()
        a = 1