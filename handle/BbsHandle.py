#coding=utf-8
from page.HomePage import HomePage
from page.LoginPage import LoginPage

class BbsHandle:
    def __init__(self,driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)

    def get_bbs_webview(self):
        webview = self.driver.contexts
        return webview