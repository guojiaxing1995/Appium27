#coding=utf-8
from handle.LoginHandle import LoginHandle
import time

class LoginBusiness:
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)

    def slide_carouselfigure(self):
        time.sleep(2)
        self.login_handle.slide('up')
        time.sleep(1)
        self.login_handle.slide('left')
        time.sleep(1)
        self.login_handle.slide('left')
        time.sleep(1)
        self.login_handle.slide('left')
        time.sleep(1)
        self.login_handle.slide('left')
        self.login_handle.click_carouselfigure()
        time.sleep(3)

    def login_pass(self):
        self.login_handle.send_username('18550903915')
        self.login_handle.send_password('qwe123')
        self.login_handle.click_login()